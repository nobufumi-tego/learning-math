# 03-2. 確率分布 — 正規分布・二項分布・ポアソン分布

**このページのゴール**: 主要な確率分布を「**いつ・なぜ・どう使うか**」で理解し、Python でサンプリング・PDF/PMF 計算ができるようになる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`03_probability_statistics/notebooks/02_distributions.ipynb`](notebooks/02_distributions.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`01_probability_basics.md`](01_probability_basics.md) — 確率の基本
> - [`02_calculus/03_integrals.md`](../02_calculus/03_integrals.md) — 積分 (連続分布の確率は積分)

---

## 1. 確率分布とは — 「確率変数の振る舞いの設計図」

**確率変数** $X$ は、サイコロの目・身長・電圧など、**結果が不確かな量** を表す変数。
**確率分布** はその「**起こりやすさのパターン**」を記述するもの。

### 2 つのタイプ

| タイプ | 例 | 確率の指定方法 |
|---|---|---|
| **離散分布** | サイコロ、コイン、人数 | **PMF** (確率質量関数) $P(X = k)$ |
| **連続分布** | 身長、温度、時間 | **PDF** (確率密度関数) $p(x)$ |

連続分布では、**1 点の確率は $0$**。代わりに「**ある区間に入る確率**」を積分で:

$$
P(a \leq X \leq b) = \int_a^b p(x)\,dx
$$

---

## 2. 正規分布 (Gaussian) — 自然界・統計の主役

最重要分布。身長・誤差・測定値・たくさんの独立な要素の和、すべてこれに従う。

### 数式

$$
X \sim \mathcal{N}(\mu, \sigma^2)
$$

確率密度関数:

$$
p(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)
$$

| パラメータ | 意味 |
|---|---|
| $\mu$ | 平均 (グラフの中心) |
| $\sigma$ | 標準偏差 (広がり) |
| $\sigma^2$ | 分散 |

### 性質

- **左右対称、釣り鐘型**
- **68-95-99.7 ルール**: 平均 $\pm 1\sigma$ に約 68%、$\pm 2\sigma$ に 95%、$\pm 3\sigma$ に 99.7% のデータが入る
- **中心極限定理**: 独立な確率変数の和は、元の分布によらず正規分布に近づく

### Python

```python
import numpy as np
from scipy import stats

rng = np.random.default_rng(seed=42)

# サンプリング
samples = rng.normal(loc=0, scale=1, size=10_000)

# 統計量
print(f'平均 μ̂  = {samples.mean():.4f}')   # ≈ 0
print(f'標準偏差 σ̂ = {samples.std():.4f}')   # ≈ 1

# PDF
print(f'p(0)   = {stats.norm.pdf(0):.4f}')         # 1/√(2π) ≈ 0.3989

# CDF (累積分布関数)
print(f'P(X ≤ 1.96) = {stats.norm.cdf(1.96):.4f}')  # ≈ 0.975 (95%信頼区間)
```

---

## 3. 二項分布 (Binomial) — 「成功/失敗を $n$ 回」

「成功確率 $p$ の試行を独立に $n$ 回繰り返したとき、成功回数 $X$」の分布。

### 数式

$$
X \sim \mathrm{Bin}(n, p)
$$

確率質量関数:

$$
P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}
\qquad (k = 0, 1, \dots, n)
$$

ここで $\binom{n}{k} = \dfrac{n!}{k!(n-k)!}$ は二項係数。

### 性質

- **平均**: $\mathbb{E}[X] = np$
- **分散**: $\mathrm{Var}[X] = np(1-p)$

### 例

「10 回コインを投げて表が出る回数」 → $\mathrm{Bin}(10, 0.5)$。
平均 $5$、分散 $2.5$。

### Python

```python
from scipy import stats
import numpy as np

# Bin(n=10, p=0.5)
n, p = 10, 0.5

# 確率質量関数
for k in [0, 5, 10]:
    print(f'P(X = {k}) = {stats.binom.pmf(k, n, p):.4f}')

# サンプリング
samples = stats.binom.rvs(n, p, size=10_000)
print(f'平均 (実測): {samples.mean():.3f}  (理論 {n*p})')
print(f'分散 (実測): {samples.var():.3f}  (理論 {n*p*(1-p)})')
```

---

## 4. ポアソン分布 (Poisson) — 「単位時間あたりの稀な事象」

「**単位時間に平均 $\lambda$ 回起こる事象が、ちょうど $k$ 回起こる確率**」の分布。

### 例

- 1 時間に来る客数
- 1 ページあたりの誤字数
- 1 平方キロメートルあたりの落雷数
- Web サーバの 1 秒あたりのリクエスト数

### 数式

$$
X \sim \mathrm{Poisson}(\lambda)
$$

確率質量関数:

$$
P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}
\qquad (k = 0, 1, 2, \dots)
$$

### 性質

- **平均と分散が等しい**: $\mathbb{E}[X] = \mathrm{Var}[X] = \lambda$
- **二項分布の極限**: $n \to \infty$, $p \to 0$ で $np = \lambda$ に保つと $\mathrm{Bin}(n, p) \to \mathrm{Poisson}(\lambda)$

### Python

```python
from scipy import stats

# Poisson(λ=3): 1時間に平均3人来る店
lam = 3.0

for k in range(8):
    print(f'P(X = {k}) = {stats.poisson.pmf(k, lam):.4f}')
```

---

## 5. 一様分布 (Uniform) — 「全部等確率」

### 連続一様分布

$X \sim U(a, b)$:

$$
p(x) = \begin{cases}
\dfrac{1}{b - a} & a \leq x \leq b \\
0 & \text{otherwise}
\end{cases}
$$

平均 $\dfrac{a+b}{2}$、分散 $\dfrac{(b-a)^2}{12}$。

### Python

```python
import numpy as np

rng = np.random.default_rng(42)

# U(0, 1) からサンプリング
samples = rng.uniform(0, 1, size=10_000)
print(f'平均 (実測): {samples.mean():.4f}  (理論 0.5)')
print(f'分散 (実測): {samples.var():.4f}  (理論 1/12 ≈ 0.0833)')
```

---

## 6. 指数分布 (Exponential) — 「次のイベントまでの待ち時間」

ポアソン過程で「**次のイベントが起こるまでの時間 $T$**」の分布。

### 数式

$$
T \sim \mathrm{Exp}(\lambda)
$$

確率密度関数:

$$
p(t) = \lambda e^{-\lambda t}
\qquad (t \geq 0)
$$

平均 $\dfrac{1}{\lambda}$、分散 $\dfrac{1}{\lambda^2}$。

### 例

時間あたり平均 $3$ 件の問い合わせがあるカスタマーサポート → 次の問い合わせまでの時間は $\mathrm{Exp}(3)$、平均 $\dfrac{1}{3}$ 時間 (約 20 分)。

---

## 7. 中心極限定理 (Central Limit Theorem, CLT)

> **どんな分布から取ったサンプルでも、$n$ が大きければサンプル平均は正規分布に従う**

数式:

$$
\sqrt{n} \left( \frac{1}{n}\sum_{i=1}^n X_i - \mu \right) \xrightarrow{d} \mathcal{N}(0, \sigma^2)
$$

これが「**正規分布が至る所に出てくる**」 理由。

### Python で確認

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# 一様分布から 30 個ずつサンプリング、その平均を 10000 セット計算
n = 30
n_sets = 10_000
sample_means = np.array([
    rng.uniform(0, 1, n).mean() for _ in range(n_sets)
])

print(f'平均の平均: {sample_means.mean():.4f}  (理論 0.5)')
print(f'平均の標準偏差: {sample_means.std():.4f}  (理論 1/√(12·30) = {1/np.sqrt(12*30):.4f})')
# → 元は一様分布なのに、平均は正規分布になる
```

---

## 8. ML / AI への接続

### モデルの「**生成過程**」の仮定

ML モデルは多くの場合、データの背後に**確率分布**を仮定します:

- 線形回帰: $y_i = w x_i + b + \epsilon_i$, $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$ → **正規分布のノイズ**
- ロジスティック回帰: $y_i \sim \mathrm{Bernoulli}\bigl(\sigma(w x_i + b)\bigr)$ → **二項分布の特殊ケース**
- ポアソン回帰: $y_i \sim \mathrm{Poisson}\bigl(\exp(w x_i)\bigr)$ → **カウントデータ**

### 重みの初期化

ニューラルネット重みは多くの場合、正規分布で初期化:

$$
w \sim \mathcal{N}\left(0, \sqrt{\frac{2}{n_{\text{in}}}}\right)
\qquad \text{(He 初期化)}
$$

### Variational Autoencoder (VAE)

VAE の潜在変数 $z$ は **正規分布から生成**:

$$
z \sim \mathcal{N}(\mu_\phi(x), \sigma_\phi(x)^2)
$$

確率分布の理解は ML を**生成的に** (= データを作る側から) 理解する鍵。

---

## 9. ハマりポイント

- **PDF と PMF を混同しない**: 連続は密度、離散は確率
- **正規分布の "1 点の確率"**: 連続分布だと $P(X = c) = 0$ (区間で考える)
- **標準偏差 $\sigma$ vs 分散 $\sigma^2$**: 後者の方が「自然」だが、人間には前者が直感的
- **$\lambda$ の単位**: ポアソン分布の $\lambda$ は **「単位時間あたりの平均回数」** であり、「全試行の確率」ではない

---

## まとめ

| 分布 | 数式 | 平均 | 分散 | SciPy |
|---|---|---|---|---|
| 正規 | $\mathcal{N}(\mu, \sigma^2)$ | $\mu$ | $\sigma^2$ | `stats.norm` |
| 二項 | $\mathrm{Bin}(n, p)$ | $np$ | $np(1-p)$ | `stats.binom` |
| ポアソン | $\mathrm{Poisson}(\lambda)$ | $\lambda$ | $\lambda$ | `stats.poisson` |
| 一様 | $U(a, b)$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | `stats.uniform` |
| 指数 | $\mathrm{Exp}(\lambda)$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | `stats.expon` |

**この章のキー**: 主要な分布の名前・式・形を覚える。中心極限定理が「正規分布があちこちに出る」理由。

---

## 次へ

→ [`03_expectation_variance.md`](03_expectation_variance.md) — 期待値・分散・共分散

## 関連
- [`02_calculus/03_integrals.md`](../02_calculus/03_integrals.md) — 期待値 = 積分
- [`07_jax/`](../07_jax/README.md) — JAX で正規分布から大量サンプリング

---

## 🔍 ググってみよう

- **中心極限定理 (Central Limit Theorem)** — 確率論の最重要定理
- **モーメント母関数 (MGF)** — 分布を一意に決める道具
- **ガウス分布の畳み込み** — 正規分布同士の和もまた正規分布
- **t 分布** — 正規分布の「ノイズ込み」版、サンプル数が少ないとき
- **χ² 分布** — 正規分布の二乗和
- **F 分布** — 分散比検定で使う
- **ベルヌーイ分布** — 二項分布の $n=1$ 版
- **多変量正規分布** — 多次元の正規分布、共分散行列を持つ

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`01_probability_basics.md`](01_probability_basics.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`03_expectation_variance.md`](03_expectation_variance.md) |
