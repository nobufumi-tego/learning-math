# 03. 確率・統計 (Probability & Statistics)

> ⚠️ **未検証の個人学習教材**: 本章は AI 協働で作成され、専門家の監修を受けていません。誤りを含む可能性があるため、必ず一次情報源で検証してください ([詳細](../DISCLAIMER.md))。
> 📜 **ライセンス**: 文書 [CC BY-NC-SA 4.0](../LICENSE-DOCS) / コード [MIT](../LICENSE-CODE) — 商用利用 (書籍化・有料講座・企業研修等) は[要相談](../DISCLAIMER.md#-商用利用について--commercial-use)

**ゴール**: 確率変数・確率分布・期待値・ベイズの定理を、数式と Python の両方で扱える。
機械学習はほぼ確率モデルなので、ここが弱いと論文が読めない。

## なぜ重要か
- 機械学習の出力はほぼ**確率**（「90% の確信度で猫」）
- 損失関数の多くは確率モデルから導かれる（クロスエントロピー = 対数尤度）
- 生成AI (LLM) は次トークンの確率分布を予測している

---

## 💡 動かす前に

このフォルダのコードは **Jupyter Lab** で対話的に動かすのが推奨です。

```bash
uv run lab.py
```

ブラウザが開いたら、左のファイルツリーから `03_probability_statistics/notebooks/` を開いて、`01_probability_basics.ipynb` から順に。

> 🐧 **「`uv` ってなに?」「ターミナルがわからない」方** は、まず以下を:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎
> - 特に [`08_uv_keeps_pet_healthy.md`](../start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) — uv の使い方
>
> **数学に苦手意識のある方** は:
> - [`start_here/`](../start_here/README.md) — 数式ゼロから始める数学
> - [`00_notation/`](../00_notation/README.md) — 数学記号の読み解き

---

## 学習ステップ

| md (解説) | ipynb (動かす) | 内容 | 所要時間 |
|---|---|---|---|
| [`01_probability_basics.md`](01_probability_basics.md) | [`notebooks/01_probability_basics.ipynb`](notebooks/01_probability_basics.ipynb) | 確率、独立性、条件付き確率、大数の法則 | 1.5時間 |
| [`02_distributions.md`](02_distributions.md) | [`notebooks/02_distributions.ipynb`](notebooks/02_distributions.ipynb) | 正規・二項・ポアソン・指数、中心極限定理 | 2時間 |
| [`03_expectation_variance.md`](03_expectation_variance.md) | [`notebooks/03_expectation_variance.ipynb`](notebooks/03_expectation_variance.ipynb) | 期待値、分散、共分散、相関、標準化 | 1.5時間 |
| [`04_bayes.md`](04_bayes.md) | [`notebooks/04_bayes.ipynb`](notebooks/04_bayes.ipynb) | ベイズの定理、ベイズ更新、ナイーブベイズ | 2時間 |

各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進めるのが効果的**です。

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
| $P(A)$ | A の確率 | 事象 A が起こる確率 |
| $P(A \mid B)$ | A given B | B が起きたという条件のもとでの A の確率 |
| $P(A \cap B)$ | A and B | A と B が同時に起こる確率 |
| $\mathbb{E}[X]$ | X の期待値 | 確率変数 X の平均 |
| $\mathrm{Var}[X]$ | X の分散 | 散らばり具合 |
| $X \sim \mathcal{N}(\mu, \sigma^2)$ | X は正規分布に従う | 確率変数の分布の宣言 |

## ML への接続
- 最尤推定 (MLE): 尤度関数を最大化
- ベイズ推定: 事後分布 $P(\theta \mid D) = P(D \mid \theta) P(\theta) / P(D)$
- 交差エントロピー損失: $-\sum y \log(\hat{y})$
- 変分推論、生成モデル (VAE, Diffusion)

## サンプル
- [`examples/distribution_demo.py`](examples/distribution_demo.py): 各種分布の可視化

---

## 📚 さらに学ぶ

- 📕 **[統計学入門 (赤本)](../appendix/books.md#統計学入門)** (東大出版会) — 統計学入門の決定版
- 📕 **[データ解析のための統計モデリング入門 (緑本)](../appendix/books.md#データ解析のための統計モデリング入門)** (久保拓弥)
- 📕 **[ベイズ推論による機械学習入門](../appendix/books.md#ベイズ推論による機械学習入門)** (須山敦志)
- 🌐 **[StatQuest](../appendix/online.md#statquest-with-josh-starmer)** — 統計を楽しく分かりやすく
- 🌐 **[Seeing Theory](../appendix/online.md#seeing-theory-brown-university)** — 確率をインタラクティブに体感

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`../02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`01_probability_basics.md`](01_probability_basics.md) |
