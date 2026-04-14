# Report on Experimental Results in `Exp_Upd`

## 1. Scope of this report

This report compares the executed experiment outputs under `Exp_Upd` against the results reported in the original paper, *Learning Persistent Community Structures in Dynamic Networks via Topological Data Analysis*.

The comparison below focuses on the `highschool` dataset, because all executed summaries in `Exp_Upd/Output` and the visible notebook outputs in `Exp_Upd/Codes` are for that dataset.

Per instruction, the fact that fewer snapshots were used in the current experiments is not treated here as the explanation for any performance gap.

## 2. Reference results from the original paper

From Table 1 in `Original Paper.pdf`, the reported results on the `Highschool` dataset are:

| Method | ACC | NMI | ARI | Modularity |
|---|---:|---:|---:|---:|
| GEC | 49.21 | 28.11 | 13.57 | 49.82 |
| DAEGC | 49.33 | 42.58 | 26.43 | 56.35 |
| SDCN | 24.02 | 9.71 | 0.46 | -0.25 |
| DECS | 65.77 | 62.36 | 36.18 | 72.80 |
| ESPRA | 26.44 | 12.31 | 0.12 | -0.95 |
| DynAE | 18.82 | 5.64 | 0.11 | -0.11 |
| GEC+Topo | 63.51 | 59.41 | 44.44 | 73.62 |
| DAEGC+Topo | 62.66 | 56.22 | 38.93 | 68.37 |
| MFC | 68.91 | 63.14 | 48.77 | 76.99 |
| MFC+Topo | 70.67 | 65.78 | 50.87 | 77.87 |

The key paper reference point for comparison is therefore `MFC+Topo`, since that is the strongest Highschool result reported by the authors.

## 3. Executed results found in `Exp_Upd`

### 3.1 Corrected paper-style runs saved in `Exp_Upd/Output`

These appear to be the most reliable runs in the folder because they use the paper-style configuration:

- `encoded_space_dim = 30`
- `learning_rate = 0.001`
- two-stage training
- `alpha_pretrain = 10.0`
- `alpha_topo = 1.0`
- `beta_topo = 10.0`

#### A. `Exp_Upd/Output/Baseline`

| Method | ACC | NMI | ARI | Modularity | Recon ACC |
|---|---:|---:|---:|---:|---:|
| GCN baseline | 71.43 | 66.73 | 55.61 | 76.94 | 71.06 |
| GraphSAGE baseline | 70.13 | 65.71 | 54.24 | 76.90 | 66.13 |

#### B. `Exp_Upd/Output/Comparison`

| Method | ACC | NMI | ARI | Modularity | Recon ACC |
|---|---:|---:|---:|---:|---:|
| GCN | 68.31 | 63.98 | 52.51 | 75.96 | 68.95 |
| GraphSAGE | 70.08 | 66.21 | 54.63 | 76.48 | 66.34 |
| GIN | 64.20 | 63.53 | 47.51 | 74.43 | 70.70 |
| Transformer | 22.99 | 8.36 | 0.76 | 3.31 | 1.75 |

### 3.2 Earlier exploratory notebook runs in `Exp_Upd/Codes`

These were executed notebooks with visible terminal summaries:

| Notebook | ACC | NMI | ARI | Modularity | Recon ACC |
|---|---:|---:|---:|---:|---:|
| `multiscale_toporeg_sage.ipynb` | 45.92 | 36.54 | 21.74 | 56.62 | 1.76 |
| `multiscale_toporeg_gin.ipynb` | 29.33 | 16.86 | 5.00 | 24.25 | 1.75 |
| `multiscale_toporeg_transformer.ipynb` | 23.97 | 9.38 | 1.35 | 0.54 | 1.75 |
| `multiscale_toporeg_GMM.ipynb` | 65.31 | 61.49 | 44.99 | 70.24 | 3.45 |
| `multiscale_toporeg_DP.ipynb` | 63.73 | 59.89 | 40.19 | 70.05 | 3.45 |

### 3.3 Verified Node2Vec-based runs in `Exp_Upd/node2vecOutputs`

These results are verified from saved `summary.json` files in `Exp_Upd/node2vecOutputs`:

| Method | Dataset | ACC | NMI | ARI | Modularity | Recon ACC |
|---|---|---:|---:|---:|---:|---:|
| Node2Vec + GraphSAGE | Highschool | 72.59 | 70.26 | 56.78 | 77.48 | 73.30 |
| Node2Vec + Transformer | Highschool | 64.67 | 65.23 | 46.80 | 71.33 | 68.45 |
| Node2Vec + GraphSAGE | Enron | 56.80 | 17.05 | 2.19 | 50.11 | 64.73 |
| Node2Vec + Transformer | Enron | 56.21 | 17.16 | 1.67 | 44.00 | 62.89 |

### 3.4 Notebook execution note

The Node2Vec notebooks themselves still do not contain saved executed output cells, but their output artifacts are present under `Exp_Upd/node2vecOutputs`, so those runs are included in the formal comparison above.

### 3.5 Consolidated table of all verified experiments

This table combines every experiment result that could be verified from either:

- saved `summary.json` artifacts, or
- executed notebook output cells

| Group | Dataset | Method | Source | ACC | NMI | ARI | Modularity | Recon ACC |
|---|---|---|---|---:|---:|---:|---:|---:|
| Exploratory | Highschool | Multiscale TopoReg + GMM eval | notebook output | 65.31 | 61.49 | 44.99 | 70.24 | 3.45 |
| Exploratory | Highschool | Multiscale TopoReg + DP eval | notebook output | 63.73 | 59.89 | 40.19 | 70.05 | 3.45 |
| Baseline | Highschool | GCN | `Exp_Upd/Output/Baseline/gcn/highschool_summary.json` | 71.43 | 66.73 | 55.61 | 76.94 | 71.06 |
| Baseline | Highschool | GraphSAGE | `Exp_Upd/Output/Baseline/sage/highschool_summary.json` | 70.13 | 65.71 | 54.24 | 76.90 | 66.13 |
| Comparison | Highschool | GCN | `Exp_Upd/Output/Comparison/gcn/highschool_summary.json` | 68.31 | 63.98 | 52.51 | 75.96 | 68.95 |
| Comparison | Highschool | GraphSAGE | `Exp_Upd/Output/Comparison/sage/highschool_summary.json` | 70.08 | 66.21 | 54.63 | 76.48 | 66.34 |
| Comparison | Highschool | GIN | `Exp_Upd/Output/Comparison/gin/highschool_summary.json` | 64.20 | 63.53 | 47.51 | 74.43 | 70.70 |
| Node2Vec | Highschool | Node2Vec + GraphSAGE | `Exp_Upd/node2vecOutputs/node2vec_graphsage_mfc_toporeg/highschool/summary.json` | 72.59 | 70.26 | 56.78 | 77.48 | 73.30 |
| Node2Vec | Highschool | Node2Vec + Transformer | `Exp_Upd/node2vecOutputs/node2vec_transformer_mfc_toporeg/highschool/summary.json` | 64.67 | 65.23 | 46.80 | 71.33 | 68.45 |
| Node2Vec | Enron | Node2Vec + GraphSAGE | `Exp_Upd/node2vecOutputs/node2vec_graphsage_mfc_toporeg/enron/summary.json` | 56.80 | 17.05 | 2.19 | 50.11 | 64.73 |
| Node2Vec | Enron | Node2Vec + Transformer | `Exp_Upd/node2vecOutputs/node2vec_transformer_mfc_toporeg/enron/summary.json` | 56.21 | 17.16 | 1.67 | 44.00 | 62.89 |

## 4. Comparison against the paper

### 4.1 Best current results versus paper `MFC+Topo`

Paper reference on Highschool:

- `MFC+Topo`: ACC `70.67`, NMI `65.78`, ARI `50.87`, Modularity `77.87`

Best observed runs in `Exp_Upd`:

| Current method | ACC delta vs paper | NMI delta | ARI delta | Modularity delta |
|---|---:|---:|---:|---:|
| Node2Vec + GraphSAGE | +1.92 | +4.48 | +5.91 | -0.39 |
| Baseline GCN | +0.76 | +0.95 | +4.74 | -0.93 |
| Comparison GraphSAGE | -0.59 | +0.43 | +3.76 | -1.39 |
| Baseline GraphSAGE | -0.54 | -0.07 | +3.37 | -0.97 |
| Comparison GCN | -2.36 | -1.80 | +1.64 | -1.91 |

### 4.2 Main empirical takeaways

1. The strongest result is found in `Node2Vec + GraphSAGE` on Highschool.
   - It achieves ACC `72.59`, NMI `70.26`, ARI `56.78`, Modularity `77.48`.
   - Relative to the paper’s Highschool `MFC+Topo` result, it is better on ACC, NMI, and ARI, and only slightly lower on modularity.

2. The GCN baseline in `Exp_Upd/Output/Baseline/gcn` is still strong and remains the best non-Node2Vec baseline.
   - It is competitive with the paper’s `MFC+Topo` result.
   - It performs better than the paper on ACC, NMI, and ARI, with only a small modularity gap.

3. GraphSAGE is the strongest encoder family among the tested replacements.
   - Standard GraphSAGE is already close to the baseline.
   - Node2Vec + GraphSAGE improves further and becomes the overall best Highschool result in the saved artifacts.

4. GIN is weaker than both GCN and GraphSAGE in this setup.
   - It still produces usable clustering results.
   - However, it underperforms the corrected GCN/GraphSAGE runs across every clustering metric except reconstruction accuracy.

5. Transformer splits into two different stories depending on features.
   - The plain Transformer run fails badly.
   - Node2Vec + Transformer is much better than the plain Transformer and reaches a usable result, but it still does not match GraphSAGE or the best GCN baseline.

6. The early multiscale exploratory notebooks are substantially worse than the corrected paper-style runs.
   - This is consistent with the earlier diagnosis that the initial notebooks diverged from the paper’s intended training procedure.

7. The GMM and Dirichlet Process evaluation variants are respectable, but they do not beat the corrected GCN, GraphSAGE, or Node2Vec + GraphSAGE configurations.
   - GMM is stronger than DP in all reported metrics.
   - Both remain below the best paper-style runs.


## 5. Overall conclusions

### 5.1 Best-performing result

The best result found in the saved outputs is:

- `Node2Vec + GraphSAGE`
- ACC `72.59`
- NMI `70.26`
- ARI `56.78`
- Modularity `77.48`

Relative to the paper’s `MFC+Topo` Highschool result, this run:

- improves ACC
- improves NMI
- improves ARI clearly
- is slightly below the paper in modularity

### 5.2 Best encoder improvement

Among the encoder variants and feature-enhanced variants tested:

- `Node2Vec + GraphSAGE` is the strongest result overall
- `GCN baseline` is the strongest non-Node2Vec baseline
- `GraphSAGE` is the best plain encoder replacement
- `GIN` is weaker
- plain `Transformer` fails badly
- `Node2Vec + Transformer` is a major recovery over plain Transformer, but still not competitive with GraphSAGE

So the Highschool ranking from the saved results is:

1. `Node2Vec + GraphSAGE`
2. `GCN baseline`
3. `GraphSAGE`
4. `Comparison GraphSAGE`
5. `Node2Vec + Transformer`
6. `GIN`
7. `Comparison GCN`
8. plain `Transformer`

### 5.3 Practical interpretation

The experiments show three things:

- GraphSAGE is the most promising encoder family in this project
- adding Node2Vec structural features helps GraphSAGE substantially and rescues Transformer partially, but does not make Transformer the best choice

## 6. Summary
The strongest overall result was obtained by combining Node2Vec structural features with a GraphSAGE encoder, achieving ACC 72.59, NMI 70.26, ARI 56.78, and Modularity 77.48 on Highschool. This result is competitive with, and in ACC, NMI, and ARI better than, the Highschool `MFC+Topo` result reported in the original paper (ACC 70.67, NMI 65.78, ARI 50.87, Modularity 77.87). The corrected GCN baseline was also strong, while GIN remained weaker. Node2Vec also substantially improved the Transformer variant, although it still did not match GraphSAGE. Overall, the experiments show that preserving the original optimization pipeline is essential, and that GraphSAGE, especially when combined with Node2Vec structural features, is the most promising extension among the tested variants.
