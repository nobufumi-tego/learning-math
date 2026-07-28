# 総和 Σ・総乗 Π・積分 ∫

論文・教科書で最も頻出する記号たち。**この3つを完璧にすれば論文の式が一気に読める**。

## Σ（シグマ）— 総和

### 記法

```
  n
  Σ  aᵢ  =  a₁ + a₂ + ... + aₙ
 i=1
```

読み方: 「i を 1 から n まで動かして a_i を全部足す」

### Python 対応

```python
import numpy as np

a = np.array([10, 20, 30, 40])  # shape: (4,) → a_1=10, a_2=20, ...

# Σ a_i (i=1..4) = 10 + 20 + 30 + 40
total = np.sum(a)
print(total)  # 100

# 上限を変える: Σ a_i (i=1..2) = 10 + 20
print(np.sum(a[:2]))  # 30

# 関数を中に入れる: Σ a_i² = 100 + 400 + 900 + 1600
print(np.sum(a ** 2))  # 3000
```

### よくある形

| 数学 | 言葉 | Python |
|---|---|---|
| `Σᵢ xᵢ` | 全要素の和 | `np.sum(x)` |
| `Σᵢ wᵢ xᵢ` | 重み付き和（内積） | `np.dot(w, x)` または `w @ x` |
| `Σᵢ (xᵢ − μ)²` | 偏差平方和 | `np.sum((x - mu) ** 2)` |
| `(1/n) Σᵢ xᵢ` | 平均 | `np.mean(x)` |
| `Σᵢⱼ Mᵢⱼ` | 行列全要素の和 | `np.sum(M)` |

### 二重和

```
  m   n
  Σ   Σ   Mᵢⱼ
 i=1 j=1
```

```python
M = np.array([[1, 2, 3],
              [4, 5, 6]])
print(np.sum(M))  # 21
```

## Π（パイ）— 総乗

### 記法

```
  n
  Π  aᵢ  =  a₁ × a₂ × ... × aₙ
 i=1
```

読み方: 「i を 1 から n まで動かして a_i を全部かける」

### Python 対応

```python
import numpy as np

a = np.array([2, 3, 4, 5])

# Π a_i = 2 × 3 × 4 × 5
print(np.prod(a))  # 120

# n! (階乗) は Π i (i=1..n)
import math
print(math.factorial(5))  # 120
```

### 応用例: 確率の独立試行

独立な事象の同時確率:
```
P(A₁ ∧ A₂ ∧ ... ∧ Aₙ) = Π P(Aᵢ)
```

```python
probs = np.array([0.5, 0.5, 0.5])
print(np.prod(probs))  # 0.125  （3回のコイン全部表）
```

## ∫（インテグラル）— 積分

### 記法

```
  b
  ∫ f(x) dx
  a
```

読み方: 「f(x) を x について a から b まで積分」

意味: 関数 f(x) のグラフと x軸の間の面積（符号付き）。

> ### ✒️ この記号の生まれ — `∫` と `Σ`
>
> `∫` の形には理由があります。ラテン語 **summa（和）の頭文字 s** を、縦に引き伸ばした形なのです。
> **ライプニッツ**が 1675 年に使い始めたとされます。積分は「細かく切って**足す**」操作なので、
> 記号自体が「これは和である」と言っているわけです。
>
> `Σ`（シグマ）も同じ発想で、ギリシャ語で **sum** にあたる語の頭文字。オイラーが 1755 年に広めました。
> **どちらも「S」から来ている**、というのが面白いところです。
>
> なお、ライプニッツとニュートンは微積分の発見者の座を争いましたが、
> 歴史的に決定的だったのは「**どちらの記号が使いやすかったか**」でした。
>
> 📖 続き → [`columns/01_leibniz_vs_newton.md`](columns/01_leibniz_vs_newton.md)（記号の優劣がイギリスの数学を 100 年遅らせた話）

### Python 対応（数値積分）

```python
import numpy as np
from scipy import integrate

def f(x: float) -> float:
    """f(x) = x²."""
    return x ** 2

# ∫₀² x² dx を計算
result, error = integrate.quad(f, 0, 2)
print(result)  # 2.6666...  （理論値 8/3）
```

### Python 対応（記号積分）

```python
import sympy as sp

x = sp.Symbol("x")
expr = x ** 2

# 不定積分: ∫ x² dx = x³/3 + C
print(sp.integrate(expr, x))           # x**3/3

# 定積分: ∫₀² x² dx
print(sp.integrate(expr, (x, 0, 2)))   # 8/3
```

## 多重積分・二重積分

```
  ∬ f(x, y) dx dy
  D
```

読み方: 「領域 D の上で f(x, y) を積分」

```python
from scipy import integrate

def f(x: float, y: float) -> float:
    return x * y

# ∫₀¹ ∫₀¹ xy dx dy = 1/4
result, _ = integrate.dblquad(f, 0, 1, 0, 1)
print(result)  # 0.25
```

## Γ（ガンマ関数）— 階乗を実数へつなぐ

### 直感

$n!$ は $1!, 2!, 3!, \dots$ と**飛び飛び**にしか定義されていません。$2.5!$ は？と聞かれると困る。

そこで「階乗の点を**なめらかにつないだ曲線**」を用意したのが **ガンマ関数 $\Gamma$** です。

```
n!  :  ● 　 ● 　 ● 　 ●        ← 整数の上にしか点がない
Γ   :  ●─╮ ●─╮ ●─╮ ●          ← その点を通る「曲線」
```

読み方は「**ガンマ**」（大文字ギリシャ文字。小文字 $\gamma$ とは別物）。

### 定義

$$
\Gamma(z) = \int_0^{\infty} t^{\,z-1} e^{-t}\,dt \qquad (z > 0)
$$

前節の $\int$ がここで効いてきます。**「積分で定義された関数」の代表例**です。

### ⚠️ 1 つズレる

いちばん引っかかるのがここです。

$$
\Gamma(n) = (n-1)! \qquad\text{であって}\qquad \Gamma(n) \ne n!
$$

| $n$ | $\Gamma(n)$ | $(n-1)!$ |
|---|---|---|
| 1 | 1 | $0! = 1$ |
| 2 | 1 | $1! = 1$ |
| 3 | 2 | $2! = 2$ |
| 4 | 6 | $3! = 6$ |
| 5 | 24 | $4! = 24$ |

$n!$ が欲しいなら $\Gamma(n+1)$ を使います。**このズレは歴史的な事情**（オイラーの定義の流儀）で、
数学的な必然ではありません。「そういうものだ」と割り切って覚えるのが早いです。

### なぜ階乗の「つづき」になるのか

鍵は**漸化式**です。部分積分をすると、次が成り立ちます:

$$
\Gamma(z+1) = z\,\Gamma(z)
$$

これは階乗の $n! = n \cdot (n-1)!$ とまったく同じ形。
出発点が $\Gamma(1) = \int_0^\infty e^{-t}dt = 1$ なので、$\Gamma(2)=1, \Gamma(3)=2, \Gamma(4)=6, \dots$ と
階乗の値をなぞっていきます。

整数以外でも値が決まるのが強みで、たとえば:

$$
\Gamma\!\left(\tfrac{1}{2}\right) = \sqrt{\pi} \approx 1.7725
$$

（この $\pi$ は**円周率**のほうです。→ [`06_greek_letters.md`](06_greek_letters.md)）

### Python

```python
import math

import numpy as np
from scipy.special import gamma, gammaln, beta

# Γ(n) = (n−1)! を確認する
for n in range(1, 6):
    print(f'Γ({n}) = {gamma(n):>4.0f}   ({n-1}! = {math.factorial(n-1)})')

# 整数以外でも値がある (階乗ではできない)
print(f'Γ(0.5) = {gamma(0.5):.4f}   (√π = {np.sqrt(np.pi):.4f})')
print(f'Γ(2.5) = {gamma(2.5):.4f}')

# ⚠️ すぐオーバーフローする -> 対数版 gammaln を使う
print(f'Γ(171) = {gamma(171):.3e}')        # 7.257e+306  ← ここまでは足りる
print(f'Γ(172) = {gamma(172)}')            # inf  ← float64 (最大 ~1.8e308) を超える
print(f'log Γ(172) = {gammaln(172):.4f}')  # 711.7147  こちらは計算できる
print(f'log Γ(10000) = {gammaln(10000):.1f}')  # 桁がいくら大きくても平気
```

> ⚠️ **実務では `gamma` ではなく `gammaln`（対数ガンマ関数）を使う場面が多い**です。
> 尤度計算では $\Gamma$ の値そのものではなく**比や積**が必要で、対数にすれば
> 掛け算が足し算になり、オーバーフローも避けられます
> （[`03_probability_statistics/09_mcmc.md`](../03_probability_statistics/09_mcmc.md) の「対数で比較する」と同じ発想）。

### どこで出会うか — ほとんどは「正規化定数」として

$\Gamma$ を単体で使うことは少なく、**確率密度の頭に付く係数**として現れます。

**ベータ関数** $B$（$\Gamma$ から作る）:

$$
B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}
$$

**ベータ分布**（0〜1 の割合を表す。ベイズの事前分布の定番）:

$$
f(x) = \frac{1}{B(\alpha,\beta)}\,x^{\alpha-1}(1-x)^{\beta-1}
= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\,x^{\alpha-1}(1-x)^{\beta-1}
\qquad (0 < x < 1)
$$

**ガンマ分布**（正の量・待ち時間・発生率）:

$$
f(x) = \frac{\beta^{\alpha}}{\Gamma(\alpha)}\,x^{\alpha-1}e^{-\beta x} \qquad (x > 0)
$$

> 📌 **どちらも「$x$ の式」の前に付いた $\Gamma$ の塊は、面積を 1 にするための割り算**です。
> つまり [`01_basic_symbols.md`](01_basic_symbols.md) の $\propto$ で**省略される部分**そのもの。
> ベイズで「$\propto$ だから正規化定数は無視してよい」と言うとき、
> 消えているのはたいていこの $\Gamma$ の塊です。
> → [`03_probability_statistics/08_bayesian_inference.md`](../03_probability_statistics/08_bayesian_inference.md)

```python
from scipy.special import beta as beta_fn, gamma
from scipy import stats
import numpy as np

ALPHA: float = 2.0
BETA: float = 5.0
x: float = 0.3

# 定義どおりに手で計算する
manual = x**(ALPHA - 1) * (1 - x)**(BETA - 1) / beta_fn(ALPHA, BETA)

# Γ で書いても同じ (B(α,β) = Γ(α)Γ(β)/Γ(α+β))
via_gamma = (gamma(ALPHA + BETA) / (gamma(ALPHA) * gamma(BETA))
             * x**(ALPHA - 1) * (1 - x)**(BETA - 1))

print(f'手計算       : {manual:.6f}')
print(f'Γ で書いた版 : {via_gamma:.6f}')
print(f'SciPy        : {stats.beta.pdf(x, ALPHA, BETA):.6f}')
assert np.isclose(manual, stats.beta.pdf(x, ALPHA, BETA))
print('✅ 3 つとも一致')
```

### Γ のハマりポイント

- **$\Gamma(n) = (n-1)!$ で 1 ズレる** — $n!$ が欲しいなら $\Gamma(n+1)$
- **大文字 $\Gamma$ と小文字 $\gamma$ は別物** — $\gamma$ は割引率・信用区間の裾確率など
- **負の整数と 0 では定義されない**（発散する）
- **$\Gamma(172)$ で `inf`** — float64 の上限（$\Gamma(171) \approx 7.3 \times 10^{306}$ が限界）。対数版 `gammaln` を使う
- **「ガンマ関数」と「ガンマ分布」は別物** — 分布の名前は、密度に $\Gamma$ が出てくることに由来

## ハマりポイント

- 添字の範囲を見落とさない: `Σ_{i=1}^{n}` か `Σ_{i=0}^{n-1}` かで意味が違う
- 数学は1始まり、Python は0始まり ← **本当によくバグる**
- `Σ x_i` のように範囲が省略されることがある（文脈から推測）
- `dx` は単なる装飾ではなく「何について積分するか」を指示する
- `∫` は「面積」「期待値」「分布関数」など意味が広い

## 練習: 期待値

確率変数 X の期待値:
```
E[X] = Σᵢ xᵢ p(xᵢ)        （離散）
E[X] = ∫ x p(x) dx         （連続）
```

Python:
```python
# 離散の例: サイコロの期待値
xs = np.array([1, 2, 3, 4, 5, 6])
ps = np.array([1/6] * 6)
ev = np.sum(xs * ps)
print(ev)  # 3.5
```

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`04_function_notation.md`](04_function_notation.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`06_greek_letters.md`](06_greek_letters.md) |
