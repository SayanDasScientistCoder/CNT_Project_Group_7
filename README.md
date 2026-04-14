# Learning Persistent Community Structures in Dynamic Networks via Topological Data Analysis

Reproduction and extension of the official PyTorch implementation of the paper *Learning Persistent Community Structures in Dynamic Networks via Topological Data Analysis*, accepted at the 38th Annual AAAI Conference on Artificial Intelligence (AAAI 2024).

**Project Group 7**

| Name | Roll Number |
|---|---|
| Sayan Das | 25CS60R01 |
| Sayan Khan | 25CS60R02 |
| Varsha Das | 25BM6JP57 |
| Lalchand Mondal | 25CS60R77 |

GitHub Repository: https://github.com/SayanDasScientistCoder/CNT_Project_Group_7

---

## Overview

This project reproduces the MFC+TopoReg framework from the original paper and extends it with alternative GNN encoders (GraphSAGE, GIN, Transformer) and Node2Vec structural feature augmentation. Experiments are conducted on the Highschool and Enron dynamic network datasets.

The best result obtained — Node2Vec + GraphSAGE on Highschool — exceeds the paper's reported MFC+Topo result on ACC, NMI, and ARI.

---

## Setup

### Environment

Python (Jupyter Notebook)

### Python Requirements

```
python=3.8.15
cudatoolkit=11.6
pytorch=1.12.1+cu116
numpy=1.23.4
matplotlib=3.6.0
scipy=1.9.3
networkx=2.8.7
gudhi=3.6.0
```

---

## Key Results (Highschool Dataset)

### Paper Reference: MFC+Topo

| ACC | NMI | ARI | Modularity |
|---:|---:|---:|---:|
| 70.67 | 65.78 | 50.87 | 77.87 |

### Best Experimental Result: Node2Vec + GraphSAGE

| ACC | NMI | ARI | Modularity | Recon ACC |
|---:|---:|---:|---:|---:|
| 72.59 | 70.26 | 56.78 | 77.48 | 73.30 |

This result surpasses the paper on ACC (+1.92), NMI (+4.48), and ARI (+5.91), with a negligible modularity gap (-0.39).

---

## Experiment Structure

```
Exp_Upd/
    Output/
        Baseline/       # GCN and GraphSAGE paper-style runs
        Comparison/     # GCN, GraphSAGE, GIN, Transformer comparison
    node2vecOutputs/    # Node2Vec + GraphSAGE and Node2Vec + Transformer
    Codes/              # Exploratory notebooks (multiscale, GMM, DP variants)
```

---

## Encoder Rankings (Highschool)

1. Node2Vec + GraphSAGE
2. GCN Baseline
3. GraphSAGE (Comparison)
4. GraphSAGE (Baseline)
5. Node2Vec + Transformer
6. GIN
7. GCN (Comparison)
8. Plain Transformer

---

## Summary of Findings

- Preserving the original two-stage optimization pipeline is essential for performance.
- GraphSAGE is the most effective encoder replacement for GCN.
- Node2Vec structural features substantially improve both GraphSAGE and Transformer.
- GIN underperforms GCN and GraphSAGE across all clustering metrics.
- The plain Transformer fails without structural feature augmentation.
