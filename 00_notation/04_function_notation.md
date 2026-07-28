# 関数記法

関数は数学の基本道具。記法を理解すれば論文の半分が読める。

## 関数の宣言

| 表記 | 読み方 | 意味 |
|---|---|---|
| `f: A → B` | "f from A to B" | f は A から B への関数 |
| `f(x)` | "f of x" | f に x を入れた値 |
| `x ↦ f(x)` | "x maps to f(x)" | x を f(x) に写す（対応規則） |

### 例

数学:
```
f: ℝ → ℝ,  x ↦ x²
```
読み方: 「f は実数から実数への関数で、x を x² に対応させる」

Python:
```python
def f(x: float) -> float:
    """二乗を返す関数 f: ℝ → ℝ."""
    return x ** 2

print(f(3.0))  # 9.0
```

## ベクトル関数・多変数関数

数学:
```
f: ℝⁿ → ℝᵐ
```
n次元ベクトルを入れて、m次元ベクトルが出る関数。

Python:
```python
import numpy as np

def f(x: np.ndarray) -> np.ndarray:
    """ℝ² → ℝ³ の関数例.
    
    Args:
        x: 入力ベクトル。shape: (2,)

    Returns:
        出力ベクトル。shape: (3,)
    """
    return np.array([x[0] + x[1], x[0] * x[1], x[0] ** 2])


x = np.array([2.0, 3.0])  # shape: (2,)
print(f(x))               # [5. 6. 4.]  shape: (3,)
```

## 合成関数

| 表記 | 読み方 | 意味 |
|---|---|---|
| `g ∘ f` | "g composed with f" / 「g マル f」 | (g∘f)(x) = g(f(x)) |
| `f⁻¹` | "f inverse" / 「f の逆関数」 | f の逆関数 |
| `f\|_A` | "f restricted to A" | f の A への制限 |

```python
def f(x: float) -> float:
    return x + 1

def g(x: float) -> float:
    return x ** 2

# (g ∘ f)(x) = g(f(x)) = (x + 1)²
def g_compose_f(x: float) -> float:
    return g(f(x))

print(g_compose_f(2.0))  # 9.0
```

## よく使う関数記法

| 記法 | 意味 | Python |
|---|---|---|
| `\|x\|` | 絶対値 | `abs(x)` |
| `\|\|x\|\|` | ノルム（ベクトルの長さ） | `np.linalg.norm(x)` |
| `⌊x⌋` | 床関数（切り捨て） | `math.floor(x)` |
| `⌈x⌉` | 天井関数（切り上げ） | `math.ceil(x)` |
| `sgn(x)` | 符号関数 | `np.sign(x)` |
| `exp(x)`, `e^x` | 指数関数 | `np.exp(x)` |
| `log(x)`, `ln(x)` | 自然対数 | `np.log(x)` |
| `log₂(x)` | 2を底とする対数 | `np.log2(x)` |
| `sin(x)`, `cos(x)`, `tan(x)` | 三角関数（引数の単位は**ラジアン**） | `np.sin(x)`, `np.cos(x)`, `np.tan(x)` |
| `I(条件)`, `𝟙[条件]` | **指示関数**（条件が真なら 1、偽なら 0） | `int(cond)` / `(arr > c).astype(float)` |
| `Γ(x)` | **ガンマ関数**（階乗を実数に拡張。$\Gamma(n) = (n-1)!$） | `scipy.special.gamma(x)` |
| `B(α, β)` | **ベータ関数** $\dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ | `scipy.special.beta(a, b)` |

### 指示関数 `I(·)` — 「数える」を「足す」に変える道具

指示関数は、**条件を満たす個数を数える**作業を、**足し算の式**に書き換えるために使います。

$$
I(\theta > c) = \begin{cases} 1 & \theta > c \text{ のとき} \\ 0 & \text{それ以外} \end{cases}
$$

だから「$c$ を超えたものの割合」は、こう書けます:

$$
\frac{1}{K}\sum_{k=1}^{K} I\!\left(\theta^{(k)} > c\right)
$$

```python
import numpy as np

THRESHOLD: float = 0.5
samples = np.array([0.3, 0.6, 0.55, 0.4, 0.8])   # shape: (5,)

# 数式の I(·) は、NumPy では「真偽値の配列」がそのまま対応する
indicator = (samples > THRESHOLD)                 # array([False, True, True, False, True])
print(indicator.astype(int))                      # [0 1 1 0 1]  ← これが I(·)
print(indicator.mean())                           # 0.6  ← (1/K)ΣI(·) = 「超えた割合」
```

> 📌 **`mean()` が「割合」になるのが指示関数の効きどころ**です。
> True/False を 1/0 とみなして平均を取ると、そのまま比率になります。
> 確率をモンテカルロで近似するときの中心的な道具
> → [`03_probability_statistics/09_mcmc.md`](../03_probability_statistics/09_mcmc.md)

```python
import numpy as np
import math

x = -2.7

print(abs(x))            # 2.7    （|x|）
print(math.floor(x))     # -3     （⌊x⌋）
print(math.ceil(x))      # -2     （⌈x⌉）
print(np.sign(x))        # -1.0   （sgn(x)）
print(np.exp(1.0))       # 2.718... （e）
print(np.log(np.e))      # 1.0    （ln(e) = 1）
print(np.sin(np.pi / 6)) # 0.5    （sin 30°。引数はラジアン）
```

> ### ✒️ この関数名の生まれ — `sin` は誤訳だった
>
> 関数名の多くは語源をたどると図形的な意味が見えます。
>
> - `tan` = **tangent**（ラテン語 *tangere*「触れる」→ **接線**）
> - `sec` = **secant**（*secare*「切る」→ **割線**）
> - `exp` = **exponential**（指数）
> - `log` = **logarithm**（ギリシャ語 *logos*「比」+ *arithmos*「数」）
>
> ところが `sin` = **sinus** はラテン語で「**入り江・懐**」。三角形とも円とも関係ありません。
>
> **これは翻訳ミスです。** 元はサンスクリット語の **jyā（弓の弦）**でした。
> アラビア語に音訳される途中で母音が失われ、12 世紀のラテン語訳者が
> 別の単語 **jaib（湾）**と読み違えたと伝えられます。
>
> **1000 年の伝言ゲームで、「弓の弦」が「入り江」になった**わけです。
>
> 📖 続き → [`columns/02_sin_mistranslation.md`](columns/02_sin_mistranslation.md)（その「弓の弦」が今、Transformer の中で単語の位置を運んでいる話）

## 添字表記

| 表記 | 意味 |
|---|---|
| `x_i` または `xᵢ` | i番目の要素（数学は1始まりが多い） |
| `x^(k)` | k番目（イテレーション k 回目、**k 番目のサンプル**など）。**累乗ではない** |
| `x_{i,j}` | 行 i 列 j の要素 |

> ⚠️ **`x^(k)` の上付きカッコは「番号」で、累乗ではありません。**
> 勾配降下法の $\theta^{(k)}$ は「$k$ 回目の反復のパラメータ」、
> MCMC の $\theta^{(k)}$ は「$k$ 番目の標本」、ML の $x^{(i)}$ は「$i$ 番目のデータ点」。
> **カッコが付いていたら番号**と覚えてください（カッコなしの $x^2$ は普通に 2 乗）。

Python（0始まり）:
```python
x = np.array([10, 20, 30, 40])
print(x[0])   # 10  （数学の x_1 に相当）
print(x[1])   # 20  （数学の x_2 に相当）

M = np.array([[1, 2, 3],
              [4, 5, 6]])
print(M[0, 1])  # 2  （数学の M_{1,2} に相当）
```

**重要**: 数学の添字は **1始まり**、Python は **0始まり**。常にずれることに注意。

## ハマりポイント

- 数学の `f(x, y)` は引数2つ、Python でも同じだが、ベクトル `f([x, y])` と区別する
- `|x|` は文脈次第で「絶対値」「ノルム」「集合の濃度」が変わる
- 対数の底: `log` は分野で違う（数学＝自然対数 `ln`、情報理論＝2を底、工学＝10を底）

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`03_logic_symbols.md`](03_logic_symbols.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`05_summation_product.md`](05_summation_product.md) |
