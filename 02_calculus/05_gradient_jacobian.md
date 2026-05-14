# 02-5. 勾配・ヤコビアン・ヘッシアン — ML 微分の総合編

**このページのゴール**: 勾配 $\nabla f$、ヤコビアン $J_f$、ヘッシアン $H_f$ を区別できるようになり、それぞれを Python で計算できるようになる。
これが**深層学習の数学の中核**。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`02_calculus/notebooks/05_gradient_jacobian.ipynb`](notebooks/05_gradient_jacobian.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`04_multivariable.md`](04_multivariable.md) — 偏微分
> - [`01_linear_algebra/02_matrices.md`](../01_linear_algebra/02_matrices.md) — 行列の基本

---

## 1. 全体像 — 3 つの "微分" の使い分け

| 名前 | 何 → 何 | 形 | ML での出番 |
|---|---|---|---|
| **勾配 $\nabla f$** | スカラー → ベクトル | ベクトル | **損失関数の勾配** (← 訓練の本体) |
| **ヤコビアン $J_f$** | ベクトル → 行列 | 行列 | 順伝播の各層の感度 |
| **ヘッシアン $H_f$** | スカラー → 行列 | 行列 (対称) | **2次最適化** (Newton 法、二次収束) |

### 入出力の対応

| 関数の型 | 1階微分 | 2階微分 |
|---|---|---|
| $f: \mathbb{R}^n \to \mathbb{R}$ (スカラー出力) | **勾配 $\nabla f \in \mathbb{R}^n$** | **ヘッシアン $H_f \in \mathbb{R}^{n \times n}$** |
| $f: \mathbb{R}^n \to \mathbb{R}^m$ (ベクトル出力) | **ヤコビアン $J_f \in \mathbb{R}^{m \times n}$** | (テンソル、深入りしない) |

---

## 2. 勾配 $\nabla f$ — 「最も急に登る方向」

### 定義

$f: \mathbb{R}^n \to \mathbb{R}$ の勾配:

$$
\nabla f(x) = \left(\frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, \dots, \frac{\partial f}{\partial x_n}\right)
$$

これは**ベクトル**で、その方向は「**この点で最も急に登る方向**」。
逆方向 $-\nabla f$ は「**最も急に降りる方向**」 → これが勾配降下法の本質。

### 例

$f(x, y) = x^2 + y^2$ の勾配:

$$
\nabla f = (2x, 2y)
$$

点 $(1, 1)$ での勾配は $(2, 2)$。
これは「**北東方向に進むと一番急に登る**」を意味します。

### Python

```python
import jax
import jax.numpy as jnp

def f(p):
    return p[0]**2 + p[1]**2

grad_f = jax.grad(f)
print(grad_f(jnp.array([1.0, 1.0])))   # [2.0, 2.0]
```

`jax.grad` は **スカラー出力の関数** にだけ使えます。
ベクトル出力なら `jacrev` / `jacfwd` を (次節)。

---

## 3. ヤコビアン $J_f$ — ベクトル → ベクトルの微分

### 定義

$f: \mathbb{R}^n \to \mathbb{R}^m$ のヤコビアンは **$m \times n$ 行列**:

$$
J_f =
\begin{pmatrix}
\dfrac{\partial f_1}{\partial x_1} & \dfrac{\partial f_1}{\partial x_2} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\[6pt]
\dfrac{\partial f_2}{\partial x_1} & \dfrac{\partial f_2}{\partial x_2} & \cdots & \dfrac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\dfrac{\partial f_m}{\partial x_1} & \dfrac{\partial f_m}{\partial x_2} & \cdots & \dfrac{\partial f_m}{\partial x_n}
\end{pmatrix}
$$

「**入力 $x$ の各成分が、出力 $f$ の各成分にどう効くか**」を表す行列。

### 例

$f: \mathbb{R}^2 \to \mathbb{R}^3$:

$$
f(x, y) = (x + y,\; xy,\; x^2)
$$

$$
J_f = \begin{pmatrix}
1 & 1 \\
y & x \\
2x & 0
\end{pmatrix}
$$

### Python

```python
import jax
import jax.numpy as jnp

def f(p):
    return jnp.array([p[0] + p[1], p[0] * p[1], p[0]**2])

# ヤコビアン (リバースモード、ML で標準)
J = jax.jacrev(f)
print(J(jnp.array([1.0, 2.0])))
# [[1. 1.]
#  [2. 1.]
#  [2. 0.]]
```

> 💡 **`jacrev` vs `jacfwd`**:
> - `jacrev` (reverse-mode): **出力次元 $m$ が小さい** ときに高速 (ML の損失関数向け)
> - `jacfwd` (forward-mode): **入力次元 $n$ が小さい** ときに高速
>
> ML では $m=1$ (損失) のことが多いので、`jacrev` (= `grad` の一般版) が定番。

---

## 4. ヘッシアン $H_f$ — 2階微分の行列

### 定義

$f: \mathbb{R}^n \to \mathbb{R}$ のヘッシアンは **$n \times n$ の対称行列**:

$$
H_f = \begin{pmatrix}
\dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1 \partial x_n} \\[6pt]
\dfrac{\partial^2 f}{\partial x_2 \partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\dfrac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \cdots & \dfrac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}
$$

### なぜ重要か

ヘッシアンの**固有値の符号** で、その点が「最小・最大・鞍点」のどれかが分かります:

| 固有値 | 意味 |
|---|---|
| 全部正 | **最小点** (お椀の底) |
| 全部負 | 最大点 (山の頂上) |
| 正負混在 | **鞍点** (馬の鞍、峠) |

ML で「**鞍点に引っかかる**」現象は、まさにヘッシアンの固有値が原因。

### Python

```python
import jax
import jax.numpy as jnp

def f(p):
    return p[0]**2 + 2*p[0]*p[1] + 3*p[1]**2

H = jax.hessian(f)
print(H(jnp.array([0.0, 0.0])))
# [[2. 2.]
#  [2. 6.]]

# 固有値 (対称行列なので eigh)
print(jnp.linalg.eigvalsh(H(jnp.array([0.0, 0.0]))))
# [1.05... 6.94...]   ← 全部正 → 最小点
```

---

## 5. 連鎖律をベクトルで書き直す

スカラーの連鎖律: $(g \circ f)' = g'(f(x)) \cdot f'(x)$

ベクトル版 (ヤコビアンを使う):

$$
J_{g \circ f}(x) = J_g(f(x)) \cdot J_f(x)
\qquad \text{(行列の積)}
$$

ニューラルネットの誤差逆伝播は、これを**層ごとに繰り返し適用**しているだけ。

$$
x \xrightarrow{\text{層1}} h_1 \xrightarrow{\text{層2}} h_2 \xrightarrow{\text{層3}} y \xrightarrow{} L
$$

$$
\frac{dL}{dx} = \frac{dL}{dh_3} \cdot J_3 \cdot J_2 \cdot J_1
$$

という行列の連鎖。

---

## 6. ベクトル⊕ヤコビアン積 (vjp) と JAX のもう1つの真価

実は ML では、**完全なヤコビアン行列を作らない** ことが多いです。
代わりに **「ヤコビアンとベクトルの積」だけ** を計算します:

```python
import jax
import jax.numpy as jnp

def f(p):
    return jnp.array([p[0]**2, p[0]*p[1], p[1]**3])

# vjp (vector-Jacobian product): "勾配がベクトルvのとき、入力側に伝わる勾配"
# ML の誤差逆伝播の本体
y, vjp_fn = jax.vjp(f, jnp.array([2.0, 3.0]))
print('y =', y)

# 出力空間でのコ・ベクトル v
v = jnp.array([1.0, 1.0, 1.0])
print('入力空間に伝わる勾配:', vjp_fn(v))
```

数式で書くと、出力勾配 $v \in \mathbb{R}^m$ に対して:

$$
\text{vjp}(v) = v^\top J_f \in \mathbb{R}^n
$$

これがあるおかげで、**1750 億パラメータのニューラルネット** でもメモリ爆発せずに勾配が取れます。

---

## 7. ML / AI への接続

### 1) 訓練ループの本体

```python
import jax
import jax.numpy as jnp

# モデル
def model(params, x):
    return jnp.dot(params, x)

# 損失
def loss(params, x, y):
    return (model(params, x) - y) ** 2

# 勾配 (パラメータについて)
grad_loss = jax.grad(loss)

# 更新
params = params - learning_rate * grad_loss(params, x, y)
```

数式での更新式:

$$
\theta \leftarrow \theta - \eta \nabla L(\theta)
$$

すべて **`jax.grad` 1 回** で済む。ヤコビアンもヘッシアンも内部では暗黙的。

### 2) 2次最適化 (Newton 法)

通常の勾配降下を、ヘッセ行列で割って改良:

$$
\theta \leftarrow \theta - H^{-1} \nabla L
$$

これが **ニュートン法**。一歩で収束することもある (ただし計算コスト大)。

ML では **L-BFGS** など「擬似ヘッシアン」を使う方法が実用的。

---

## 8. ハマりポイント

- **`jax.grad` はスカラー出力専用**: ベクトル出力なら `jacrev`/`jacfwd`
- **`jacrev` vs `jacfwd` の選択**: 出力 $m$ と入力 $n$ のサイズで決める
- **ヘッシアンは大きい**: $n$ 次元なら $n \times n$ 行列。1750億変数だと不可能
- **対称性の検証**: ヘッシアンは理論上対称、数値的にズレることがある
- **ベクトル化**: 複数点で勾配を取りたいなら `jax.vmap(jax.grad(f))`

---

## まとめ

| 概念 | 入力 → 出力 | 形 | JAX |
|---|---|---|---|
| 勾配 $\nabla f$ | $\mathbb{R}^n \to \mathbb{R}$ | ベクトル $(n,)$ | `jax.grad(f)` |
| ヤコビアン $J_f$ | $\mathbb{R}^n \to \mathbb{R}^m$ | 行列 $(m, n)$ | `jax.jacrev(f)` / `jax.jacfwd(f)` |
| ヘッシアン $H_f$ | $\mathbb{R}^n \to \mathbb{R}$ の 2階 | 行列 $(n, n)$ 対称 | `jax.hessian(f)` |
| VJP | (出力勾配) → (入力勾配) | – | `jax.vjp(f, x)` |
| JVP | (入力方向) → (出力変化) | – | `jax.jvp(f, x, v)` |

**この章のキー**: ML の微分はすべて `jax.grad` (とその仲間) で取れる。完全な行列を作らない VJP/JVP がメモリ効率の鍵。

---

## 微積分章 完了 🎉

これで 02_calculus 章は卒業です。
次は確率・統計に進むと、ML の「**データから学ぶ**」側面が見えてきます。

→ [`../03_probability_statistics/README.md`](../03_probability_statistics/README.md)

## 関連
- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX 自動微分の本格学習
- [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 勾配降下法
- [`06_ml_math_bridge/02_backprop.md`](../06_ml_math_bridge/02_backprop.md) — 誤差逆伝播

---

## 🔍 ググってみよう

- **勾配 (gradient)** — ML の本体
- **ヤコビアン (Jacobian)** — 多変数→多変数 関数の微分
- **ヘッセ行列 (Hessian)** — 2階微分の行列
- **ニュートン法 (Newton's method)** — ヘッセ行列を使う2次最適化
- **L-BFGS** — 擬似ヘッセ行列を使う実用的な手法
- **誤差逆伝播法 (backpropagation)** — ヤコビアンの連鎖律の応用
- **vjp / jvp** — 自動微分の2つのモード
- **鞍点問題 (saddle point problem)** — 高次元最適化の難所

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`04_multivariable.md`](04_multivariable.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`../03_probability_statistics/README.md`](../03_probability_statistics/README.md) |
