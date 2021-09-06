# contract source code retrieved from eveem.org
# retrieved on 2019-12-03

#  addr = 0x1719EBdc0646fbF268B4FeEb57af842FFbe4d45F 
#  network = mainnet 
#  ver = 26 Apr 2019 
#  problems = {} 

# storage definitions
def storage:
    # storage address 0
    unknown3a7b779eAddress # mask: a s
    # storage address 1
    unknownb4b31becAddress # mask: a s
    # storage address 2
    unknown45d03fceAddress # mask: a s
    # storage address 2
    unknown85463816 # mask: a s
    # storage address 3
    blockNumber # mask: a s
    # storage address 4
    unknown7651bc92
# hash = 0x3a7b779e
# getter = ['storage', 160, 0, 0]
# const = None
# payable = True
def unknown3a7b779e() payable: 
  return munknown3a7b779eAddress


# hash = 0x45d03fce
# getter = ['storage', 160, 0, 2]
# const = None
# payable = True
def unknown45d03fce() payable: 
  return munknown45d03fceAddress


# hash = 0x57e871e7
# getter = ['storage', 256, 0, 3]
# const = None
# payable = True
def blockNumber() payable: 
  return mblockNumber


# hash = 0x7651bc92
# getter = ['storage', 256, 0, ['array', ['range', 0, ['storage', 256, 0, ['length', ['loc', 4]]]], ['loc', 4]]]
# const = None
# payable = True
def unknown7651bc92() payable: 
  return munknown7651bc92m[0 len munknown7651bc92m.lengthm]m.field_0


# hash = 0x85463816
# getter = ['storage', 8, 160, 2]
# const = None
# payable = True
def unknown85463816() payable: 
  return munknown85463816


# hash = 0xb4b31bec
# getter = ['storage', 160, 0, 1]
# const = None
# payable = True
def unknownb4b31bec() payable: 
  return munknownb4b31becAddress


# hash = 0xbb7e8c28
# getter = None
# const = None
# payable = True
def unknownbb7e8c28() payable: 
  if munknown85463816:
      if block.number - mblockNumber >= 35:
          if eth.balance(this.address) > 0:
              mem[164] = uint256(munknown7651bc92m.field_0)
              [94midx = 164
              [94ms = 0
              mwhile munknown7651bc92m.length + 164 > [94midx + 32m:
                  mem[[94midx + 32] = munknown7651bc92m[[94msm]m.field_256
                  [94midx = [94midx + 32
                  [94ms = [94ms + 1
                  mcontinue 
              call munknownb4b31becAddress.queuePayment(bytes bitcoinAddress) with:
                 value eth.balance(this.address) wei
                   gas gas_remaining - 34050 wei
                  args Array(len=munknown7651bc92m.length, data=mem[164 len munknown7651bc92m.length + (floor32(munknown7651bc92m.length - 1) + -munknown7651bc92m.length + 32 % 32)])
              require ext_call.success
          munknown85463816 = 0


# hash = _fallback()
# getter = None
# const = None
# payable = True
def _fallback() payable: # default function
  revert 


