# Sereum Evaluation Data

The data in this repository was produced during a research collaboration of [NEC Labs Europe](http://www.neclab.eu) and [University of Duisburg-Essen](https://www.syssec.wiwi.uni-due.de/), which resulted in the publication of the NDSS19  paper ["Sereum: Protecting Existing Smart Contracts Against Re-Entrancy Attacks"](https://arxiv.org/abs/1812.05934). 
This repository contains raw and processed data of an extended evaluation of Sereum.
This includes basic unconditional reentrancy detection and covering more blocks of the ethereum mainnet (currently up to block 8 million).

The structure of the repository is:

* [./raw/](raw/) contains the raw data of running Sereum against transactions
    * `reentrancy_from_X_until_Y.csv.xz` - a list of all transactions flagged
       as possible re-entrancy attack in the block range [X, Y] (including both endpoints).
    * `missing_blocks_from_X_until_Y.txt` - a list of blocks that we were not
      able to analyze (e.g., because replaying the block took too long)
* ...

**Note:** This repository uses [git lfs](https://git-lfs.github.com/), be sure to install it!


## Citing in Academic Work

If you want to refer to this data in academic work, please cite [our NDSS paper](https://arxiv.org/abs/1812.05934):

```bibtex
@inproceedings{sereum-ndss19,
  title     = "Sereum: Protecting Existing Smart Contracts Against Re-Entrancy Attacks",
  booktitle = "Proceedings of the Network and Distributed System Security Symposium ({NDSS'19})",
  author    = "Rodler, Michael and Li, Wenting and Karame, Ghassan O and Davi, Lucas",
  year      =  2019
}
```
