# 05-2. 勾配降下法 — ML 学習の本体

**このページのゴール**: 勾配降下法 (Gradient Descent) のすべてのバリエーション (GD/SGD/Mini-batch/Momentum/Adam) を理解し、JAX で実装できるようになる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`05_optimization/notebooks/02_gradient_descent.ipynb`](notebooks/02_gradient_descent.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`01_basic_concepts.md`](01_basic_concepts.md) — 最適化問題の枠組み
> - [`02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md) — 勾配
> - [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX の自動微分

---

## 1. 勾配降下法 — 「一番急に降りる方向」に進む

### 直感

霧の山中で、家までの**最短ルート**を探したい。

→ 「**今いる場所で、最も急に下る方向**」 に少しずつ進む。
これを繰り返せば、谷底 (= 最小点) に着く。

### 数式 — 更新式

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \nabla L(\boldsymbol{\theta}_t)
$$

| 記号 | 意味 |
|---|---|
| $\boldsymbol{\theta}_t$ | $t$ 反復目のパラメータ |
| $\nabla L(\boldsymbol{\theta}_t)$ | 損失関数の勾配 (= 上り方向) |
| $-\nabla L$ | **下り方向** (符号反転) |
| $\eta$ | **学習率** (step size) |

「**現在の位置から、最も急に降りる方向に $\eta$ だけ進む**」 = 1 ステップ。
これを収束するまで繰り返す。

---

## 2. Python で実装

### 標準形式 (NumPy)

```python
import numpy as np

def gradient_descent(grad_f, x0, lr=0.1, n_iter=100):
    """勾配降下法の基本形.

    Args:
        grad_f: 勾配関数 (np.ndarray → np.ndarray)
        x0: 初期値
        lr: 学習率 η
        n_iter: 反復回数

    Returns:
        最終 x と軌跡のリスト
    """
    x = x0.copy()
    trajectory = [x.copy()]
    for _ in range(n_iter):
        x = x - lr * grad_f(x)
        trajectory.append(x.copy())
    return x, trajectory


# f(x, y) = (x-1)² + (y-2)² の最小化
def grad(p):
    return np.array([2*(p[0] - 1), 2*(p[1] - 2)])

x_final, traj = gradient_descent(grad, np.array([0.0, 0.0]), lr=0.1, n_iter=50)
print(f'最終: {x_final}')   # ≈ [1, 2]
```

### JAX 形式 (本命)

JAX なら**勾配を手で書かない**:

```python
import jax
import jax.numpy as jnp

def f(p):
    return (p[0] - 1)**2 + (p[1] - 2)**2

# JAX に勾配を任せる
grad_f = jax.grad(f)

# 訓練ループ
x = jnp.array([0.0, 0.0])
lr = 0.1
for _ in range(50):
    x = x - lr * grad_f(x)

print(f'最終: {x}')   # ≈ [1.0, 2.0]
```

これが **ML の訓練ループの最小形**。

---

## 3. 学習率 (Learning Rate) の選び方

### 学習率が結果を決める

| $\eta$ | 結果 |
|---|---|
| 大きすぎ ($\eta = 1.5$) | **発散** (ピンポン現象) |
| 適切 ($\eta = 0.1$) | **収束** ✅ |
| 小さすぎ ($\eta = 0.001$) | 収束はするが**遅すぎ** |

### 適応的学習率

「最初は大胆に、終盤は慎重に」が定石:

#### Step decay (階段減衰)
$$
\eta_t = \eta_0 \cdot \gamma^{\lfloor t/T \rfloor}
$$
($T$ ステップごとに $\gamma$ 倍)

#### Cosine annealing (コサイン減衰)
$$
\eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max} - \eta_{\min})(1 + \cos(\pi t / T))
$$

最近の LLM 訓練ではコサイン減衰が定番。

#### Warmup (ウォームアップ)
最初は$\eta$ を 0 から徐々に上げる → 安定して大きい$\eta$ に到達できる。

---

## 4. 確率的勾配降下法 (SGD) — データ全体じゃなく一部だけ

### 問題: 通常の勾配降下は「全データ」が必要

$$
\nabla L(\boldsymbol{\theta}) = \frac{1}{N} \sum_{i=1}^N \nabla \ell(f(x_i; \boldsymbol{\theta}), y_i)
$$

データが $N = 10^7$ あると、1 ステップ毎に**1000万件**の損失と勾配を計算 → 重い。

### 解決: 確率的勾配降下法 (SGD)

毎ステップ、**ランダムに 1 件**だけ選んで勾配計算:

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \nabla \ell(f(x_{i_t}; \boldsymbol{\theta}_t), y_{i_t})
$$

ノイズが入るが**1ステップが軽い**ので、大量データに有効。

### 中間: ミニバッチ勾配降下法

実用的にはこれが定番:

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \cdot \frac{1}{|B|} \sum_{i \in B} \nabla \ell(\dots)
$$

毎ステップ、ランダムに $|B|$ 個 (例: 32, 64, 128 個) のバッチで勾配計算。
**GPU 並列を活かしつつ、ノイズで局所最適を脱出**。

| 方式 | 1ステップ計算量 | ノイズ | GPU効率 |
|---|---|---|---|
| GD (バッチ) | $O(N)$ | 0 | 良い |
| SGD (1 件) | $O(1)$ | 大 | 悪い |
| **Mini-batch** | $O(\|B\|)$ | 中 | **良い** ← 定番 |

---

## 5. モメンタム (Momentum) — 「慣性」を加える

### 直感

谷をボールが転がる比喩:
- 普通の SGD: 摩擦が大きい → 細かい谷で止まる
- モメンタム: **慣性で勢いが残る** → 細かい谷を突き抜けて深い谷へ

### 数式

$$
\mathbf{v}_{t+1} = \beta \mathbf{v}_t + \nabla L(\boldsymbol{\theta}_t)
$$

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \mathbf{v}_{t+1}
$$

$\mathbf{v}$ が「速度ベクトル」、$\beta \in [0, 1)$ が**慣性パラメータ** (普通 0.9)。

過去の勾配の**指数移動平均**を使うため、**振動を抑制**しながら**前進力**が出る。

### Python

```python
import jax
import jax.numpy as jnp

def momentum_step(params, v, grad_fn, lr=0.01, beta=0.9):
    """モメンタム付き勾配降下の 1 ステップ."""
    g = grad_fn(params)
    v_new = beta * v + g
    params_new = params - lr * v_new
    return params_new, v_new
```

---

## 6. Adam — モダン ML の標準オプティマイザ

### 何が偉大か

**勾配の方向と大きさを、過去履歴から自動調整**:
- モメンタム的な慣性
- パラメータごとに学習率を適応化 (RMSProp の機能)

### 数式

$$
\mathbf{m}_t = \beta_1 \mathbf{m}_{t-1} + (1 - \beta_1) \nabla L(\boldsymbol{\theta}_t)
$$

$$
\mathbf{v}_t = \beta_2 \mathbf{v}_{t-1} + (1 - \beta_2) (\nabla L(\boldsymbol{\theta}_t))^2
$$

バイアス補正:

$$
\hat{\mathbf{m}}_t = \frac{\mathbf{m}_t}{1 - \beta_1^t}, \quad \hat{\mathbf{v}}_t = \frac{\mathbf{v}_t}{1 - \beta_2^t}
$$

更新:

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \cdot \frac{\hat{\mathbf{m}}_t}{\sqrt{\hat{\mathbf{v}}_t} + \epsilon}
$$

| ハイパー | デフォルト |
|---|---|
| $\beta_1$ | 0.9 |
| $\beta_2$ | 0.999 |
| $\epsilon$ | $10^{-8}$ |
| $\eta$ | $10^{-3}$ |

### Python (JAX + Optax)

実用では **Optax** ライブラリを使う:

```python
import jax
import optax

# 定義
optimizer = optax.adam(learning_rate=1e-3)

# 初期化
params = init_params()
opt_state = optimizer.init(params)

# 訓練ループ
for batch in data_loader:
    grads = jax.grad(loss_fn)(params, batch)
    updates, opt_state = optimizer.update(grads, opt_state)
    params = optax.apply_updates(params, updates)
```

> 💡 **Adam は ML の "デフォルト"**。「とりあえず Adam」 で 90% は OK。
> ただし大規模訓練では**SGD + Momentum** の方が**汎化性能が良い**ことも (理由は研究中)。

---

## 7. 主要オプティマイザ比較

| 名前 | 特徴 | 使い所 |
|---|---|---|
| **SGD** | 純粋な確率的勾配降下 | 単純、強い汎化 |
| **SGD + Momentum** | 慣性追加 | 大規模学習の定番 |
| **AdaGrad** | パラメータ毎の適応学習率 | スパース勾配 |
| **RMSProp** | AdaGrad の改良 (移動平均) | RNN 訓練 |
| **Adam** | RMSProp + Momentum | **デフォルト** |
| **AdamW** | Adam + 重み減衰の修正 | Transformer 訓練の定番 |
| **Lion** | 2023 年 Google 発、Adam より省メモリ | 最新研究 |

ChatGPT/Claude の訓練は **AdamW** が中心。

---

## 8. 学習が失敗するパターン

### (1) 勾配消失 (Vanishing Gradient)

深い NN で、層を逆伝播するうちに勾配が**指数的に小さくなる**現象。
→ ReLU 活性化、Batch Normalization、Residual Connection で対処。

### (2) 勾配爆発 (Exploding Gradient)

逆に勾配が**指数的に大きくなる**現象。
→ **勾配クリッピング** (`jax.tree.map(lambda g: jnp.clip(g, -c, c), grads)`)

### (3) 学習率が悪い

- 大きすぎ → 発散
- 小さすぎ → 収束遅い
- → 学習率スケジュール (warmup + cosine) で対処

### (4) 鞍点に捕まる

高次元では局所最適より**鞍点 (saddle point)** が問題。
→ Adam の慣性、SGD のノイズで脱出。

### (5) 過学習 (Overfitting)

訓練データに過剰適合 → テスト性能ダウン。
→ **正則化** (L1/L2)、Dropout、Early Stopping、データ拡張で対処。

---

## 9. ML / AI への接続

### 実際の訓練コード (JAX + Optax)

```python
import jax
import jax.numpy as jnp
import optax

# 損失関数
def loss(params, x, y):
    pred = model(params, x)
    return jnp.mean((pred - y)**2)

# Adam optimizer
optimizer = optax.adam(learning_rate=1e-3)
opt_state = optimizer.init(params)

# 訓練 1 ステップ
@jax.jit
def train_step(params, opt_state, x, y):
    loss_val, grads = jax.value_and_grad(loss)(params, x, y)
    updates, opt_state = optimizer.update(grads, opt_state)
    params = optax.apply_updates(params, updates)
    return params, opt_state, loss_val

# エポックループ
for epoch in range(n_epochs):
    for batch in data_loader:
        params, opt_state, loss_val = train_step(params, opt_state, *batch)
```

これが**現代の ML 訓練コードの典型形**。
すべての概念 (勾配・最適化・JAX) が結集している。

---

## 10. ハマりポイント

- **学習率は試行錯誤**: 1e-3, 1e-4 から始める。LR finder ツールも便利
- **ミニバッチサイズ**: 32, 64, 128 が定番。大きいほど安定するがメモリ食う
- **勾配確認**: `jnp.isnan(grad).any()` で NaN チェック必須
- **オプティマイザの状態**: Adam の $\mathbf{m}, \mathbf{v}$ も保存・復元する必要

---

## まとめ

| 手法 | 更新式 | ハイパーパラメータ |
|---|---|---|
| GD | $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \eta \nabla L$ | $\eta$ |
| SGD | 1サンプルで近似 | $\eta$ |
| Mini-batch | バッチで近似 | $\eta$, $|B|$ |
| Momentum | $\mathbf{v} \leftarrow \beta \mathbf{v} + \nabla L$ | $\eta$, $\beta$ |
| Adam | 適応的 + 慣性 | $\eta$, $\beta_1$, $\beta_2$, $\epsilon$ |

**この章のキー**: 勾配降下 = 「下り方向に進む」反復法。Adam は ML のデフォルト。学習率がすべてを決める。

## 次へ

最適化章 完了 🎉

→ 次の章: [`../06_ml_math_bridge/README.md`](../06_ml_math_bridge/README.md) — ここまで学んだすべてを ML に統合

## 関連
- [`02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md) — 勾配の理論
- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX の自動微分
- [`06_ml_math_bridge/02_backprop.md`](../06_ml_math_bridge/02_backprop.md) — 誤差逆伝播

---

## 🔍 ググってみよう

- **Optax** — JAX 用のオプティマイザライブラリ (PyTorch の torch.optim 相当)
- **Adam: A Method for Stochastic Optimization** (Kingma & Ba, 2014) — Adam の原論文
- **Newton's method** — 2次情報を使う最適化、収束は速いが計算重い
- **L-BFGS** — 擬似ヘッシアンを使う実用的手法
- **学習率スケジューラ** — warmup, cosine annealing, step decay
- **勾配クリッピング (gradient clipping)** — 勾配爆発の対策
- **Lion オプティマイザ** — 2023 年に Google が発表
- **Lookahead, RAdam** — Adam の改良版
- **シャープな最小値 vs フラットな最小値** — 汎化性能の研究

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`01_basic_concepts.md`](01_basic_concepts.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`../06_ml_math_bridge/README.md`](../06_ml_math_bridge/README.md) |
