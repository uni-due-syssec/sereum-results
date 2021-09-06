true_positive: no  
fp_type: unknown  
source: yes

# Notes

The analyzed transaction is definitely not an attack, since no attack contract
seems to be involved.

The reason for the re-entrancy locking is the use of the `SafeMathOZ` library,
which checks for integer overflows.

This contract/function seems safe. A re-entrancy is probably not possible,
since the SafeMath library will revert the transaction, when there is not
enough `stake` available, i.e., it would underflow from 0 to uint256 maximum.
In this case `SafeMathOZ` requires the second operand to be smaller than the
first for subtraction. 

It seems to be a rather bad coding practice to rely on a SafeMath library for
such checks, which are relevant for the business logic of the contract.


This is the first called function of the contract:

```solidity
function buyForWorkOrder(
        uint256 _marketorderIdx,
        address _workerpool,
        address _app,
        address _dataset,
        string  _params,
        address _callback,
        address _beneficiary)
external returns (address)
{
        address requester = msg.sender;
/// (1.) Sereum External Call
/// This external call trigger a re-entrancy into the lockForOrder function
        require(marketplace.consumeMarketOrderAsk(_marketorderIdx, requester, _workerpool));

/// (3.) Sereum Write to locked variable
        uint256 emitcost = lockWorkOrderCost(requester, _workerpool, _app, _dataset);

/// We don't even get here in the trace. We don't see any CREATE instruction,
/// so this can't actually be executed before the re-entrancy detection alerts
/// and aborts the transaction.
        WorkOrder workorder = new WorkOrder(
                _marketorderIdx,
                requester,
                _app,
                _dataset,
                _workerpool,
                emitcost,
                _params,
                _callback,
                _beneficiary
        );

        m_woidRegistered[workorder] = true;

        require(WorkerPool(_workerpool).emitWorkOrder(workorder, _marketorderIdx));

        emit WorkOrderActivated(workorder, _workerpool);
        return workorder;
}


function lockWorkOrderCost(
        address _requester,
        address _workerpool, // Address of a smartcontract
        address _app,        // Address of a smartcontract
        address _dataset)    // Address of a smartcontract
internal returns (uint256)
{
        // APP
        App app = App(_app);
        require(appHub.isAppRegistered (_app));
        // initialize usercost with dapp price
        uint256 emitcost = app.m_appPrice();

        // DATASET
        if (_dataset != address(0)) // address(0) → no dataset
        {
                Dataset dataset = Dataset(_dataset);
                require(datasetHub.isDatasetRegistred(_dataset));
                // add optional datasetPrice for userCost
                emitcost = emitcost.add(dataset.m_datasetPrice());
        }

        // WORKERPOOL
        require(workerPoolHub.isWorkerPoolRegistered(_workerpool));

/// This is the same function, which 
        require(lock(_requester, emitcost)); // Lock funds for app + dataset payment

        return emitcost;
}
```

This is the function, which results in the write-locks:

```solidity
/// relevant data types
mapping(address => IexecLib.Account) public m_accounts;
struct Account
{
        uint256 stake;
        uint256 locked;
}

function lockForOrder(address _user, uint256 _amount) public onlyMarketplace returns (bool)
{
        require(lock(_user, _amount));
        return true;
}

function lock(address _user, uint256 _amount) internal returns (bool)
{
/// (2.) Sereum Lock
/// Here the _user adddres is the same as the msg.sender and thus the requester variable
/// in the first call buyForWorkOrder.
/// This locks the m_accounts[_user].(stake|locked) variable, because both use
/// the SafeMath library to add/sub the integer. This includes an integer
/// overflow check and as such a conditional branch
        m_accounts[_user].stake  = m_accounts[_user].stake.sub(_amount);
        m_accounts[_user].locked = m_accounts[_user].locked.add(_amount);
        return true;
}
```
