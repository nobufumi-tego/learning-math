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
```

## 添字表記

| 表記 | 意味 |
|---|---|
| `x_i` または `xᵢ` | i番目の要素（数学は1始まりが多い） |
| `x^(k)` | k番目（イテレーション k 回目など） |
| `x_{i,j}` | 行 i 列 j の要素 |

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
