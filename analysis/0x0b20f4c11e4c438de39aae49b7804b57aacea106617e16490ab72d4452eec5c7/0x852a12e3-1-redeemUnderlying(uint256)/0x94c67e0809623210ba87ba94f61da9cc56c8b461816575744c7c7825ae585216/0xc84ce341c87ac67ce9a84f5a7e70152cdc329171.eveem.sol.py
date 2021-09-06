# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0xC84Ce341c87aC67cE9a84f5a7E70152CDC329171 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    paused # mask: a s
    # storage address 0
    comptrollerAddress # mask: a s
    # storage address 1
    _assetPrices
    # storage address 2
    anchorAdminAddress # mask: a s
    # storage address 3
    pendingAnchorAdminAddress # mask: a s
    # storage address 4
    posterAddress # mask: a s
    # storage address 5
    maxSwing # mask: a s
    # storage address 6
    anchors
    # storage address 7
    pendingAnchors
# hash = 0x00e4768b
# getter = None
# const = None
# payable = False
def setPrice(address _asset, uint256 _requestedPriceMantissa): # not payable
  require calldata.size - 4 >= 64
  if posterAddress != caller:
      log OracleFailure(
            address msgSender=caller,
            address asset=addr(_asset),
            uint256 error=1,
            uint256 info=8,
            uint256 detail=0)
      return 1
  if pendingAnchors[addr(_asset)]:
      if pendingAnchors[addr(_asset)] <= _requestedPriceMantissa:
          require pendingAnchors[addr(_asset)] <= _requestedPriceMantissa
          if not _requestedPriceMantissa - pendingAnchors[addr(_asset)]:
              require pendingAnchors[addr(_asset)]
              if 0 / pendingAnchors[addr(_asset)] > maxSwing:
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_asset),
                        uint256 error=2,
                        uint256 info=6,
                        uint256 detail=0 / pendingAnchors[addr(_asset)])
                  return 2
          else:
              require (10^18 * _requestedPriceMantissa) - (10^18 * pendingAnchors[addr(_asset)]) / _requestedPriceMantissa - pendingAnchors[addr(_asset)] == 10^18
              require pendingAnchors[addr(_asset)]
              if (10^18 * _requestedPriceMantissa) - (10^18 * pendingAnchors[addr(_asset)]) / pendingAnchors[addr(_asset)] > maxSwing:
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_asset),
                        uint256 error=2,
                        uint256 info=6,
                        uint256 detail=(10^18 * _requestedPriceMantissa) - (10^18 * pendingAnchors[addr(_asset)]) / pendingAnchors[addr(_asset)])
                  return 2
      else:
          require _requestedPriceMantissa <= pendingAnchors[addr(_asset)]
          if not pendingAnchors[addr(_asset)] - _requestedPriceMantissa:
              require pendingAnchors[addr(_asset)]
              if 0 / pendingAnchors[addr(_asset)] > maxSwing:
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_asset),
                        uint256 error=2,
                        uint256 info=6,
                        uint256 detail=0 / pendingAnchors[addr(_asset)])
                  return 2
          else:
              require (10^18 * pendingAnchors[addr(_asset)]) - (10^18 * _requestedPriceMantissa) / pendingAnchors[addr(_asset)] - _requestedPriceMantissa == 10^18
              require pendingAnchors[addr(_asset)]
              if (10^18 * pendingAnchors[addr(_asset)]) - (10^18 * _requestedPriceMantissa) / pendingAnchors[addr(_asset)] > maxSwing:
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_asset),
                        uint256 error=2,
                        uint256 info=6,
                        uint256 detail=(10^18 * pendingAnchors[addr(_asset)]) - (10^18 * _requestedPriceMantissa) / pendingAnchors[addr(_asset)])
                  return 2
      if not pendingAnchors[addr(_asset)]:
          log OracleFailure(
                address msgSender=caller,
                address asset=addr(_asset),
                uint256 error=2,
                uint256 info=7,
                uint256 detail=0)
          return 2
      if not _requestedPriceMantissa:
          log OracleFailure(
                address msgSender=caller,
                address asset=addr(_asset),
                uint256 error=2,
                uint256 info=9,
                uint256 detail=0)
          return 2
      if pendingAnchors[addr(_asset)]:
          pendingAnchors[addr(_asset)] = 0
      if (block.number / 120) + 1 > 0:
          anchors[addr(_asset)].field_0 = (block.number / 120) + 1
          anchors[addr(_asset)].field_256 = _requestedPriceMantissa
      _assetPrices[addr(_asset)] = _requestedPriceMantissa
      log PricePosted(
            address asset=addr(_asset),
            uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
            uint256 requestedPriceMantissa=_requestedPriceMantissa,
            uint256 newPriceMantissa=_requestedPriceMantissa)
  else:
      if not anchors[addr(_asset)].field_0:
          if not _requestedPriceMantissa:
              log OracleFailure(
                    address msgSender=caller,
                    address asset=addr(_asset),
                    uint256 error=2,
                    uint256 info=7,
                    uint256 detail=0)
              return 2
          if not _requestedPriceMantissa:
              log OracleFailure(
                    address msgSender=caller,
                    address asset=addr(_asset),
                    uint256 error=2,
                    uint256 info=9,
                    uint256 detail=0)
              return 2
          if pendingAnchors[addr(_asset)]:
              pendingAnchors[addr(_asset)] = 0
          if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
              anchors[addr(_asset)].field_0 = (block.number / 120) + 1
              anchors[addr(_asset)].field_256 = _requestedPriceMantissa
          _assetPrices[addr(_asset)] = _requestedPriceMantissa
          log PricePosted(
                address asset=addr(_asset),
                uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                uint256 requestedPriceMantissa=_requestedPriceMantissa,
                uint256 newPriceMantissa=_requestedPriceMantissa)
      else:
          if maxSwing + 10^18 < 10^18:
              log OracleFailure(
                    address msgSender=caller,
                    address asset=addr(_asset),
                    uint256 error=2,
                    uint256 info=5,
                    uint256 detail=12)
              return 2
          if not anchors[addr(_asset)].field_256:
              if _requestedPriceMantissa > 0:
                  if anchors[addr(_asset)].field_256:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=9,
                            uint256 detail=0)
                  else:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=7,
                            uint256 detail=0)
                  return 2
              if maxSwing > 10^18:
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_asset),
                        uint256 error=2,
                        uint256 info=5,
                        uint256 detail=12)
                  return 2
              if not anchors[addr(_asset)].field_256:
                  if _requestedPriceMantissa < 0:
                      if anchors[addr(_asset)].field_256:
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_asset),
                                uint256 error=2,
                                uint256 info=9,
                                uint256 detail=0)
                      else:
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_asset),
                                uint256 error=2,
                                uint256 info=7,
                                uint256 detail=0)
                      return 2
                  if not anchors[addr(_asset)].field_256:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=7,
                            uint256 detail=0)
                      return 2
                  if not _requestedPriceMantissa:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=9,
                            uint256 detail=0)
                      return 2
                  if pendingAnchors[addr(_asset)]:
                      pendingAnchors[addr(_asset)] = 0
                  if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
                      anchors[addr(_asset)].field_0 = (block.number / 120) + 1
                      anchors[addr(_asset)].field_256 = _requestedPriceMantissa
                  _assetPrices[addr(_asset)] = _requestedPriceMantissa
                  log PricePosted(
                        address asset=addr(_asset),
                        uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                        uint256 requestedPriceMantissa=_requestedPriceMantissa,
                        uint256 newPriceMantissa=_requestedPriceMantissa)
              else:
                  require (10^18 * anchors[addr(_asset)].field_256) - (maxSwing * anchors[addr(_asset)].field_256) / anchors[addr(_asset)].field_256 == -maxSwing + 10^18
                  require (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 >= 5 * 10^17
                  if not anchors[addr(_asset)].field_256:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=7,
                            uint256 detail=0)
                      return 2
                  if _requestedPriceMantissa >= (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18:
                      if not _requestedPriceMantissa:
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_asset),
                                uint256 error=2,
                                uint256 info=9,
                                uint256 detail=0)
                          return 2
                      if pendingAnchors[addr(_asset)]:
                          pendingAnchors[addr(_asset)] = 0
                      if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
                          anchors[addr(_asset)].field_0 = (block.number / 120) + 1
                          anchors[addr(_asset)].field_256 = _requestedPriceMantissa
                      _assetPrices[addr(_asset)] = _requestedPriceMantissa
                      log PricePosted(
                            address asset=addr(_asset),
                            uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                            uint256 requestedPriceMantissa=_requestedPriceMantissa,
                            uint256 newPriceMantissa=_requestedPriceMantissa)
                  else:
                      if not (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18:
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_asset),
                                uint256 error=2,
                                uint256 info=9,
                                uint256 detail=0)
                          return 2
                      if pendingAnchors[addr(_asset)]:
                          pendingAnchors[addr(_asset)] = 0
                      if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
                          anchors[addr(_asset)].field_0 = (block.number / 120) + 1
                          anchors[addr(_asset)].field_256 = (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18
                      _assetPrices[addr(_asset)] = (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18
                      log PricePosted(
                            address asset=addr(_asset),
                            uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                            uint256 requestedPriceMantissa=_requestedPriceMantissa,
                            uint256 newPriceMantissa=(10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18)
                      log CappedPricePosted(
                            address asset=addr(_asset),
                            uint256 requestedPriceMantissa=_requestedPriceMantissa,
                            uint256 anchorPriceMantissa=anchors[addr(_asset)].field_256,
                            uint256 cappedPriceMantissa=(10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18)
          else:
              if (maxSwing * anchors[addr(_asset)].field_256) + (10^18 * anchors[addr(_asset)].field_256) / anchors[addr(_asset)].field_256 != maxSwing + 10^18:
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_asset),
                        uint256 error=2,
                        uint256 info=5,
                        uint256 detail=12)
                  return 2
              if (maxSwing * anchors[addr(_asset)].field_256) + (10^18 * anchors[addr(_asset)].field_256) + 5 * 10^17 < 5 * 10^17:
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_asset),
                        uint256 error=2,
                        uint256 info=5,
                        uint256 detail=12)
                  return 2
              if _requestedPriceMantissa > (10^18 * anchors[addr(_asset)].field_256) + (maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18:
                  if not anchors[addr(_asset)].field_256:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=7,
                            uint256 detail=0)
                      return 2
                  if not (10^18 * anchors[addr(_asset)].field_256) + (maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=9,
                            uint256 detail=0)
                      return 2
                  if pendingAnchors[addr(_asset)]:
                      pendingAnchors[addr(_asset)] = 0
                  if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
                      anchors[addr(_asset)].field_0 = (block.number / 120) + 1
                      anchors[addr(_asset)].field_256 = (10^18 * anchors[addr(_asset)].field_256) + (maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18
                  _assetPrices[addr(_asset)] = (10^18 * anchors[addr(_asset)].field_256) + (maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18
                  log PricePosted(
                        address asset=addr(_asset),
                        uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                        uint256 requestedPriceMantissa=_requestedPriceMantissa,
                        uint256 newPriceMantissa=(10^18 * anchors[addr(_asset)].field_256) + (maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18)
                  log CappedPricePosted(
                        address asset=addr(_asset),
                        uint256 requestedPriceMantissa=_requestedPriceMantissa,
                        uint256 anchorPriceMantissa=anchors[addr(_asset)].field_256,
                        uint256 cappedPriceMantissa=(10^18 * anchors[addr(_asset)].field_256) + (maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18)
              else:
                  if maxSwing > 10^18:
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_asset),
                            uint256 error=2,
                            uint256 info=5,
                            uint256 detail=12)
                      return 2
                  if not anchors[addr(_asset)].field_256:
                      if _requestedPriceMantissa < 0:
                          if anchors[addr(_asset)].field_256:
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_asset),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                          else:
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_asset),
                                    uint256 error=2,
                                    uint256 info=7,
                                    uint256 detail=0)
                          return 2
                      if not anchors[addr(_asset)].field_256:
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_asset),
                                uint256 error=2,
                                uint256 info=7,
                                uint256 detail=0)
                          return 2
                      if not _requestedPriceMantissa:
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_asset),
                                uint256 error=2,
                                uint256 info=9,
                                uint256 detail=0)
                          return 2
                      if pendingAnchors[addr(_asset)]:
                          pendingAnchors[addr(_asset)] = 0
                      if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
                          anchors[addr(_asset)].field_0 = (block.number / 120) + 1
                          anchors[addr(_asset)].field_256 = _requestedPriceMantissa
                      _assetPrices[addr(_asset)] = _requestedPriceMantissa
                      log PricePosted(
                            address asset=addr(_asset),
                            uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                            uint256 requestedPriceMantissa=_requestedPriceMantissa,
                            uint256 newPriceMantissa=_requestedPriceMantissa)
                  else:
                      require (10^18 * anchors[addr(_asset)].field_256) - (maxSwing * anchors[addr(_asset)].field_256) / anchors[addr(_asset)].field_256 == -maxSwing + 10^18
                      require (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 >= 5 * 10^17
                      if not anchors[addr(_asset)].field_256:
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_asset),
                                uint256 error=2,
                                uint256 info=7,
                                uint256 detail=0)
                          return 2
                      if _requestedPriceMantissa >= (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18:
                          if not _requestedPriceMantissa:
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_asset),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                              return 2
                          if pendingAnchors[addr(_asset)]:
                              pendingAnchors[addr(_asset)] = 0
                          if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
                              anchors[addr(_asset)].field_0 = (block.number / 120) + 1
                              anchors[addr(_asset)].field_256 = _requestedPriceMantissa
                          _assetPrices[addr(_asset)] = _requestedPriceMantissa
                          log PricePosted(
                                address asset=addr(_asset),
                                uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                                uint256 requestedPriceMantissa=_requestedPriceMantissa,
                                uint256 newPriceMantissa=_requestedPriceMantissa)
                      else:
                          if not (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18:
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_asset),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                              return 2
                          if pendingAnchors[addr(_asset)]:
                              pendingAnchors[addr(_asset)] = 0
                          if (block.number / 120) + 1 > anchors[addr(_asset)].field_0:
                              anchors[addr(_asset)].field_0 = (block.number / 120) + 1
                              anchors[addr(_asset)].field_256 = (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18
                          _assetPrices[addr(_asset)] = (10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18
                          log PricePosted(
                                address asset=addr(_asset),
                                uint256 previousPriceMantissa=_assetPrices[addr(_asset)],
                                uint256 requestedPriceMantissa=_requestedPriceMantissa,
                                uint256 newPriceMantissa=(10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18)
                          log CappedPricePosted(
                                address asset=addr(_asset),
                                uint256 requestedPriceMantissa=_requestedPriceMantissa,
                                uint256 anchorPriceMantissa=anchors[addr(_asset)].field_256,
                                uint256 cappedPriceMantissa=(10^18 * anchors[addr(_asset)].field_256) + (-1 * maxSwing * anchors[addr(_asset)].field_256) + 5 * 10^17 / 10^18)
  return 0


# hash = 0x08f31857
# getter = ['storage', 160, 0, 2]
# const = None
# payable = False
def anchorAdmin(): # not payable
  return anchorAdminAddress


# hash = 0x0c9c6301
# getter = None
# const = ['return', 100000000000000000]
# payable = False
const maxSwingMantissa = 10^17


# hash = 0x183f3444
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 1]]]
# const = None
# payable = False
def _assetPrices(address _param1): # not payable
  require calldata.size - 4 >= 32
  return _assetPrices[_param1]


# hash = 0x26617c28
# getter = None
# const = None
# payable = False
def _setPaused(bool _requestedState): # not payable
  require calldata.size - 4 >= 32
  if anchorAdminAddress != caller:
      log OracleFailure(
            address msgSender=caller,
            address asset=0,
            uint256 error=1,
            uint256 info=1,
            uint256 detail=0)
      return 1
  paused = uint8(_requestedState)
  log SetPaused(bool newState=_requestedState)
  return 0


# hash = 0x41976e09
# getter = None
# const = None
# payable = False
def getPrice(address _token): # not payable
  require calldata.size - 4 >= 32
  if not paused:
      return _assetPrices[addr(_token)]
  else:
      return 0


# hash = 0x4352fa9f
# getter = None
# const = None
# payable = False
def setPrices(address[] _assets, uint256[] _requestedPriceMantissas): # not payable
  require calldata.size - 4 >= 64
  require _assets <= 4294967296
  require _assets + 36 <= calldata.size
  require _assets.length <= 4294967296 and _assets + (32 * _assets.length) + 36 <= calldata.size
  mem[96] = _assets.length
  mem[128 len 32 * _assets.length] = call.data[_assets + 36 len 32 * _assets.length]
  require _requestedPriceMantissas <= 4294967296
  require _requestedPriceMantissas + 36 <= calldata.size
  require _requestedPriceMantissas.length <= 4294967296 and _requestedPriceMantissas + (32 * _requestedPriceMantissas.length) + 36 <= calldata.size
  mem[(32 * _assets.length) + 128] = _requestedPriceMantissas.length
  mem[(32 * _assets.length) + 160 len 32 * _requestedPriceMantissas.length] = call.data[_requestedPriceMantissas + 36 len 32 * _requestedPriceMantissas.length]
  if posterAddress != caller:
      log OracleFailure(
            address msgSender=caller,
            address asset=0,
            uint256 error=1,
            uint256 info=8,
            uint256 detail=0)
      return Array(len=1, data=1)
  if not _assets.length:
      log OracleFailure(
            address msgSender=caller,
            address asset=0,
            uint256 error=2,
            uint256 info=10,
            uint256 detail=0)
      return Array(len=1, data=2)
  if _requestedPriceMantissas.length != _assets.length:
      log OracleFailure(
            address msgSender=caller,
            address asset=0,
            uint256 error=2,
            uint256 info=10,
            uint256 detail=0)
      return Array(len=1, data=2)
  mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160] = _assets.length
  mem[64] = (64 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192
  if not _assets.length:
      [94midx = 0
      while [94midx < _assets.length:
          require [94midx < mem[96]
          [94m_5548 = mem[(32 * [94midx) + 128]
          require [94midx < mem[(32 * _assets.length) + 128]
          [94m_5555 = mem[(32 * [94midx) + (32 * _assets.length) + 160]
          [94m_5561 = mem[64]
          mem[64] = mem[64] + 256
          [94m_5563 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5563] = 0
          mem[[94m_5561] = [94m_5563
          [94m_5565 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5565] = 0
          mem[[94m_5561 + 32] = [94m_5565
          [94m_5567 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5567] = 0
          mem[[94m_5561 + 64] = [94m_5567
          mem[[94m_5561 + 96] = 0
          mem[[94m_5561 + 160] = 0
          mem[[94m_5561 + 192] = 0
          mem[[94m_5561 + 128] = (block.number / 120) + 1
          mem[0] = addr([94m_5548)
          mem[32] = 7
          mem[[94m_5561 + 224] = pendingAnchors[addr([94m_5548)]
          [94m_5570 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5570] = [94m_5555
          mem[[94m_5561] = [94m_5570
          if pendingAnchors[addr([94m_5548)]:
              mem[[94m_5561 + 96] = 0
              [94m_5578 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5578] = pendingAnchors[addr([94m_5548)]
              mem[[94m_5561 + 64] = [94m_5578
              [94m_5594 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5594] = 0
              [94m_5601 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5601] = 0
              [94m_5609 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5609] = 0
              if pendingAnchors[addr([94m_5548)] <= [94m_5555:
                  [94m_5710 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5710] = 0
                  require pendingAnchors[addr([94m_5548)] <= [94m_5555
                  [94m_5839 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5839] = [94m_5555 - pendingAnchors[addr([94m_5548)]
                  [94m_5853 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5853] = 0
                  [94m_5867 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5867] = 0
                  if not [94m_5555 - pendingAnchors[addr([94m_5548)]:
                      require pendingAnchors[addr([94m_5548)]
                      [94m_5889 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5889] = 0 / pendingAnchors[addr([94m_5548)]
                      mem[[94m_5561 + 32] = [94m_5889
                      [94m_5914 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5914] = maxSwing
                      if 0 / pendingAnchors[addr([94m_5548)] > maxSwing:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5548)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 6
                          mem[mem[64] + 128] = 0 / pendingAnchors[addr([94m_5548)]
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5548),
                                uint256 error=2,
                                uint256 info=6,
                                uint256 detail=0 / pendingAnchors[addr(_5548)])
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not pendingAnchors[addr([94m_5548)]:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5548)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 7
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5548),
                                    uint256 error=2,
                                    uint256 info=7,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              if not [94m_5555:
                                  mem[mem[64]] = caller
                                  mem[mem[64] + 32] = addr([94m_5548)
                                  mem[mem[64] + 64] = 2
                                  mem[mem[64] + 96] = 9
                                  mem[mem[64] + 128] = 0
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=9,
                                        uint256 detail=0)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                              else:
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 7
                                  if not pendingAnchors[addr([94m_5548)]:
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6136 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6136] = [94m_5555
                                      else:
                                          [94m_6094 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6094] = (block.number / 120) + 1
                                          mem[[94m_6094 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6232 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6232] = [94m_5555
                                  else:
                                      mem[0] = addr([94m_5548)
                                      mem[32] = 7
                                      pendingAnchors[addr([94m_5548)] = 0
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6235 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6235] = [94m_5555
                                      else:
                                          [94m_6145 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6145] = (block.number / 120) + 1
                                          mem[[94m_6145 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6353 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6353] = [94m_5555
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 1
                                  _assetPrices[addr([94m_5548)] = [94m_5555
                                  mem[mem[64]] = addr([94m_5548)
                                  mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                  mem[mem[64] + 64] = [94m_5555
                                  mem[mem[64] + 96] = [94m_5555
                                  log PricePosted(
                                        address asset=addr(_5548),
                                        uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                        uint256 requestedPriceMantissa=_5555,
                                        uint256 newPriceMantissa=_5555)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                  else:
                      require (10^18 * [94m_5555) - (10^18 * pendingAnchors[addr([94m_5548)]) / [94m_5555 - pendingAnchors[addr([94m_5548)] == 10^18
                      require pendingAnchors[addr([94m_5548)]
                      [94m_5899 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5899] = (10^18 * [94m_5555) - (10^18 * pendingAnchors[addr([94m_5548)]) / pendingAnchors[addr([94m_5548)]
                      mem[[94m_5561 + 32] = [94m_5899
                      [94m_5932 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5932] = maxSwing
                      if (10^18 * [94m_5555) - (10^18 * pendingAnchors[addr([94m_5548)]) / pendingAnchors[addr([94m_5548)] > maxSwing:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5548)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 6
                          mem[mem[64] + 128] = (10^18 * [94m_5555) - (10^18 * pendingAnchors[addr([94m_5548)]) / pendingAnchors[addr([94m_5548)]
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5548),
                                uint256 error=2,
                                uint256 info=6,
                                uint256 detail=(10^18 * _5555) - (10^18 * pendingAnchors[addr(_5548)]) / pendingAnchors[addr(_5548)])
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not pendingAnchors[addr([94m_5548)]:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5548)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 7
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5548),
                                    uint256 error=2,
                                    uint256 info=7,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              if not [94m_5555:
                                  mem[mem[64]] = caller
                                  mem[mem[64] + 32] = addr([94m_5548)
                                  mem[mem[64] + 64] = 2
                                  mem[mem[64] + 96] = 9
                                  mem[mem[64] + 128] = 0
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=9,
                                        uint256 detail=0)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                              else:
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 7
                                  if not pendingAnchors[addr([94m_5548)]:
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6320 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6320] = [94m_5555
                                      else:
                                          [94m_6218 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6218] = (block.number / 120) + 1
                                          mem[[94m_6218 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6456 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6456] = [94m_5555
                                  else:
                                      mem[0] = addr([94m_5548)
                                      mem[32] = 7
                                      pendingAnchors[addr([94m_5548)] = 0
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6459 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6459] = [94m_5555
                                      else:
                                          [94m_6329 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6329] = (block.number / 120) + 1
                                          mem[[94m_6329 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6612 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6612] = [94m_5555
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 1
                                  _assetPrices[addr([94m_5548)] = [94m_5555
                                  mem[mem[64]] = addr([94m_5548)
                                  mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                  mem[mem[64] + 64] = [94m_5555
                                  mem[mem[64] + 96] = [94m_5555
                                  log PricePosted(
                                        address asset=addr(_5548),
                                        uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                        uint256 requestedPriceMantissa=_5555,
                                        uint256 newPriceMantissa=_5555)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
              else:
                  [94m_5711 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5711] = 0
                  require [94m_5555 <= pendingAnchors[addr([94m_5548)]
                  [94m_5841 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5841] = pendingAnchors[addr([94m_5548)] - [94m_5555
                  [94m_5857 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5857] = 0
                  [94m_5870 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5870] = 0
                  if not pendingAnchors[addr([94m_5548)] - [94m_5555:
                      require pendingAnchors[addr([94m_5548)]
                      [94m_5894 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5894] = 0 / pendingAnchors[addr([94m_5548)]
                      mem[[94m_5561 + 32] = [94m_5894
                      [94m_5923 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5923] = maxSwing
                      if 0 / pendingAnchors[addr([94m_5548)] > maxSwing:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5548)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 6
                          mem[mem[64] + 128] = 0 / pendingAnchors[addr([94m_5548)]
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5548),
                                uint256 error=2,
                                uint256 info=6,
                                uint256 detail=0 / pendingAnchors[addr(_5548)])
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not pendingAnchors[addr([94m_5548)]:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5548)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 7
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5548),
                                    uint256 error=2,
                                    uint256 info=7,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              if not [94m_5555:
                                  mem[mem[64]] = caller
                                  mem[mem[64] + 32] = addr([94m_5548)
                                  mem[mem[64] + 64] = 2
                                  mem[mem[64] + 96] = 9
                                  mem[mem[64] + 128] = 0
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=9,
                                        uint256 detail=0)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                              else:
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 7
                                  if not pendingAnchors[addr([94m_5548)]:
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6245 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6245] = [94m_5555
                                      else:
                                          [94m_6161 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6161] = (block.number / 120) + 1
                                          mem[[94m_6161 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6373 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6373] = [94m_5555
                                  else:
                                      mem[0] = addr([94m_5548)
                                      mem[32] = 7
                                      pendingAnchors[addr([94m_5548)] = 0
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6376 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6376] = [94m_5555
                                      else:
                                          [94m_6254 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6254] = (block.number / 120) + 1
                                          mem[[94m_6254 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6515 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6515] = [94m_5555
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 1
                                  _assetPrices[addr([94m_5548)] = [94m_5555
                                  mem[mem[64]] = addr([94m_5548)
                                  mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                  mem[mem[64] + 64] = [94m_5555
                                  mem[mem[64] + 96] = [94m_5555
                                  log PricePosted(
                                        address asset=addr(_5548),
                                        uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                        uint256 requestedPriceMantissa=_5555,
                                        uint256 newPriceMantissa=_5555)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                  else:
                      require (10^18 * pendingAnchors[addr([94m_5548)]) - (10^18 * [94m_5555) / pendingAnchors[addr([94m_5548)] - [94m_5555 == 10^18
                      require pendingAnchors[addr([94m_5548)]
                      [94m_5904 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5904] = (10^18 * pendingAnchors[addr([94m_5548)]) - (10^18 * [94m_5555) / pendingAnchors[addr([94m_5548)]
                      mem[[94m_5561 + 32] = [94m_5904
                      [94m_5946 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5946] = maxSwing
                      if (10^18 * pendingAnchors[addr([94m_5548)]) - (10^18 * [94m_5555) / pendingAnchors[addr([94m_5548)] > maxSwing:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5548)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 6
                          mem[mem[64] + 128] = (10^18 * pendingAnchors[addr([94m_5548)]) - (10^18 * [94m_5555) / pendingAnchors[addr([94m_5548)]
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5548),
                                uint256 error=2,
                                uint256 info=6,
                                uint256 detail=(10^18 * pendingAnchors[addr(_5548)]) - (10^18 * _5555) / pendingAnchors[addr(_5548)])
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not pendingAnchors[addr([94m_5548)]:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5548)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 7
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5548),
                                    uint256 error=2,
                                    uint256 info=7,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              if not [94m_5555:
                                  mem[mem[64]] = caller
                                  mem[mem[64] + 32] = addr([94m_5548)
                                  mem[mem[64] + 64] = 2
                                  mem[mem[64] + 96] = 9
                                  mem[mem[64] + 128] = 0
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=9,
                                        uint256 detail=0)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                              else:
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 7
                                  if not pendingAnchors[addr([94m_5548)]:
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6482 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6482] = [94m_5555
                                      else:
                                          [94m_6359 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6359] = (block.number / 120) + 1
                                          mem[[94m_6359 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6629 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6629] = [94m_5555
                                  else:
                                      mem[0] = addr([94m_5548)
                                      mem[32] = 7
                                      pendingAnchors[addr([94m_5548)] = 0
                                      if (block.number / 120) + 1 <= 0:
                                          mem[0] = addr([94m_5548)
                                          [94m_6632 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6632] = [94m_5555
                                      else:
                                          [94m_6491 = mem[64]
                                          mem[64] = mem[64] + 64
                                          mem[[94m_6491] = (block.number / 120) + 1
                                          mem[[94m_6491 + 32] = [94m_5555
                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                          mem[0] = addr([94m_5548)
                                          [94m_6765 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6765] = [94m_5555
                                  mem[0] = addr([94m_5548)
                                  mem[32] = 1
                                  _assetPrices[addr([94m_5548)] = [94m_5555
                                  mem[mem[64]] = addr([94m_5548)
                                  mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                  mem[mem[64] + 64] = [94m_5555
                                  mem[mem[64] + 96] = [94m_5555
                                  log PricePosted(
                                        address asset=addr(_5548),
                                        uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                        uint256 requestedPriceMantissa=_5555,
                                        uint256 newPriceMantissa=_5555)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
          else:
              mem[[94m_5561 + 96] = anchors[addr([94m_5548)].field_0
              [94m_5576 = mem[64]
              mem[64] = mem[64] + 32
              mem[0] = addr([94m_5548)
              mem[32] = 6
              mem[[94m_5576] = anchors[addr([94m_5548)].field_256
              mem[[94m_5561 + 64] = [94m_5576
              if not anchors[addr([94m_5548)].field_0:
                  [94m_5587 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5587] = [94m_5555
                  mem[[94m_5561 + 64] = [94m_5587
                  if not [94m_5555:
                      mem[mem[64]] = caller
                      mem[mem[64] + 32] = addr([94m_5548)
                      mem[mem[64] + 64] = 2
                      mem[mem[64] + 96] = 7
                      mem[mem[64] + 128] = 0
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_5548),
                            uint256 error=2,
                            uint256 info=7,
                            uint256 detail=0)
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                  else:
                      if not [94m_5555:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5548)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 9
                          mem[mem[64] + 128] = 0
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5548),
                                uint256 error=2,
                                uint256 info=9,
                                uint256 detail=0)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          mem[0] = addr([94m_5548)
                          mem[32] = 7
                          if not pendingAnchors[addr([94m_5548)]:
                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                  mem[0] = addr([94m_5548)
                                  [94m_5657 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5657] = [94m_5555
                              else:
                                  [94m_5636 = mem[64]
                                  mem[64] = mem[64] + 64
                                  mem[[94m_5636] = (block.number / 120) + 1
                                  mem[[94m_5636 + 32] = [94m_5555
                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                  anchors[addr([94m_5548)].field_256 = [94m_5555
                                  mem[0] = addr([94m_5548)
                                  [94m_5700 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5700] = [94m_5555
                          else:
                              mem[0] = addr([94m_5548)
                              mem[32] = 7
                              pendingAnchors[addr([94m_5548)] = 0
                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                  mem[0] = addr([94m_5548)
                                  [94m_5703 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5703] = [94m_5555
                              else:
                                  [94m_5666 = mem[64]
                                  mem[64] = mem[64] + 64
                                  mem[[94m_5666] = (block.number / 120) + 1
                                  mem[[94m_5666 + 32] = [94m_5555
                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                  anchors[addr([94m_5548)].field_256 = [94m_5555
                                  mem[0] = addr([94m_5548)
                                  [94m_5744 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5744] = [94m_5555
                          mem[0] = addr([94m_5548)
                          mem[32] = 1
                          _assetPrices[addr([94m_5548)] = [94m_5555
                          mem[mem[64]] = addr([94m_5548)
                          mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                          mem[mem[64] + 64] = [94m_5555
                          mem[mem[64] + 96] = [94m_5555
                          log PricePosted(
                                address asset=addr(_5548),
                                uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                uint256 requestedPriceMantissa=_5555,
                                uint256 newPriceMantissa=_5555)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
              else:
                  [94m_5598 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5598] = 0
                  [94m_5604 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5604] = 0
                  [94m_5608 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5608] = 10^18
                  [94m_5613 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5613] = 0
                  [94m_5628 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5628] = 0
                  [94m_5675 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5675] = 0
                  [94m_5747 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5747] = 0
                  [94m_5791 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5791] = maxSwing
                  [94m_5830 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5830] = 0
                  if maxSwing + 10^18 < 10^18:
                      [94m_5849 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5849] = 0
                      [94m_5861 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5861] = 0
                      mem[[94m_5561] = [94m_5861
                      mem[[94m_5561 + 160] = 0
                      mem[mem[64]] = caller
                      mem[mem[64] + 32] = addr([94m_5548)
                      mem[mem[64] + 64] = 2
                      mem[mem[64] + 96] = 5
                      mem[mem[64] + 128] = 12
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_5548),
                            uint256 error=2,
                            uint256 info=5,
                            uint256 detail=12)
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                  else:
                      [94m_5850 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5850] = maxSwing + 10^18
                      [94m_5869 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5869] = 0
                      if not anchors[addr([94m_5548)].field_256:
                          [94m_5910 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5910] = 0
                          if [94m_5555 > 0:
                              mem[[94m_5561] = [94m_5910
                              mem[[94m_5561 + 160] = 1
                              mem[[94m_5561 + 192] = anchors[addr([94m_5548)].field_256
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5548)
                              mem[mem[64] + 64] = 2
                              if anchors[addr([94m_5548)].field_256:
                                  mem[mem[64] + 96] = 9
                                  mem[mem[64] + 128] = 0
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=9,
                                        uint256 detail=0)
                              else:
                                  mem[mem[64] + 96] = 7
                                  mem[mem[64] + 128] = 0
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=7,
                                        uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              [94m_5968 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5968] = maxSwing
                              [94m_5996 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5996] = 0
                              if maxSwing > 10^18:
                                  [94m_6083 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_6083] = 0
                                  [94m_6317 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_6317] = 0
                                  mem[[94m_5561] = [94m_6317
                                  mem[[94m_5561 + 160] = 0
                                  mem[mem[64]] = caller
                                  mem[mem[64] + 32] = addr([94m_5548)
                                  mem[mem[64] + 64] = 2
                                  mem[mem[64] + 96] = 5
                                  mem[mem[64] + 128] = 12
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=5,
                                        uint256 detail=12)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                              else:
                                  [94m_6084 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_6084] = -maxSwing + 10^18
                                  [94m_6590 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_6590] = 0
                                  if not anchors[addr([94m_5548)].field_256:
                                      [94m_7711 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_7711] = 0
                                      if [94m_5555 < 0:
                                          mem[[94m_5561] = [94m_7711
                                          mem[[94m_5561 + 160] = 1
                                          mem[[94m_5561 + 192] = anchors[addr([94m_5548)].field_256
                                          mem[mem[64]] = caller
                                          mem[mem[64] + 32] = addr([94m_5548)
                                          mem[mem[64] + 64] = 2
                                          if anchors[addr([94m_5548)].field_256:
                                              mem[mem[64] + 96] = 9
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5548),
                                                    uint256 error=2,
                                                    uint256 info=9,
                                                    uint256 detail=0)
                                          else:
                                              mem[mem[64] + 96] = 7
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5548),
                                                    uint256 error=2,
                                                    uint256 info=7,
                                                    uint256 detail=0)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                      else:
                                          mem[[94m_5561] = [94m_5570
                                          mem[[94m_5561 + 160] = 0
                                          if not anchors[addr([94m_5548)].field_256:
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5548)
                                              mem[mem[64] + 64] = 2
                                              mem[mem[64] + 96] = 7
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5548),
                                                    uint256 error=2,
                                                    uint256 info=7,
                                                    uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              if not [94m_5555:
                                                  mem[mem[64]] = caller
                                                  mem[mem[64] + 32] = addr([94m_5548)
                                                  mem[mem[64] + 64] = 2
                                                  mem[mem[64] + 96] = 9
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5548),
                                                        uint256 error=2,
                                                        uint256 info=9,
                                                        uint256 detail=0)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                              else:
                                                  mem[0] = addr([94m_5548)
                                                  mem[32] = 7
                                                  if not pendingAnchors[addr([94m_5548)]:
                                                      if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                          mem[0] = addr([94m_5548)
                                                          [94m_8127 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_8127] = [94m_5555
                                                      else:
                                                          [94m_7982 = mem[64]
                                                          mem[64] = mem[64] + 64
                                                          mem[[94m_7982] = (block.number / 120) + 1
                                                          mem[[94m_7982 + 32] = [94m_5555
                                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                                          mem[0] = addr([94m_5548)
                                                          [94m_8408 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_8408] = [94m_5555
                                                  else:
                                                      mem[0] = addr([94m_5548)
                                                      mem[32] = 7
                                                      pendingAnchors[addr([94m_5548)] = 0
                                                      if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                          mem[0] = addr([94m_5548)
                                                          [94m_8411 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_8411] = [94m_5555
                                                      else:
                                                          [94m_8136 = mem[64]
                                                          mem[64] = mem[64] + 64
                                                          mem[[94m_8136] = (block.number / 120) + 1
                                                          mem[[94m_8136 + 32] = [94m_5555
                                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                                          mem[0] = addr([94m_5548)
                                                          [94m_8802 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_8802] = [94m_5555
                                                  mem[0] = addr([94m_5548)
                                                  mem[32] = 1
                                                  _assetPrices[addr([94m_5548)] = [94m_5555
                                                  mem[mem[64]] = addr([94m_5548)
                                                  mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                                  mem[mem[64] + 64] = [94m_5555
                                                  mem[mem[64] + 96] = [94m_5555
                                                  log PricePosted(
                                                        address asset=addr(_5548),
                                                        uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                                        uint256 requestedPriceMantissa=_5555,
                                                        uint256 newPriceMantissa=_5555)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                  else:
                                      require (10^18 * anchors[addr([94m_5548)].field_256) - (maxSwing * anchors[addr([94m_5548)].field_256) / anchors[addr([94m_5548)].field_256 == -maxSwing + 10^18
                                      require (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 >= 5 * 10^17
                                      [94m_7714 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_7714] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                      if [94m_5555 >= (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18:
                                          mem[[94m_5561] = [94m_5570
                                          mem[[94m_5561 + 160] = 0
                                          if not anchors[addr([94m_5548)].field_256:
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5548)
                                              mem[mem[64] + 64] = 2
                                              mem[mem[64] + 96] = 7
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5548),
                                                    uint256 error=2,
                                                    uint256 info=7,
                                                    uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              if not [94m_5555:
                                                  mem[mem[64]] = caller
                                                  mem[mem[64] + 32] = addr([94m_5548)
                                                  mem[mem[64] + 64] = 2
                                                  mem[mem[64] + 96] = 9
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5548),
                                                        uint256 error=2,
                                                        uint256 info=9,
                                                        uint256 detail=0)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                              else:
                                                  mem[0] = addr([94m_5548)
                                                  mem[32] = 7
                                                  if not pendingAnchors[addr([94m_5548)]:
                                                      if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                          mem[0] = addr([94m_5548)
                                                          [94m_8715 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_8715] = [94m_5555
                                                      else:
                                                          [94m_8358 = mem[64]
                                                          mem[64] = mem[64] + 64
                                                          mem[[94m_8358] = (block.number / 120) + 1
                                                          mem[[94m_8358 + 32] = [94m_5555
                                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                                          mem[0] = addr([94m_5548)
                                                          [94m_9200 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_9200] = [94m_5555
                                                  else:
                                                      mem[0] = addr([94m_5548)
                                                      mem[32] = 7
                                                      pendingAnchors[addr([94m_5548)] = 0
                                                      if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                          mem[0] = addr([94m_5548)
                                                          [94m_9203 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_9203] = [94m_5555
                                                      else:
                                                          [94m_8724 = mem[64]
                                                          mem[64] = mem[64] + 64
                                                          mem[[94m_8724] = (block.number / 120) + 1
                                                          mem[[94m_8724 + 32] = [94m_5555
                                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                          anchors[addr([94m_5548)].field_256 = [94m_5555
                                                          mem[0] = addr([94m_5548)
                                                          [94m_9710 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_9710] = [94m_5555
                                                  mem[0] = addr([94m_5548)
                                                  mem[32] = 1
                                                  _assetPrices[addr([94m_5548)] = [94m_5555
                                                  mem[mem[64]] = addr([94m_5548)
                                                  mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                                  mem[mem[64] + 64] = [94m_5555
                                                  mem[mem[64] + 96] = [94m_5555
                                                  log PricePosted(
                                                        address asset=addr(_5548),
                                                        uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                                        uint256 requestedPriceMantissa=_5555,
                                                        uint256 newPriceMantissa=_5555)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                      else:
                                          mem[[94m_5561] = [94m_7714
                                          mem[[94m_5561 + 160] = 1
                                          mem[[94m_5561 + 192] = anchors[addr([94m_5548)].field_256
                                          if not anchors[addr([94m_5548)].field_256:
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5548)
                                              mem[mem[64] + 64] = 2
                                              mem[mem[64] + 96] = 7
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5548),
                                                    uint256 error=2,
                                                    uint256 info=7,
                                                    uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              if not (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18:
                                                  mem[mem[64]] = caller
                                                  mem[mem[64] + 32] = addr([94m_5548)
                                                  mem[mem[64] + 64] = 2
                                                  mem[mem[64] + 96] = 9
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5548),
                                                        uint256 error=2,
                                                        uint256 info=9,
                                                        uint256 detail=0)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                              else:
                                                  mem[0] = addr([94m_5548)
                                                  mem[32] = 7
                                                  if not pendingAnchors[addr([94m_5548)]:
                                                      if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                          mem[0] = addr([94m_5548)
                                                          [94m_8769 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_8769] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                      else:
                                                          [94m_8394 = mem[64]
                                                          mem[64] = mem[64] + 64
                                                          mem[[94m_8394] = (block.number / 120) + 1
                                                          mem[[94m_8394 + 32] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                          anchors[addr([94m_5548)].field_256 = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          mem[0] = addr([94m_5548)
                                                          [94m_9245 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_9245] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                  else:
                                                      mem[0] = addr([94m_5548)
                                                      mem[32] = 7
                                                      pendingAnchors[addr([94m_5548)] = 0
                                                      if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                          mem[0] = addr([94m_5548)
                                                          [94m_9248 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_9248] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                      else:
                                                          [94m_8778 = mem[64]
                                                          mem[64] = mem[64] + 64
                                                          mem[[94m_8778] = (block.number / 120) + 1
                                                          mem[[94m_8778 + 32] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                          anchors[addr([94m_5548)].field_256 = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          mem[0] = addr([94m_5548)
                                                          [94m_9764 = mem[64]
                                                          mem[64] = mem[64] + 32
                                                          mem[[94m_9764] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                  mem[0] = addr([94m_5548)
                                                  mem[32] = 1
                                                  _assetPrices[addr([94m_5548)] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                  log PricePosted(
                                                        address asset=addr(_5548),
                                                        uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                                        uint256 requestedPriceMantissa=_5555,
                                                        uint256 newPriceMantissa=(10^18 * anchors[addr(_5548)].field_256) + (-1 * maxSwing * anchors[addr(_5548)].field_256) + 5 * 10^17 / 10^18)
                                                  mem[mem[64]] = addr([94m_5548)
                                                  mem[mem[64] + 32] = [94m_5555
                                                  mem[mem[64] + 64] = anchors[addr([94m_5548)].field_256
                                                  mem[mem[64] + 96] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                  log CappedPricePosted(
                                                        address asset=addr(_5548),
                                                        uint256 requestedPriceMantissa=_5555,
                                                        uint256 anchorPriceMantissa=anchors[addr(_5548)].field_256,
                                                        uint256 cappedPriceMantissa=(10^18 * anchors[addr(_5548)].field_256) + (-1 * maxSwing * anchors[addr(_5548)].field_256) + 5 * 10^17 / 10^18)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                      else:
                          if (maxSwing * anchors[addr([94m_5548)].field_256) + (10^18 * anchors[addr([94m_5548)].field_256) / anchors[addr([94m_5548)].field_256 != maxSwing + 10^18:
                              [94m_5883 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5883] = 0
                              [94m_5893 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5893] = 0
                              mem[[94m_5561] = [94m_5893
                              mem[[94m_5561 + 160] = 0
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5548)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 5
                              mem[mem[64] + 128] = 12
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5548),
                                    uint256 error=2,
                                    uint256 info=5,
                                    uint256 detail=12)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              if (maxSwing * anchors[addr([94m_5548)].field_256) + (10^18 * anchors[addr([94m_5548)].field_256) + 5 * 10^17 < 5 * 10^17:
                                  [94m_5903 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5903] = 0
                                  [94m_5909 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5909] = 0
                                  mem[[94m_5561] = [94m_5909
                                  mem[[94m_5561 + 160] = 0
                                  mem[mem[64]] = caller
                                  mem[mem[64] + 32] = addr([94m_5548)
                                  mem[mem[64] + 64] = 2
                                  mem[mem[64] + 96] = 5
                                  mem[mem[64] + 128] = 12
                                  log OracleFailure(
                                        address msgSender=caller,
                                        address asset=addr(_5548),
                                        uint256 error=2,
                                        uint256 info=5,
                                        uint256 detail=12)
                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                              else:
                                  [94m_5917 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_5917] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                  if [94m_5555 > (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18:
                                      mem[[94m_5561] = [94m_5917
                                      mem[[94m_5561 + 160] = 1
                                      mem[[94m_5561 + 192] = anchors[addr([94m_5548)].field_256
                                      if not anchors[addr([94m_5548)].field_256:
                                          mem[mem[64]] = caller
                                          mem[mem[64] + 32] = addr([94m_5548)
                                          mem[mem[64] + 64] = 2
                                          mem[mem[64] + 96] = 7
                                          mem[mem[64] + 128] = 0
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5548),
                                                uint256 error=2,
                                                uint256 info=7,
                                                uint256 detail=0)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                      else:
                                          if not (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18:
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5548)
                                              mem[mem[64] + 64] = 2
                                              mem[mem[64] + 96] = 9
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5548),
                                                    uint256 error=2,
                                                    uint256 info=9,
                                                    uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              mem[0] = addr([94m_5548)
                                              mem[32] = 7
                                              if not pendingAnchors[addr([94m_5548)]:
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                      mem[0] = addr([94m_5548)
                                                      [94m_7199 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_7199] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                  else:
                                                      [94m_7080 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_7080] = (block.number / 120) + 1
                                                      mem[[94m_7080 + 32] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                      anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5548)].field_256 = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                      mem[0] = addr([94m_5548)
                                                      [94m_7347 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_7347] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                              else:
                                                  mem[0] = addr([94m_5548)
                                                  mem[32] = 7
                                                  pendingAnchors[addr([94m_5548)] = 0
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                      mem[0] = addr([94m_5548)
                                                      [94m_7350 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_7350] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                  else:
                                                      [94m_7208 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_7208] = (block.number / 120) + 1
                                                      mem[[94m_7208 + 32] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                      anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5548)].field_256 = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                      mem[0] = addr([94m_5548)
                                                      [94m_7488 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_7488] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                              mem[0] = addr([94m_5548)
                                              mem[32] = 1
                                              _assetPrices[addr([94m_5548)] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                              log PricePosted(
                                                    address asset=addr(_5548),
                                                    uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                                    uint256 requestedPriceMantissa=_5555,
                                                    uint256 newPriceMantissa=(10^18 * anchors[addr(_5548)].field_256) + (maxSwing * anchors[addr(_5548)].field_256) + 5 * 10^17 / 10^18)
                                              mem[mem[64]] = addr([94m_5548)
                                              mem[mem[64] + 32] = [94m_5555
                                              mem[mem[64] + 64] = anchors[addr([94m_5548)].field_256
                                              mem[mem[64] + 96] = (10^18 * anchors[addr([94m_5548)].field_256) + (maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                              log CappedPricePosted(
                                                    address asset=addr(_5548),
                                                    uint256 requestedPriceMantissa=_5555,
                                                    uint256 anchorPriceMantissa=anchors[addr(_5548)].field_256,
                                                    uint256 cappedPriceMantissa=(10^18 * anchors[addr(_5548)].field_256) + (maxSwing * anchors[addr(_5548)].field_256) + 5 * 10^17 / 10^18)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                  else:
                                      [94m_5995 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_5995] = maxSwing
                                      [94m_6025 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6025] = 0
                                      if maxSwing > 10^18:
                                          [94m_6209 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6209] = 0
                                          [94m_6587 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6587] = 0
                                          mem[[94m_5561] = [94m_6587
                                          mem[[94m_5561 + 160] = 0
                                          mem[mem[64]] = caller
                                          mem[mem[64] + 32] = addr([94m_5548)
                                          mem[mem[64] + 64] = 2
                                          mem[mem[64] + 96] = 5
                                          mem[mem[64] + 128] = 12
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5548),
                                                uint256 error=2,
                                                uint256 info=5,
                                                uint256 detail=12)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                      else:
                                          [94m_6210 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6210] = -maxSwing + 10^18
                                          [94m_6831 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_6831] = 0
                                          if not anchors[addr([94m_5548)].field_256:
                                              [94m_7713 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_7713] = 0
                                              if [94m_5555 < 0:
                                                  mem[[94m_5561] = [94m_7713
                                                  mem[[94m_5561 + 160] = 1
                                                  mem[[94m_5561 + 192] = anchors[addr([94m_5548)].field_256
                                                  mem[mem[64]] = caller
                                                  mem[mem[64] + 32] = addr([94m_5548)
                                                  mem[mem[64] + 64] = 2
                                                  if anchors[addr([94m_5548)].field_256:
                                                      mem[mem[64] + 96] = 9
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5548),
                                                            uint256 error=2,
                                                            uint256 info=9,
                                                            uint256 detail=0)
                                                  else:
                                                      mem[mem[64] + 96] = 7
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5548),
                                                            uint256 error=2,
                                                            uint256 info=7,
                                                            uint256 detail=0)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                              else:
                                                  mem[[94m_5561] = [94m_5570
                                                  mem[[94m_5561 + 160] = 0
                                                  if not anchors[addr([94m_5548)].field_256:
                                                      mem[mem[64]] = caller
                                                      mem[mem[64] + 32] = addr([94m_5548)
                                                      mem[mem[64] + 64] = 2
                                                      mem[mem[64] + 96] = 7
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5548),
                                                            uint256 error=2,
                                                            uint256 info=7,
                                                            uint256 detail=0)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                  else:
                                                      if not [94m_5555:
                                                          mem[mem[64]] = caller
                                                          mem[mem[64] + 32] = addr([94m_5548)
                                                          mem[mem[64] + 64] = 2
                                                          mem[mem[64] + 96] = 9
                                                          mem[mem[64] + 128] = 0
                                                          log OracleFailure(
                                                                address msgSender=caller,
                                                                address asset=addr(_5548),
                                                                uint256 error=2,
                                                                uint256 info=9,
                                                                uint256 detail=0)
                                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                      else:
                                                          mem[0] = addr([94m_5548)
                                                          mem[32] = 7
                                                          if not pendingAnchors[addr([94m_5548)]:
                                                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_8643 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_8643] = [94m_5555
                                                              else:
                                                                  [94m_8310 = mem[64]
                                                                  mem[64] = mem[64] + 64
                                                                  mem[[94m_8310] = (block.number / 120) + 1
                                                                  mem[[94m_8310 + 32] = [94m_5555
                                                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                                  anchors[addr([94m_5548)].field_256 = [94m_5555
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_9140 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_9140] = [94m_5555
                                                          else:
                                                              mem[0] = addr([94m_5548)
                                                              mem[32] = 7
                                                              pendingAnchors[addr([94m_5548)] = 0
                                                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_9143 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_9143] = [94m_5555
                                                              else:
                                                                  [94m_8652 = mem[64]
                                                                  mem[64] = mem[64] + 64
                                                                  mem[[94m_8652] = (block.number / 120) + 1
                                                                  mem[[94m_8652 + 32] = [94m_5555
                                                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                                  anchors[addr([94m_5548)].field_256 = [94m_5555
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_9638 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_9638] = [94m_5555
                                                          mem[0] = addr([94m_5548)
                                                          mem[32] = 1
                                                          _assetPrices[addr([94m_5548)] = [94m_5555
                                                          mem[mem[64]] = addr([94m_5548)
                                                          mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                                          mem[mem[64] + 64] = [94m_5555
                                                          mem[mem[64] + 96] = [94m_5555
                                                          log PricePosted(
                                                                address asset=addr(_5548),
                                                                uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                                                uint256 requestedPriceMantissa=_5555,
                                                                uint256 newPriceMantissa=_5555)
                                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                          else:
                                              require (10^18 * anchors[addr([94m_5548)].field_256) - (maxSwing * anchors[addr([94m_5548)].field_256) / anchors[addr([94m_5548)].field_256 == -maxSwing + 10^18
                                              require (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 >= 5 * 10^17
                                              [94m_7717 = mem[64]
                                              mem[64] = mem[64] + 32
                                              mem[[94m_7717] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                              if [94m_5555 >= (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18:
                                                  mem[[94m_5561] = [94m_5570
                                                  mem[[94m_5561 + 160] = 0
                                                  if not anchors[addr([94m_5548)].field_256:
                                                      mem[mem[64]] = caller
                                                      mem[mem[64] + 32] = addr([94m_5548)
                                                      mem[mem[64] + 64] = 2
                                                      mem[mem[64] + 96] = 7
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5548),
                                                            uint256 error=2,
                                                            uint256 info=7,
                                                            uint256 detail=0)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                  else:
                                                      if not [94m_5555:
                                                          mem[mem[64]] = caller
                                                          mem[mem[64] + 32] = addr([94m_5548)
                                                          mem[mem[64] + 64] = 2
                                                          mem[mem[64] + 96] = 9
                                                          mem[mem[64] + 128] = 0
                                                          log OracleFailure(
                                                                address msgSender=caller,
                                                                address asset=addr(_5548),
                                                                uint256 error=2,
                                                                uint256 info=9,
                                                                uint256 detail=0)
                                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                      else:
                                                          mem[0] = addr([94m_5548)
                                                          mem[32] = 7
                                                          if not pendingAnchors[addr([94m_5548)]:
                                                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_9551 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_9551] = [94m_5555
                                                              else:
                                                                  [94m_9090 = mem[64]
                                                                  mem[64] = mem[64] + 64
                                                                  mem[[94m_9090] = (block.number / 120) + 1
                                                                  mem[[94m_9090 + 32] = [94m_5555
                                                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                                  anchors[addr([94m_5548)].field_256 = [94m_5555
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_10060 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_10060] = [94m_5555
                                                          else:
                                                              mem[0] = addr([94m_5548)
                                                              mem[32] = 7
                                                              pendingAnchors[addr([94m_5548)] = 0
                                                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_10063 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_10063] = [94m_5555
                                                              else:
                                                                  [94m_9560 = mem[64]
                                                                  mem[64] = mem[64] + 64
                                                                  mem[[94m_9560] = (block.number / 120) + 1
                                                                  mem[[94m_9560 + 32] = [94m_5555
                                                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                                  anchors[addr([94m_5548)].field_256 = [94m_5555
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_10470 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_10470] = [94m_5555
                                                          mem[0] = addr([94m_5548)
                                                          mem[32] = 1
                                                          _assetPrices[addr([94m_5548)] = [94m_5555
                                                          mem[mem[64]] = addr([94m_5548)
                                                          mem[mem[64] + 32] = _assetPrices[addr([94m_5548)]
                                                          mem[mem[64] + 64] = [94m_5555
                                                          mem[mem[64] + 96] = [94m_5555
                                                          log PricePosted(
                                                                address asset=addr(_5548),
                                                                uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                                                uint256 requestedPriceMantissa=_5555,
                                                                uint256 newPriceMantissa=_5555)
                                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                              else:
                                                  mem[[94m_5561] = [94m_7717
                                                  mem[[94m_5561 + 160] = 1
                                                  mem[[94m_5561 + 192] = anchors[addr([94m_5548)].field_256
                                                  if not anchors[addr([94m_5548)].field_256:
                                                      mem[mem[64]] = caller
                                                      mem[mem[64] + 32] = addr([94m_5548)
                                                      mem[mem[64] + 64] = 2
                                                      mem[mem[64] + 96] = 7
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5548),
                                                            uint256 error=2,
                                                            uint256 info=7,
                                                            uint256 detail=0)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                  else:
                                                      if not (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18:
                                                          mem[mem[64]] = caller
                                                          mem[mem[64] + 32] = addr([94m_5548)
                                                          mem[mem[64] + 64] = 2
                                                          mem[mem[64] + 96] = 9
                                                          mem[mem[64] + 128] = 0
                                                          log OracleFailure(
                                                                address msgSender=caller,
                                                                address asset=addr(_5548),
                                                                uint256 error=2,
                                                                uint256 info=9,
                                                                uint256 detail=0)
                                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                      else:
                                                          mem[0] = addr([94m_5548)
                                                          mem[32] = 7
                                                          if not pendingAnchors[addr([94m_5548)]:
                                                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_9605 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_9605] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                              else:
                                                                  [94m_9126 = mem[64]
                                                                  mem[64] = mem[64] + 64
                                                                  mem[[94m_9126] = (block.number / 120) + 1
                                                                  mem[[94m_9126 + 32] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                                  anchors[addr([94m_5548)].field_256 = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_10105 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_10105] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          else:
                                                              mem[0] = addr([94m_5548)
                                                              mem[32] = 7
                                                              pendingAnchors[addr([94m_5548)] = 0
                                                              if (block.number / 120) + 1 <= anchors[addr([94m_5548)].field_0:
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_10108 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_10108] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                              else:
                                                                  [94m_9614 = mem[64]
                                                                  mem[64] = mem[64] + 64
                                                                  mem[[94m_9614] = (block.number / 120) + 1
                                                                  mem[[94m_9614 + 32] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                                  anchors[addr([94m_5548)].field_0 = (block.number / 120) + 1
                                                                  anchors[addr([94m_5548)].field_256 = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                                  mem[0] = addr([94m_5548)
                                                                  [94m_10524 = mem[64]
                                                                  mem[64] = mem[64] + 32
                                                                  mem[[94m_10524] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          mem[0] = addr([94m_5548)
                                                          mem[32] = 1
                                                          _assetPrices[addr([94m_5548)] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          log PricePosted(
                                                                address asset=addr(_5548),
                                                                uint256 previousPriceMantissa=_assetPrices[addr(_5548)],
                                                                uint256 requestedPriceMantissa=_5555,
                                                                uint256 newPriceMantissa=(10^18 * anchors[addr(_5548)].field_256) + (-1 * maxSwing * anchors[addr(_5548)].field_256) + 5 * 10^17 / 10^18)
                                                          mem[mem[64]] = addr([94m_5548)
                                                          mem[mem[64] + 32] = [94m_5555
                                                          mem[mem[64] + 64] = anchors[addr([94m_5548)].field_256
                                                          mem[mem[64] + 96] = (10^18 * anchors[addr([94m_5548)].field_256) + (-1 * maxSwing * anchors[addr([94m_5548)].field_256) + 5 * 10^17 / 10^18
                                                          log CappedPricePosted(
                                                                address asset=addr(_5548),
                                                                uint256 requestedPriceMantissa=_5555,
                                                                uint256 anchorPriceMantissa=anchors[addr(_5548)].field_256,
                                                                uint256 cappedPriceMantissa=(10^18 * anchors[addr(_5548)].field_256) + (-1 * maxSwing * anchors[addr(_5548)].field_256) + 5 * 10^17 / 10^18)
                                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
          [94midx = [94midx + 1
          continue 
      mem[mem[64]] = 32
      mem[mem[64] + 32] = mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
      [94m_5547 = mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
      mem[mem[64] + 64 len floor32(mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160])] = mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192 len floor32(mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160])]
      return 32, mem[mem[64] + 32 len (32 * [94m_5547) + 32]
  mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192 len 32 * _assets.length] = code.data[5617 len 32 * _assets.length]
  [94midx = 0
  while [94midx < _assets.length:
      require [94midx < mem[96]
      [94m_5553 = mem[(32 * [94midx) + 128]
      require [94midx < mem[(32 * _assets.length) + 128]
      [94m_5556 = mem[(32 * [94midx) + (32 * _assets.length) + 160]
      [94m_5562 = mem[64]
      mem[64] = mem[64] + 256
      [94m_5564 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_5564] = 0
      mem[[94m_5562] = [94m_5564
      [94m_5566 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_5566] = 0
      mem[[94m_5562 + 32] = [94m_5566
      [94m_5568 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_5568] = 0
      mem[[94m_5562 + 64] = [94m_5568
      mem[[94m_5562 + 96] = 0
      mem[[94m_5562 + 160] = 0
      mem[[94m_5562 + 192] = 0
      mem[[94m_5562 + 128] = (block.number / 120) + 1
      mem[0] = addr([94m_5553)
      mem[32] = 7
      mem[[94m_5562 + 224] = pendingAnchors[addr([94m_5553)]
      [94m_5573 = mem[64]
      mem[64] = mem[64] + 32
      mem[[94m_5573] = [94m_5556
      mem[[94m_5562] = [94m_5573
      if pendingAnchors[addr([94m_5553)]:
          mem[[94m_5562 + 96] = 0
          [94m_5584 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5584] = pendingAnchors[addr([94m_5553)]
          mem[[94m_5562 + 64] = [94m_5584
          [94m_5596 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5596] = 0
          [94m_5602 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5602] = 0
          [94m_5612 = mem[64]
          mem[64] = mem[64] + 32
          mem[[94m_5612] = 0
          if pendingAnchors[addr([94m_5553)] <= [94m_5556:
              [94m_5727 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5727] = 0
              require pendingAnchors[addr([94m_5553)] <= [94m_5556
              [94m_5846 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5846] = [94m_5556 - pendingAnchors[addr([94m_5553)]
              [94m_5854 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5854] = 0
              [94m_5868 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5868] = 0
              if not [94m_5556 - pendingAnchors[addr([94m_5553)]:
                  require pendingAnchors[addr([94m_5553)]
                  [94m_5891 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5891] = 0 / pendingAnchors[addr([94m_5553)]
                  mem[[94m_5562 + 32] = [94m_5891
                  [94m_5916 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5916] = maxSwing
                  if 0 / pendingAnchors[addr([94m_5553)] > maxSwing:
                      mem[mem[64]] = caller
                      mem[mem[64] + 32] = addr([94m_5553)
                      mem[mem[64] + 64] = 2
                      mem[mem[64] + 96] = 6
                      mem[mem[64] + 128] = 0 / pendingAnchors[addr([94m_5553)]
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_5553),
                            uint256 error=2,
                            uint256 info=6,
                            uint256 detail=0 / pendingAnchors[addr(_5553)])
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                  else:
                      if not pendingAnchors[addr([94m_5553)]:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5553)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 7
                          mem[mem[64] + 128] = 0
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5553),
                                uint256 error=2,
                                uint256 info=7,
                                uint256 detail=0)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not [94m_5556:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5553)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 9
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              mem[0] = addr([94m_5553)
                              mem[32] = 7
                              if not pendingAnchors[addr([94m_5553)]:
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6175 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6175] = [94m_5556
                                  else:
                                      [94m_6119 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6119] = (block.number / 120) + 1
                                      mem[[94m_6119 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6286 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6286] = [94m_5556
                              else:
                                  mem[0] = addr([94m_5553)
                                  mem[32] = 7
                                  pendingAnchors[addr([94m_5553)] = 0
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6289 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6289] = [94m_5556
                                  else:
                                      [94m_6184 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6184] = (block.number / 120) + 1
                                      mem[[94m_6184 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6419 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6419] = [94m_5556
                              mem[0] = addr([94m_5553)
                              mem[32] = 1
                              _assetPrices[addr([94m_5553)] = [94m_5556
                              mem[mem[64]] = addr([94m_5553)
                              mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                              mem[mem[64] + 64] = [94m_5556
                              mem[mem[64] + 96] = [94m_5556
                              log PricePosted(
                                    address asset=addr(_5553),
                                    uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                    uint256 requestedPriceMantissa=_5556,
                                    uint256 newPriceMantissa=_5556)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
              else:
                  require (10^18 * [94m_5556) - (10^18 * pendingAnchors[addr([94m_5553)]) / [94m_5556 - pendingAnchors[addr([94m_5553)] == 10^18
                  require pendingAnchors[addr([94m_5553)]
                  [94m_5901 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5901] = (10^18 * [94m_5556) - (10^18 * pendingAnchors[addr([94m_5553)]) / pendingAnchors[addr([94m_5553)]
                  mem[[94m_5562 + 32] = [94m_5901
                  [94m_5936 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5936] = maxSwing
                  if (10^18 * [94m_5556) - (10^18 * pendingAnchors[addr([94m_5553)]) / pendingAnchors[addr([94m_5553)] > maxSwing:
                      mem[mem[64]] = caller
                      mem[mem[64] + 32] = addr([94m_5553)
                      mem[mem[64] + 64] = 2
                      mem[mem[64] + 96] = 6
                      mem[mem[64] + 128] = (10^18 * [94m_5556) - (10^18 * pendingAnchors[addr([94m_5553)]) / pendingAnchors[addr([94m_5553)]
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_5553),
                            uint256 error=2,
                            uint256 info=6,
                            uint256 detail=(10^18 * _5556) - (10^18 * pendingAnchors[addr(_5553)]) / pendingAnchors[addr(_5553)])
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                  else:
                      if not pendingAnchors[addr([94m_5553)]:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5553)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 7
                          mem[mem[64] + 128] = 0
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5553),
                                uint256 error=2,
                                uint256 info=7,
                                uint256 detail=0)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not [94m_5556:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5553)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 9
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              mem[0] = addr([94m_5553)
                              mem[32] = 7
                              if not pendingAnchors[addr([94m_5553)]:
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6386 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6386] = [94m_5556
                                  else:
                                      [94m_6272 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6272] = (block.number / 120) + 1
                                      mem[[94m_6272 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6525 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6525] = [94m_5556
                              else:
                                  mem[0] = addr([94m_5553)
                                  mem[32] = 7
                                  pendingAnchors[addr([94m_5553)] = 0
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6528 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6528] = [94m_5556
                                  else:
                                      [94m_6395 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6395] = (block.number / 120) + 1
                                      mem[[94m_6395 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6680 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6680] = [94m_5556
                              mem[0] = addr([94m_5553)
                              mem[32] = 1
                              _assetPrices[addr([94m_5553)] = [94m_5556
                              mem[mem[64]] = addr([94m_5553)
                              mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                              mem[mem[64] + 64] = [94m_5556
                              mem[mem[64] + 96] = [94m_5556
                              log PricePosted(
                                    address asset=addr(_5553),
                                    uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                    uint256 requestedPriceMantissa=_5556,
                                    uint256 newPriceMantissa=_5556)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
          else:
              [94m_5728 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5728] = 0
              require [94m_5556 <= pendingAnchors[addr([94m_5553)]
              [94m_5848 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5848] = pendingAnchors[addr([94m_5553)] - [94m_5556
              [94m_5860 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5860] = 0
              [94m_5872 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5872] = 0
              if not pendingAnchors[addr([94m_5553)] - [94m_5556:
                  require pendingAnchors[addr([94m_5553)]
                  [94m_5897 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5897] = 0 / pendingAnchors[addr([94m_5553)]
                  mem[[94m_5562 + 32] = [94m_5897
                  [94m_5930 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5930] = maxSwing
                  if 0 / pendingAnchors[addr([94m_5553)] > maxSwing:
                      mem[mem[64]] = caller
                      mem[mem[64] + 32] = addr([94m_5553)
                      mem[mem[64] + 64] = 2
                      mem[mem[64] + 96] = 6
                      mem[mem[64] + 128] = 0 / pendingAnchors[addr([94m_5553)]
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_5553),
                            uint256 error=2,
                            uint256 info=6,
                            uint256 detail=0 / pendingAnchors[addr(_5553)])
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                  else:
                      if not pendingAnchors[addr([94m_5553)]:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5553)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 7
                          mem[mem[64] + 128] = 0
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5553),
                                uint256 error=2,
                                uint256 info=7,
                                uint256 detail=0)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not [94m_5556:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5553)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 9
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              mem[0] = addr([94m_5553)
                              mem[32] = 7
                              if not pendingAnchors[addr([94m_5553)]:
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6299 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6299] = [94m_5556
                                  else:
                                      [94m_6200 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6200] = (block.number / 120) + 1
                                      mem[[94m_6200 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6439 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6439] = [94m_5556
                              else:
                                  mem[0] = addr([94m_5553)
                                  mem[32] = 7
                                  pendingAnchors[addr([94m_5553)] = 0
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6442 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6442] = [94m_5556
                                  else:
                                      [94m_6308 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6308] = (block.number / 120) + 1
                                      mem[[94m_6308 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6584 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6584] = [94m_5556
                              mem[0] = addr([94m_5553)
                              mem[32] = 1
                              _assetPrices[addr([94m_5553)] = [94m_5556
                              mem[mem[64]] = addr([94m_5553)
                              mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                              mem[mem[64] + 64] = [94m_5556
                              mem[mem[64] + 96] = [94m_5556
                              log PricePosted(
                                    address asset=addr(_5553),
                                    uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                    uint256 requestedPriceMantissa=_5556,
                                    uint256 newPriceMantissa=_5556)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
              else:
                  require (10^18 * pendingAnchors[addr([94m_5553)]) - (10^18 * [94m_5556) / pendingAnchors[addr([94m_5553)] - [94m_5556 == 10^18
                  require pendingAnchors[addr([94m_5553)]
                  [94m_5907 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5907] = (10^18 * pendingAnchors[addr([94m_5553)]) - (10^18 * [94m_5556) / pendingAnchors[addr([94m_5553)]
                  mem[[94m_5562 + 32] = [94m_5907
                  [94m_5954 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5954] = maxSwing
                  if (10^18 * pendingAnchors[addr([94m_5553)]) - (10^18 * [94m_5556) / pendingAnchors[addr([94m_5553)] > maxSwing:
                      mem[mem[64]] = caller
                      mem[mem[64] + 32] = addr([94m_5553)
                      mem[mem[64] + 64] = 2
                      mem[mem[64] + 96] = 6
                      mem[mem[64] + 128] = (10^18 * pendingAnchors[addr([94m_5553)]) - (10^18 * [94m_5556) / pendingAnchors[addr([94m_5553)]
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_5553),
                            uint256 error=2,
                            uint256 info=6,
                            uint256 detail=(10^18 * pendingAnchors[addr(_5553)]) - (10^18 * _5556) / pendingAnchors[addr(_5553)])
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                  else:
                      if not pendingAnchors[addr([94m_5553)]:
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5553)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 7
                          mem[mem[64] + 128] = 0
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5553),
                                uint256 error=2,
                                uint256 info=7,
                                uint256 detail=0)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if not [94m_5556:
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5553)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 9
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              mem[0] = addr([94m_5553)
                              mem[32] = 7
                              if not pendingAnchors[addr([94m_5553)]:
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6551 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6551] = [94m_5556
                                  else:
                                      [94m_6425 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6425] = (block.number / 120) + 1
                                      mem[[94m_6425 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6697 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6697] = [94m_5556
                              else:
                                  mem[0] = addr([94m_5553)
                                  mem[32] = 7
                                  pendingAnchors[addr([94m_5553)] = 0
                                  if (block.number / 120) + 1 <= 0:
                                      mem[0] = addr([94m_5553)
                                      [94m_6700 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6700] = [94m_5556
                                  else:
                                      [94m_6560 = mem[64]
                                      mem[64] = mem[64] + 64
                                      mem[[94m_6560] = (block.number / 120) + 1
                                      mem[[94m_6560 + 32] = [94m_5556
                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                      mem[0] = addr([94m_5553)
                                      [94m_6819 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6819] = [94m_5556
                              mem[0] = addr([94m_5553)
                              mem[32] = 1
                              _assetPrices[addr([94m_5553)] = [94m_5556
                              mem[mem[64]] = addr([94m_5553)
                              mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                              mem[mem[64] + 64] = [94m_5556
                              mem[mem[64] + 96] = [94m_5556
                              log PricePosted(
                                    address asset=addr(_5553),
                                    uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                    uint256 requestedPriceMantissa=_5556,
                                    uint256 newPriceMantissa=_5556)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
      else:
          mem[[94m_5562 + 96] = anchors[addr([94m_5553)].field_0
          [94m_5582 = mem[64]
          mem[64] = mem[64] + 32
          mem[0] = addr([94m_5553)
          mem[32] = 6
          mem[[94m_5582] = anchors[addr([94m_5553)].field_256
          mem[[94m_5562 + 64] = [94m_5582
          if not anchors[addr([94m_5553)].field_0:
              [94m_5590 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5590] = [94m_5556
              mem[[94m_5562 + 64] = [94m_5590
              if not [94m_5556:
                  mem[mem[64]] = caller
                  mem[mem[64] + 32] = addr([94m_5553)
                  mem[mem[64] + 64] = 2
                  mem[mem[64] + 96] = 7
                  mem[mem[64] + 128] = 0
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_5553),
                        uint256 error=2,
                        uint256 info=7,
                        uint256 detail=0)
                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
              else:
                  if not [94m_5556:
                      mem[mem[64]] = caller
                      mem[mem[64] + 32] = addr([94m_5553)
                      mem[mem[64] + 64] = 2
                      mem[mem[64] + 96] = 9
                      mem[mem[64] + 128] = 0
                      log OracleFailure(
                            address msgSender=caller,
                            address asset=addr(_5553),
                            uint256 error=2,
                            uint256 info=9,
                            uint256 detail=0)
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                  else:
                      mem[0] = addr([94m_5553)
                      mem[32] = 7
                      if not pendingAnchors[addr([94m_5553)]:
                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                              mem[0] = addr([94m_5553)
                              [94m_5676 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5676] = [94m_5556
                          else:
                              [94m_5648 = mem[64]
                              mem[64] = mem[64] + 64
                              mem[[94m_5648] = (block.number / 120) + 1
                              mem[[94m_5648 + 32] = [94m_5556
                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                              anchors[addr([94m_5553)].field_256 = [94m_5556
                              mem[0] = addr([94m_5553)
                              [94m_5717 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5717] = [94m_5556
                      else:
                          mem[0] = addr([94m_5553)
                          mem[32] = 7
                          pendingAnchors[addr([94m_5553)] = 0
                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                              mem[0] = addr([94m_5553)
                              [94m_5720 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5720] = [94m_5556
                          else:
                              [94m_5685 = mem[64]
                              mem[64] = mem[64] + 64
                              mem[[94m_5685] = (block.number / 120) + 1
                              mem[[94m_5685 + 32] = [94m_5556
                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                              anchors[addr([94m_5553)].field_256 = [94m_5556
                              mem[0] = addr([94m_5553)
                              [94m_5767 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5767] = [94m_5556
                      mem[0] = addr([94m_5553)
                      mem[32] = 1
                      _assetPrices[addr([94m_5553)] = [94m_5556
                      mem[mem[64]] = addr([94m_5553)
                      mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                      mem[mem[64] + 64] = [94m_5556
                      mem[mem[64] + 96] = [94m_5556
                      log PricePosted(
                            address asset=addr(_5553),
                            uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                            uint256 requestedPriceMantissa=_5556,
                            uint256 newPriceMantissa=_5556)
                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
          else:
              [94m_5600 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5600] = 0
              [94m_5606 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5606] = 0
              [94m_5611 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5611] = 10^18
              [94m_5614 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5614] = 0
              [94m_5632 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5632] = 0
              [94m_5694 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5694] = 0
              [94m_5770 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5770] = 0
              [94m_5808 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5808] = maxSwing
              [94m_5834 = mem[64]
              mem[64] = mem[64] + 32
              mem[[94m_5834] = 0
              if maxSwing + 10^18 < 10^18:
                  [94m_5851 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5851] = 0
                  [94m_5864 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5864] = 0
                  mem[[94m_5562] = [94m_5864
                  mem[[94m_5562 + 160] = 0
                  mem[mem[64]] = caller
                  mem[mem[64] + 32] = addr([94m_5553)
                  mem[mem[64] + 64] = 2
                  mem[mem[64] + 96] = 5
                  mem[mem[64] + 128] = 12
                  log OracleFailure(
                        address msgSender=caller,
                        address asset=addr(_5553),
                        uint256 error=2,
                        uint256 info=5,
                        uint256 detail=12)
                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
              else:
                  [94m_5852 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5852] = maxSwing + 10^18
                  [94m_5871 = mem[64]
                  mem[64] = mem[64] + 32
                  mem[[94m_5871] = 0
                  if not anchors[addr([94m_5553)].field_256:
                      [94m_5912 = mem[64]
                      mem[64] = mem[64] + 32
                      mem[[94m_5912] = 0
                      if [94m_5556 > 0:
                          mem[[94m_5562] = [94m_5912
                          mem[[94m_5562 + 160] = 1
                          mem[[94m_5562 + 192] = anchors[addr([94m_5553)].field_256
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5553)
                          mem[mem[64] + 64] = 2
                          if anchors[addr([94m_5553)].field_256:
                              mem[mem[64] + 96] = 9
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=9,
                                    uint256 detail=0)
                          else:
                              mem[mem[64] + 96] = 7
                              mem[mem[64] + 128] = 0
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=7,
                                    uint256 detail=0)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          [94m_5976 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5976] = maxSwing
                          [94m_6005 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_6005] = 0
                          if maxSwing > 10^18:
                              [94m_6108 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_6108] = 0
                              [94m_6383 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_6383] = 0
                              mem[[94m_5562] = [94m_6383
                              mem[[94m_5562 + 160] = 0
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5553)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 5
                              mem[mem[64] + 128] = 12
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=5,
                                    uint256 detail=12)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              [94m_6109 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_6109] = -maxSwing + 10^18
                              [94m_6658 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_6658] = 0
                              if not anchors[addr([94m_5553)].field_256:
                                  [94m_7712 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_7712] = 0
                                  if [94m_5556 < 0:
                                      mem[[94m_5562] = [94m_7712
                                      mem[[94m_5562 + 160] = 1
                                      mem[[94m_5562 + 192] = anchors[addr([94m_5553)].field_256
                                      mem[mem[64]] = caller
                                      mem[mem[64] + 32] = addr([94m_5553)
                                      mem[mem[64] + 64] = 2
                                      if anchors[addr([94m_5553)].field_256:
                                          mem[mem[64] + 96] = 9
                                          mem[mem[64] + 128] = 0
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5553),
                                                uint256 error=2,
                                                uint256 info=9,
                                                uint256 detail=0)
                                      else:
                                          mem[mem[64] + 96] = 7
                                          mem[mem[64] + 128] = 0
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5553),
                                                uint256 error=2,
                                                uint256 info=7,
                                                uint256 detail=0)
                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                  else:
                                      mem[[94m_5562] = [94m_5573
                                      mem[[94m_5562 + 160] = 0
                                      if not anchors[addr([94m_5553)].field_256:
                                          mem[mem[64]] = caller
                                          mem[mem[64] + 32] = addr([94m_5553)
                                          mem[mem[64] + 64] = 2
                                          mem[mem[64] + 96] = 7
                                          mem[mem[64] + 128] = 0
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5553),
                                                uint256 error=2,
                                                uint256 info=7,
                                                uint256 detail=0)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                      else:
                                          if not [94m_5556:
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5553)
                                              mem[mem[64] + 64] = 2
                                              mem[mem[64] + 96] = 9
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5553),
                                                    uint256 error=2,
                                                    uint256 info=9,
                                                    uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              mem[0] = addr([94m_5553)
                                              mem[32] = 7
                                              if not pendingAnchors[addr([94m_5553)]:
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                      mem[0] = addr([94m_5553)
                                                      [94m_8223 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_8223] = [94m_5556
                                                  else:
                                                      [94m_8058 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_8058] = (block.number / 120) + 1
                                                      mem[[94m_8058 + 32] = [94m_5556
                                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                                      mem[0] = addr([94m_5553)
                                                      [94m_8576 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_8576] = [94m_5556
                                              else:
                                                  mem[0] = addr([94m_5553)
                                                  mem[32] = 7
                                                  pendingAnchors[addr([94m_5553)] = 0
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                      mem[0] = addr([94m_5553)
                                                      [94m_8579 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_8579] = [94m_5556
                                                  else:
                                                      [94m_8232 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_8232] = (block.number / 120) + 1
                                                      mem[[94m_8232 + 32] = [94m_5556
                                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                                      mem[0] = addr([94m_5553)
                                                      [94m_9030 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_9030] = [94m_5556
                                              mem[0] = addr([94m_5553)
                                              mem[32] = 1
                                              _assetPrices[addr([94m_5553)] = [94m_5556
                                              mem[mem[64]] = addr([94m_5553)
                                              mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                                              mem[mem[64] + 64] = [94m_5556
                                              mem[mem[64] + 96] = [94m_5556
                                              log PricePosted(
                                                    address asset=addr(_5553),
                                                    uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                                    uint256 requestedPriceMantissa=_5556,
                                                    uint256 newPriceMantissa=_5556)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                              else:
                                  require (10^18 * anchors[addr([94m_5553)].field_256) - (maxSwing * anchors[addr([94m_5553)].field_256) / anchors[addr([94m_5553)].field_256 == -maxSwing + 10^18
                                  require (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 >= 5 * 10^17
                                  [94m_7716 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_7716] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                  if [94m_5556 >= (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18:
                                      mem[[94m_5562] = [94m_5573
                                      mem[[94m_5562 + 160] = 0
                                      if not anchors[addr([94m_5553)].field_256:
                                          mem[mem[64]] = caller
                                          mem[mem[64] + 32] = addr([94m_5553)
                                          mem[mem[64] + 64] = 2
                                          mem[mem[64] + 96] = 7
                                          mem[mem[64] + 128] = 0
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5553),
                                                uint256 error=2,
                                                uint256 info=7,
                                                uint256 detail=0)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                      else:
                                          if not [94m_5556:
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5553)
                                              mem[mem[64] + 64] = 2
                                              mem[mem[64] + 96] = 9
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5553),
                                                    uint256 error=2,
                                                    uint256 info=9,
                                                    uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              mem[0] = addr([94m_5553)
                                              mem[32] = 7
                                              if not pendingAnchors[addr([94m_5553)]:
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                      mem[0] = addr([94m_5553)
                                                      [94m_8943 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_8943] = [94m_5556
                                                  else:
                                                      [94m_8526 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_8526] = (block.number / 120) + 1
                                                      mem[[94m_8526 + 32] = [94m_5556
                                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                                      mem[0] = addr([94m_5553)
                                                      [94m_9432 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_9432] = [94m_5556
                                              else:
                                                  mem[0] = addr([94m_5553)
                                                  mem[32] = 7
                                                  pendingAnchors[addr([94m_5553)] = 0
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                      mem[0] = addr([94m_5553)
                                                      [94m_9435 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_9435] = [94m_5556
                                                  else:
                                                      [94m_8952 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_8952] = (block.number / 120) + 1
                                                      mem[[94m_8952 + 32] = [94m_5556
                                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5553)].field_256 = [94m_5556
                                                      mem[0] = addr([94m_5553)
                                                      [94m_9962 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_9962] = [94m_5556
                                              mem[0] = addr([94m_5553)
                                              mem[32] = 1
                                              _assetPrices[addr([94m_5553)] = [94m_5556
                                              mem[mem[64]] = addr([94m_5553)
                                              mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                                              mem[mem[64] + 64] = [94m_5556
                                              mem[mem[64] + 96] = [94m_5556
                                              log PricePosted(
                                                    address asset=addr(_5553),
                                                    uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                                    uint256 requestedPriceMantissa=_5556,
                                                    uint256 newPriceMantissa=_5556)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                  else:
                                      mem[[94m_5562] = [94m_7716
                                      mem[[94m_5562 + 160] = 1
                                      mem[[94m_5562 + 192] = anchors[addr([94m_5553)].field_256
                                      if not anchors[addr([94m_5553)].field_256:
                                          mem[mem[64]] = caller
                                          mem[mem[64] + 32] = addr([94m_5553)
                                          mem[mem[64] + 64] = 2
                                          mem[mem[64] + 96] = 7
                                          mem[mem[64] + 128] = 0
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5553),
                                                uint256 error=2,
                                                uint256 info=7,
                                                uint256 detail=0)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                      else:
                                          if not (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18:
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5553)
                                              mem[mem[64] + 64] = 2
                                              mem[mem[64] + 96] = 9
                                              mem[mem[64] + 128] = 0
                                              log OracleFailure(
                                                    address msgSender=caller,
                                                    address asset=addr(_5553),
                                                    uint256 error=2,
                                                    uint256 info=9,
                                                    uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              mem[0] = addr([94m_5553)
                                              mem[32] = 7
                                              if not pendingAnchors[addr([94m_5553)]:
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                      mem[0] = addr([94m_5553)
                                                      [94m_8997 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_8997] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                  else:
                                                      [94m_8562 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_8562] = (block.number / 120) + 1
                                                      mem[[94m_8562 + 32] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5553)].field_256 = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      mem[0] = addr([94m_5553)
                                                      [94m_9477 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_9477] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                              else:
                                                  mem[0] = addr([94m_5553)
                                                  mem[32] = 7
                                                  pendingAnchors[addr([94m_5553)] = 0
                                                  if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                      mem[0] = addr([94m_5553)
                                                      [94m_9480 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_9480] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                  else:
                                                      [94m_9006 = mem[64]
                                                      mem[64] = mem[64] + 64
                                                      mem[[94m_9006] = (block.number / 120) + 1
                                                      mem[[94m_9006 + 32] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                      anchors[addr([94m_5553)].field_256 = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      mem[0] = addr([94m_5553)
                                                      [94m_10016 = mem[64]
                                                      mem[64] = mem[64] + 32
                                                      mem[[94m_10016] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                              mem[0] = addr([94m_5553)
                                              mem[32] = 1
                                              _assetPrices[addr([94m_5553)] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                              log PricePosted(
                                                    address asset=addr(_5553),
                                                    uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                                    uint256 requestedPriceMantissa=_5556,
                                                    uint256 newPriceMantissa=(10^18 * anchors[addr(_5553)].field_256) + (-1 * maxSwing * anchors[addr(_5553)].field_256) + 5 * 10^17 / 10^18)
                                              mem[mem[64]] = addr([94m_5553)
                                              mem[mem[64] + 32] = [94m_5556
                                              mem[mem[64] + 64] = anchors[addr([94m_5553)].field_256
                                              mem[mem[64] + 96] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                              log CappedPricePosted(
                                                    address asset=addr(_5553),
                                                    uint256 requestedPriceMantissa=_5556,
                                                    uint256 anchorPriceMantissa=anchors[addr(_5553)].field_256,
                                                    uint256 cappedPriceMantissa=(10^18 * anchors[addr(_5553)].field_256) + (-1 * maxSwing * anchors[addr(_5553)].field_256) + 5 * 10^17 / 10^18)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                  else:
                      if (maxSwing * anchors[addr([94m_5553)].field_256) + (10^18 * anchors[addr([94m_5553)].field_256) / anchors[addr([94m_5553)].field_256 != maxSwing + 10^18:
                          [94m_5885 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5885] = 0
                          [94m_5896 = mem[64]
                          mem[64] = mem[64] + 32
                          mem[[94m_5896] = 0
                          mem[[94m_5562] = [94m_5896
                          mem[[94m_5562 + 160] = 0
                          mem[mem[64]] = caller
                          mem[mem[64] + 32] = addr([94m_5553)
                          mem[mem[64] + 64] = 2
                          mem[mem[64] + 96] = 5
                          mem[mem[64] + 128] = 12
                          log OracleFailure(
                                address msgSender=caller,
                                address asset=addr(_5553),
                                uint256 error=2,
                                uint256 info=5,
                                uint256 detail=12)
                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                      else:
                          if (maxSwing * anchors[addr([94m_5553)].field_256) + (10^18 * anchors[addr([94m_5553)].field_256) + 5 * 10^17 < 5 * 10^17:
                              [94m_5906 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5906] = 0
                              [94m_5911 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5911] = 0
                              mem[[94m_5562] = [94m_5911
                              mem[[94m_5562 + 160] = 0
                              mem[mem[64]] = caller
                              mem[mem[64] + 32] = addr([94m_5553)
                              mem[mem[64] + 64] = 2
                              mem[mem[64] + 96] = 5
                              mem[mem[64] + 128] = 12
                              log OracleFailure(
                                    address msgSender=caller,
                                    address asset=addr(_5553),
                                    uint256 error=2,
                                    uint256 info=5,
                                    uint256 detail=12)
                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                          else:
                              [94m_5924 = mem[64]
                              mem[64] = mem[64] + 32
                              mem[[94m_5924] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                              if [94m_5556 > (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18:
                                  mem[[94m_5562] = [94m_5924
                                  mem[[94m_5562 + 160] = 1
                                  mem[[94m_5562 + 192] = anchors[addr([94m_5553)].field_256
                                  if not anchors[addr([94m_5553)].field_256:
                                      mem[mem[64]] = caller
                                      mem[mem[64] + 32] = addr([94m_5553)
                                      mem[mem[64] + 64] = 2
                                      mem[mem[64] + 96] = 7
                                      mem[mem[64] + 128] = 0
                                      log OracleFailure(
                                            address msgSender=caller,
                                            address asset=addr(_5553),
                                            uint256 error=2,
                                            uint256 info=7,
                                            uint256 detail=0)
                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                  else:
                                      if not (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18:
                                          mem[mem[64]] = caller
                                          mem[mem[64] + 32] = addr([94m_5553)
                                          mem[mem[64] + 64] = 2
                                          mem[mem[64] + 96] = 9
                                          mem[mem[64] + 128] = 0
                                          log OracleFailure(
                                                address msgSender=caller,
                                                address asset=addr(_5553),
                                                uint256 error=2,
                                                uint256 info=9,
                                                uint256 detail=0)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                      else:
                                          mem[0] = addr([94m_5553)
                                          mem[32] = 7
                                          if not pendingAnchors[addr([94m_5553)]:
                                              if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                  mem[0] = addr([94m_5553)
                                                  [94m_7272 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_7272] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                              else:
                                                  [94m_7138 = mem[64]
                                                  mem[64] = mem[64] + 64
                                                  mem[[94m_7138] = (block.number / 120) + 1
                                                  mem[[94m_7138 + 32] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                  anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                  anchors[addr([94m_5553)].field_256 = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                  mem[0] = addr([94m_5553)
                                                  [94m_7411 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_7411] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                          else:
                                              mem[0] = addr([94m_5553)
                                              mem[32] = 7
                                              pendingAnchors[addr([94m_5553)] = 0
                                              if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                  mem[0] = addr([94m_5553)
                                                  [94m_7414 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_7414] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                              else:
                                                  [94m_7281 = mem[64]
                                                  mem[64] = mem[64] + 64
                                                  mem[[94m_7281] = (block.number / 120) + 1
                                                  mem[[94m_7281 + 32] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                  anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                  anchors[addr([94m_5553)].field_256 = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                  mem[0] = addr([94m_5553)
                                                  [94m_7542 = mem[64]
                                                  mem[64] = mem[64] + 32
                                                  mem[[94m_7542] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                          mem[0] = addr([94m_5553)
                                          mem[32] = 1
                                          _assetPrices[addr([94m_5553)] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                          log PricePosted(
                                                address asset=addr(_5553),
                                                uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                                uint256 requestedPriceMantissa=_5556,
                                                uint256 newPriceMantissa=(10^18 * anchors[addr(_5553)].field_256) + (maxSwing * anchors[addr(_5553)].field_256) + 5 * 10^17 / 10^18)
                                          mem[mem[64]] = addr([94m_5553)
                                          mem[mem[64] + 32] = [94m_5556
                                          mem[mem[64] + 64] = anchors[addr([94m_5553)].field_256
                                          mem[mem[64] + 96] = (10^18 * anchors[addr([94m_5553)].field_256) + (maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                          log CappedPricePosted(
                                                address asset=addr(_5553),
                                                uint256 requestedPriceMantissa=_5556,
                                                uint256 anchorPriceMantissa=anchors[addr(_5553)].field_256,
                                                uint256 cappedPriceMantissa=(10^18 * anchors[addr(_5553)].field_256) + (maxSwing * anchors[addr(_5553)].field_256) + 5 * 10^17 / 10^18)
                                          require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                          mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                              else:
                                  [94m_6004 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_6004] = maxSwing
                                  [94m_6031 = mem[64]
                                  mem[64] = mem[64] + 32
                                  mem[[94m_6031] = 0
                                  if maxSwing > 10^18:
                                      [94m_6263 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6263] = 0
                                      [94m_6655 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6655] = 0
                                      mem[[94m_5562] = [94m_6655
                                      mem[[94m_5562 + 160] = 0
                                      mem[mem[64]] = caller
                                      mem[mem[64] + 32] = addr([94m_5553)
                                      mem[mem[64] + 64] = 2
                                      mem[mem[64] + 96] = 5
                                      mem[mem[64] + 128] = 12
                                      log OracleFailure(
                                            address msgSender=caller,
                                            address asset=addr(_5553),
                                            uint256 error=2,
                                            uint256 info=5,
                                            uint256 detail=12)
                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                  else:
                                      [94m_6264 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6264] = -maxSwing + 10^18
                                      [94m_6891 = mem[64]
                                      mem[64] = mem[64] + 32
                                      mem[[94m_6891] = 0
                                      if not anchors[addr([94m_5553)].field_256:
                                          [94m_7715 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_7715] = 0
                                          if [94m_5556 < 0:
                                              mem[[94m_5562] = [94m_7715
                                              mem[[94m_5562 + 160] = 1
                                              mem[[94m_5562 + 192] = anchors[addr([94m_5553)].field_256
                                              mem[mem[64]] = caller
                                              mem[mem[64] + 32] = addr([94m_5553)
                                              mem[mem[64] + 64] = 2
                                              if anchors[addr([94m_5553)].field_256:
                                                  mem[mem[64] + 96] = 9
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5553),
                                                        uint256 error=2,
                                                        uint256 info=9,
                                                        uint256 detail=0)
                                              else:
                                                  mem[mem[64] + 96] = 7
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5553),
                                                        uint256 error=2,
                                                        uint256 info=7,
                                                        uint256 detail=0)
                                              require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                              mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                          else:
                                              mem[[94m_5562] = [94m_5573
                                              mem[[94m_5562 + 160] = 0
                                              if not anchors[addr([94m_5553)].field_256:
                                                  mem[mem[64]] = caller
                                                  mem[mem[64] + 32] = addr([94m_5553)
                                                  mem[mem[64] + 64] = 2
                                                  mem[mem[64] + 96] = 7
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5553),
                                                        uint256 error=2,
                                                        uint256 info=7,
                                                        uint256 detail=0)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                              else:
                                                  if not [94m_5556:
                                                      mem[mem[64]] = caller
                                                      mem[mem[64] + 32] = addr([94m_5553)
                                                      mem[mem[64] + 64] = 2
                                                      mem[mem[64] + 96] = 9
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5553),
                                                            uint256 error=2,
                                                            uint256 info=9,
                                                            uint256 detail=0)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                  else:
                                                      mem[0] = addr([94m_5553)
                                                      mem[32] = 7
                                                      if not pendingAnchors[addr([94m_5553)]:
                                                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                              mem[0] = addr([94m_5553)
                                                              [94m_8871 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_8871] = [94m_5556
                                                          else:
                                                              [94m_8478 = mem[64]
                                                              mem[64] = mem[64] + 64
                                                              mem[[94m_8478] = (block.number / 120) + 1
                                                              mem[[94m_8478 + 32] = [94m_5556
                                                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                              anchors[addr([94m_5553)].field_256 = [94m_5556
                                                              mem[0] = addr([94m_5553)
                                                              [94m_9372 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_9372] = [94m_5556
                                                      else:
                                                          mem[0] = addr([94m_5553)
                                                          mem[32] = 7
                                                          pendingAnchors[addr([94m_5553)] = 0
                                                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                              mem[0] = addr([94m_5553)
                                                              [94m_9375 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_9375] = [94m_5556
                                                          else:
                                                              [94m_8880 = mem[64]
                                                              mem[64] = mem[64] + 64
                                                              mem[[94m_8880] = (block.number / 120) + 1
                                                              mem[[94m_8880 + 32] = [94m_5556
                                                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                              anchors[addr([94m_5553)].field_256 = [94m_5556
                                                              mem[0] = addr([94m_5553)
                                                              [94m_9890 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_9890] = [94m_5556
                                                      mem[0] = addr([94m_5553)
                                                      mem[32] = 1
                                                      _assetPrices[addr([94m_5553)] = [94m_5556
                                                      mem[mem[64]] = addr([94m_5553)
                                                      mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                                                      mem[mem[64] + 64] = [94m_5556
                                                      mem[mem[64] + 96] = [94m_5556
                                                      log PricePosted(
                                                            address asset=addr(_5553),
                                                            uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                                            uint256 requestedPriceMantissa=_5556,
                                                            uint256 newPriceMantissa=_5556)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                      else:
                                          require (10^18 * anchors[addr([94m_5553)].field_256) - (maxSwing * anchors[addr([94m_5553)].field_256) / anchors[addr([94m_5553)].field_256 == -maxSwing + 10^18
                                          require (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 >= 5 * 10^17
                                          [94m_7720 = mem[64]
                                          mem[64] = mem[64] + 32
                                          mem[[94m_7720] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                          if [94m_5556 >= (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18:
                                              mem[[94m_5562] = [94m_5573
                                              mem[[94m_5562 + 160] = 0
                                              if not anchors[addr([94m_5553)].field_256:
                                                  mem[mem[64]] = caller
                                                  mem[mem[64] + 32] = addr([94m_5553)
                                                  mem[mem[64] + 64] = 2
                                                  mem[mem[64] + 96] = 7
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5553),
                                                        uint256 error=2,
                                                        uint256 info=7,
                                                        uint256 detail=0)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                              else:
                                                  if not [94m_5556:
                                                      mem[mem[64]] = caller
                                                      mem[mem[64] + 32] = addr([94m_5553)
                                                      mem[mem[64] + 64] = 2
                                                      mem[mem[64] + 96] = 9
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5553),
                                                            uint256 error=2,
                                                            uint256 info=9,
                                                            uint256 detail=0)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                  else:
                                                      mem[0] = addr([94m_5553)
                                                      mem[32] = 7
                                                      if not pendingAnchors[addr([94m_5553)]:
                                                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                              mem[0] = addr([94m_5553)
                                                              [94m_9803 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_9803] = [94m_5556
                                                          else:
                                                              [94m_9322 = mem[64]
                                                              mem[64] = mem[64] + 64
                                                              mem[[94m_9322] = (block.number / 120) + 1
                                                              mem[[94m_9322 + 32] = [94m_5556
                                                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                              anchors[addr([94m_5553)].field_256 = [94m_5556
                                                              mem[0] = addr([94m_5553)
                                                              [94m_10260 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_10260] = [94m_5556
                                                      else:
                                                          mem[0] = addr([94m_5553)
                                                          mem[32] = 7
                                                          pendingAnchors[addr([94m_5553)] = 0
                                                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                              mem[0] = addr([94m_5553)
                                                              [94m_10263 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_10263] = [94m_5556
                                                          else:
                                                              [94m_9812 = mem[64]
                                                              mem[64] = mem[64] + 64
                                                              mem[[94m_9812] = (block.number / 120) + 1
                                                              mem[[94m_9812 + 32] = [94m_5556
                                                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                              anchors[addr([94m_5553)].field_256 = [94m_5556
                                                              mem[0] = addr([94m_5553)
                                                              [94m_10618 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_10618] = [94m_5556
                                                      mem[0] = addr([94m_5553)
                                                      mem[32] = 1
                                                      _assetPrices[addr([94m_5553)] = [94m_5556
                                                      mem[mem[64]] = addr([94m_5553)
                                                      mem[mem[64] + 32] = _assetPrices[addr([94m_5553)]
                                                      mem[mem[64] + 64] = [94m_5556
                                                      mem[mem[64] + 96] = [94m_5556
                                                      log PricePosted(
                                                            address asset=addr(_5553),
                                                            uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                                            uint256 requestedPriceMantissa=_5556,
                                                            uint256 newPriceMantissa=_5556)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
                                          else:
                                              mem[[94m_5562] = [94m_7720
                                              mem[[94m_5562 + 160] = 1
                                              mem[[94m_5562 + 192] = anchors[addr([94m_5553)].field_256
                                              if not anchors[addr([94m_5553)].field_256:
                                                  mem[mem[64]] = caller
                                                  mem[mem[64] + 32] = addr([94m_5553)
                                                  mem[mem[64] + 64] = 2
                                                  mem[mem[64] + 96] = 7
                                                  mem[mem[64] + 128] = 0
                                                  log OracleFailure(
                                                        address msgSender=caller,
                                                        address asset=addr(_5553),
                                                        uint256 error=2,
                                                        uint256 info=7,
                                                        uint256 detail=0)
                                                  require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                  mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                              else:
                                                  if not (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18:
                                                      mem[mem[64]] = caller
                                                      mem[mem[64] + 32] = addr([94m_5553)
                                                      mem[mem[64] + 64] = 2
                                                      mem[mem[64] + 96] = 9
                                                      mem[mem[64] + 128] = 0
                                                      log OracleFailure(
                                                            address msgSender=caller,
                                                            address asset=addr(_5553),
                                                            uint256 error=2,
                                                            uint256 info=9,
                                                            uint256 detail=0)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 2
                                                  else:
                                                      mem[0] = addr([94m_5553)
                                                      mem[32] = 7
                                                      if not pendingAnchors[addr([94m_5553)]:
                                                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                              mem[0] = addr([94m_5553)
                                                              [94m_9857 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_9857] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                          else:
                                                              [94m_9358 = mem[64]
                                                              mem[64] = mem[64] + 64
                                                              mem[[94m_9358] = (block.number / 120) + 1
                                                              mem[[94m_9358 + 32] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                              anchors[addr([94m_5553)].field_256 = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                              mem[0] = addr([94m_5553)
                                                              [94m_10305 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_10305] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      else:
                                                          mem[0] = addr([94m_5553)
                                                          mem[32] = 7
                                                          pendingAnchors[addr([94m_5553)] = 0
                                                          if (block.number / 120) + 1 <= anchors[addr([94m_5553)].field_0:
                                                              mem[0] = addr([94m_5553)
                                                              [94m_10308 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_10308] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                          else:
                                                              [94m_9866 = mem[64]
                                                              mem[64] = mem[64] + 64
                                                              mem[[94m_9866] = (block.number / 120) + 1
                                                              mem[[94m_9866 + 32] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                              anchors[addr([94m_5553)].field_0 = (block.number / 120) + 1
                                                              anchors[addr([94m_5553)].field_256 = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                              mem[0] = addr([94m_5553)
                                                              [94m_10672 = mem[64]
                                                              mem[64] = mem[64] + 32
                                                              mem[[94m_10672] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      mem[0] = addr([94m_5553)
                                                      mem[32] = 1
                                                      _assetPrices[addr([94m_5553)] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      log PricePosted(
                                                            address asset=addr(_5553),
                                                            uint256 previousPriceMantissa=_assetPrices[addr(_5553)],
                                                            uint256 requestedPriceMantissa=_5556,
                                                            uint256 newPriceMantissa=(10^18 * anchors[addr(_5553)].field_256) + (-1 * maxSwing * anchors[addr(_5553)].field_256) + 5 * 10^17 / 10^18)
                                                      mem[mem[64]] = addr([94m_5553)
                                                      mem[mem[64] + 32] = [94m_5556
                                                      mem[mem[64] + 64] = anchors[addr([94m_5553)].field_256
                                                      mem[mem[64] + 96] = (10^18 * anchors[addr([94m_5553)].field_256) + (-1 * maxSwing * anchors[addr([94m_5553)].field_256) + 5 * 10^17 / 10^18
                                                      log CappedPricePosted(
                                                            address asset=addr(_5553),
                                                            uint256 requestedPriceMantissa=_5556,
                                                            uint256 anchorPriceMantissa=anchors[addr(_5553)].field_256,
                                                            uint256 cappedPriceMantissa=(10^18 * anchors[addr(_5553)].field_256) + (-1 * maxSwing * anchors[addr(_5553)].field_256) + 5 * 10^17 / 10^18)
                                                      require [94midx < mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
                                                      mem[(32 * [94midx) + (32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192] = 0
      [94midx = [94midx + 1
      continue 
  mem[mem[64]] = 32
  mem[mem[64] + 32] = mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
  [94m_5552 = mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160]
  mem[mem[64] + 64 len floor32(mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160])] = mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 192 len floor32(mem[(32 * _assets.length) + (32 * _requestedPriceMantissas.length) + 160])]
  return 32, mem[mem[64] + 32 len (32 * [94m_5552) + 32]


# hash = 0x451b1e3a
# getter = ['storage', 160, 0, 3]
# const = None
# payable = False
def pendingAnchorAdmin(): # not payable
  return pendingAnchorAdminAddress


# hash = 0x485feabe
# getter = None
# const = ['return', 120]
# payable = False
const numBlocksPerPeriod = 120


# hash = 0x5c975abb
# getter = ['bool', ['storage', 8, 0, 0]]
# const = None
# payable = False
def paused(): # not payable
  return bool(paused)


# hash = 0x5e9a523c
# getter = None
# const = None
# payable = False
def assetPrices(address _asset): # not payable
  require calldata.size - 4 >= 32
  if not paused:
      return _assetPrices[addr(_asset)]
  else:
      return 0


# hash = 0x5fe3b567
# getter = ['storage', 160, 8, 0]
# const = None
# payable = False
def comptroller(): # not payable
  return comptrollerAddress


# hash = 0x66331bba
# getter = None
# const = ['return', 1]
# payable = False
const unknown66331bba = 1


# hash = 0x692374e3
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 6]]]
# const = None
# payable = False
def anchors(address _param1): # not payable
  require calldata.size - 4 >= 32
  return anchors[_param1].field_0, anchors[_param1].field_256


# hash = 0x80959721
# getter = ['storage', 160, 0, 4]
# const = None
# payable = False
def poster(): # not payable
  return posterAddress


# hash = 0x9964622c
# getter = None
# const = None
# payable = False
def _setPendingAnchorAdmin(address _newPendingAnchorAdmin): # not payable
  require calldata.size - 4 >= 32
  if anchorAdminAddress != caller:
      log OracleFailure(
            address msgSender=caller,
            address asset=0,
            uint256 error=1,
            uint256 info=2,
            uint256 detail=0)
      return 1
  pendingAnchorAdminAddress = _newPendingAnchorAdmin
  log NewPendingAnchorAdmin(
        address oldPendingAnchorAdmin=pendingAnchorAdminAddress,
        address newPendingAnchorAdmin=_newPendingAnchorAdmin)
  return 0


# hash = 0x9e8c4d95
# getter = ['storage', 256, 0, ['sha3', ['data', ['cd', 4], 7]]]
# const = None
# payable = False
def pendingAnchors(address _param1): # not payable
  require calldata.size - 4 >= 32
  return pendingAnchors[_param1]


# hash = 0xc5faf1d5
# getter = ['storage', 256, 0, 5]
# const = None
# payable = False
def maxSwing(): # not payable
  return maxSwing


# hash = 0xccb13cbd
# getter = None
# const = None
# payable = False
def _acceptAnchorAdmin(): # not payable
  if pendingAnchorAdminAddress != caller:
      log OracleFailure(
            address msgSender=caller,
            address asset=0,
            uint256 error=1,
            uint256 info=0,
            uint256 detail=0)
      return 1
  anchorAdminAddress = pendingAnchorAdminAddress
  pendingAnchorAdminAddress = 0
  log NewAnchorAdmin(
        address oldAnchorAdmin=anchorAdminAddress,
        address newAnchorAdmin=caller)
  return 0


# hash = 0xde9d0e85
# getter = None
# const = None
# payable = False
def _setPendingAnchor(address _asset, uint256 _newScaledPrice): # not payable
  require calldata.size - 4 >= 64
  if anchorAdminAddress != caller:
      log OracleFailure(
            address msgSender=caller,
            address asset=addr(_asset),
            uint256 error=1,
            uint256 info=3,
            uint256 detail=0)
      return 1
  pendingAnchors[addr(_asset)] = _newScaledPrice
  log NewPendingAnchor(
        address anchorAdmin=caller,
        address asset=addr(_asset),
        uint256 oldScaledPrice=pendingAnchors[addr(_asset)],
        uint256 newScaledPrice=_newScaledPrice)
  return 0


# hash = 0xfc57d4df
# getter = None
# const = None
# payable = False
def unknownfc57d4df(addr _param1): # not payable
  require calldata.size - 4 >= 32
  require ext_code.size(comptrollerAddress)
  static call comptrollerAddress.markets(address param1) with:
          gas gas_remaining wei
         args _param1
  if not ext_call.success:
      revert with ext_call.return_data[0 len return_data.size]
  require return_data.size >= 96
  if ext_call.return_data[0]:
      require ext_code.size(_param1)
      static call _param1.underlying() with:
              gas gas_remaining wei
      if not ext_call.success:
          revert with ext_call.return_data[0 len return_data.size]
      require return_data.size >= 32
      if not paused:
          return _assetPrices[ext_call.return_data[12 len 20]]
      else:
          return 0
  else:
      return 0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert


