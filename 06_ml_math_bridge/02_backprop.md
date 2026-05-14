# 06-2. 誤差逆伝播法 (Backpropagation) — ニューラルネットの心臓部

**このページのゴール**: 誤差逆伝播法 = 連鎖律の繰り返し適用 = ニューラルネットの勾配計算アルゴリズムを理解し、JAX による自動化を腹落ちさせる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`06_ml_math_bridge/notebooks/02_backprop.ipynb`](notebooks/02_backprop.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_calculus/02_derivatives.md`](../02_calculus/02_derivatives.md) — 連鎖律
> - [`01_loss_functions.md`](01_loss_functions.md) — 損失関数
> - [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX 自動微分

---

## 1. ひと言で

> **誤差逆伝播法** = 「**損失から各層のパラメータまで連鎖律で勾配を遡る**」アルゴリズム

ニューラルネットは入力 → 層1 → 層2 → 層3 → 損失 という流れ。
学習には **「各層のパラメータを動かしたら損失がどう変わるか」** = 勾配が必要。

連鎖律で**逆向きに**計算する → これが backpropagation (バックプロパゲーション、略して "backprop")。

---

## 2. 基本: 1 層のネットワーク

### モデル

入力 $\mathbf{x}$、重み $W$、バイアス $\mathbf{b}$、活性化関数 $\sigma$:

$$
\mathbf{z} = W \mathbf{x} + \mathbf{b}, \quad \hat{\mathbf{y}} = \sigma(\mathbf{z})
$$

損失 $L = L(\hat{\mathbf{y}}, \mathbf{y})$ について、パラメータの勾配を求めたい:

$$
\frac{\partial L}{\partial W}, \quad \frac{\partial L}{\partial \mathbf{b}}
$$

### 連鎖律で勾配を逆伝播

$L \to \hat{\mathbf{y}} \to \mathbf{z} \to W$ の流れを**逆順に辿る**:

$$
\frac{\partial L}{\partial W} = \frac{\partial L}{\partial \hat{\mathbf{y}}} \cdot \frac{\partial \hat{\mathbf{y}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial W}
$$

各項:
- $\frac{\partial L}{\partial \hat{\mathbf{y}}}$: 損失の勾配 (損失関数による)
- $\frac{\partial \hat{\mathbf{y}}}{\partial \mathbf{z}} = \sigma'(\mathbf{z})$: 活性化関数の微分
- $\frac{\partial \mathbf{z}}{\partial W} = \mathbf{x}^\top$: 線形変換の微分

---

## 3. 多層の場合

### モデル (3 層 NN の例)

$$
\mathbf{h}_1 = \sigma(W_1 \mathbf{x} + \mathbf{b}_1)
$$

$$
\mathbf{h}_2 = \sigma(W_2 \mathbf{h}_1 + \mathbf{b}_2)
$$

$$
\hat{\mathbf{y}} = W_3 \mathbf{h}_2 + \mathbf{b}_3
$$

$$
L = \text{loss}(\hat{\mathbf{y}}, \mathbf{y})
$$

### 順伝播 (Forward) と 逆伝播 (Backward)

**順伝播**: 入力 → 出力 → 損失 を計算

**逆伝播**: 損失 → 入力 へ、勾配を逆向きに計算

$$
\frac{\partial L}{\partial W_1} = \frac{\partial L}{\partial \hat{\mathbf{y}}} \cdot \frac{\partial \hat{\mathbf{y}}}{\partial \mathbf{h}_2} \cdot \frac{\partial \mathbf{h}_2}{\partial \mathbf{h}_1} \cdot \frac{\partial \mathbf{h}_1}{\partial W_1}
$$

「**右から左へ**」 ヤコビアンを掛けていく。

---

## 4. 「逆向き」が効率的な理由

### 単純計算なら $O(n^2)$ なのに

100 層ネットで 100 個のパラメータの勾配を直接計算 → ヤコビアンを 100 個全部作る = メモリ爆発。

### 逆伝播なら $O(n)$

「**勾配ベクトル**」を 1 本だけ伝播させる → メモリ効率が良い。
これが **VJP (Vector-Jacobian Product)** の使い方。

→ 詳しくは [`02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md)

---

## 5. NumPy で手書き backprop (簡単な MLP)

### モデル

入力 $\mathbf{x} \in \mathbb{R}^{d_0}$ → 隠れ層 ($d_1$ ニューロン、ReLU) → 出力 ($d_2$ ニューロン)

$$
\mathbf{z}_1 = W_1 \mathbf{x} + \mathbf{b}_1, \quad \mathbf{h}_1 = \text{ReLU}(\mathbf{z}_1)
$$

$$
\hat{\mathbf{y}} = W_2 \mathbf{h}_1 + \mathbf{b}_2
$$

損失 $L = \frac{1}{2} \|\hat{\mathbf{y}} - \mathbf{y}\|^2$

### 手書き勾配

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

def relu_grad(z):
    return (z > 0).astype(float)

def forward(x, W1, b1, W2, b2):
    z1 = W1 @ x + b1
    h1 = relu(z1)
    y_hat = W2 @ h1 + b2
    return z1, h1, y_hat

def backward(x, y, z1, h1, y_hat, W1, W2):
    """損失 L = 1/2 ||y_hat - y||² の勾配を逆伝播."""
    # 損失から出力への勾配
    dL_dy_hat = y_hat - y                          # (d2,)
    
    # 出力層のパラメータ勾配
    dL_dW2 = np.outer(dL_dy_hat, h1)               # (d2, d1)
    dL_db2 = dL_dy_hat                              # (d2,)
    
    # 隠れ層への勾配
    dL_dh1 = W2.T @ dL_dy_hat                      # (d1,)
    dL_dz1 = dL_dh1 * relu_grad(z1)                # (d1,)
    
    # 入力層のパラメータ勾配
    dL_dW1 = np.outer(dL_dz1, x)                   # (d1, d0)
    dL_db1 = dL_dz1                                 # (d1,)
    
    return dL_dW1, dL_db1, dL_dW2, dL_db2
```

これが **NN の手書き backprop**。これを毎層書くのは大変…。

---

## 6. JAX で自動微分 — backprop が消える

JAX (PyTorch も同様) なら、**手書き backprop が不要**:

```python
import jax
import jax.numpy as jnp

def model(params, x):
    W1, b1, W2, b2 = params
    h1 = jnp.maximum(0, W1 @ x + b1)   # ReLU
    return W2 @ h1 + b2

def loss(params, x, y):
    y_hat = model(params, x)
    return 0.5 * jnp.sum((y_hat - y)**2)

# これだけ!
grad_loss = jax.grad(loss)

# 訓練ループ
params = init_params()
for x_batch, y_batch in dataloader:
    grads = grad_loss(params, x_batch, y_batch)
    params = jax.tree.map(lambda p, g: p - lr * g, params, grads)
```

`jax.grad(loss)` が**内部で勾配を逆伝播**してくれる。
人間は「**損失関数の式を書くだけ**」で、勾配導出は完全自動。

---

## 7. 計算グラフ — backprop の理論的基礎

### 計算グラフとは

すべての計算を**ノード (演算) と エッジ (データ流れ)** で表したグラフ。

例: $L = (a + b) \cdot c$

```
a ─┐
   ├─[+]──┐
b ─┘      ├─[×]── L
       c ─┘
```

各ノードが「**自分のローカルな勾配**」を覚えていれば、連鎖律で全体の勾配が計算できる。

### Reverse-mode 自動微分 = backprop

JAX や PyTorch の自動微分は、内部で:
1. **順伝播**: グラフを左→右にたどり、中間値を保存
2. **逆伝播**: グラフを右→左にたどり、勾配を伝播

完全に自動化されたバージョンが **`jax.grad`**。

---

## 8. 数式で完全に追う: 1 層 + MSE

線形回帰 $\hat{y} = w x + b$, 損失 $L = (y - \hat{y})^2$

連鎖律で:

$$
\frac{\partial L}{\partial \hat{y}} = -2(y - \hat{y})
$$

$$
\frac{\partial \hat{y}}{\partial w} = x, \quad \frac{\partial \hat{y}}{\partial b} = 1
$$

合成:

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w} = -2x(y - \hat{y})
$$

$$
\frac{\partial L}{\partial b} = -2(y - \hat{y})
$$

これを SymPy で確認:

```python
import sympy as sp

w, b, x, y = sp.symbols('w b x y')
y_hat = w * x + b
L = (y - y_hat)**2

print(sp.simplify(sp.diff(L, w)))  # -2*x*(y - w*x - b)
print(sp.simplify(sp.diff(L, b)))  # -2*(y - w*x - b)
```

---

## 9. ML / AI への接続

### 現代の NN の訓練

```python
import jax
import jax.numpy as jnp
import optax

def model(params, x):
    """3 層 MLP."""
    W1, b1, W2, b2, W3, b3 = params
    h1 = jax.nn.relu(W1 @ x + b1)
    h2 = jax.nn.relu(W2 @ h1 + b2)
    return W3 @ h2 + b3

def loss(params, x, y):
    y_hat = model(params, x)
    return jnp.mean((y_hat - y)**2)

# Adam optimizer + JAX 自動微分
optimizer = optax.adam(1e-3)
opt_state = optimizer.init(params)

@jax.jit
def step(params, opt_state, x, y):
    grads = jax.grad(loss)(params, x, y)        # ← backprop が自動
    updates, opt_state = optimizer.update(grads, opt_state)
    params = optax.apply_updates(params, updates)
    return params, opt_state
```

これが**現代 ML 訓練の最小コード**。
ChatGPT も Claude も Gemini も、内部で同じ仕組みが動いています (規模が違うだけ)。

---

## 10. ハマりポイント

- **勾配消失**: ReLU 以前のシグモイド/tanh で起きやすい → ReLU 系を使う
- **勾配爆発**: RNN/Transformer で起きやすい → クリッピング、残差接続
- **ストップ勾配**: 一部のパラメータを更新しない場合 `jax.lax.stop_gradient` を使う
- **勾配チェック**: 自分で書いた勾配は `jax.grad` の値と比較して検証 (差分が 1e-5 以内ならOK)

---

## まとめ

| 概念 | 数式 | Python |
|---|---|---|
| 順伝播 | $\mathbf{x} \to \mathbf{h}_1 \to \dots \to \hat{\mathbf{y}} \to L$ | `model(params, x)` |
| 逆伝播 (連鎖律) | $\frac{\partial L}{\partial W_k} = \prod_j \frac{\partial \mathbf{h}_{j+1}}{\partial \mathbf{h}_j} \cdot \frac{\partial \mathbf{h}_k}{\partial W_k}$ | `jax.grad(loss)(params, x, y)` |
| パラメータ更新 | $\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} - \eta \nabla L$ | `optax.apply_updates` |

**この章のキー**: 誤差逆伝播 = 連鎖律の繰り返し適用。手で書くと長いが、`jax.grad` で完全自動。これが ML 訓練の心臓。

## 次へ

ML 橋渡し章 完了 🎉

これまでで:
- 線形代数 (01) → 行列演算
- 微積分 (02) → 勾配・連鎖律
- 確率・統計 (03) → 損失関数の確率的解釈
- 最適化 (05) → 勾配降下法
- ML 橋渡し (06) → 損失関数 + 誤差逆伝播 ← **すべての統合**

→ 次の章 (実装の最先端へ): [`../07_jax/README.md`](../07_jax/README.md)

## 関連
- [`02_calculus/02_derivatives.md`](../02_calculus/02_derivatives.md) — 連鎖律の基礎
- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — `jax.grad` の詳細
- [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 勾配を使った最適化

---

## 🔍 ググってみよう

- **Backpropagation** (Rumelhart, Hinton, Williams, 1986) — 古典的論文
- **Computational graph** — 自動微分の基礎概念
- **Forward-mode vs Reverse-mode** — どちらを使うかの判断基準
- **Vanishing/Exploding gradient** — 深い NN の歴史的問題
- **Residual connection (ResNet)** — 勾配消失の解決策、2015年
- **Layer Normalization, Batch Normalization** — 訓練を安定化する技術
- **Stop gradient** — 部分的に勾配を止める技 (GAN、自己教師ありで多用)
- **Gradient checkpointing** — メモリ節約のテクニック
- **Higher-order autodiff** — 2階微分を効率的に取る技

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`01_loss_functions.md`](01_loss_functions.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`../07_jax/README.md`](../07_jax/README.md) |
