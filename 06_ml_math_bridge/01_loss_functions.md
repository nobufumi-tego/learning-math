# 06-1. 損失関数 — MSE と クロスエントロピー

**このページのゴール**: 機械学習で頻出する 2 大損失関数 (MSE と クロスエントロピー) を、数式・確率的な意味・Python の3面で理解する。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`06_ml_math_bridge/notebooks/01_loss_functions.ipynb`](notebooks/01_loss_functions.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_calculus/03_integrals.md`](../02_calculus/03_integrals.md) — 期待値の積分定義
> - [`03_probability_statistics/02_distributions.md`](../03_probability_statistics/02_distributions.md) — 正規分布、二項分布
> - [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 勾配降下法

---

## 1. 損失関数とは — 「予測の悪さ」を数値化

### 直感

予測 $\hat{y}$ と正解 $y$ がどれくらい離れているか:

| 観測 | 予測 | 損失 |
|---|---|---|
| 真値 5 | 予測 5 | $0$ (完璧!) |
| 真値 5 | 予測 4 | 小さい |
| 真値 5 | 予測 100 | 大きい |

この「**離れ度合い**」を **1 つのスカラー** で表すのが**損失関数**。
ML 訓練 = この損失関数を最小化する $\boldsymbol{\theta}$ を見つけること。

---

## 2. 平均二乗誤差 (Mean Squared Error, MSE)

### 数式

$$
\text{MSE}(\boldsymbol{\theta}) = \frac{1}{N} \sum_{i=1}^N \bigl(y_i - \hat{y}_i(\boldsymbol{\theta})\bigr)^2
$$

「**誤差を 2 乗して平均**」。

### 性質

- **連続値**を予測するタスク (回帰) で使う
- **凸関数** (線形モデルなら大域最適到達可)
- **大きな誤差を強く罰する** (2 乗するため)
- 外れ値に敏感

### 確率的な意味

「**正解 $y$ にガウスノイズが乗っている**」という仮定の下で、**最尤推定**が MSE 最小化と等価:

$$
y = f(x; \boldsymbol{\theta}) + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2)
$$

対数尤度を最大化 = **MSE 最小化**

### Python (NumPy + JAX)

```python
import numpy as np
import jax.numpy as jnp

def mse(y_true, y_pred):
    return jnp.mean((y_true - y_pred) ** 2)

# 例
y_true = jnp.array([1.0, 2.0, 3.0])
y_pred = jnp.array([1.1, 1.9, 3.2])
print(mse(y_true, y_pred))   # 0.02
```

### MSE の勾配

線形モデル $\hat{y} = w x + b$ なら:

$$
\frac{\partial L}{\partial w} = -\frac{2}{N} \sum_i x_i (y_i - w x_i - b)
$$

$$
\frac{\partial L}{\partial b} = -\frac{2}{N} \sum_i (y_i - w x_i - b)
$$

JAX なら手で微分する必要なし:

```python
import jax

def loss(params, x, y):
    w, b = params
    return jnp.mean((y - (w * x + b))**2)

grad_loss = jax.grad(loss)
```

---

## 3. クロスエントロピー (Cross-Entropy)

### 数式 (二値分類)

$y \in \{0, 1\}$, $\hat{y} = \sigma(z) \in (0, 1)$ (シグモイド出力):

$$
\text{BCE}(y, \hat{y}) = -\bigl[y \log \hat{y} + (1 - y) \log(1 - \hat{y})\bigr]
$$

### 数式 (多クラス分類)

$y$ がワンホット ($K$ クラス)、$\hat{y}$ がソフトマックス出力なら:

$$
\text{CE}(y, \hat{y}) = -\sum_{k=1}^K y_k \log \hat{y}_k
$$

正解クラスの予測確率の **負の対数**。

### 性質

- **離散カテゴリ**を予測するタスク (分類) で使う
- **凸関数** (ロジスティック回帰なら大域最適到達可)
- 「**自信を持って外したとき**」 に大きく罰する (対数のため)
- ML の分類問題のデフォルト損失

### 確率的な意味

「正解クラスを当てる確率を最大化」 = 対数尤度を最大化 = **クロスエントロピー最小化**

$$
\boldsymbol{\theta}^* = \arg\max_{\boldsymbol{\theta}} \prod_{i=1}^N P(y_i \mid x_i; \boldsymbol{\theta}) = \arg\min_{\boldsymbol{\theta}} -\sum_i \log P(y_i \mid x_i; \boldsymbol{\theta})
$$

### 「クロスエントロピー」の意味

情報理論で:
- **エントロピー** $H(p) = -\sum p \log p$: 分布の不確かさ
- **クロスエントロピー** $H(p, q) = -\sum p \log q$: 分布 $p$ を $q$ で表現する平均ビット数

$p$ = 真の分布、$q$ = モデル予測 → 一致するほど小さくなる。

### Python (NumPy + JAX)

```python
import jax.numpy as jnp

EPSILON = 1e-12   # log(0) を避けるため

def cross_entropy(y_true, y_pred):
    """y_true: ワンホット (N, K), y_pred: ソフトマックス出力 (N, K)."""
    return -jnp.mean(jnp.sum(y_true * jnp.log(y_pred + EPSILON), axis=1))

# 例: 3 クラス分類、2 サンプル
y_true = jnp.array([[1, 0, 0], [0, 1, 0]], dtype=jnp.float32)
y_pred = jnp.array([[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]])
print(cross_entropy(y_true, y_pred))   # 0.29...
```

### Softmax + Cross-Entropy の合体技

実装上は、**数値安定性**のため `softmax_cross_entropy_with_logits` を使う:

```python
import jax.nn as jnn
import jax.numpy as jnp

def loss(logits, labels):
    """logits: (N, K), labels: (N,) のクラスインデックス."""
    log_probs = jnn.log_softmax(logits)
    return -jnp.mean(log_probs[jnp.arange(len(labels)), labels])
```

これは PyTorch の `nn.CrossEntropyLoss` と同じ。

---

## 4. 主要な損失関数のまとめ

| 名前 | 数式 | タスク | 特徴 |
|---|---|---|---|
| **MSE** | $\frac{1}{N}\sum(y - \hat{y})^2$ | 回帰 | 凸、外れ値に敏感 |
| **MAE** | $\frac{1}{N}\sum |y - \hat{y}|$ | 回帰 | 外れ値に頑健、勾配が一様 |
| **Huber** | MSE と MAE の折衷 | 回帰 | バランス型 |
| **BCE** | 上の式 | 二値分類 | シグモイドと組合せ |
| **CE (Categorical)** | $-\sum y_k \log \hat{y}_k$ | 多クラス分類 | ソフトマックスと組合せ |
| **Focal Loss** | CE を難サンプル重視に修正 | 不均衡分類 | 物体検出で標準 |
| **Hinge Loss** | $\max(0, 1 - y \hat{y})$ | 二値分類 | SVM で使う |
| **KL ダイバージェンス** | $\sum p \log(p/q)$ | 分布のフィット | VAE, GAN で使う |

---

## 5. 損失関数選びの指針

```
タスクは何?
├─ 回帰 (連続値)
│   ├─ 標準: MSE
│   ├─ 外れ値が多い: MAE / Huber
│   └─ 量子値: Quantile Loss
└─ 分類 (カテゴリ)
    ├─ 二値: BCE
    ├─ 多クラス: Categorical Cross-Entropy
    └─ クラス不均衡: Focal Loss / 重み付き CE
```

---

## 6. 正則化項を加えた損失

実用では、**過学習防止のための正則化項**を損失に追加します:

$$
L_{\text{total}}(\boldsymbol{\theta}) = L_{\text{data}}(\boldsymbol{\theta}) + \lambda R(\boldsymbol{\theta})
$$

### よく使う正則化

| 名前 | $R(\boldsymbol{\theta})$ | 効果 |
|---|---|---|
| **L² (Ridge)** | $\sum_i \theta_i^2 = \|\boldsymbol{\theta}\|^2$ | 重みを小さく抑える |
| **L¹ (Lasso)** | $\sum_i |\theta_i| = \|\boldsymbol{\theta}\|_1$ | スパース化 (多くの $\theta_i = 0$) |
| **Elastic Net** | $\alpha \|\boldsymbol{\theta}\|_1 + (1-\alpha) \|\boldsymbol{\theta}\|^2$ | L¹ と L² の折衷 |

詳しくは → [`01_linear_algebra/01_vectors.md`](../01_linear_algebra/01_vectors.md) のノルム

---

## 7. ML / AI への接続 — 訓練ループ

```python
import jax
import jax.numpy as jnp
import optax

def model(params, x):
    W, b = params['W'], params['b']
    return W @ x + b

def loss_fn(params, x, y):
    pred = model(params, x)
    mse_loss = jnp.mean((pred - y)**2)
    l2_reg = 0.001 * (jnp.sum(params['W']**2) + jnp.sum(params['b']**2))
    return mse_loss + l2_reg

# 訓練
optimizer = optax.adam(1e-3)
opt_state = optimizer.init(params)

@jax.jit
def update(params, opt_state, x, y):
    grads = jax.grad(loss_fn)(params, x, y)
    updates, opt_state = optimizer.update(grads, opt_state)
    params = optax.apply_updates(params, updates)
    return params, opt_state
```

これが**現代の ML 訓練の最小コード**。

---

## 8. ハマりポイント

- **MSE で分類すると性能悪い**: 確率出力を 2 乗するのは**情報の使い方が悪い** → CE を使う
- **CE で `log(0)` エラー**: $\epsilon$ を足すか、`log_softmax` を使う
- **クラス不均衡**: 「99% は健康」のデータで普通の CE → 全部「健康」と予測する
- **数値安定性**: `softmax + log` を分けず `log_softmax` を使う

---

## まとめ

| 損失 | 数式 | 用途 | Python |
|---|---|---|---|
| MSE | $\frac{1}{N}\sum(y - \hat{y})^2$ | 回帰 | `jnp.mean((y - p)**2)` |
| BCE | $-[y\log p + (1-y)\log(1-p)]$ | 二値分類 | `optax.sigmoid_binary_cross_entropy` |
| CE | $-\sum_k y_k \log \hat{y}_k$ | 多クラス分類 | `optax.softmax_cross_entropy` |
| L2正則化 | $\lambda \|\boldsymbol{\theta}\|^2$ | 過学習防止 | `lambda_reg * jnp.sum(p**2)` |

**この章のキー**: 損失関数 = 「予測の悪さ」のスカラー化。回帰には MSE、分類にはクロスエントロピー。すべては最尤推定からの導出。

## 次へ

→ [`02_backprop.md`](02_backprop.md) — 誤差逆伝播法 (損失の勾配を効率的に計算する技)

## 関連
- [`02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md) — 勾配計算の理論
- [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 損失を最小化する手法
- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX で自動勾配

---

## 🔍 ググってみよう

- **Cross-Entropy Loss vs MSE for classification** — なぜ分類に MSE は不適切か
- **Focal Loss** (Lin et al., 2017) — 不均衡分類の必殺技
- **Label Smoothing** — 過信を防ぐテクニック
- **Contrastive Loss** — 自己教師あり学習で頻出
- **Triplet Loss** — 顔認識・類似度学習で頻出
- **KL ダイバージェンス** — 分布間の距離、VAE/GAN で必須
- **Wasserstein 距離** — 「最適輸送」由来の距離、WGAN
- **MAP 推定 vs 最尤推定** — 正則化を確率的に解釈

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [章 TOP](README.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`02_backprop.md`](02_backprop.md) |
