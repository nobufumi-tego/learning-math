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

🚀 **起動方法** (リポジトリのルートで実行):
- 🪟 **Windows**: [`start.bat`](../start.bat) を **ダブルクリック** ⭐
- 🍎 **Mac** / 🐧 **Linux**: ターミナルで `./start.sh`
- 🪟 **PowerShell 派**: `.\start.ps1`
- 🛠️ **すでに環境がある人**: `uv run lab.py`

uv のインストールから依存関係取得、Jupyter Lab 起動まで全部自動です。

> ⏰ **初回起動は 5〜15 分かかります** (依存関係 500MB〜1GB のダウンロード)。途中で中断せず気長に待ってください。「応答なし」 と出ても OS 更新の遅延なので焦らず ☕
> 2 回目以降は 10〜20 秒で起動します。詳細は ROOT [`README.md`](../README.md#-待ち時間の目安--フリーズしてない-と心配しないでください) の「待ち時間の目安」 参照。

詳細・トラブルシューティングは ROOT [`README.md`](../README.md#step-2--ワンショットスクリプトで起動-推奨) 参照。
🧪 **Jupyter Lab の使い方** (Shift+Enter でセル実行など) は [`docs/jupyter_lab_guide.md`](../docs/jupyter_lab_guide.md) を参照。

ブラウザが開いたら、左のファイルツリーから `03_probability_statistics/notebooks/` を開いて、[`01_probability_basics.ipynb`](notebooks/01_probability_basics.ipynb) から順に。

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
| [`05_descriptive_stats.md`](05_descriptive_stats.md) | [`notebooks/05_descriptive_stats.ipynb`](notebooks/05_descriptive_stats.ipynb) | 中央値・四分位・歪度・尖度、アンスコムの四重奏 | 1.5時間 |
| [`06_estimation.md`](06_estimation.md) | [`notebooks/06_estimation.ipynb`](notebooks/06_estimation.ipynb) | 点推定・区間推定・t分布・最尤推定・MAP推定 | 2.5時間 |
| [`07_hypothesis_testing.md`](07_hypothesis_testing.md) | [`notebooks/07_hypothesis_testing.ipynb`](notebooks/07_hypothesis_testing.ipynb) | 帰無仮説・p値・過誤・検出力・t検定・pハッキング | 2時間 |
| [`08_bayesian_inference.md`](08_bayesian_inference.md) | [`notebooks/08_bayesian_inference.ipynb`](notebooks/08_bayesian_inference.ipynb) | 共役モデル・事後予測分布・信用区間/HPD・ベイズファクター | 2.5時間 |
| [`09_mcmc.md`](09_mcmc.md) | [`notebooks/09_mcmc.ipynb`](notebooks/09_mcmc.ipynb) | モンテカルロ・Metropolis法・収束診断・階層モデル・縮小 | 2.5時間 |

各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進めるのが効果的**です。

> 💡 **01〜04 は「確率」の話、05〜07 は「統計」の話**です。
> 確率は「モデルが分かっているとき、データがどう出るか」を問い、
> 統計は逆に「データが出たとき、モデルはどうなっているか」を問います。
> 05 以降で $\mu$（真の値）と $\bar{x}$（手元のデータ）の区別が主役になります。
>
> 🎲 **08〜09 は「もう一つの立場」＝ベイズ**です。
> 05〜07 の頻度論が「手順の長期的な性質」を問うのに対し、ベイズは「**観測後に残る不確実性**」を
> 確率分布そのもので表します。信頼区間と信用区間の読み方の違いが、その象徴です。

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
| $\pi(\theta)$ / $\pi(\theta \mid x)$ | パイ・シータ | ベイズの**事前分布 / 事後分布**（円周率ではない） |
| $L(\theta; x)$ | 尤度 | $\theta$ の関数として見たデータの出やすさ |
| $\propto$ | proportional to | 比例（正規化定数を省いた、の意味） |
| $\tilde{x}$ | エックス・チルダ | **これから観測する**データ（観測済みの $x$ と区別） |
| $\theta^{(k)}$ | シータ・スーパースクリプト・ケー | $k$ 番目の**標本**（累乗ではない） |

## ML への接続
- 最尤推定 (MLE): 尤度関数を最大化
- ベイズ推定: 事後分布 $P(\theta \mid D) = P(D \mid \theta) P(\theta) / P(D)$
- 交差エントロピー損失: $-\sum y \log(\hat{y})$
- 変分推論、生成モデル (VAE, Diffusion)

## サンプル
- [`examples/distribution_demo.py`](examples/distribution_demo.py): 各種分布の可視化

---

## 📚 さらに学ぶ

- 📕 **[統計学入門 (赤本)](../appendix/books.md#統計学入門-赤本)** (東大出版会) — 統計学入門の決定版
- 📕 **[データ解析のための統計モデリング入門 (緑本)](../appendix/books.md#データ解析のための統計モデリング入門-緑本)** (久保拓弥)
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
