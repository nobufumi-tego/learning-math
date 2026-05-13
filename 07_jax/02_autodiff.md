# 02. 自動微分 — `jax.grad` の威力

JAX の最大の価値は**自動微分** (automatic differentiation, autodiff)。
微分を手で導出せず、**関数を渡すだけで勾配関数が手に入る**。

## なぜ重要か

機械学習の訓練は **勾配降下法** = 損失関数の勾配を求めて更新を繰り返す。
損失関数が複雑になると、手で勾配を計算するのは現実的でない。
JAX（や PyTorch）はこれを完全自動化する。

## 基本

```python
import jax
import jax.numpy as jnp

# f(x) = x²
def f(x):
    return x ** 2

# df/dx を返す関数
df_dx = jax.grad(f)

print(df_dx(3.0))   # 6.0  ← 解析解 2x | x=3
```

これだけ。関数 `f` を渡すと、その勾配を計算する**関数**が返ってくる。

## 多変数関数

`jax.grad` はデフォルトで**第1引数についての勾配**を返す。
ベクトル入力 → ベクトル勾配。

```python
def g(x):
    """g: ℝ² → ℝ, g(x) = x[0]² + x[0]*x[1] + x[1]²."""
    return x[0]**2 + x[0] * x[1] + x[1]**2

grad_g = jax.grad(g)

x = jnp.array([1.0, 2.0])
print(grad_g(x))    # [4., 5.]  ← (∂g/∂x₀, ∂g/∂x₁) = (2x₀+x₁, x₀+2x₁)
```

## 値と勾配を同時に: `value_and_grad`

学習ループでは「損失の値も知りたい、勾配も知りたい」が普通。

```python
val_and_grad = jax.value_and_grad(g)
value, grad = val_and_grad(x)
print(value)   # 7.0
print(grad)    # [4., 5.]
```

`f(x)` を 2 回呼ぶ必要がなく効率的。

## 別の引数で微分する: `argnums`

```python
def h(x, y):
    return x**2 + y**3

# x で微分
dh_dx = jax.grad(h, argnums=0)
print(dh_dx(2.0, 3.0))  # 4.0   (2x)

# y で微分
dh_dy = jax.grad(h, argnums=1)
print(dh_dy(2.0, 3.0))  # 27.0  (3y²)

# 両方で微分
dh_both = jax.grad(h, argnums=(0, 1))
print(dh_both(2.0, 3.0))  # (4.0, 27.0)
```

## 高階微分

`jax.grad` を**重ねがけ**できる。

```python
def f(x):
    return x ** 3       # f(x) = x³

df = jax.grad(f)        # f'(x) = 3x²
d2f = jax.grad(df)      # f''(x) = 6x
d3f = jax.grad(d2f)     # f'''(x) = 6

print(df(2.0))   # 12.0
print(d2f(2.0))  # 12.0
print(d3f(2.0))  # 6.0
```

## ヤコビアン・ヘッシアン

ベクトル → ベクトルの関数のヤコビアン（一階偏微分の行列）:

```python
def vector_f(x):
    """f: ℝ² → ℝ³."""
    return jnp.array([
        x[0] + x[1],
        x[0] * x[1],
        x[0] ** 2,
    ])

jacobian = jax.jacfwd(vector_f)         # forward-mode
# または jax.jacrev(vector_f)            # reverse-mode

x = jnp.array([1.0, 2.0])
print(jacobian(x))
# [[1.  1. ]    ← ∂f₀/∂x₀, ∂f₀/∂x₁
#  [2.  1. ]    ← ∂f₁/∂x₀, ∂f₁/∂x₁
#  [2.  0. ]]   ← ∂f₂/∂x₀, ∂f₂/∂x₁
```

ヘッシアン（二階偏微分の行列）:

```python
def g(x):
    return jnp.sum(x ** 3)

hessian = jax.hessian(g)
print(hessian(jnp.array([1.0, 2.0, 3.0])))
# [[ 6.  0.  0.]
#  [ 0. 12.  0.]
#  [ 0.  0. 18.]]   ← ∂²g/∂xᵢ∂xⱼ = 6xᵢ if i==j else 0
```

## 数学との対応

| 数学 | JAX |
|---|---|
| `df/dx` | `jax.grad(f)` |
| `∂f/∂x` (多変数) | `jax.grad(f)` (xに関して) |
| `∇f` (勾配) | `jax.grad(f)` |
| `Jf` (ヤコビアン) | `jax.jacfwd(f)` |
| `Hf` (ヘッシアン) | `jax.hessian(f)` |
| `f^(n)` (n階微分) | `jax.grad` を n 回ネスト |

## ハマりポイント

- 微分対象の関数は**スカラーを返す**必要がある（`jax.grad` の場合）
  - ベクトル出力なら `jacfwd` か `jacrev`
- 整数で微分しようとするとエラー: `jax.grad(f)(3)` → `jax.grad(f)(3.0)`
- 「`x[0]` での微分」ではなく**「`x`（ベクトル）での微分」が `[∂f/∂x[0], ∂f/∂x[1]]`** を返す
- 計算グラフを保持するため、極めて深いネストはメモリ食う

## ML での代表的使い方

```python
# 訓練ループの中核（疑似コード）
loss_fn = lambda params, x, y: ...   # 損失関数

# 値と勾配を同時に
loss_val, grads = jax.value_and_grad(loss_fn)(params, x, y)

# パラメータ更新
params = jax.tree.map(lambda p, g: p - lr * g, params, grads)
```

これがニューラルネット訓練の本体。**勾配導出を一切書かない**で済む。

---

## 📍 ナビゲーション

| ← 前 | 🏠 目次 | 次 → |
|---|---|---|
| [`01_basics.md`](01_basics.md) | [章 TOP](README.md) | [`03_jit_vmap.md`](03_jit_vmap.md) |
