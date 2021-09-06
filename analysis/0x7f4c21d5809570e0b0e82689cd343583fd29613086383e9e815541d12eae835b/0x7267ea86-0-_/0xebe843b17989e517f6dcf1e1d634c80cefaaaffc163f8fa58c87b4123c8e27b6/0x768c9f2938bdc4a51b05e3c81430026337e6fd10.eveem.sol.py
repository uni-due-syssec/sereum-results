# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x768C9f2938BDC4A51b05e3c81430026337e6fd10 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    stor0 # mask: a s
    # storage address 1
    owner # mask: a s
    # storage address 2
    stor2 # mask: a s
    # storage address 3
    bZRxTokenContractAddress # mask: a s
    # storage address 4
    bZxEtherContractAddress # mask: a s
    # storage address 5
    wethContractAddress # mask: a s
    # storage address 6
    vaultContractAddress # mask: a s
    # storage address 7
    oracleRegistryContractAddress # mask: a s
    # storage address 8
    bZxTo0xContractAddress # mask: a s
    # storage address 9
    DEBUG_MODE # mask: a s
    # storage address 9
    bZxTo0xV2ContractAddress # mask: a s
    # storage address 10
    orders
    # storage address 11
    stor11
    # storage address 12
    orderFilledAmounts
    # storage address 13
    orderCancelledAmounts
    # storage address 14
    orderLender
    # storage address 15
    loanPositions
    # storage address 16
    loanPositionsIds
    # storage address 17
    orderList
    # storage address 18
    orderListIndex
    # storage address 19
    orderPositionList
    # storage address 20
    positionList
    # storage address 21
    positionListIndex
    # storage address 22
    tokenInterestOwed
    # storage address 23
    lenderOracleInterest
    # storage address 24
    lenderOrderInterest
    # storage address 25
    traderLoanInterest
    # storage address 26
    oracle
    # storage address 27
    stor27
    # storage address 28
    stor28
    # storage address 39
    targets
    # storage address 40
    stor40
    # storage address 4801487210070163406695185129569382613135035780967894086459536802062928083825974
    stor4801487210070163406695185129569382613135035780967894086459536802062928083825974
    # storage address 29456154062828672557473723247354683789153397515171478680395262379846516970189683
    stor29456154062828672557473723247354683789153397515171478680395262379846516970189683
    # storage address 2887321634239590173202952427458392614084464846611674846609868523121592145258312563
    stor2887321634239590173202952427458392614084464846611674846609868523121592145258312563
    # storage address 314670265799158229021154762285524441673326758555173735815261779228073799381270279478
    stor314670265799158229021154762285524441673326758555173735815261779228073799381270279478
    # storage address 345363845990158578749239147842276833049654305397491675352759186696237954790302270405519791502646
    stor345363845990158578749239147842276833049654305397491675352759186696237954790302270405519791502646
    # storage address 31929580591138833295107912024239320474032466845733167646700326940729900686625803126442027013219956022
    stor31929580591138833295107912024239320474032466845733167646700326940729900686625803126442027013219956022
    # storage address 1971679009334041223483585458060883655714374740470832198349128243053021680524270936327331864041374659825331620859095085510606293073765233472822
    stor1971679009334041223483585458060883655714374740470832198349128243053021680524270936327331864041374659825331620859095085510606293073765233472822
    # storage address 129215955555715725620020244269108767008651120148380956293515326643303427904161733263736194045240448676845477670197311821194978314666604319848150326
    stor129215955555715725620020244269108767008651120148380956293515326643303427904161733263736194045240448676845477670197311821194978314666604319848150326
# hash = 0x093983bd
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 14]]]
# const = None
# payable = True
def orderLender(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orderLender[_param1]


# hash = 0x09c5a317
# getter = None
# const = None
# payable = True
def unknown09c5a317(uint256 _param1, addr _param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == stor0
  stor0 = 2
  stor2 = gas_remaining + 21000
  if not orders[_param1].field_0:
      revert with 0, ')BZxLoanHealth::changeCollateral loanOrder.loanTokenAddress == address(0)'
  if not loanPositions[stor16[_param1][caller]].field_768:
      revert with 0, ')BZxLoanHealth::changeCollateral loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not loanPositions[stor16[_param1][caller]].field_2304:
      revert with 0, ')BZxLoanHealth::changeCollateral loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if block.timestamp >= loanPositions[stor16[_param1][caller]].field_2048:
      revert with 0, ')BZxLoanHealth::changeCollateral block.timestamp >= loanPosition.loanEndUnixTimestampSec'
  if not _param2:
      revert with 0, 
                  ')BZxLoanHealth::changeCollateral collateralTokenFilled == address(0) || collateralTokenFilled == loanPosition.collateralTokenAddressFilled'
  if loanPositions[stor16[_param1][caller]].field_256 == _param2:
      revert with 0, 
                  ')BZxLoanHealth::changeCollateral collateralTokenFilled == address(0) || collateralTokenFilled == loanPosition.collateralTokenAddressFilled'
  if not orders[_param1].field_0:
      require loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
      if loanPositions[stor16[_param1][caller]].field_1280 <= 0:
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return loanPositions[stor16[_param1][caller]].field_1280
      require ext_code.size(oracle[stor10[_param1].field_768])
      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
              gas gas_remaining wei
             args loanPositions[stor16[_param1][caller]].field_256, addr(_param2), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 96
      if not loanPositions[stor16[_param1][caller]].field_1280:
          require ext_call.return_data[32]
          if not 0 / ext_call.return_data[32]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
               gas gas_remaining wei
              args addr(_param2), caller, 0 / ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
          if loanPositions[stor16[_param1][caller]].field_1280 > 0:
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          loanPositions[stor16[_param1][caller]].field_1280 = 0 / ext_call.return_data[32]
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return (0 / ext_call.return_data[32])
      require ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / loanPositions[stor16[_param1][caller]].field_1280 == ext_call.return_data[0]
      require ext_call.return_data[32]
      if not ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param2), caller, ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
      if loanPositions[stor16[_param1][caller]].field_1280 > 0:
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
      loanPositions[stor16[_param1][caller]].field_256 = _param2
      loanPositions[stor16[_param1][caller]].field_1280 = ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x7724d39a with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
      stor2 = 0
      stor0 = 1
      return (ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32])
  if not loanPositions[stor16[_param1][caller]].field_768:
      require loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
      if loanPositions[stor16[_param1][caller]].field_1280 <= 0:
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return loanPositions[stor16[_param1][caller]].field_1280
      require ext_code.size(oracle[stor10[_param1].field_768])
      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
              gas gas_remaining wei
             args loanPositions[stor16[_param1][caller]].field_256, addr(_param2), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 96
      if not loanPositions[stor16[_param1][caller]].field_1280:
          require ext_call.return_data[32]
          if not 0 / ext_call.return_data[32]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
               gas gas_remaining wei
              args addr(_param2), caller, 0 / ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
          if loanPositions[stor16[_param1][caller]].field_1280 > 0:
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          loanPositions[stor16[_param1][caller]].field_1280 = 0 / ext_call.return_data[32]
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return (0 / ext_call.return_data[32])
      require ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / loanPositions[stor16[_param1][caller]].field_1280 == ext_call.return_data[0]
      require ext_call.return_data[32]
      if not ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param2), caller, ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
      if loanPositions[stor16[_param1][caller]].field_1280 > 0:
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
      loanPositions[stor16[_param1][caller]].field_256 = _param2
      loanPositions[stor16[_param1][caller]].field_1280 = ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x7724d39a with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
      stor2 = 0
      stor0 = 1
      return (ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32])
  if not loanPositions[stor16[_param1][caller]].field_2304:
      require loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
      if loanPositions[stor16[_param1][caller]].field_1280 <= 0:
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return loanPositions[stor16[_param1][caller]].field_1280
      require ext_code.size(oracle[stor10[_param1].field_768])
      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
              gas gas_remaining wei
             args loanPositions[stor16[_param1][caller]].field_256, addr(_param2), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 96
      if not loanPositions[stor16[_param1][caller]].field_1280:
          require ext_call.return_data[32]
          if not 0 / ext_call.return_data[32]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
               gas gas_remaining wei
              args addr(_param2), caller, 0 / ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
          if loanPositions[stor16[_param1][caller]].field_1280 > 0:
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          loanPositions[stor16[_param1][caller]].field_1280 = 0 / ext_call.return_data[32]
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return (0 / ext_call.return_data[32])
      require ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / loanPositions[stor16[_param1][caller]].field_1280 == ext_call.return_data[0]
      require ext_call.return_data[32]
      if not ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param2), caller, ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
      if loanPositions[stor16[_param1][caller]].field_1280 > 0:
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
      loanPositions[stor16[_param1][caller]].field_256 = _param2
      loanPositions[stor16[_param1][caller]].field_1280 = ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x7724d39a with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
      stor2 = 0
      stor0 = 1
      return (ext_call.return_data[0] * loanPositions[stor16[_param1][caller]].field_1280 / ext_call.return_data[32])
  require ext_code.size(oracle[stor10[_param1].field_768])
  static call oracle[stor10[_param1].field_768].'^?K<' with:
          gas gas_remaining wei
         args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  if not ext_call.return_data[0]:
      require ext_call.return_data[96] + loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
      if ext_call.return_data[96] + loanPositions[stor16[_param1][caller]].field_1280 <= 0:
          if loanPositions[stor16[_param1][caller]].field_1280 > 0:
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          loanPositions[stor16[_param1][caller]].field_1280 += ext_call.return_data[96]
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return (ext_call.return_data[96] + loanPositions[stor16[_param1][caller]].field_1280)
      require ext_code.size(oracle[stor10[_param1].field_768])
      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
              gas gas_remaining wei
             args loanPositions[stor16[_param1][caller]].field_256, addr(_param2), -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 96
      if not ext_call.return_data[96] + loanPositions[stor16[_param1][caller]].field_1280:
          require ext_call.return_data[32]
          if not 0 / ext_call.return_data[32]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
               gas gas_remaining wei
              args addr(_param2), caller, 0 / ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
          if loanPositions[stor16[_param1][caller]].field_1280 > 0:
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
          loanPositions[stor16[_param1][caller]].field_256 = _param2
          loanPositions[stor16[_param1][caller]].field_1280 = 0 / ext_call.return_data[32]
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x7724d39a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
          stor2 = 0
          stor0 = 1
          return (0 / ext_call.return_data[32])
      require (ext_call.return_data[96] * ext_call.return_data[0]) + (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) / ext_call.return_data[96] + loanPositions[stor16[_param1][caller]].field_1280 == ext_call.return_data[0]
      require ext_call.return_data[32]
      if not (ext_call.return_data[96] * ext_call.return_data[0]) + (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) / ext_call.return_data[32]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param2), caller, (ext_call.return_data[96] * ext_call.return_data[0]) + (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) / ext_call.return_data[32]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
      if loanPositions[stor16[_param1][caller]].field_1280 > 0:
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
      loanPositions[stor16[_param1][caller]].field_256 = _param2
      loanPositions[stor16[_param1][caller]].field_1280 = (ext_call.return_data[96] * ext_call.return_data[0]) + (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) / ext_call.return_data[32]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x7724d39a with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
      stor2 = 0
      stor0 = 1
      return ((ext_call.return_data[96] * ext_call.return_data[0]) + (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) / ext_call.return_data[32])
  if ext_call.return_data[96] >= loanPositions[stor16[_param1][caller]].field_1280:
      if loanPositions[stor16[_param1][caller]].field_1280 > 0:
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
      loanPositions[stor16[_param1][caller]].field_256 = _param2
      loanPositions[stor16[_param1][caller]].field_1280 = 0
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x7724d39a with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
      stor2 = 0
      stor0 = 1
      return 0
  if loanPositions[stor16[_param1][caller]].field_1280 - ext_call.return_data[96] <= 0:
      if loanPositions[stor16[_param1][caller]].field_1280 > 0:
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
      loanPositions[stor16[_param1][caller]].field_256 = _param2
      loanPositions[stor16[_param1][caller]].field_1280 -= ext_call.return_data[96]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x7724d39a with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
      stor2 = 0
      stor0 = 1
      return (loanPositions[stor16[_param1][caller]].field_1280 - ext_call.return_data[96])
  require ext_code.size(oracle[stor10[_param1].field_768])
  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
          gas gas_remaining wei
         args loanPositions[stor16[_param1][caller]].field_256, addr(_param2), -1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 96
  if not loanPositions[stor16[_param1][caller]].field_1280 - ext_call.return_data[96]:
      require ext_call.return_data[32]
      if not 0 / ext_call.return_data[32]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param2), caller, 0 / ext_call.return_data[32]
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
      if loanPositions[stor16[_param1][caller]].field_1280 > 0:
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
      loanPositions[stor16[_param1][caller]].field_256 = _param2
      loanPositions[stor16[_param1][caller]].field_1280 = 0 / ext_call.return_data[32]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x7724d39a with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
      stor2 = 0
      stor0 = 1
      return (0 / ext_call.return_data[32])
  require (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) - (ext_call.return_data[96] * ext_call.return_data[0]) / loanPositions[stor16[_param1][caller]].field_1280 - ext_call.return_data[96] == ext_call.return_data[0]
  require ext_call.return_data[32]
  if not (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) - (ext_call.return_data[96] * ext_call.return_data[0]) / ext_call.return_data[32]:
      revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral == 0'
  require ext_code.size(vaultContractAddress)
  call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
       gas gas_remaining wei
      args addr(_param2), caller, (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) - (ext_call.return_data[96] * ext_call.return_data[0]) / ext_call.return_data[32]
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.depositToken new collateral failed'
  if loanPositions[stor16[_param1][caller]].field_1280 > 0:
      require ext_code.size(vaultContractAddress)
      call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
           gas gas_remaining wei
          args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, ')BZxLoanHealth::changeCollateral BZxVault.withdrawToken old collateral failed'
  loanPositions[stor16[_param1][caller]].field_256 = _param2
  loanPositions[stor16[_param1][caller]].field_1280 = (loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) - (ext_call.return_data[96] * ext_call.return_data[0]) / ext_call.return_data[32]
  require ext_code.size(oracle[stor10[_param1].field_768])
  call oracle[stor10[_param1].field_768].0x7724d39a with:
       gas gas_remaining wei
      args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ')BZxLoanHealth::changeCollateral OracleInterface.didChangeCollateral failed'
  stor2 = 0
  stor0 = 1
  return ((loanPositions[stor16[_param1][caller]].field_1280 * ext_call.return_data[0]) - (ext_call.return_data[96] * ext_call.return_data[0]) / ext_call.return_data[32])


# hash = 0x13e97c71
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 22]]]]]
# const = None
# payable = True
def tokenInterestOwed(address _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return tokenInterestOwed[_param1][_param2]


# hash = 0x16a6bff6
# getter = ['storage', 160, 0, ['sha3', ['data', ['mask_shl', 32, 224, 0, ['cd', 4]], 39]]]
# const = None
# payable = True
def targets(bytes4 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return targets[Mask(32, 224, _param1)]


# hash = 0x2035d73b
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['mask_shl', 32, 224, 0, ['cd', 4]], 40]]]]
# const = None
# payable = True
def targetIsPaused(bytes4 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return bool(stor40[Mask(32, 224, _param1)])


# hash = 0x2274346b
# getter = ['storage', 160, 0, 6]
# const = None
# payable = True
def vaultContract() payable: 
  return vaultContractAddress


# hash = 0x42ad3526
# getter = ['struct', ['loc', 18]]
# const = None
# payable = True
def orderListIndex(bytes32 _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return orderListIndex[_param1][_param2].field_0, bool(orderListIndex[_param1][_param2].field_256)


# hash = 0x4780eac1
# getter = ['storage', 160, 0, 5]
# const = None
# payable = True
def wethContract() payable: 
  return wethContractAddress


# hash = 0x4a7c3d50
# getter = ['struct', ['loc', 21]]
# const = None
# payable = True
def positionListIndex(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return positionListIndex[_param1].field_0, bool(positionListIndex[_param1].field_256)


# hash = 0x4b4056c5
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 24]]]
# const = None
# payable = True
def lenderOrderInterest(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return lenderOrderInterest[_param1].field_0, lenderOrderInterest[_param1].field_256, lenderOrderInterest[_param1].field_512


# hash = 0x52cccdb3
# getter = None
# const = None
# payable = True
def unknown52cccdb3(uint256 _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >=′ 96
  require 1 == stor0
  stor0 = 2
  stor2 = gas_remaining + 21000
  if _param3 <= 0:
      revert with 0, 'depositAmount too low'
  if not orders[_param1].field_0:
      revert with 0, 'loanOrder.loanTokenAddress == address(0)'
  if not loanPositions[stor16[_param1][caller]].field_768:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not loanPositions[stor16[_param1][caller]].field_2304:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if orders[_param1].field_0 != loanPositions[stor16[_param1][caller]].field_512:
      if caller != caller:
          revert with 0, 'unauthorized'
  require ext_code.size(vaultContractAddress)
  if loanPositions[stor16[_param1][caller]].field_256 == _param2:
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param2), caller, _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.depositToken position failed'
      require _param3 + loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
      loanPositions[stor16[_param1][caller]].field_1280 += _param3
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x33ac22b4 with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, _param3, stor2
  else:
      call vaultContractAddress.transferTokenFrom(address tokenContract, address transferTo, address transferFrom, uint256 value) with:
           gas gas_remaining wei
          args addr(_param2), caller, oracle[stor10[_param1].field_768], _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.transferTokenFrom failed'
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x4849b6c8 with:
           gas gas_remaining wei
          args addr(_param2), loanPositions[stor16[_param1][caller]].field_256, _param3, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 64
      if not ext_call.return_data[0]:
          revert with 0, 'collateralTokenAmountReceived == 0'
      if ext_call.return_data[32] < _param3:
          require ext_call.return_data[32] <= _param3
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args addr(_param2), caller, _param3 - ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxVault.withdrawToken deposit failed'
      require ext_call.return_data[0] + loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
      loanPositions[stor16[_param1][caller]].field_1280 += ext_call.return_data[0]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x33ac22b4 with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, ext_call.return_data[0], stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'OracleInterface.didDepositCollateral failed'
  stor2 = 0
  stor0 = 1
  return 1


# hash = 0x5c445c86
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 68], ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 23]]]]]]]
# const = None
# payable = True
def lenderOracleInterest(address _param1, address _param2, address _param3) payable: 
  require calldata.size - 4 >=′ 96
  return lenderOracleInterest[_param1][_param2][_param3].field_0, 
         lenderOracleInterest[_param1][_param2][_param3].field_256,
         lenderOracleInterest[_param1][_param2][_param3].field_512


# hash = 0x64a71040
# getter = ['storage', 160, 0, 4]
# const = None
# payable = True
def bZxEtherContract() payable: 
  return bZxEtherContractAddress


# hash = 0x71eb125e
# getter = ['storage', 160, 0, ['sha3', ['data', ['cd', 4], 26]]]
# const = None
# payable = True
def oracleAddresses(address _param1) payable: 
  require calldata.size - 4 >=′ 32
  return oracle[_param1]


# hash = 0x779dec5b
# getter = ['storage', 160, 0, 3]
# const = None
# payable = True
def bZRxTokenContract() payable: 
  return bZRxTokenContractAddress


# hash = 0x7955f60f
# getter = ['struct', ['loc', 20]]
# const = None
# payable = True
def positionList(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  require _param1 < positionList.length
  return positionList[_param1].field_0, positionList[_param1].field_256


# hash = 0x7b8e3514
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 28]]]]]]
# const = None
# payable = True
def allowedValidators(address _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return bool(stor28[_param1][_param2])


# hash = 0x82c174d0
# getter = ['bool', ['storage', 8, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 27]]]]]]
# const = None
# payable = True
def preSigned(bytes32 _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return bool(stor27[_param1][_param2])


# hash = 0x853002d3
# getter = None
# const = None
# payable = True
def unknown853002d3(uint256 _param1, addr _param2) payable: 
  require calldata.size - 4 >=′ 64
  if not orders[_param1].field_0:
      return 0
  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
      return 0
  if not loanPositions[stor16[_param1][addr(_param2)]].field_2304:
      return 0
  require ext_code.size(oracle[stor10[_param1].field_768])
  static call oracle[stor10[_param1].field_768].'^?K<' with:
          gas gas_remaining wei
         args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][addr(_param2)]].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_768, loanPositions[stor16[_param1][addr(_param2)]].field_1024, loanPositions[stor16[_param1][addr(_param2)]].field_1280, loanPositions[stor16[_param1][addr(_param2)]].field_1536, loanPositions[stor16[_param1][addr(_param2)]].field_1792, loanPositions[stor16[_param1][addr(_param2)]].field_2048, bool(loanPositions[stor16[_param1][addr(_param2)]].field_2304), loanPositions[stor16[_param1][addr(_param2)]].field_2560
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  return bool(ext_call.return_data[0]), ext_call.return_data[32], ext_call.return_data[64], ext_call.return_data[96]


# hash = 0x86042ec6
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 36], ['sha3', ['data', ['cd', 4], 16]]]]]
# const = None
# payable = True
def loanPositionsIds(bytes32 _param1, address _param2) payable: 
  require calldata.size - 4 >=′ 64
  return loanPositionsIds[_param1][_param2]


# hash = 0x8638aa65
# getter = ['bool', ['storage', 8, 160, 9]]
# const = None
# payable = True
def DEBUG_MODE() payable: 
  return bool(DEBUG_MODE)


# hash = 0x8da5cb5b
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def owner() payable: 
  return owner


# hash = 0x9048617a
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 25]]]
# const = None
# payable = True
def traderLoanInterest(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return traderLoanInterest[_param1].field_0, 
         traderLoanInterest[_param1].field_256,
         traderLoanInterest[_param1].field_512,
         traderLoanInterest[_param1].field_768


# hash = 0x9437d0ea
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 19]]], ['cd', 36]]]
# const = None
# payable = True
def orderPositionList(bytes32 _param1, uint256 _param2) payable: 
  require calldata.size - 4 >=′ 64
  require _param2 < orderPositionList[_param1]
  return orderPositionList[_param1][_param2]


# hash = 0x99a8548a
# getter = None
# const = None
# payable = True
def unknown99a8548a(uint256 _param1, addr _param2, addr _param3, uint256 _param4) payable: 
  require calldata.size - 4 >=′ 128
  require 1 == stor0
  stor0 = 2
  stor2 = gas_remaining + 21000
  if _param4 <= 0:
      revert with 0, 'depositAmount too low'
  if not orders[_param1].field_0:
      revert with 0, 'loanOrder.loanTokenAddress == address(0)'
  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not loanPositions[stor16[_param1][addr(_param2)]].field_2304:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
      if _param2 != caller:
          revert with 0, 'unauthorized'
  require ext_code.size(vaultContractAddress)
  if loanPositions[stor16[_param1][addr(_param2)]].field_256 == _param3:
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param3), caller, _param4
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.depositToken position failed'
      require _param4 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280
      loanPositions[stor16[_param1][addr(_param2)]].field_1280 += _param4
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x33ac22b4 with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][addr(_param2)]].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_768, loanPositions[stor16[_param1][addr(_param2)]].field_1024, loanPositions[stor16[_param1][addr(_param2)]].field_1280, loanPositions[stor16[_param1][addr(_param2)]].field_1536, loanPositions[stor16[_param1][addr(_param2)]].field_1792, loanPositions[stor16[_param1][addr(_param2)]].field_2048, bool(loanPositions[stor16[_param1][addr(_param2)]].field_2304), loanPositions[stor16[_param1][addr(_param2)]].field_2560, _param4, stor2
  else:
      call vaultContractAddress.transferTokenFrom(address tokenContract, address transferTo, address transferFrom, uint256 value) with:
           gas gas_remaining wei
          args addr(_param3), caller, oracle[stor10[_param1].field_768], _param4
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.transferTokenFrom failed'
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x4849b6c8 with:
           gas gas_remaining wei
          args addr(_param3), loanPositions[stor16[_param1][addr(_param2)]].field_256, _param4, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 64
      if not ext_call.return_data[0]:
          revert with 0, 'collateralTokenAmountReceived == 0'
      if ext_call.return_data[32] < _param4:
          require ext_call.return_data[32] <= _param4
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args addr(_param3), caller, _param4 - ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxVault.withdrawToken deposit failed'
      require ext_call.return_data[0] + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280
      loanPositions[stor16[_param1][addr(_param2)]].field_1280 += ext_call.return_data[0]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x33ac22b4 with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][addr(_param2)]].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_768, loanPositions[stor16[_param1][addr(_param2)]].field_1024, loanPositions[stor16[_param1][addr(_param2)]].field_1280, loanPositions[stor16[_param1][addr(_param2)]].field_1536, loanPositions[stor16[_param1][addr(_param2)]].field_1792, loanPositions[stor16[_param1][addr(_param2)]].field_2048, bool(loanPositions[stor16[_param1][addr(_param2)]].field_2304), loanPositions[stor16[_param1][addr(_param2)]].field_2560, ext_call.return_data[0], stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'OracleInterface.didDepositCollateral failed'
  stor2 = 0
  stor0 = 1
  return 1


# hash = 0x9ae6b186
# getter = ['storage', 160, 0, 9]
# const = None
# payable = True
def bZxTo0xV2Contract() payable: 
  return bZxTo0xV2ContractAddress


# hash = 0x9c3f1e90
# getter = ['struct', ['loc', 10]]
# const = None
# payable = True
def orders(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orders[_param1].field_0, 
         orders[_param1].field_256,
         orders[_param1].field_512,
         orders[_param1].field_768,
         orders[_param1].field_1024,
         orders[_param1].field_1280,
         orders[_param1].field_1536,
         orders[_param1].field_1792,
         orders[_param1].field_2048,
         orders[_param1].field_2304


# hash = 0x9e312dac
# getter = ['struct', ['loc', 15]]
# const = None
# payable = True
def loanPositions(uint256 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return loanPositions[_param1].field_0, 
         loanPositions[_param1].field_256,
         loanPositions[_param1].field_512,
         loanPositions[_param1].field_768,
         loanPositions[_param1].field_1024,
         loanPositions[_param1].field_1280,
         loanPositions[_param1].field_1536,
         loanPositions[_param1].field_1792,
         loanPositions[_param1].field_2048,
         bool(loanPositions[_param1].field_2304),
         loanPositions[_param1].field_2560


# hash = 0xa1e93482
# getter = None
# const = None
# payable = True
def unknowna1e93482(uint256 _param1, uint256 _param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == stor0
  stor0 = 2
  stor2 = gas_remaining + 21000
  if not orders[_param1].field_0:
      stor2 = 0
      stor0 = 1
      return 0
  if not loanPositions[stor16[_param1][caller]].field_768:
      stor2 = 0
      stor0 = 1
      return 0
  if not loanPositions[stor16[_param1][caller]].field_2304:
      stor2 = 0
      stor0 = 1
      return 0
  require ext_code.size(oracle[stor10[_param1].field_768])
  static call oracle[stor10[_param1].field_768].'^?K<' with:
          gas gas_remaining wei
         args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  if not ext_call.return_data[96]:
      stor2 = 0
      stor0 = 1
      return 0
  if not ext_call.return_data[0]:
      stor2 = 0
      stor0 = 1
      return 0
  if _param2 < ext_call.return_data[96]:
      if _param2 <= loanPositions[stor16[_param1][caller]].field_1280:
          if not _param2:
              stor2 = 0
              stor0 = 1
              return 0
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::withdrawCollaterl: BZxVault.withdrawToken collateral failed'
          require _param2 <= loanPositions[stor16[_param1][caller]].field_1280
          loanPositions[stor16[_param1][caller]].field_1280 -= _param2
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x18ddd6a8 with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, _param2, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::withdrawCollaterl: OracleInterface.didWithdrawCollateral failed'
          stor2 = 0
          stor0 = 1
          return _param2
      if loanPositions[stor16[_param1][caller]].field_1536 > 0:
          if loanPositions[stor16[_param1][caller]].field_256 == loanPositions[stor16[_param1][caller]].field_512:
              require _param2 - loanPositions[stor16[_param1][caller]].field_1280 <= loanPositions[stor16[_param1][caller]].field_1536
              loanPositions[stor16[_param1][caller]].field_1536 = loanPositions[stor16[_param1][caller]].field_1536 - _param2 + loanPositions[stor16[_param1][caller]].field_1280
              require _param2 >= loanPositions[stor16[_param1][caller]].field_1280
              loanPositions[stor16[_param1][caller]].field_1280 = _param2
          else:
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_512, oracle[stor10[_param1].field_768], loanPositions[stor16[_param1][caller]].field_1536
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: BZxVault.withdrawToken (position) failed'
              require ext_code.size(oracle[stor10[_param1].field_768])
              call oracle[stor10[_param1].field_768].0x4849b6c8 with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_1536, _param2 - loanPositions[stor16[_param1][caller]].field_1280
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 64
              if loanPositions[stor16[_param1][caller]].field_1536 < ext_call.return_data[32]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: positionTokenAmountFilled < sourceTokenAmountUsed'
              if ext_call.return_data[0]:
                  require ext_call.return_data[32] <= loanPositions[stor16[_param1][caller]].field_1536
              else:
                  if ext_call.return_data[32] > 0:
                      revert with 0, ')BZxLoanHealth::withdrawCollaterl: invalid trade'
              loanPositions[stor16[_param1][caller]].field_1536 -= ext_call.return_data[32]
              require ext_call.return_data[0] + loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
              loanPositions[stor16[_param1][caller]].field_1280 += ext_call.return_data[0]
          if _param2 <= loanPositions[stor16[_param1][caller]].field_1280:
              if not _param2:
                  stor2 = 0
                  stor0 = 1
                  return 0
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_256, caller, _param2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: BZxVault.withdrawToken collateral failed'
              require _param2 <= loanPositions[stor16[_param1][caller]].field_1280
              loanPositions[stor16[_param1][caller]].field_1280 -= _param2
              require ext_code.size(oracle[stor10[_param1].field_768])
              call oracle[stor10[_param1].field_768].0x18ddd6a8 with:
                   gas gas_remaining wei
                  args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, _param2, stor2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: OracleInterface.didWithdrawCollateral failed'
              stor2 = 0
              stor0 = 1
              return _param2
  else:
      if ext_call.return_data[96] <= loanPositions[stor16[_param1][caller]].field_1280:
          if not ext_call.return_data[96]:
              stor2 = 0
              stor0 = 1
              return 0
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_256, caller, ext_call.return_data[96]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::withdrawCollaterl: BZxVault.withdrawToken collateral failed'
          require ext_call.return_data[96] <= loanPositions[stor16[_param1][caller]].field_1280
          loanPositions[stor16[_param1][caller]].field_1280 -= ext_call.return_data[96]
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0x18ddd6a8 with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, ext_call.return_data[96], stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, ')BZxLoanHealth::withdrawCollaterl: OracleInterface.didWithdrawCollateral failed'
          stor2 = 0
          stor0 = 1
          return ext_call.return_data[96]
      if loanPositions[stor16[_param1][caller]].field_1536 > 0:
          if loanPositions[stor16[_param1][caller]].field_256 == loanPositions[stor16[_param1][caller]].field_512:
              require ext_call.return_data[96] - loanPositions[stor16[_param1][caller]].field_1280 <= loanPositions[stor16[_param1][caller]].field_1536
              loanPositions[stor16[_param1][caller]].field_1536 = loanPositions[stor16[_param1][caller]].field_1536 - ext_call.return_data[96] + loanPositions[stor16[_param1][caller]].field_1280
              require ext_call.return_data[96] >= loanPositions[stor16[_param1][caller]].field_1280
              loanPositions[stor16[_param1][caller]].field_1280 = ext_call.return_data[96]
          else:
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_512, oracle[stor10[_param1].field_768], loanPositions[stor16[_param1][caller]].field_1536
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: BZxVault.withdrawToken (position) failed'
              require ext_code.size(oracle[stor10[_param1].field_768])
              call oracle[stor10[_param1].field_768].0x4849b6c8 with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_1536, ext_call.return_data[96] - loanPositions[stor16[_param1][caller]].field_1280
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 64
              if loanPositions[stor16[_param1][caller]].field_1536 < ext_call.return_data[32]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: positionTokenAmountFilled < sourceTokenAmountUsed'
              if ext_call.return_data[0]:
                  require ext_call.return_data[32] <= loanPositions[stor16[_param1][caller]].field_1536
              else:
                  if ext_call.return_data[32] > 0:
                      revert with 0, ')BZxLoanHealth::withdrawCollaterl: invalid trade'
              loanPositions[stor16[_param1][caller]].field_1536 -= ext_call.return_data[32]
              require ext_call.return_data[0] + loanPositions[stor16[_param1][caller]].field_1280 >= loanPositions[stor16[_param1][caller]].field_1280
              loanPositions[stor16[_param1][caller]].field_1280 += ext_call.return_data[0]
          if ext_call.return_data[96] <= loanPositions[stor16[_param1][caller]].field_1280:
              if not ext_call.return_data[96]:
                  stor2 = 0
                  stor0 = 1
                  return 0
              require ext_code.size(vaultContractAddress)
              call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
                   gas gas_remaining wei
                  args loanPositions[stor16[_param1][caller]].field_256, caller, ext_call.return_data[96]
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: BZxVault.withdrawToken collateral failed'
              require ext_call.return_data[96] <= loanPositions[stor16[_param1][caller]].field_1280
              loanPositions[stor16[_param1][caller]].field_1280 -= ext_call.return_data[96]
              require ext_code.size(oracle[stor10[_param1].field_768])
              call oracle[stor10[_param1].field_768].0x18ddd6a8 with:
                   gas gas_remaining wei
                  args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, ext_call.return_data[96], stor2
              if not ext_call.success:
                  revert with ext_call.return_data[0 len return_data.size]
              require return_data.size >=′ 32
              if not ext_call.return_data[0]:
                  revert with 0, ')BZxLoanHealth::withdrawCollaterl: OracleInterface.didWithdrawCollateral failed'
              stor2 = 0
              stor0 = 1
              return ext_call.return_data[96]
  if not loanPositions[stor16[_param1][caller]].field_1280:
      stor2 = 0
      stor0 = 1
      return 0
  require ext_code.size(vaultContractAddress)
  call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
       gas gas_remaining wei
      args loanPositions[stor16[_param1][caller]].field_256, caller, loanPositions[stor16[_param1][caller]].field_1280
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ')BZxLoanHealth::withdrawCollaterl: BZxVault.withdrawToken collateral failed'
  require loanPositions[stor16[_param1][caller]].field_1280 <= loanPositions[stor16[_param1][caller]].field_1280
  loanPositions[stor16[_param1][caller]].field_1280 = 0
  require ext_code.size(oracle[stor10[_param1].field_768])
  call oracle[stor10[_param1].field_768].0x18ddd6a8 with:
       gas gas_remaining wei
      args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, loanPositions[stor16[_param1][caller]].field_1280, stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, ')BZxLoanHealth::withdrawCollaterl: OracleInterface.didWithdrawCollateral failed'
  stor2 = 0
  stor0 = 1
  return loanPositions[stor16[_param1][caller]].field_1280


# hash = 0xa72480ae
# getter = None
# const = None
# payable = True
def orderAux(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  mem[128] = stor11[_param1][9].field_0
  [94midx = 128
  [94ms = 0
  while stor11[_param1][9].length + 96 > [94midx:
      mem[[94midx + 32] = stor11[_param1][[94ms + 9].field_256
      [94midx = [94midx + 32
      [94ms = [94ms + 1
      continue 
  return stor11[_param1].field_0, 
         stor11[_param1].field_256,
         stor11[_param1].field_512,
         stor11[_param1].field_768,
         stor11[_param1].field_1024,
         stor11[_param1].field_1280,
         stor11[_param1].field_1536,
         stor11[_param1].field_1792,
         bool(stor11[_param1].field_2048),
         Array(len=stor11[_param1][9].length, data=mem[128 len ceil32(stor11[_param1][9].length)])


# hash = 0xac5da9db
# getter = None
# const = None
# payable = True
def unknownac5da9db(uint256 _param1, addr _param2, uint256 _param3) payable: 
  require calldata.size - 4 >=′ 96
  require 1 == stor0
  stor0 = 2
  stor2 = gas_remaining + 21000
  if _param3 <= 0:
      revert with 0, 'depositAmount too low'
  if not orders[_param1].field_0:
      revert with 0, 'loanOrder.loanTokenAddress == address(0)'
  if not loanPositions[stor16[_param1][caller]].field_768:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not loanPositions[stor16[_param1][caller]].field_2304:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if orders[_param1].field_0 != loanPositions[stor16[_param1][caller]].field_512:
      if caller != caller:
          revert with 0, 'unauthorized'
  require ext_code.size(vaultContractAddress)
  if loanPositions[stor16[_param1][caller]].field_512 == _param2:
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param2), caller, _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.depositToken position failed'
      require _param3 + loanPositions[stor16[_param1][caller]].field_1536 >= loanPositions[stor16[_param1][caller]].field_1536
      loanPositions[stor16[_param1][caller]].field_1536 += _param3
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0xfd670cbd with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, _param3, stor2
  else:
      call vaultContractAddress.transferTokenFrom(address tokenContract, address transferTo, address transferFrom, uint256 value) with:
           gas gas_remaining wei
          args addr(_param2), caller, oracle[stor10[_param1].field_768], _param3
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.transferTokenFrom failed'
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x4849b6c8 with:
           gas gas_remaining wei
          args addr(_param2), loanPositions[stor16[_param1][caller]].field_512, _param3, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 64
      if not ext_call.return_data[0]:
          revert with 0, 'positionTokenAmountReceived == 0'
      if ext_call.return_data[32] < _param3:
          require ext_call.return_data[32] <= _param3
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args addr(_param2), caller, _param3 - ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxVault.withdrawToken deposit failed'
      require ext_call.return_data[0] + loanPositions[stor16[_param1][caller]].field_1536 >= loanPositions[stor16[_param1][caller]].field_1536
      loanPositions[stor16[_param1][caller]].field_1536 += ext_call.return_data[0]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0xfd670cbd with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, ext_call.return_data[0], stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'OracleInterface.didDepositPosition failed'
  stor2 = 0
  stor0 = 1
  return 1


# hash = 0xb7a025f9
# getter = ['storage', 160, 0, 8]
# const = None
# payable = True
def bZxTo0xContract() payable: 
  return bZxTo0xContractAddress


# hash = 0xbab7d1a3
# getter = None
# const = None
# payable = True
def unknownbab7d1a3(uint256 _param1, addr _param2, addr _param3, uint256 _param4) payable: 
  require calldata.size - 4 >=′ 128
  require 1 == stor0
  stor0 = 2
  stor2 = gas_remaining + 21000
  if _param4 <= 0:
      revert with 0, 'depositAmount too low'
  if not orders[_param1].field_0:
      revert with 0, 'loanOrder.loanTokenAddress == address(0)'
  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if not loanPositions[stor16[_param1][addr(_param2)]].field_2304:
      revert with 0, 'loanPosition.loanTokenAmountFilled == 0 || !loanPosition.active'
  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
      if _param2 != caller:
          revert with 0, 'unauthorized'
  require ext_code.size(vaultContractAddress)
  if loanPositions[stor16[_param1][addr(_param2)]].field_512 == _param3:
      call vaultContractAddress.depositToken(address from, address token, uint256 amount) with:
           gas gas_remaining wei
          args addr(_param3), caller, _param4
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.depositToken position failed'
      require _param4 + loanPositions[stor16[_param1][addr(_param2)]].field_1536 >= loanPositions[stor16[_param1][addr(_param2)]].field_1536
      loanPositions[stor16[_param1][addr(_param2)]].field_1536 += _param4
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0xfd670cbd with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][addr(_param2)]].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_768, loanPositions[stor16[_param1][addr(_param2)]].field_1024, loanPositions[stor16[_param1][addr(_param2)]].field_1280, loanPositions[stor16[_param1][addr(_param2)]].field_1536, loanPositions[stor16[_param1][addr(_param2)]].field_1792, loanPositions[stor16[_param1][addr(_param2)]].field_2048, bool(loanPositions[stor16[_param1][addr(_param2)]].field_2304), loanPositions[stor16[_param1][addr(_param2)]].field_2560, _param4, stor2
  else:
      call vaultContractAddress.transferTokenFrom(address tokenContract, address transferTo, address transferFrom, uint256 value) with:
           gas gas_remaining wei
          args addr(_param3), caller, oracle[stor10[_param1].field_768], _param4
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 32
      if not ext_call.return_data[0]:
          revert with 0, 'BZxVault.transferTokenFrom failed'
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0x4849b6c8 with:
           gas gas_remaining wei
          args addr(_param3), loanPositions[stor16[_param1][addr(_param2)]].field_512, _param4, -1
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >=′ 64
      if not ext_call.return_data[0]:
          revert with 0, 'positionTokenAmountReceived == 0'
      if ext_call.return_data[32] < _param4:
          require ext_call.return_data[32] <= _param4
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args addr(_param3), caller, _param4 - ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxVault.withdrawToken deposit failed'
      require ext_call.return_data[0] + loanPositions[stor16[_param1][addr(_param2)]].field_1536 >= loanPositions[stor16[_param1][addr(_param2)]].field_1536
      loanPositions[stor16[_param1][addr(_param2)]].field_1536 += ext_call.return_data[0]
      require ext_code.size(oracle[stor10[_param1].field_768])
      call oracle[stor10[_param1].field_768].0xfd670cbd with:
           gas gas_remaining wei
          args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][addr(_param2)]].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_768, loanPositions[stor16[_param1][addr(_param2)]].field_1024, loanPositions[stor16[_param1][addr(_param2)]].field_1280, loanPositions[stor16[_param1][addr(_param2)]].field_1536, loanPositions[stor16[_param1][addr(_param2)]].field_1792, loanPositions[stor16[_param1][addr(_param2)]].field_2048, bool(loanPositions[stor16[_param1][addr(_param2)]].field_2304), loanPositions[stor16[_param1][addr(_param2)]].field_2560, ext_call.return_data[0], stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'OracleInterface.didDepositPosition failed'
  stor2 = 0
  stor0 = 1
  return 1


# hash = 0xc4d66de8
# getter = None
# const = None
# payable = True
def initialize(address _sender) payable: 
  require calldata.size - 4 >=′ 32
  require caller == owner
  stor39[Mask(32, 224, ('name', 'stor3A64', 31929580591138833295107912024239320474032466845733167646700326940729900686625803126442027013219956022))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2964', 129215955555715725620020244269108767008651120148380956293515326643303427904161733263736194045240448676845477670197311821194978314666604319848150326))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2977', 314670265799158229021154762285524441673326758555173735815261779228073799381270279478))] = _sender
  stor39[Mask(32, 224, ('name', 'storFE63', 29456154062828672557473723247354683789153397515171478680395262379846516970189683))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2977', 4801487210070163406695185129569382613135035780967894086459536802062928083825974))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2964', 345363845990158578749239147842276833049654305397491675352759186696237954790302270405519791502646))] = _sender
  stor39[Mask(32, 224, ('name', 'stor2964', 1971679009334041223483585458060883655714374740470832198349128243053021680524270936327331864041374659825331620859095085510606293073765233472822))] = _sender
  stor39[Mask(32, 224, ('name', 'stor6167', 2887321634239590173202952427458392614084464846611674846609868523121592145258312563))] = _sender
  targets[Mask(32, 224, sha3(0.00390625 / 'getTotalEscrow(bytes32,address)'))] = _sender


# hash = 0xcce37f3e
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 12]]]
# const = None
# payable = True
def orderFilledAmounts(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orderFilledAmounts[_param1]


# hash = 0xd9fd7341
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 13]]]
# const = None
# payable = True
def orderCancelledAmounts(bytes32 _param1) payable: 
  require calldata.size - 4 >=′ 32
  return orderCancelledAmounts[_param1]


# hash = 0xde3f26eb
# getter = ['storage', 160, 0, 7]
# const = None
# payable = True
def oracleRegistryContract() payable: 
  return oracleRegistryContractAddress


# hash = 0xe53599c3
# getter = None
# const = None
# payable = True
def unknowne53599c3(uint256 _param1, uint256 _param2) payable: 
  require calldata.size - 4 >=′ 64
  require 1 == stor0
  stor0 = 2
  stor2 = gas_remaining + 21000
  if not orders[_param1].field_0:
      stor2 = 0
      stor0 = 1
      return 0
  if not loanPositions[stor16[_param1][caller]].field_768:
      stor2 = 0
      stor0 = 1
      return 0
  if not loanPositions[stor16[_param1][caller]].field_2304:
      stor2 = 0
      stor0 = 1
      return 0
  require ext_code.size(oracle[stor10[_param1].field_768])
  static call oracle[stor10[_param1].field_768].'^?K<' with:
          gas gas_remaining wei
         args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 128
  if not ext_call.return_data[32]:
      stor2 = 0
      stor0 = 1
      return 0
  if not ext_call.return_data[0]:
      stor2 = 0
      stor0 = 1
      return 0
  if block.timestamp >= loanPositions[stor16[_param1][caller]].field_2048:
      stor2 = 0
      stor0 = 1
      return 0
  if _param2 < ext_call.return_data[32]:
      if _param2 <= loanPositions[stor16[_param1][caller]].field_1536:
          if not _param2:
              stor2 = 0
              stor0 = 1
              return 0
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_512, caller, _param2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: BZxVault.withdrawToken loan failed'
          require _param2 <= loanPositions[stor16[_param1][caller]].field_1536
          loanPositions[stor16[_param1][caller]].field_1536 -= _param2
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0xf2a2583a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, _param2, stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: OracleInterface.didWithdrawPosition failed'
          log LogWithdrawPosition(
                bytes32 loanOrderHash=_param2,
                address trader=loanPositions[stor16[_param1][caller]].field_1536,
                uint256 positionAmount=loanPositions[stor16[_param1][caller]].field_2560,
                uint256 remainingPosition=orders[_param1].field_2304,
                uint256 positionId=caller)
          stor2 = 0
          stor0 = 1
          return _param2
  else:
      if ext_call.return_data[32] <= loanPositions[stor16[_param1][caller]].field_1536:
          if not ext_call.return_data[32]:
              stor2 = 0
              stor0 = 1
              return 0
          require ext_code.size(vaultContractAddress)
          call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
               gas gas_remaining wei
              args loanPositions[stor16[_param1][caller]].field_512, caller, ext_call.return_data[32]
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: BZxVault.withdrawToken loan failed'
          require ext_call.return_data[32] <= loanPositions[stor16[_param1][caller]].field_1536
          loanPositions[stor16[_param1][caller]].field_1536 -= ext_call.return_data[32]
          require ext_code.size(oracle[stor10[_param1].field_768])
          call oracle[stor10[_param1].field_768].0xf2a2583a with:
               gas gas_remaining wei
              args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, ext_call.return_data[32], stor2
          if not ext_call.success:
              revert with ext_call.return_data[0 len return_data.size]
          require return_data.size >=′ 32
          if not ext_call.return_data[0]:
              revert with 0, 'BZxLoanHealth::withdrawPosition: OracleInterface.didWithdrawPosition failed'
          log LogWithdrawPosition(
                bytes32 loanOrderHash=ext_call.return_data[32],
                address trader=loanPositions[stor16[_param1][caller]].field_1536,
                uint256 positionAmount=loanPositions[stor16[_param1][caller]].field_2560,
                uint256 remainingPosition=orders[_param1].field_2304,
                uint256 positionId=caller)
          stor2 = 0
          stor0 = 1
          return ext_call.return_data[32]
  if not loanPositions[stor16[_param1][caller]].field_1536:
      stor2 = 0
      stor0 = 1
      return 0
  require ext_code.size(vaultContractAddress)
  call vaultContractAddress.withdrawToken(address token, address to, uint256 value) with:
       gas gas_remaining wei
      args loanPositions[stor16[_param1][caller]].field_512, caller, loanPositions[stor16[_param1][caller]].field_1536
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'BZxLoanHealth::withdrawPosition: BZxVault.withdrawToken loan failed'
  require loanPositions[stor16[_param1][caller]].field_1536 <= loanPositions[stor16[_param1][caller]].field_1536
  loanPositions[stor16[_param1][caller]].field_1536 = 0
  require ext_code.size(oracle[stor10[_param1].field_768])
  call oracle[stor10[_param1].field_768].0xf2a2583a with:
       gas gas_remaining wei
      args orders[_param1].field_0, orders[_param1].field_256, orders[_param1].field_512, orders[_param1].field_768, orders[_param1].field_1024, orders[_param1].field_1280, orders[_param1].field_1536, orders[_param1].field_1792, orders[_param1].field_2048, orders[_param1].field_2304, loanPositions[stor16[_param1][caller]].field_0, loanPositions[stor16[_param1][caller]].field_256, loanPositions[stor16[_param1][caller]].field_512, loanPositions[stor16[_param1][caller]].field_768, loanPositions[stor16[_param1][caller]].field_1024, loanPositions[stor16[_param1][caller]].field_1280, loanPositions[stor16[_param1][caller]].field_1536, loanPositions[stor16[_param1][caller]].field_1792, loanPositions[stor16[_param1][caller]].field_2048, bool(loanPositions[stor16[_param1][caller]].field_2304), loanPositions[stor16[_param1][caller]].field_2560, loanPositions[stor16[_param1][caller]].field_1536, stor2
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >=′ 32
  if not ext_call.return_data[0]:
      revert with 0, 'BZxLoanHealth::withdrawPosition: OracleInterface.didWithdrawPosition failed'
  log LogWithdrawPosition(
        bytes32 loanOrderHash=loanPositions[stor16[_param1][caller]].field_1536,
        address trader=loanPositions[stor16[_param1][caller]].field_1536,
        uint256 positionAmount=loanPositions[stor16[_param1][caller]].field_2560,
        uint256 remainingPosition=orders[_param1].field_2304,
        uint256 positionId=caller)
  stor2 = 0
  stor0 = 1
  return loanPositions[stor16[_param1][caller]].field_1536


# hash = 0xf2fde38b
# getter = None
# const = None
# payable = True
def transferOwnership(address _newOwner) payable: 
  require calldata.size - 4 >=′ 32
  require caller == owner
  require _newOwner
  log OwnershipTransferred(
        address previousOwner=owner,
        address newOwner=_newOwner)
  owner = _newOwner


# hash = 0xf4fb9b2f
# getter = ['storage', 256, 0, ['add', ['sha3', ['sha3', ['data', ['cd', 4], 17]]], ['cd', 36]]]
# const = None
# payable = True
def orderList(address _param1, uint256 _param2) payable: 
  require calldata.size - 4 >=′ 64
  require _param2 < orderList[_param1]
  return orderList[_param1][_param2]


# hash = 0xf7a8c508
# getter = None
# const = None
# payable = True
def unknownf7a8c508(uint256 _param1, addr _param2) payable: 
  require calldata.size - 4 >=′ 64
  if not orders[_param1].field_0:
      return 0
  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
      return 0
  if not loanPositions[stor16[_param1][addr(_param2)]].field_2304:
      return 0
  if loanPositions[stor16[_param1][addr(_param2)]].field_2048 <= block.timestamp:
      if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
          if loanPositions[stor16[_param1][addr(_param2)]].field_512 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                          return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                 0,
                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                  else:
                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                          return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                      if loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                 0,
                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
              else:
                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                              return loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                     0,
                                     0
                      else:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                              return 0
                          if -loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                     0,
                                     0
                  else:
                      require ext_code.size(oracle[stor10[_param1].field_768])
                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                              gas gas_remaining wei
                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 96
                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                          if ext_call.return_data[32]:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0 / ext_call.return_data[32]:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                             0,
                                             0 / ext_call.return_data[32]
                              else:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                      return 0, 0, 0 / ext_call.return_data[32]
                                  if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                             0,
                                             0 / ext_call.return_data[32]
                      else:
                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                              if ext_call.return_data[32]:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 0,
                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                          return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                 0,
                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
          else:
              if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                  if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                      if 0 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                          if -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                              return -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                     0,
                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                      else:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768:
                              return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768, 
                                     0,
                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                  else:
                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                              return 0
                          if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0
                      else:
                          require ext_code.size(oracle[stor10[_param1].field_768])
                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                  gas gas_remaining wei
                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 96
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                              if ext_call.return_data[32]:
                                  if 0 > 0 / ext_call.return_data[32]:
                                      if -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 0,
                                                 0 / ext_call.return_data[32]
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0 / ext_call.return_data[32]:
                                          return 0, 0, 0 / ext_call.return_data[32]
                                      if 0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]), 
                                                 0,
                                                 0 / ext_call.return_data[32]
                          else:
                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                  if ext_call.return_data[32]:
                                      if 0 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                          if -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0,
                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                              return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]), 
                                                     0,
                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
              else:
                  require ext_code.size(oracle[stor10[_param1].field_768])
                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                          gas gas_remaining wei
                         args loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 96
                  if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                      if ext_call.return_data[32]:
                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                              if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                             0,
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                      return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                             0,
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                          else:
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if 0 / ext_call.return_data[32] > 0:
                                      if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                          return 0
                                      if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 0, 0
                              else:
                                  if not ext_call.return_data[0]:
                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                  else:
                                      if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                  gas gas_remaining wei
                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >=′ 96
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if ext_call.return_data[32]:
                                          if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0 / ext_call.return_data[32]
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                  return 0, 0, 0 / ext_call.return_data[32]
                                              if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0 / ext_call.return_data[32]
                                  else:
                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                          if ext_call.return_data[32]:
                                              if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                  if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0,
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                      return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                             0,
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                  else:
                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / loanPositions[stor16[_param1][addr(_param2)]].field_1536 == ext_call.return_data[0]:
                          if ext_call.return_data[32]:
                              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 0,
                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                          return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                 0,
                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0,
                                                     0
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                              return 0
                                          if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                     0,
                                                     0
                                  else:
                                      if not ext_call.return_data[0]:
                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                  gas gas_remaining wei
                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >=′ 96
                                      else:
                                          if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if ext_call.return_data[32]:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0,
                                                             0 / ext_call.return_data[32]
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                      return 0, 0, 0 / ext_call.return_data[32]
                                                  if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                             0,
                                                             0 / ext_call.return_data[32]
                                      else:
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                              if ext_call.return_data[32]:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 0,
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                          return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                 0,
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
      else:
          require ext_code.size(oracle[stor10[_param1].field_768])
          if loanPositions[stor16[_param1][addr(_param2)]].field_512 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                          gas gas_remaining wei
                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 96
                  if ext_call.return_data[32]:
                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                              return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                     0 / ext_call.return_data[32],
                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                      else:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                              return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                     0 / ext_call.return_data[32],
                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
              else:
                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                              gas gas_remaining wei
                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 96
                      if ext_call.return_data[32]:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                         0 / ext_call.return_data[32],
                                         0
                          else:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                  return 0, 0 / ext_call.return_data[32], 0
                              if -loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                         0 / ext_call.return_data[32],
                                         0
                  else:
                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                              gas gas_remaining wei
                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 96
                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                          if ext_call.return_data[32]:
                              if orders[_param1].field_256 != orders[_param1].field_0:
                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                              if ext_call.return_data[32]:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0 / ext_call.return_data[32]:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 0 / ext_call.return_data[32],
                                                 0 / ext_call.return_data[32]
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                          return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                      if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                 0 / ext_call.return_data[32],
                                                 0 / ext_call.return_data[32]
                      else:
                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                              if ext_call.return_data[32]:
                                  if orders[_param1].field_256 != orders[_param1].field_0:
                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                  if ext_call.return_data[32]:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0 / ext_call.return_data[32],
                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                              return 0, 
                                                     0 / ext_call.return_data[32],
                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                     0 / ext_call.return_data[32],
                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
          else:
              if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                  if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                              gas gas_remaining wei
                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                      if not ext_call.success:
                          revert with ext_call.return_data[0 len return_data.size]
                      require return_data.size >=′ 96
                      if ext_call.return_data[32]:
                          if 0 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                              if -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                  return -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                         0 / ext_call.return_data[32],
                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                          else:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768, 
                                         0 / ext_call.return_data[32],
                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                  else:
                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                  gas gas_remaining wei
                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 96
                          if ext_call.return_data[32]:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                  return 0, 0 / ext_call.return_data[32], 0
                              if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0
                      else:
                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                  gas gas_remaining wei
                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 96
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                              if ext_call.return_data[32]:
                                  if orders[_param1].field_256 != orders[_param1].field_0:
                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                  if ext_call.return_data[32]:
                                      if 0 > 0 / ext_call.return_data[32]:
                                          if -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0 / ext_call.return_data[32],
                                                     0 / ext_call.return_data[32]
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0 / ext_call.return_data[32]:
                                              return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                          if 0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]), 
                                                     0 / ext_call.return_data[32],
                                                     0 / ext_call.return_data[32]
                          else:
                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                  if ext_call.return_data[32]:
                                      if orders[_param1].field_256 != orders[_param1].field_0:
                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                  gas gas_remaining wei
                                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >=′ 96
                                      if ext_call.return_data[32]:
                                          if 0 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                              if -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                  return 0, 
                                                         0 / ext_call.return_data[32],
                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]), 
                                                         0 / ext_call.return_data[32],
                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
              else:
                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                          gas gas_remaining wei
                         args loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                  if not ext_call.success:
                      revert with ext_call.return_data[0 len return_data.size]
                  require return_data.size >=′ 96
                  if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                      if ext_call.return_data[32]:
                          if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_512:
                              if ext_call.return_data[32]:
                                  if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                      if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0 / ext_call.return_data[32],
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                              return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                     0 / ext_call.return_data[32],
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  else:
                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if 0 / ext_call.return_data[32] > 0:
                                              if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         0
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                  return 0, 0 / ext_call.return_data[32], 0
                                              if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                         0 / ext_call.return_data[32],
                                                         0
                                      else:
                                          if not ext_call.return_data[0]:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                          else:
                                              if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if ext_call.return_data[32]:
                                                  if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                          return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                      if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                          else:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                  if ext_call.return_data[32]:
                                                      if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                              return 0, 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                          else:
                              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if ext_call.return_data[32]:
                                      if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0 / ext_call.return_data[32],
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                              return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                     0 / ext_call.return_data[32],
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                      if ext_call.return_data[32]:
                                          if 0 / ext_call.return_data[32] > 0:
                                              if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         0
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                  return 0, 0 / ext_call.return_data[32], 0
                                              if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                         0 / ext_call.return_data[32],
                                                         0
                                  else:
                                      if not ext_call.return_data[0]:
                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                  gas gas_remaining wei
                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >=′ 96
                                      else:
                                          if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if ext_call.return_data[32]:
                                              if orders[_param1].field_256 != orders[_param1].field_0:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              if ext_call.return_data[32]:
                                                  if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                          return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                      if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                      else:
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                              if ext_call.return_data[32]:
                                                  if orders[_param1].field_256 != orders[_param1].field_0:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                  if ext_call.return_data[32]:
                                                      if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                              return 0, 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                  else:
                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / loanPositions[stor16[_param1][addr(_param2)]].field_1536 == ext_call.return_data[0]:
                          if ext_call.return_data[32]:
                              if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                  if ext_call.return_data[32]:
                                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                  return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                         0 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0 / ext_call.return_data[32],
                                                             0
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                      return 0, 0 / ext_call.return_data[32], 0
                                                  if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                             0 / ext_call.return_data[32],
                                                             0
                                          else:
                                              if not ext_call.return_data[0]:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              else:
                                                  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if ext_call.return_data[32]:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                              return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                              else:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                  return 0, 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                              else:
                                  if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                      if ext_call.return_data[32]:
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                  return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                         0 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  else:
                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                  gas gas_remaining wei
                                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >=′ 96
                                          if ext_call.return_data[32]:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0 / ext_call.return_data[32],
                                                             0
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                      return 0, 0 / ext_call.return_data[32], 0
                                                  if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                             0 / ext_call.return_data[32],
                                                             0
                                      else:
                                          if not ext_call.return_data[0]:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                          else:
                                              if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if ext_call.return_data[32]:
                                                  if orders[_param1].field_256 != orders[_param1].field_0:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                  if ext_call.return_data[32]:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                              return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                          else:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                  if ext_call.return_data[32]:
                                                      if orders[_param1].field_256 != orders[_param1].field_0:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                      if ext_call.return_data[32]:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                  return 0, 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
  else:
      if block.timestamp <= loanPositions[stor16[_param1][addr(_param2)]].field_2048:
          if not loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp:
              if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                  if loanPositions[stor16[_param1][addr(_param2)]].field_512 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                         0,
                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                          else:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                  return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                         0,
                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                      else:
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                             0,
                                             0
                              else:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                      return 0
                                  if -loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                             0,
                                             0
                          else:
                              require ext_code.size(oracle[stor10[_param1].field_768])
                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                      gas gas_remaining wei
                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 96
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if ext_call.return_data[32]:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0 / ext_call.return_data[32]:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0,
                                                     0 / ext_call.return_data[32]
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                              return 0, 0, 0 / ext_call.return_data[32]
                                          if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                     0,
                                                     0 / ext_call.return_data[32]
                              else:
                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                      if ext_call.return_data[32]:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0,
                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                  return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                         0,
                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                  else:
                      if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                              if 0 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                             0,
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768, 
                                             0,
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                          else:
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                      return 0
                                  if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0
                              else:
                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if ext_call.return_data[32]:
                                          if 0 > 0 / ext_call.return_data[32]:
                                              if -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0,
                                                         0 / ext_call.return_data[32]
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0 / ext_call.return_data[32]:
                                                  return 0, 0, 0 / ext_call.return_data[32]
                                              if 0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]), 
                                                         0,
                                                         0 / ext_call.return_data[32]
                                  else:
                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                          if ext_call.return_data[32]:
                                              if 0 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                  if -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0,
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                      return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]), 
                                                             0,
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                      else:
                          require ext_code.size(oracle[stor10[_param1].field_768])
                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                  gas gas_remaining wei
                                 args loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 96
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                              if ext_call.return_data[32]:
                                  if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                      if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0,
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                              return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                     0,
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  else:
                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if 0 / ext_call.return_data[32] > 0:
                                              if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                  return 0
                                              if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 0, 0
                                      else:
                                          if not ext_call.return_data[0]:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                          else:
                                              if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if ext_call.return_data[32]:
                                                  if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0 / ext_call.return_data[32]
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                          return 0, 0, 0 / ext_call.return_data[32]
                                                      if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0, 0 / ext_call.return_data[32]
                                          else:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                  if ext_call.return_data[32]:
                                                      if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0,
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                              return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                     0,
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                          else:
                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / loanPositions[stor16[_param1][addr(_param2)]].field_1536 == ext_call.return_data[0]:
                                  if ext_call.return_data[32]:
                                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0,
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                  return 0, 0, loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                         0,
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0,
                                                             0
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                      return 0
                                                  if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                             0,
                                                             0
                                          else:
                                              if not ext_call.return_data[0]:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              else:
                                                  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if ext_call.return_data[32]:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0,
                                                                     0 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                              return 0, 0, 0 / ext_call.return_data[32]
                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                     0,
                                                                     0 / ext_call.return_data[32]
                                              else:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0,
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                  return 0, 0, ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                         0,
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
              else:
                  require ext_code.size(oracle[stor10[_param1].field_768])
                  if loanPositions[stor16[_param1][addr(_param2)]].field_512 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                  gas gas_remaining wei
                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 96
                          if ext_call.return_data[32]:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                             0 / ext_call.return_data[32],
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                      return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                             0 / ext_call.return_data[32],
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                      else:
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                      gas gas_remaining wei
                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 96
                              if ext_call.return_data[32]:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 0 / ext_call.return_data[32],
                                                 0
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                          return 0, 0 / ext_call.return_data[32], 0
                                      if -loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                 0 / ext_call.return_data[32],
                                                 0
                          else:
                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                      gas gas_remaining wei
                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 96
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if ext_call.return_data[32]:
                                      if orders[_param1].field_256 != orders[_param1].field_0:
                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                  gas gas_remaining wei
                                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >=′ 96
                                      if ext_call.return_data[32]:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0 / ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         0 / ext_call.return_data[32]
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                  return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                              if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                         0 / ext_call.return_data[32],
                                                         0 / ext_call.return_data[32]
                              else:
                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                      if ext_call.return_data[32]:
                                          if orders[_param1].field_256 != orders[_param1].field_0:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                          if ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0 / ext_call.return_data[32],
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                      return 0, 
                                                             0 / ext_call.return_data[32],
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                             0 / ext_call.return_data[32],
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                  else:
                      if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                      gas gas_remaining wei
                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 96
                              if ext_call.return_data[32]:
                                  if 0 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 0 / ext_call.return_data[32],
                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768, 
                                                 0 / ext_call.return_data[32],
                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                          else:
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if ext_call.return_data[32]:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                          return 0, 0 / ext_call.return_data[32], 0
                                      if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0
                              else:
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if ext_call.return_data[32]:
                                          if orders[_param1].field_256 != orders[_param1].field_0:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                          if ext_call.return_data[32]:
                                              if 0 > 0 / ext_call.return_data[32]:
                                                  if -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0 / ext_call.return_data[32],
                                                             0 / ext_call.return_data[32]
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0 / ext_call.return_data[32]:
                                                      return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                  if 0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]), 
                                                             0 / ext_call.return_data[32],
                                                             0 / ext_call.return_data[32]
                                  else:
                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                          if ext_call.return_data[32]:
                                              if orders[_param1].field_256 != orders[_param1].field_0:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              if ext_call.return_data[32]:
                                                  if 0 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                      if -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 0 / ext_call.return_data[32],
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                          return 0, 
                                                                 0 / ext_call.return_data[32],
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]), 
                                                                 0 / ext_call.return_data[32],
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                      else:
                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                  gas gas_remaining wei
                                 args loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                          if not ext_call.success:
                              revert with ext_call.return_data[0 len return_data.size]
                          require return_data.size >=′ 96
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                              if ext_call.return_data[32]:
                                  if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                      if ext_call.return_data[32]:
                                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                              if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0 / ext_call.return_data[32],
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                                      return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                             0 / ext_call.return_data[32],
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if 0 / ext_call.return_data[32] > 0:
                                                      if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 0 / ext_call.return_data[32],
                                                                 0
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                          return 0, 0 / ext_call.return_data[32], 0
                                                      if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                                 0 / ext_call.return_data[32],
                                                                 0
                                              else:
                                                  if not ext_call.return_data[0]:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                  else:
                                                      if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      if ext_call.return_data[32]:
                                                          if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                                  return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                              if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                  else:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                          if ext_call.return_data[32]:
                                                              if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                  if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             0 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                                      return 0, 
                                                                             0 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                             0 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                  else:
                                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                  gas gas_remaining wei
                                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                          if not ext_call.success:
                                              revert with ext_call.return_data[0 len return_data.size]
                                          require return_data.size >=′ 96
                                          if ext_call.return_data[32]:
                                              if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             0 / ext_call.return_data[32],
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                                      return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                             0 / ext_call.return_data[32],
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                              if ext_call.return_data[32]:
                                                  if 0 / ext_call.return_data[32] > 0:
                                                      if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 0 / ext_call.return_data[32],
                                                                 0
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                          return 0, 0 / ext_call.return_data[32], 0
                                                      if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                                 0 / ext_call.return_data[32],
                                                                 0
                                          else:
                                              if not ext_call.return_data[0]:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              else:
                                                  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if ext_call.return_data[32]:
                                                      if orders[_param1].field_256 != orders[_param1].field_0:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                      if ext_call.return_data[32]:
                                                          if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                                  return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                              if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                              else:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if orders[_param1].field_256 != orders[_param1].field_0:
                                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                      gas gas_remaining wei
                                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              require return_data.size >=′ 96
                                                          if ext_call.return_data[32]:
                                                              if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                  if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             0 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                                      return 0, 
                                                                             0 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                             0 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                          else:
                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / loanPositions[stor16[_param1][addr(_param2)]].field_1536 == ext_call.return_data[0]:
                                  if ext_call.return_data[32]:
                                      if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                          if ext_call.return_data[32]:
                                              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 0 / ext_call.return_data[32],
                                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                          return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                 0 / ext_call.return_data[32],
                                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              else:
                                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     0
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                              return 0, 0 / ext_call.return_data[32], 0
                                                          if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     0
                                                  else:
                                                      if not ext_call.return_data[0]:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                      else:
                                                          if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                      gas gas_remaining wei
                                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              require return_data.size >=′ 96
                                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                          if ext_call.return_data[32]:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             0 / ext_call.return_data[32],
                                                                             0 / ext_call.return_data[32]
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                      return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                  if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                             0 / ext_call.return_data[32],
                                                                             0 / ext_call.return_data[32]
                                                      else:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                              if ext_call.return_data[32]:
                                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                 0 / ext_call.return_data[32],
                                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                  else:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                          return 0, 
                                                                                 0 / ext_call.return_data[32],
                                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                 0 / ext_call.return_data[32],
                                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                      else:
                                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                              if ext_call.return_data[32]:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 0 / ext_call.return_data[32],
                                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                          return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                 0 / ext_call.return_data[32],
                                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                                  if ext_call.return_data[32]:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     0
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                              return 0, 0 / ext_call.return_data[32], 0
                                                          if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     0
                                              else:
                                                  if not ext_call.return_data[0]:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                  else:
                                                      if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      if ext_call.return_data[32]:
                                                          if orders[_param1].field_256 != orders[_param1].field_0:
                                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                      gas gas_remaining wei
                                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              require return_data.size >=′ 96
                                                          if ext_call.return_data[32]:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             0 / ext_call.return_data[32],
                                                                             0 / ext_call.return_data[32]
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                      return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                  if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                             0 / ext_call.return_data[32],
                                                                             0 / ext_call.return_data[32]
                                                  else:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                          if ext_call.return_data[32]:
                                                              if orders[_param1].field_256 != orders[_param1].field_0:
                                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                          gas gas_remaining wei
                                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  require return_data.size >=′ 96
                                                              if ext_call.return_data[32]:
                                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                 0 / ext_call.return_data[32],
                                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                  else:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                          return 0, 
                                                                                 0 / ext_call.return_data[32],
                                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                 0 / ext_call.return_data[32],
                                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
          else:
              if (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / loanPositions[stor16[_param1][addr(_param2)]].field_2048 - block.timestamp == traderLoanInterest[stor16[_param1][addr(_param2)]].field_0:
                  if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                      if loanPositions[stor16[_param1][addr(_param2)]].field_512 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                      return 0, 
                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                          else:
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 0
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                          return 0, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 0
                                      if -loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 0
                              else:
                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if ext_call.return_data[32]:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0 / ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                         0 / ext_call.return_data[32]
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                  return 0, 
                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                         0 / ext_call.return_data[32]
                                              if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                         0 / ext_call.return_data[32]
                                  else:
                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                          if ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                      return 0, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                      else:
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                  if 0 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  else:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          return 0, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                          return 0, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 0
                                      if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                 0
                                  else:
                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if ext_call.return_data[32]:
                                              if 0 > 0 / ext_call.return_data[32]:
                                                  if -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             0 / ext_call.return_data[32]
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0 / ext_call.return_data[32]:
                                                      return 0, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             0 / ext_call.return_data[32]
                                                  if 0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]), 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             0 / ext_call.return_data[32]
                                      else:
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                              if ext_call.return_data[32]:
                                                  if 0 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                      if -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                          return 0, 
                                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]), 
                                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                 ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                          else:
                              require ext_code.size(oracle[stor10[_param1].field_768])
                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                      gas gas_remaining wei
                                     args loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 96
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                  if ext_call.return_data[32]:
                                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                          if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                                  return 0, 
                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if 0 / ext_call.return_data[32] > 0:
                                                  if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             0
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                      return 0, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             0
                                                  if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             0
                                          else:
                                              if not ext_call.return_data[0]:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              else:
                                                  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if ext_call.return_data[32]:
                                                      if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                     0 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                              return 0, 
                                                                     (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                     0 / ext_call.return_data[32]
                                                          if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                     0 / ext_call.return_data[32]
                                              else:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                              if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                                  return 0, 
                                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                              else:
                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / loanPositions[stor16[_param1][addr(_param2)]].field_1536 == ext_call.return_data[0]:
                                      if ext_call.return_data[32]:
                                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                      return 0, 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                 0
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                          return 0, 
                                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                 0
                                                      if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                 (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                 0
                                              else:
                                                  if not ext_call.return_data[0]:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                  else:
                                                      if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      if ext_call.return_data[32]:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                         0 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                  return 0, 
                                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                         0 / ext_call.return_data[32]
                                                              if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                         (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                         0 / ext_call.return_data[32]
                                                  else:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                          if ext_call.return_data[32]:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                      return 0, 
                                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                             (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600,
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                  else:
                      require ext_code.size(oracle[stor10[_param1].field_768])
                      if loanPositions[stor16[_param1][addr(_param2)]].field_512 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                      gas gas_remaining wei
                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 96
                              if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                  if ext_call.return_data[32]:
                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                     0 / ext_call.return_data[32],
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                      else:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                              return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                     0 / ext_call.return_data[32],
                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                      if ext_call.return_data[32]:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                  return 0, 
                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                          else:
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                      if ext_call.return_data[32]:
                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         0
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                  return 0, 0 / ext_call.return_data[32], 0
                                              if -loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                         0 / ext_call.return_data[32],
                                                         0
                                  else:
                                      if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                          if ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1536 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             0
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                      return 0, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             0
                                                  if -loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             0
                              else:
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      if ext_call.return_data[32]:
                                          if orders[_param1].field_256 != orders[_param1].field_0:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                          if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                              if ext_call.return_data[32]:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0 / ext_call.return_data[32]:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                 0 / ext_call.return_data[32],
                                                                 0 / ext_call.return_data[32]
                                                  else:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                          return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                      if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                                 0 / ext_call.return_data[32],
                                                                 0 / ext_call.return_data[32]
                                          else:
                                              if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                  if ext_call.return_data[32]:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > 0 / ext_call.return_data[32]:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                              return 0, 
                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                                          if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                  else:
                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                          if ext_call.return_data[32]:
                                              if orders[_param1].field_256 != orders[_param1].field_0:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                  if ext_call.return_data[32]:
                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                              return 0, 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                                     0 / ext_call.return_data[32],
                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              else:
                                                  if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1536 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1536 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                                                  return 0, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_1536 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1536, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                      else:
                          if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                          gas gas_remaining wei
                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                  if not ext_call.success:
                                      revert with ext_call.return_data[0 len return_data.size]
                                  require return_data.size >=′ 96
                                  if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                      if ext_call.return_data[32]:
                                          if 0 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                              if -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                         0 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768, 
                                                         0 / ext_call.return_data[32],
                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                  else:
                                      if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                          if ext_call.return_data[32]:
                                              if 0 > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  if -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return -loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              else:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      return 0, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                              else:
                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                      if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                          if ext_call.return_data[32]:
                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                  return 0, 0 / ext_call.return_data[32], 0
                                              if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0
                                      else:
                                          if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                              if ext_call.return_data[32]:
                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                      return 0, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             0
                                                  if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                             0
                                  else:
                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                              gas gas_remaining wei
                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                      if not ext_call.success:
                                          revert with ext_call.return_data[0 len return_data.size]
                                      require return_data.size >=′ 96
                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                          if ext_call.return_data[32]:
                                              if orders[_param1].field_256 != orders[_param1].field_0:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                              if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                  if ext_call.return_data[32]:
                                                      if 0 > 0 / ext_call.return_data[32]:
                                                          if -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0 / ext_call.return_data[32]:
                                                              return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                          if 0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     0 / ext_call.return_data[32]
                                              else:
                                                  if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if 0 > 0 / ext_call.return_data[32]:
                                                              if -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return -(0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         0 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0 / ext_call.return_data[32]:
                                                                  return 0, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         0 / ext_call.return_data[32]
                                                              if 0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]), 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         0 / ext_call.return_data[32]
                                      else:
                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                              if ext_call.return_data[32]:
                                                  if orders[_param1].field_256 != orders[_param1].field_0:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                  if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                      if ext_call.return_data[32]:
                                                          if 0 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                              if -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                  return 0, 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]), 
                                                                         0 / ext_call.return_data[32],
                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                  else:
                                                      if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                          if ext_call.return_data[32]:
                                                              if 0 > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                  if -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return -(ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                      return 0, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]), 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                          else:
                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                      gas gas_remaining wei
                                     args loanPositions[stor16[_param1][addr(_param2)]].field_512, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                              if not ext_call.success:
                                  revert with ext_call.return_data[0 len return_data.size]
                              require return_data.size >=′ 96
                              if not loanPositions[stor16[_param1][addr(_param2)]].field_1536:
                                  if ext_call.return_data[32]:
                                      if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                          if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                              if ext_call.return_data[32]:
                                                  if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                                      if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                          if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                                              return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  else:
                                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                          if 0 / ext_call.return_data[32] > 0:
                                                              if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0 / ext_call.return_data[32],
                                                                         0
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                                  return 0, 0 / ext_call.return_data[32], 0
                                                              if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                                         0 / ext_call.return_data[32],
                                                                         0
                                                      else:
                                                          if not ext_call.return_data[0]:
                                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                      gas gas_remaining wei
                                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              require return_data.size >=′ 96
                                                          else:
                                                              if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                          gas gas_remaining wei
                                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  require return_data.size >=′ 96
                                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                              if ext_call.return_data[32]:
                                                                  if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                  else:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                                          return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                      if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                          else:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                                  if ext_call.return_data[32]:
                                                                      if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     0 / ext_call.return_data[32],
                                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                      else:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                                              return 0, 
                                                                                     0 / ext_call.return_data[32],
                                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                                     0 / ext_call.return_data[32],
                                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                          else:
                                              if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                  if ext_call.return_data[32]:
                                                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                                          if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                              if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                                                  return 0, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                      else:
                                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                              if 0 / ext_call.return_data[32] > 0:
                                                                  if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             0
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                                      return 0, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             0
                                                                  if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             0
                                                          else:
                                                              if not ext_call.return_data[0]:
                                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                          gas gas_remaining wei
                                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  require return_data.size >=′ 96
                                                              else:
                                                                  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                              gas gas_remaining wei
                                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      require return_data.size >=′ 96
                                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                                  if ext_call.return_data[32]:
                                                                      if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                                      else:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                                              return 0, 
                                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                                          if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                              else:
                                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                                      if ext_call.return_data[32]:
                                                                          if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                              if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                          else:
                                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                                                  return 0, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                      else:
                                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                      gas gas_remaining wei
                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                              if not ext_call.success:
                                                  revert with ext_call.return_data[0 len return_data.size]
                                              require return_data.size >=′ 96
                                              if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                  if ext_call.return_data[32]:
                                                      if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                          if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                     0 / ext_call.return_data[32],
                                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                      else:
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                                              return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                                     0 / ext_call.return_data[32],
                                                                     loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              else:
                                                  if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if 0 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                              if (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (0 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]):
                                                                  return 0, 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (0 / ext_call.return_data[32]), 
                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                          else:
                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                                  if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                      if ext_call.return_data[32]:
                                                          if 0 / ext_call.return_data[32] > 0:
                                                              if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0 / ext_call.return_data[32],
                                                                         0
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                                  return 0, 0 / ext_call.return_data[32], 0
                                                              if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                                         0 / ext_call.return_data[32],
                                                                         0
                                                  else:
                                                      if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                          if ext_call.return_data[32]:
                                                              if 0 / ext_call.return_data[32] > 0:
                                                                  if (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             0
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -0 / ext_call.return_data[32]:
                                                                      return 0, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             0
                                                                  if -0 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (0 / ext_call.return_data[32]), 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             0
                                              else:
                                                  if not ext_call.return_data[0]:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                  else:
                                                      if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      if ext_call.return_data[32]:
                                                          if orders[_param1].field_256 != orders[_param1].field_0:
                                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                      gas gas_remaining wei
                                                                     args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              require return_data.size >=′ 96
                                                          if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                              if ext_call.return_data[32]:
                                                                  if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                  else:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                                          return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                      if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                          else:
                                                              if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                                  if ext_call.return_data[32]:
                                                                      if 0 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                                      else:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= 0:
                                                                              return 0, 
                                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                                          if 0 <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                  else:
                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                          if ext_call.return_data[32]:
                                                              if orders[_param1].field_256 != orders[_param1].field_0:
                                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                          gas gas_remaining wei
                                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  require return_data.size >=′ 96
                                                              if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                                  if ext_call.return_data[32]:
                                                                      if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     0 / ext_call.return_data[32],
                                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                      else:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                                              return 0, 
                                                                                     0 / ext_call.return_data[32],
                                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                                     0 / ext_call.return_data[32],
                                                                                     ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                              else:
                                                                  if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                                      if ext_call.return_data[32]:
                                                                          if 0 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                              if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                          else:
                                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]):
                                                                                  return 0, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (0 / ext_call.return_data[32]), 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                              else:
                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / loanPositions[stor16[_param1][addr(_param2)]].field_1536 == ext_call.return_data[0]:
                                      if ext_call.return_data[32]:
                                          if orders[_param1].field_256 == loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                              if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                  if ext_call.return_data[32]:
                                                      if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                  return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                         0 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                      else:
                                                          if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             0 / ext_call.return_data[32],
                                                                             0
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                                      return 0, 0 / ext_call.return_data[32], 0
                                                                  if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                             0 / ext_call.return_data[32],
                                                                             0
                                                          else:
                                                              if not ext_call.return_data[0]:
                                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                          gas gas_remaining wei
                                                                         args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  require return_data.size >=′ 96
                                                              else:
                                                                  if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                              gas gas_remaining wei
                                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      require return_data.size >=′ 96
                                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                                  if ext_call.return_data[32]:
                                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     0 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                                      else:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                              return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                     0 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                              else:
                                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                                      if ext_call.return_data[32]:
                                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                         0 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                          else:
                                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                                  return 0, 
                                                                                         0 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                         0 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                              else:
                                                  if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                      if ext_call.return_data[32]:
                                                          if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                      return 0, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                          else:
                                                              if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                 ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                 0
                                                                  else:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                                          return 0, 
                                                                                 ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                 0
                                                                      if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                 ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                 0
                                                              else:
                                                                  if not ext_call.return_data[0]:
                                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                              gas gas_remaining wei
                                                                             args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      require return_data.size >=′ 96
                                                                  else:
                                                                      if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                                  gas gas_remaining wei
                                                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                          if not ext_call.success:
                                                                              revert with ext_call.return_data[0 len return_data.size]
                                                                          require return_data.size >=′ 96
                                                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                                      if ext_call.return_data[32]:
                                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         0 / ext_call.return_data[32]
                                                                          else:
                                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                                  return 0, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         0 / ext_call.return_data[32]
                                                                              if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         0 / ext_call.return_data[32]
                                                                  else:
                                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                                          if ext_call.return_data[32]:
                                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                              else:
                                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                                      return 0, 
                                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                          else:
                                              if orders[_param1].field_0 == loanPositions[stor16[_param1][addr(_param2)]].field_256:
                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                          gas gas_remaining wei
                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                  if not ext_call.success:
                                                      revert with ext_call.return_data[0 len return_data.size]
                                                  require return_data.size >=′ 96
                                                  if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                      if ext_call.return_data[32]:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                         0 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                          else:
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                  return 0, 0 / ext_call.return_data[32], loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                         0 / ext_call.return_data[32],
                                                                         loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                  else:
                                                      if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                          if ext_call.return_data[32]:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - loanPositions[stor16[_param1][addr(_param2)]].field_768 + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                      return 0, 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_768 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - loanPositions[stor16[_param1][addr(_param2)]].field_768 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                             loanPositions[stor16[_param1][addr(_param2)]].field_768
                                              else:
                                                  if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                              gas gas_remaining wei
                                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                      if not ext_call.success:
                                                          revert with ext_call.return_data[0 len return_data.size]
                                                      require return_data.size >=′ 96
                                                      if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                          if ext_call.return_data[32]:
                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                             0 / ext_call.return_data[32],
                                                                             0
                                                              else:
                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                                      return 0, 0 / ext_call.return_data[32], 0
                                                                  if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                             0 / ext_call.return_data[32],
                                                                             0
                                                      else:
                                                          if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                              if ext_call.return_data[32]:
                                                                  if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0:
                                                                      if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                 ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                 0
                                                                  else:
                                                                      if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]:
                                                                          return 0, 
                                                                                 ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                 0
                                                                      if -ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                          return loanPositions[stor16[_param1][addr(_param2)]].field_1280 + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                 ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                 0
                                                  else:
                                                      if not ext_call.return_data[0]:
                                                          require ext_code.size(oracle[stor10[_param1].field_768])
                                                          static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                  gas gas_remaining wei
                                                                 args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                          if not ext_call.success:
                                                              revert with ext_call.return_data[0 len return_data.size]
                                                          require return_data.size >=′ 96
                                                      else:
                                                          if orders[_param1].field_0 != loanPositions[stor16[_param1][addr(_param2)]].field_512:
                                                              require ext_code.size(oracle[stor10[_param1].field_768])
                                                              static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                      gas gas_remaining wei
                                                                     args orders[_param1].field_0, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                              if not ext_call.success:
                                                                  revert with ext_call.return_data[0 len return_data.size]
                                                              require return_data.size >=′ 96
                                                      if not loanPositions[stor16[_param1][addr(_param2)]].field_768:
                                                          if ext_call.return_data[32]:
                                                              if orders[_param1].field_256 != orders[_param1].field_0:
                                                                  require ext_code.size(oracle[stor10[_param1].field_768])
                                                                  static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                          gas gas_remaining wei
                                                                         args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                  if not ext_call.success:
                                                                      revert with ext_call.return_data[0 len return_data.size]
                                                                  require return_data.size >=′ 96
                                                              if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                                  if ext_call.return_data[32]:
                                                                      if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                          if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                     0 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                                      else:
                                                                          if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                              return 0, 0 / ext_call.return_data[32], 0 / ext_call.return_data[32]
                                                                          if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                              return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                     0 / ext_call.return_data[32],
                                                                                     0 / ext_call.return_data[32]
                                                              else:
                                                                  if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                                      if ext_call.return_data[32]:
                                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > 0 / ext_call.return_data[32]:
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (0 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         0 / ext_call.return_data[32]
                                                                          else:
                                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                                  return 0, 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         0 / ext_call.return_data[32]
                                                                              if (0 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (0 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                         ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                         0 / ext_call.return_data[32]
                                                      else:
                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / loanPositions[stor16[_param1][addr(_param2)]].field_768 == ext_call.return_data[0]:
                                                              if ext_call.return_data[32]:
                                                                  if orders[_param1].field_256 != orders[_param1].field_0:
                                                                      require ext_code.size(oracle[stor10[_param1].field_768])
                                                                      static call oracle[stor10[_param1].field_768].0x6599aa0 with:
                                                                              gas gas_remaining wei
                                                                             args orders[_param1].field_256, loanPositions[stor16[_param1][addr(_param2)]].field_256, -1
                                                                      if not ext_call.success:
                                                                          revert with ext_call.return_data[0 len return_data.size]
                                                                      require return_data.size >=′ 96
                                                                  if not (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600:
                                                                      if ext_call.return_data[32]:
                                                                          if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                         0 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                          else:
                                                                              if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                                  return 0, 
                                                                                         0 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                              if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                  return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                         0 / ext_call.return_data[32],
                                                                                         ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                  else:
                                                                      if ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 == ext_call.return_data[0]:
                                                                          if ext_call.return_data[32]:
                                                                              if ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32] > ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]:
                                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280 >= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                      return (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + loanPositions[stor16[_param1][addr(_param2)]].field_1280, 
                                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                              else:
                                                                                  if loanPositions[stor16[_param1][addr(_param2)]].field_1280 <= (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]):
                                                                                      return 0, 
                                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
                                                                                  if (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]) <= loanPositions[stor16[_param1][addr(_param2)]].field_1280:
                                                                                      return loanPositions[stor16[_param1][addr(_param2)]].field_1280 - (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]) + (ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_1536 / ext_call.return_data[32]), 
                                                                                             ext_call.return_data[0] * (loanPositions[stor16[_param1][addr(_param2)]].field_2048 * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) - (block.timestamp * traderLoanInterest[stor16[_param1][addr(_param2)]].field_0) / 24 * 3600 / ext_call.return_data[32],
                                                                                             ext_call.return_data[0] * loanPositions[stor16[_param1][addr(_param2)]].field_768 / ext_call.return_data[32]
  revert


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert with 0, 'fallback not allowed'


