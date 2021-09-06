true_positive: yes  
fp_type: None  
source: no

# Notes

This seems to be another case for an intentionally vulnerable contract.

Speaking for this:

* The target contract is very simple - basically only `deposit`, `getBalance`
  and a withdraw function.
* Very few transactions and little involved ether.
* Victim contract only used very shortly.

Speaking against this:

* Attacker and victim contract creator are not the same.

