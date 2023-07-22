# FIEOD
Zhong Yuan, **Hongmei Chen***, Tianrui Li, Jia liu, and Shu Wang, 
[Fuzzy Information Entropy-Based Adaptive Approach for Hybrid Feature Outlier Detection](FIEOD_code/2021-FIEOD.pdf), 
Fuzzy Sets and Systems, Volume: 421, Pages: 1-28, 30 September 2021,, 
DOI: [10.1016/j.fss.2020.10.017](https://doi.org/10.1016/j.fss.2020.10.017). (Code)

## Abstract
Fuzzy information entropy based on fuzzy relation in fuzzy rough set theory is an important metric of uncertainty. 
However, the research of fuzzy information entropy for hybrid feature outlier detection has not been reported. 
On this basis, this paper constructs a hybrid feature outlier detection method based on fuzzy information entropy by using fuzzy approximate space with fuzzy similarity relation. 
Firstly, the adaptive fuzzy radius of standard deviation and hybrid fuzzy similarity are employed to construct the fuzzy approximate space, and the relative fuzzy entropy is defined based on the fuzzy information entropy. 
Then, two kinds of metrics are constructed to describe the outlier degree of object. 
Finally, the fuzzy entropy-based outlier factor is integrated to implement outlier detection, and the relevant fuzzy information entropy-based outlier detection algorithm (FIEOD) is designed. 
The FIEOD algorithm is compared with the main outlier detection algorithms on public data. 
The experimental results reveal that the proposed method has better effectiveness and adaptability.

## Usage
You can run Demo_FIEOD.m:
```
clc;
clear all;
format short

load Example.mat

Dataori=Example;

trandata=Dataori;
trandata(:,2:3)=normalize(trandata(:,2:3),'range');

delta=1;
out_factors=FIEOD(trandata,delta)

```
You can get outputs as follows:
```
out_factors =
      0.4106
      0.3320
      0.4272
      0.4295
      0.3690
      0.6077
```

## Citation
If you find FIEOD useful in your research, please consider citing:
```
@article{yuan2021fuzzy,
    title = {Fuzzy information entropy-based adaptive approach for hybrid feature outlier detection},
    author = {Yuan, Zhong and Chen, Hong Mei and Li, Tian Rui and Liu, Jia and Wang, Shu},
    journal = {Fuzzy Sets and Systems},
    volume={421},
    pages={1--28},
    year = {2021},
    doi={10.1016/j.fss.2020.10.017},
    publisher={Elsevier}
}
```