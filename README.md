# Sereum Evaluation Data

This repository contains raw and processed data of the evaluation of Sereum v2.
This includes basic unconditional reentrancy detection and covering more
(nearly all) blocks of the ethereum mainnet.

The structure of the repository is:

* [./raw/](raw/) contains the raw data of running Sereum against transactions
    * `reentrancy_from_X_until_Y.csv.xz` - a list of all transactions flagged
       as possible re-entrancy attack in the block range $[X, Y]$.
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
