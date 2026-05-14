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
