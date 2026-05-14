# 03-3. 期待値・分散・共分散 — 確率変数の "重心" と "広がり"

**このページのゴール**: 期待値・分散・共分散・相関の意味と計算、ML での使われ方を理解する。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`03_probability_statistics/notebooks/03_expectation_variance.ipynb`](notebooks/03_expectation_variance.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_distributions.md`](02_distributions.md) — 確率分布
> - [`02_calculus/03_integrals.md`](../02_calculus/03_integrals.md) — 積分

---

## 1. 期待値 (Expectation) — 「平均的に何が出るか」

### 直感

サイコロを何回も振ったら、平均的に何が出る?

$$
\mathbb{E}[X] = \frac{1+2+3+4+5+6}{6} = 3.5
$$

**期待値**は「**長い目で見たときの平均**」。
重心、と覚えてもOK。

### 数式

#### 離散の場合

$$
\mathbb{E}[X] = \sum_i x_i \cdot P(X = x_i)
$$

#### 連続の場合

$$
\mathbb{E}[X] = \int_{-\infty}^{\infty} x \cdot p(x)\,dx
$$

「**値 $\times$ 確率 (密度)**」を全範囲で足す (積分する)。

### 線形性 — 期待値の最強性質

$$
\mathbb{E}[aX + bY] = a \mathbb{E}[X] + b \mathbb{E}[Y]
$$

$X$ と $Y$ が**独立じゃなくても**成立。**期待値の線形性** は確率論の最重要ツール。

### Python

```python
import numpy as np
from scipy import stats

# サイコロ
xs = np.array([1, 2, 3, 4, 5, 6])
ps = np.array([1/6] * 6)
ev = np.sum(xs * ps)
print(f'E[サイコロ] = {ev}')   # 3.5

# 正規分布 N(0, 1) の期待値
print(f'E[N(0,1)] = {stats.norm.mean():.4f}')   # 0.0

# 標本平均で近似
rng = np.random.default_rng(42)
samples = rng.normal(0, 1, size=1_000_000)
print(f'標本平均: {samples.mean():.4f}')   # ≈ 0
```

---

## 2. 分散 (Variance) — 「広がりの大きさ」

### 直感

期待値だけだと「平均値」しか分からない。
**「平均からどれくらい離れているか」** を測るのが分散。

### 数式

$$
\mathrm{Var}[X] = \mathbb{E}\bigl[(X - \mu)^2\bigr]
\qquad \text{ここで } \mu = \mathbb{E}[X]
$$

「**平均からの距離の 2 乗の期待値**」。

#### 計算しやすい等価形

$$
\mathrm{Var}[X] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2
$$

これを **「2 乗の期待値 − 期待値の 2 乗」** と覚える。

### 標準偏差

$$
\sigma = \sqrt{\mathrm{Var}[X]}
$$

分散は単位が 2 乗されて (例: $\text{m}^2$) 直感的に分かりにくいので、平方根を取った**標準偏差**を使うことが多い。
標準偏差は元と同じ単位 (例: $\text{m}$)。

### 性質

- $\mathrm{Var}[aX + b] = a^2 \mathrm{Var}[X]$ (定数 $b$ は影響なし、$a$ は 2 乗で効く)
- 独立なら $\mathrm{Var}[X + Y] = \mathrm{Var}[X] + \mathrm{Var}[Y]$ (※独立性が必要)

### Python

```python
import numpy as np

rng = np.random.default_rng(42)
data = rng.normal(0, 2, size=10_000)   # N(0, 4)

print(f'平均:       {data.mean():.4f}')   # ≈ 0
print(f'分散:       {data.var():.4f}')    # ≈ 4
print(f'標準偏差:   {data.std():.4f}')    # ≈ 2

# 確認: E[X²] - (E[X])²
print(f'E[X²] - (E[X])² = {(data**2).mean() - data.mean()**2:.4f}')
```

> 💡 **`np.var` の `ddof` 引数**: デフォルトは $0$ (母分散)。サンプルから推定するときは `ddof=1` で **不偏分散** (n で割らず n-1 で割る) を使う。

---

## 3. 共分散 (Covariance) と 相関 (Correlation)

### 共分散

2 つの確率変数 $X, Y$ の **共変動** を測る:

$$
\mathrm{Cov}[X, Y] = \mathbb{E}\bigl[(X - \mu_X)(Y - \mu_Y)\bigr]
$$

| 値 | 意味 |
|---|---|
| 正 | $X$ が大きいとき $Y$ も大きい傾向 (正の相関) |
| 負 | $X$ が大きいとき $Y$ は小さい傾向 (負の相関) |
| 0 | 線形な関係なし (※独立とは限らない) |

### 相関係数 (Pearson)

共分散は単位の影響を受けるので、$-1 \sim +1$ に正規化:

$$
\rho_{X, Y} = \frac{\mathrm{Cov}[X, Y]}{\sigma_X \sigma_Y}
$$

| 値 | 意味 |
|---|---|
| $+1$ | 完全な正の線形関係 |
| $0$ | 線形相関なし |
| $-1$ | 完全な負の線形関係 |

### Python

```python
import numpy as np

rng = np.random.default_rng(42)

# 強い正の相関を持つ 2 変数
x = rng.normal(0, 1, size=1000)
y = 0.7 * x + 0.3 * rng.normal(0, 1, size=1000)   # x の影響 + ノイズ

# 共分散行列
cov_matrix = np.cov(x, y)
print('共分散行列:')
print(cov_matrix)

# 相関係数
corr = np.corrcoef(x, y)[0, 1]
print(f'\n相関係数: {corr:.4f}')  # ≈ 0.9 程度
```

### ⚠️ 「相関は因果ではない」

これは数学だけでなく**統計の最も重要な教訓**:

- アイスクリームの売上と水難事故件数は強く相関 → どっちも夏に増えるだけ
- 国の GDP と国民の幸福度は相関 → でも GDP を上げれば幸福になる、とは限らない

→ ググってみよう: **「Spurious correlation」**

---

## 4. 多変量の場合 — 共分散行列

ベクトル $\mathbf{X} = (X_1, X_2, \dots, X_n)^\top$ に対して、**共分散行列** $\Sigma$:

$$
\Sigma_{ij} = \mathrm{Cov}[X_i, X_j]
$$

つまり:

$$
\Sigma = \begin{pmatrix}
\mathrm{Var}[X_1] & \mathrm{Cov}[X_1, X_2] & \cdots & \mathrm{Cov}[X_1, X_n] \\
\mathrm{Cov}[X_2, X_1] & \mathrm{Var}[X_2] & \cdots & \mathrm{Cov}[X_2, X_n] \\
\vdots & \vdots & \ddots & \vdots \\
\mathrm{Cov}[X_n, X_1] & \mathrm{Cov}[X_n, X_2] & \cdots & \mathrm{Var}[X_n]
\end{pmatrix}
$$

### 性質

- **対称** ($\Sigma_{ij} = \Sigma_{ji}$)
- **半正定値** (固有値はすべて非負)
- 対角は各変数の分散

機械学習では **PCA (主成分分析)** で共分散行列を固有値分解し、データの本質的な軸を見つけます (→ [`01_linear_algebra/03_eigenvalues.md`](../01_linear_algebra/03_eigenvalues.md))。

---

## 5. 標準化 (Standardization)

データを **平均 $0$、標準偏差 $1$** に変換する操作:

$$
Z = \frac{X - \mu}{\sigma}
$$

- ML の前処理で頻出
- 異なるスケールの特徴量を比較可能にする
- 多くの学習アルゴリズムが**標準化されたデータで性能が出る**

```python
import numpy as np

data = np.array([10, 20, 30, 40, 50])

# 標準化
mu = data.mean()
sigma = data.std()
z = (data - mu) / sigma

print(z)
print(f'標準化後の平均: {z.mean():.4f}')   # ≈ 0
print(f'標準化後の標準偏差: {z.std():.4f}')  # ≈ 1
```

scikit-learn なら `StandardScaler` で一発。

---

## 6. ML / AI への接続

### 損失関数の中身

平均二乗誤差 (MSE):

$$
\mathrm{MSE} = \mathbb{E}\bigl[(Y - \hat{Y})^2\bigr]
$$

これは「**予測誤差の分散** + **バイアスの 2 乗**」に分解できます (バイアス・分散分解):

$$
\mathrm{MSE}(\hat{f}) = \mathrm{Var}[\hat{f}] + \mathrm{Bias}^2[\hat{f}] + \sigma^2
$$

ML モデル選びは「**バイアスと分散のトレードオフ**」を意識する。

### 重みの初期化

ニューラルネットの重み $W$ を**平均 $0$、特定の分散** で初期化することで、勾配消失/爆発を防ぐ:

- **Xavier 初期化**: $\sigma = \sqrt{\frac{1}{n_{\text{in}}}}$
- **He 初期化** (ReLU 用): $\sigma = \sqrt{\frac{2}{n_{\text{in}}}}$

### 正規化 (Normalization)

**バッチ正規化 (BatchNorm)** や **層正規化 (LayerNorm)** は、各層の出力を **平均 $0$、分散 $1$** に標準化する操作。
深いネットの訓練を安定させる必須技術。

---

## 7. ハマりポイント

- **分散と標準偏差を混同**: 単位が違う (前者は 2 乗単位)
- **相関 ≠ 因果**: 見落とすと統計の解釈を間違える
- **不偏分散 vs 母分散**: `numpy.var` のデフォルト `ddof=0` (母分散)、サンプルからの推定は `ddof=1` (不偏)
- **共分散行列は半正定値**: 数値誤差で固有値が微小な負になることがある (`np.linalg.eigh` を使い、負を 0 にクリップ)

---

## まとめ

| 概念 | 数式 | NumPy |
|---|---|---|
| 期待値 | $\mathbb{E}[X] = \sum x_i P(x_i)$ または $\int x \, p(x)\,dx$ | `np.mean(x)` |
| 分散 | $\mathrm{Var}[X] = \mathbb{E}[(X-\mu)^2]$ | `np.var(x)` |
| 標準偏差 | $\sigma = \sqrt{\mathrm{Var}[X]}$ | `np.std(x)` |
| 共分散 | $\mathrm{Cov}[X, Y] = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)]$ | `np.cov(x, y)` |
| 相関係数 | $\rho = \dfrac{\mathrm{Cov}}{\sigma_X \sigma_Y}$ | `np.corrcoef(x, y)` |
| 標準化 | $Z = \dfrac{X - \mu}{\sigma}$ | `(x - x.mean()) / x.std()` |

**この章のキー**: 期待値は重心、分散は広がり、共分散は共変動。ML の損失・前処理・初期化、すべてここから。

---

## 次へ

→ [`04_bayes.md`](04_bayes.md) — ベイズの定理: 条件付き確率の応用、ML の根幹

## 関連
- [`01_linear_algebra/03_eigenvalues.md`](../01_linear_algebra/03_eigenvalues.md) — 共分散行列の固有値分解 = PCA

---

## 🔍 ググってみよう

- **バイアス-分散分解** — モデルの誤差を理解する根本原理
- **不偏推定量** — 標本平均が母平均の不偏推定量である理由
- **Cauchy-Schwarz 不等式** — 相関係数が $|ρ| \leq 1$ の証明
- **共分散行列のスペクトル分解** — PCA の数学的基礎
- **マハラノビス距離** — 共分散行列で重み付けした距離
- **モーメント (moment)** — 1次=平均、2次=分散、3次=歪度、4次=尖度
- **チェビシェフの不等式** — 「平均から離れる確率」の上界

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`02_distributions.md`](02_distributions.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`04_bayes.md`](04_bayes.md) |
