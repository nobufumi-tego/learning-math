# 02-4. 多変数関数と偏微分 — ML パラメータの世界

**このページのゴール**: 多変数関数の偏微分を理解し、Python で偏微分を計算できるようになる。
これが**ニューラルネットの何百万次元のパラメータ空間**を扱う基礎。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`02_calculus/notebooks/04_multivariable.ipynb`](notebooks/04_multivariable.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_derivatives.md`](02_derivatives.md) — 1変数の微分
> - [`01_linear_algebra/01_vectors.md`](../01_linear_algebra/01_vectors.md) — ベクトル

---

## 1. 多変数関数とは

入力が **2つ以上の数** を取る関数:

$$
\begin{aligned}
f(x, y) &= x^2 + y^2 & &\text{← 2変数}\\
f(x, y, z) &= x + 2y + 3z & &\text{← 3変数}\\
f(x_1, x_2, \dots, x_n) & & &\text{← } n \text{変数 (ML では } n = \text{数億)}
\end{aligned}
$$

機械学習では、入力データのベクトル $x \in \mathbb{R}^n$ や、モデルパラメータ $w \in \mathbb{R}^d$ を引数に取るので、**ほぼ全ての関数が多変数関数**。

---

## 2. 偏微分 (partial derivative) — 「1つの変数だけ動かす」微分

多変数関数で「**1つの変数だけ少し動かしたら、出力はどう変わる?**」を測るのが偏微分。

### 記号

$$
\frac{\partial f}{\partial x}
\qquad \text{← 「} f \text{ を } x \text{ について偏微分」}
$$

$\partial$ (ラウンド・ディー) は普通の $d$ と区別するための記号。**「他の変数は固定して、$x$ だけ動かす」** という意味。

### 例

$f(x, y) = x^2 + 3xy + y^2$

- **$x$ だけ動かす** ($y$ は定数扱い):

  $$
  \frac{\partial f}{\partial x} = 2x + 3y
  $$

- **$y$ だけ動かす** ($x$ は定数扱い):

  $$
  \frac{\partial f}{\partial y} = 3x + 2y
  $$

> 💡 **「他の変数は定数とみなして、普通の微分」** がポイント。

### 直感: 山の上の地形図

$f(x, y)$ を「ある点の標高」と思うと:
- $\dfrac{\partial f}{\partial x}$: **東 ($x$ 方向) に1歩進んだときの標高変化**
- $\dfrac{\partial f}{\partial y}$: **北 ($y$ 方向) に1歩進んだときの標高変化**

$f$ のグラフを切って「**$x$ 方向の断面の傾き**」「**$y$ 方向の断面の傾き**」を測るイメージ。

---

## 3. Python で偏微分

### 標準形式 1: SymPy

```python
import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + 3*x*y + y**2

# ∂f/∂x
print(sp.diff(f, x))   # 2*x + 3*y

# ∂f/∂y
print(sp.diff(f, y))   # 3*x + 2*y

# 値を代入
print(sp.diff(f, x).subs([(x, 1), (y, 2)]))   # 2 + 6 = 8
```

### 標準形式 2: 数値偏微分

```python
import numpy as np

def f(x, y):
    return x**2 + 3*x*y + y**2

def partial_x(f, x, y, h=1e-5):
    """x について偏微分."""
    return (f(x + h, y) - f(x - h, y)) / (2 * h)

def partial_y(f, x, y, h=1e-5):
    """y について偏微分."""
    return (f(x, y + h) - f(x, y - h)) / (2 * h)

print(partial_x(f, 1.0, 2.0))  # ≈ 8
print(partial_y(f, 1.0, 2.0))  # ≈ 7
```

### JAX 形式 (本命)

JAX の `jax.grad` は **第 1 引数についての偏微分** を返します:

```python
import jax
import jax.numpy as jnp

def f(p):
    """p[0] を x、p[1] を y として扱う."""
    return p[0]**2 + 3*p[0]*p[1] + p[1]**2

# 勾配ベクトル ∇f = (∂f/∂x, ∂f/∂y)
grad_f = jax.grad(f)
print(grad_f(jnp.array([1.0, 2.0])))   # [8.0, 7.0]
```

`jax.grad(f)` は **入力ベクトルの全成分について偏微分** を一気に返してくれます。これが **勾配ベクトル**:

$$
\nabla f = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n}\right)
$$

詳しくは → [`05_gradient_jacobian.md`](05_gradient_jacobian.md)

---

## 4. 多変数の連鎖律 (multivariable chain rule)

$z = f\bigl(g(x), h(x)\bigr)$ のような、内部で多変数を経由するケース:

$$
\frac{dz}{dx} = \frac{\partial f}{\partial g} \cdot \frac{dg}{dx} + \frac{\partial f}{\partial h} \cdot \frac{dh}{dx}
$$

「**それぞれの中間変数経由の影響を全部足し算**」。

ニューラルネットの誤差逆伝播は、このルールを多層に拡張したものです。

---

## 5. 多変数の最大・最小

1 変数で「$f'(x) = 0$ になる点が極値の候補」だったように、多変数では:

> **$\nabla f = 0$** (すべての偏微分がゼロ) になる点が **極値の候補**

例えば $f(x, y) = (x-1)^2 + (y-2)^2$ の最小値は $(1, 2)$ で、そこで $\dfrac{\partial f}{\partial x} = \dfrac{\partial f}{\partial y} = 0$。

```python
import jax
import jax.numpy as jnp

def f(p):
    return (p[0] - 1)**2 + (p[1] - 2)**2

grad_f = jax.grad(f)
print(grad_f(jnp.array([1.0, 2.0])))   # [0.0, 0.0]  ← 最小点!
```

これが **勾配降下法** の基礎。
詳しくは → [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md)

---

## 6. 等高線で可視化

多変数関数は $(x, y) \to z$ の 3 次元グラフですが、紙に描くとき **等高線** で表現するのが便利:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # f(x,y) = x² + y²

plt.contour(X, Y, Z, levels=20)
plt.colorbar()
plt.axis('equal')
plt.show()
```

→ 同心円が表示される (お椀型のグラフを上から見たとき)。
**勾配は等高線に垂直**な方向 (= 一番急に登る方向) を指します。

---

## 7. ML / AI への接続

### ニューラルネットのパラメータは「超多変数関数」

GPT-4 規模のモデル: **約 1750 億パラメータ**。
損失関数 $L(w_1, w_2, \dots, w_{1.75 \times 10^{11}})$ は **1750 億変数の関数**。

各パラメータ $w_i$ についての偏微分 $\dfrac{\partial L}{\partial w_i}$ を**全部一気に計算**する必要があります。
これを高速にやるのが **JAX の `grad`** や **PyTorch の `backward`**。

### 例: 線形回帰の偏微分

```python
import jax
import jax.numpy as jnp

# モデル: y = wx + b、損失: (y - (wx+b))²
def loss(params, x, y):
    w, b = params['w'], params['b']
    return (y - (w * x + b))**2

grads = jax.grad(loss)({'w': 0.5, 'b': 0.1}, 2.0, 3.0)
print(grads)   # {'w': ..., 'b': ...}  ← 各パラメータの偏微分
```

これが **学習の本体**。詳しくは → [`06_ml_math_bridge/`](../06_ml_math_bridge/README.md)

---

## 8. ハマりポイント

- **どの変数で微分するかを明示**: $\dfrac{\partial f}{\partial x}$ vs $\dfrac{\partial f}{\partial y}$ 混同しない
- **等高線の解釈**: 等高線の **間隔が狭い = 傾きが急**
- **関数の引数の取り方**: JAX では `f(p)` のように **ベクトルで渡す** のが標準
- **shape の一貫性**: ベクトル入力なら勾配もベクトル (同じ shape)

---

## まとめ

| 概念 | 数式 | Python |
|---|---|---|
| 偏微分 | $\dfrac{\partial f}{\partial x}$ | `sympy.diff(f, x)` / `jax.grad` |
| 多変数関数 | $f(x_1, x_2, \dots)$ | `lambda p: ...` |
| 勾配ベクトル | $\nabla f = \left(\dfrac{\partial f}{\partial x_1}, \dots, \dfrac{\partial f}{\partial x_n}\right)$ | `jax.grad(f)(p)` |
| 極値の必要条件 | $\nabla f = 0$ | `grad_f(p) ≈ 0` |

**この章のキー**: 偏微分は「1変数だけ動かして他は固定」の微分。`jax.grad` で関数を渡せばベクトル全体の偏微分を一気に取れる。

---

## 次へ

→ [`05_gradient_jacobian.md`](05_gradient_jacobian.md) — 勾配ベクトル・ヤコビアン・ヘッシアン

## 関連
- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX 自動微分の本格学習
- [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 勾配を使った最適化

---

## 🔍 ググってみよう

- **偏微分 (partial derivative)** — 多変数微積分の基本
- **全微分 (total derivative)** — 複数変数の同時変化
- **ヤコビアン (Jacobian)** — 多変数→多変数 関数の微分行列
- **ヘッセ行列 (Hessian)** — 2階偏微分の行列、最適化で重要
- **ラグランジュ乗数法** — 制約付き最適化の必殺技
- **勾配場 (gradient field)** — ベクトル場としての勾配
- **方向微分 (directional derivative)** — 任意方向への変化率

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`03_integrals.md`](03_integrals.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`05_gradient_jacobian.md`](05_gradient_jacobian.md) |
