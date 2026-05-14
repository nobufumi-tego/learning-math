# 02-3. 積分 — 「面積」と「累積」を扱う

**このページのゴール**: 積分を「**グラフの下の面積**」「**累積**」の道具として直感し、数値積分・記号積分の両方を Python で扱えるようになる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`02_calculus/notebooks/03_integrals.ipynb`](notebooks/03_integrals.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_derivatives.md`](02_derivatives.md) — 微分 (積分は微分の "逆")
> - [`00_notation/05_summation_product.md`](../00_notation/05_summation_product.md) — `∫` `Σ` の感覚

---

## 1. ひと言で

> **積分** = 「**ある関数の "下の面積"**」を計算する道具

具体例:
- 速度 → 積分 → **走った距離**
- 電力 → 積分 → **使った電力量 (kWh)**
- 確率密度 → 積分 → **確率**
- 損失関数 → 積分 → **平均的な誤差**

**「微小な変化を全部足し上げる」** のが積分。
微分が「**変化の速さ**」、積分は「**累積した量**」、と覚えておけばOK。

---

## 2. 記号と読み方

| 記号 | 読み方 | 意味 |
|---|---|---|
| `∫ f(x) dx` | "the integral of f of x dee-x" | 不定積分 (関数を返す) |
| `∫_a^b f(x) dx` | "integral from a to b of f(x) dx" | **定積分** (a〜b の面積、数値を返す) |
| `dx` | "dee x" | 「x について積分する」の記号 |
| `F(x)` | "big F" | f の不定積分 (原始関数) |

**微積分学の基本定理** (これが超重要):
```
∫_a^b f(x) dx = F(b) - F(a)        ただし F'(x) = f(x)
```

訳: 「**面積を計算するには、原始関数 F を見つけて、両端での値の差を取る**」
= **微分の逆操作で積分が解ける**。

---

## 3. 直感: 「短冊の和」が「面積」になる

絵で考えると:

```
        f(x)
         │
   ┌────╮
   │    │╮
   │    │╮╮             ← グラフ
   │    │  ╮╮╮
   ├────┤    ╮╮
   │ ▮  │ ▮  │  ▮       ← 短冊で近似
   │ ▮  │ ▮  │  ▮
   └────┴────┴────→ x
   a    ...     b
```

「**短冊の幅を限りなく細くしていく → 真の面積**」 が積分の定義。
これを **リーマン和** と呼びます (大学数学で出てくる)。

---

## 4. 主要な公式

| f(x) | ∫ f(x) dx (+C) |
|---|---|
| `定数 c` | `c·x` |
| `xⁿ` | `xⁿ⁺¹ / (n+1)` (n ≠ -1) |
| `1/x` | `ln|x|` |
| `e^x` | `e^x` |
| `sin x` | `-cos x` |
| `cos x` | `sin x` |

> 💡 `+C` (積分定数) は不定積分でつく。**定積分では消える**ので気にしなくていい場面多い。

---

## 5. Python で積分

### 標準形式 1: SymPy (記号積分 — 厳密に解く)

```python
import sympy as sp

x = sp.Symbol('x')
f = x**2

# 不定積分
print(sp.integrate(f, x))          # x³/3

# 定積分: ∫₀² x² dx = 8/3
print(sp.integrate(f, (x, 0, 2)))  # 8/3
```

複雑な関数も:
```python
# ∫ sin(x) dx = -cos(x)
print(sp.integrate(sp.sin(x), x))            # -cos(x)

# ∫₀^π sin(x) dx = 2
print(sp.integrate(sp.sin(x), (x, 0, sp.pi)))  # 2
```

### 標準形式 2: SciPy (数値積分 — 速くて実用的)

```python
import numpy as np
from scipy import integrate

def f(x):
    return x**2

# ∫₀² x² dx を数値計算
result, error = integrate.quad(f, 0, 2)
print(f'結果: {result:.6f},  誤差推定: {error:.2e}')
# 結果: 2.666667 (= 8/3)
```

`scipy.integrate.quad` は **適応的に短冊の幅を変える賢いアルゴリズム** を使うので、SymPy が解けない関数でも数値解が出ます。

### 多重積分

二重積分 ∫∫ f(x,y) dxdy:

```python
from scipy import integrate

def f(x, y):
    return x * y

# ∫₀¹ ∫₀¹ xy dxdy = 1/4
result, _ = integrate.dblquad(f, 0, 1, 0, 1)
print(result)   # 0.25
```

### JAX 形式 (数値積分用)

JAX には専用の積分関数は薄いですが、**台形則** などは自分で書けます:

```python
import jax.numpy as jnp
import jax

def trapezoid(f, a, b, n=1000):
    """台形則 (区間を n 等分して台形の面積を足す)."""
    xs = jnp.linspace(a, b, n + 1)
    ys = jax.vmap(f)(xs)
    h = (b - a) / n
    return h * (jnp.sum(ys) - 0.5 * (ys[0] + ys[-1]))

print(trapezoid(lambda x: x**2, 0.0, 2.0))   # 約 2.667
```

`jax.vmap` で関数を全点に並列適用、`jnp.sum` で台形を足し上げる。
**勾配を取りたい積分計算 (例: 物理シミュ + ML)** には JAX が便利。

---

## 6. ML / AI への接続

### 期待値 = 積分

確率変数 X の期待値:
```
E[X] = ∫ x · p(x) dx
```

**確率密度関数 p(x)** で重み付けして x を全部足す = 積分。

```python
from scipy import integrate
import numpy as np

# 標準正規分布 N(0, 1) の期待値 (= 0 のはず)
def integrand(x):
    return x * np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

result, _ = integrate.quad(integrand, -np.inf, np.inf)
print(result)   # ≈ 0.0  (理論通り)
```

### 確率の規格化条件

確率密度 p(x) は必ず `∫ p(x) dx = 1` を満たす:

```python
def gaussian(x):
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

result, _ = integrate.quad(gaussian, -np.inf, np.inf)
print(result)   # 1.0  (規格化されている)
```

### 損失の汎化誤差

理論上、機械学習モデルの「**汎化損失**」は:
```
L = ∫ ℓ(model(x), y) p(x, y) dx dy
```

実際は積分が解けないので、データの平均で近似する → これが**経験リスク**。

---

## 7. ハマりポイント

- **`+C` (積分定数)** を忘れない (不定積分では必須)
- **被積分関数の特異点**: `1/x` を 0 を含む区間で積分すると発散
- **数値積分の精度**: 振動が激しい関数は `quad` でも誤差大 → 区間を分割する
- **無限区間**: `quad(f, -np.inf, np.inf)` も使えるが、収束しない関数もある
- **JAX で積分の勾配**: `quad` は JAX-traceable じゃない。台形則を自分で書くと OK

---

## まとめ

| 概念 | 数式 | Python |
|---|---|---|
| 不定積分 | `∫ f(x) dx = F(x) + C` | `sympy.integrate(f, x)` |
| 定積分 | `∫_a^b f(x) dx` | `sympy.integrate(f, (x, a, b))` |
| 数値定積分 | – | `scipy.integrate.quad(f, a, b)` |
| 二重積分 | `∫∫ f dx dy` | `scipy.integrate.dblquad` |
| 台形則 (JAX) | – | 自分で書ける、`vmap` で高速 |

**この章のキー**: 積分 = グラフの下の面積、もしくは「微小な量の累積」。微分の逆操作。

---

## 次へ

→ [`04_multivariable.md`](04_multivariable.md) — 多変数関数: ML のパラメータは何百万次元

## 関連
- [`03_probability_statistics/01_probability_basics.md`](../03_probability_statistics/01_probability_basics.md) — 確率と積分
- [`07_jax/`](../07_jax/README.md) — JAX で積分の勾配を取る応用

---

## 🔍 ググってみよう

- **微積分学の基本定理 (Fundamental Theorem of Calculus)** — 微分と積分を結ぶ橋
- **リーマン和 (Riemann sum)** — 積分の厳密な定義
- **置換積分・部分積分** — 積分計算のテクニック
- **モンテカルロ積分** — 高次元積分を確率的に解く
- **ガウス求積 (Gaussian quadrature)** — `scipy.integrate.quad` の中身
- **シンプソン則 (Simpson's rule)** — 台形則より精度の高い数値積分
- **積分変換 (Fourier, Laplace)** — 関数を別の空間に持っていく道具

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`02_derivatives.md`](02_derivatives.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`04_multivariable.md`](04_multivariable.md) |
