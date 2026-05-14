# 03-4. ベイズの定理 — 「観測から学ぶ」を数学にする

**このページのゴール**: ベイズの定理を理解し、Python で事前→事後の更新ができるようになる。
これが**機械学習の根本原理**の1つ (ベイズ推論)。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`03_probability_statistics/notebooks/04_bayes.ipynb`](notebooks/04_bayes.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`01_probability_basics.md`](01_probability_basics.md) — 条件付き確率
> - [`02_distributions.md`](02_distributions.md) — 確率分布

---

## 1. ベイズの定理 — 条件付き確率を「ひっくり返す」

### 数式

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
$$

これだけ。
**右辺の $P(B \mid A)$ から、左辺の $P(A \mid B)$ を求めるための式**。

### 何が嬉しいのか

普通、データから直接計算できるのは:
- $P(\text{症状} \mid \text{病気})$ : 病気の人の何 % が発熱するか (← 病院のデータ)
- $P(\text{単語} \mid \text{スパム})$ : スパムメールに「キャンペーン」が出る確率 (← 過去のラベル)

でも本当に知りたいのは:
- $P(\text{病気} \mid \text{症状})$ : この症状なら病気の確率は?
- $P(\text{スパム} \mid \text{単語})$ : この単語があるならスパムか?

ベイズの定理が**この方向の変換**をしてくれる。

---

## 2. 用語整理

ベイズの定理を再掲して、各部分に名前をつけます:

$$
\underbrace{P(\theta \mid D)}_{\text{事後 (posterior)}}
=
\frac{\overbrace{P(D \mid \theta)}^{\text{尤度 (likelihood)}} \cdot \overbrace{P(\theta)}^{\text{事前 (prior)}}}{\underbrace{P(D)}_{\text{周辺尤度 (evidence)}}}
$$

| 名前 | 意味 |
|---|---|
| **事前 $P(\theta)$** | データを見る前の信念 |
| **尤度 $P(D \mid \theta)$** | パラメータ $\theta$ の下でデータ $D$ が出る確率 |
| **事後 $P(\theta \mid D)$** | データを見た後の信念 (更新済み) |
| **周辺尤度 $P(D)$** | データそのものの確率 (規格化のための定数) |

ベイズの定理は、要するに:

> **事後 ∝ 尤度 × 事前**

「**観測データに合うように、信念を更新せよ**」 ということ。

---

## 3. 古典的な例: 病気の検査

ある病気の検査:
- 病気の事前確率: $P(D) = 1\%$
- 検査の感度: $P(+ \mid D) = 99\%$ (病気の人が陽性となる確率)
- 検査の特異度: $P(- \mid \neg D) = 99\%$ (健康な人が陰性となる確率)

**陽性が出たとき、本当に病気である確率 $P(D \mid +)$ は?**

### 計算

ベイズの定理:

$$
P(D \mid +) = \frac{P(+ \mid D) \cdot P(D)}{P(+)}
$$

分母は全確率の定理:

$$
P(+) = P(+ \mid D) P(D) + P(+ \mid \neg D) P(\neg D)
     = 0.99 \cdot 0.01 + 0.01 \cdot 0.99
     = 0.0198
$$

よって:

$$
P(D \mid +) = \frac{0.99 \cdot 0.01}{0.0198} = 0.5
$$

### Python

```python
P_D = 0.01           # 事前確率
P_pos_given_D = 0.99  # 感度
P_neg_given_notD = 0.99  # 特異度
P_pos_given_notD = 1 - P_neg_given_notD

# 全確率
P_pos = P_pos_given_D * P_D + P_pos_given_notD * (1 - P_D)

# ベイズの定理
P_D_given_pos = P_pos_given_D * P_D / P_pos
print(f'P(病気 | +) = {P_D_given_pos:.4f}')   # 0.5
```

### 衝撃の事実

「**99% 正確な検査**」で陽性が出ても、本当に病気な確率は **わずか 50%**。

理由: 「病気の事前確率 1%」が低すぎるため、健康な人 99% のうち偽陽性 (1%) で出る人数が、病気の人 (1%) と同じくらいになる。

→ **基底率の無視 (base rate fallacy)** という、人類が陥りがちな認知バイアスの数学的解釈。

---

## 4. ベイズ更新 — データが増えるたびに信念を更新

### コインの偏りを推定

「**このコインは表が出やすい/裏が出やすい?**」を、投げる回数を増やしながら推定:

#### 設定
- $\theta$: 表が出る確率 (未知)
- 事前 $P(\theta)$: 一様分布 $U(0, 1)$ (どんな $\theta$ も等確率)
- データ $D$: 投げ結果 (例: 表表裏表裏)

#### 尤度

$n$ 回中 $k$ 回表が出たデータ:

$$
P(D \mid \theta) = \theta^k (1 - \theta)^{n - k}
$$

#### 事後

$$
P(\theta \mid D) \propto \theta^k (1 - \theta)^{n - k} \cdot 1
$$

これは **ベータ分布** $\mathrm{Beta}(k+1, n-k+1)$ になります (一様事前のとき)。

### Python で逐次更新

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# 真のコインの偏り (本当は分からない)
true_p = 0.7
rng = np.random.default_rng(42)

theta_grid = np.linspace(0, 1, 200)
prior = np.ones_like(theta_grid)   # 一様事前

# 段階的にデータを増やして事後を計算
for n_flips in [0, 5, 20, 100, 1000]:
    flips = rng.binomial(1, true_p, n_flips)
    k = flips.sum()
    
    # 事後 ∝ 尤度 × 事前
    likelihood = theta_grid**k * (1 - theta_grid)**(n_flips - k)
    posterior = likelihood * prior
    posterior /= posterior.sum()  # 規格化
    
    map_estimate = theta_grid[posterior.argmax()]
    print(f'n={n_flips}: MAP推定 θ ≈ {map_estimate:.3f}')
```

データを増やすほど、事後は真の値 $\theta = 0.7$ に集中していきます。

---

## 5. ML / AI への接続

### ナイーブベイズ分類器

メールがスパムか普通か:

$$
P(\text{spam} \mid \text{words}) \propto P(\text{words} \mid \text{spam}) \cdot P(\text{spam})
$$

「ナイーブ」に **単語が条件付き独立** と仮定:

$$
P(\text{words} \mid \text{spam}) = \prod_i P(w_i \mid \text{spam})
$$

仮定は強引だが、シンプルで強力。スパムフィルタの定番。

### ベイズ最適化 (Bayesian Optimization)

ハイパーパラメータ探索の手法。
「次にどの設定を試すか」を、これまでの試行データから**ベイズ的に決定**。

### 変分ベイズ (Variational Bayes) と VAE

ベイズの定理の事後 $P(\theta \mid D)$ が解析的に計算できないとき、**簡単な分布で近似**する技法。
**Variational Autoencoder (VAE)** や **拡散モデル (Diffusion Model)** の根幹。

### Bayesian Deep Learning

ニューラルネットの重み $W$ を**点推定**ではなく**分布 $P(W \mid D)$** として推定する分野。
「予測の不確かさ」を出せるのが特徴。

---

## 6. ベイズ vs 頻度主義 — 確率の解釈論争

| | **ベイズ主義 (Bayesian)** | **頻度主義 (Frequentist)** |
|---|---|---|
| 確率の意味 | **信念の度合い** | **長期的な頻度** |
| パラメータ | **確率変数** (分布を持つ) | 固定された未知の値 |
| 推定 | **事後分布** | **最尤推定 (MLE)** |
| 信頼区間 | **信用区間** (確率で書ける) | **信頼区間** (区間が動く) |

ML 界隈は、**ベイズ寄り**の文化。
ChatGPT のような生成モデルも、**「次の単語の確率分布」を推論する**点でベイズ的です。

---

## 7. ハマりポイント

- **事前を主観で決めて良いのか?**: 大量データがあれば事後は事前の影響を受けにくい (asymptotic に消える)。少ないデータなら事前が大事。
- **基底率を忘れない**: 病気検査の例のように、事前確率が低い疾患の陽性は信用しすぎない
- **「事前は無情報がいい」とは限らない**: 一様事前にも仮定が入っている (どのスケールで一様か?)
- **規格化定数 $P(D)$ は計算が大変**: 数値的には省いて事後 $\propto$ 尤度 $\times$ 事前 だけで OK のことが多い

---

## まとめ

| 概念 | 数式 |
|---|---|
| ベイズの定理 | $P(\theta \mid D) = \dfrac{P(D \mid \theta) P(\theta)}{P(D)}$ |
| 全確率の定理 | $P(D) = \sum_\theta P(D \mid \theta) P(\theta)$ |
| 事後 ∝ 尤度 × 事前 | $P(\theta \mid D) \propto P(D \mid \theta) P(\theta)$ |
| ナイーブベイズ | $P(c \mid x_1,\dots,x_n) \propto P(c) \prod_i P(x_i \mid c)$ |

**この章のキー**: ベイズの定理は「**条件付き確率を逆転する**」道具。事前を持って、データで更新するのが ML の根本パラダイム。

---

## 次へ

確率・統計章 完了 🎉

→ 次の章: [`../05_optimization/README.md`](../05_optimization/README.md)

## 関連
- [`02_distributions.md`](02_distributions.md) — 事前・尤度として使う分布
- [`06_ml_math_bridge/`](../06_ml_math_bridge/README.md) — クロスエントロピー = 対数尤度

---

## 🔍 ググってみよう

- **トーマス・ベイズ (Thomas Bayes)** — 1763年に死後に発表された定理
- **基底率の誤謬 (base rate fallacy)** — ベイズを知らないと陥る認知バイアス
- **共役事前分布 (conjugate prior)** — 事後が事前と同じ分布族になる便利な組み合わせ
- **MCMC (Markov Chain Monte Carlo)** — 複雑な事後分布をサンプリングする手法
- **PyMC, Stan, NumPyro** — ベイズ推論の代表的なライブラリ
- **A/B テストのベイズ的解釈** — 頻度主義と何が違うか
- **クロスエントロピー = 負の対数尤度** — 分類問題の損失関数の正体
- **モンティ・ホール問題** — ベイズで解ける有名なパズル

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`03_expectation_variance.md`](03_expectation_variance.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`../05_optimization/README.md`](../05_optimization/README.md) |
