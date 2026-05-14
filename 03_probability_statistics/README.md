# 03. 確率・統計 (Probability & Statistics)

**ゴール**: 確率変数・確率分布・期待値・ベイズの定理を、数式と Python の両方で扱える。
機械学習はほぼ確率モデルなので、ここが弱いと論文が読めない。

## なぜ重要か
- 機械学習の出力はほぼ**確率**（「90% の確信度で猫」）
- 損失関数の多くは確率モデルから導かれる（クロスエントロピー = 対数尤度）
- 生成AI (LLM) は次トークンの確率分布を予測している

## 学習ステップ

| ファイル | 内容 | 所要時間 |
|---|---|---|
| `01_probability_basics.md` | 確率、独立性、条件付き確率 | 1.5時間 |
| `02_distributions.md` | 正規分布、二項分布、ポアソン分布 | 2時間 |
| `03_expectation_variance.md` | 期待値、分散、共分散 | 1.5時間 |
| `04_bayes.md` | ベイズの定理、事前・事後分布 | 2時間 |

## キーとなる Python ツール

```python
import numpy as np
from scipy import stats

# サンプリング
rng = np.random.default_rng(seed=42)
samples = rng.normal(loc=0, scale=1, size=1000)  # N(0, 1) から1000個

# 統計量
print(np.mean(samples))   # 平均 μ
print(np.std(samples))    # 標準偏差 σ
print(np.var(samples))    # 分散 σ²

# 分布の確率密度関数 (PDF)
x = np.linspace(-4, 4, 100)
pdf = stats.norm.pdf(x, loc=0, scale=1)

# 累積分布関数 (CDF)
cdf = stats.norm.cdf(1.96)  # ≈ 0.975

# ベイズ的計算は手で書くか pymc を使う
```

## 重要な記法

| 記号 | 読み方 | 意味 |
|---|---|---|
| `P(A)` | A の確率 | 事象 A が起こる確率 |
| `P(A \| B)` | A given B | B が起きたという条件のもとでの A の確率 |
| `P(A ∩ B)` | A and B | A と B が同時に起こる確率 |
| `E[X]` | X の期待値 | 確率変数 X の平均 |
| `Var[X]` | X の分散 | 散らばり具合 |
| `X ~ N(μ, σ²)` | X は正規分布に従う | 確率変数の分布の宣言 |

## ML への接続
- 最尤推定 (MLE): 尤度関数を最大化
- ベイズ推定: 事後分布 P(θ|D) = P(D|θ)P(θ)/P(D)
- 交差エントロピー損失: −Σ y log(ŷ)
- 変分推論、生成モデル (VAE, Diffusion)

## サンプル
- [`examples/distribution_demo.py`](examples/distribution_demo.py): 各種分布の可視化

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`../02_calculus/README.md`](../02_calculus/README.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`../05_optimization/README.md`](../05_optimization/README.md) |

> ⚠️ この章は現在 **README + サンプルのみ** の骨格状態です。本文の md は今後拡充予定。
