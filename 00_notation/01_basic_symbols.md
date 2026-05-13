# 基本記号

数値・関係を表す基本記号。中学・高校で見たものから、大学院でも使うものまで。

## 等号・不等号系

| 記号 | 読み方（英 / 日） | 意味 | Python |
|---|---|---|---|
| `=` | "equals" / 「等しい」 | 等しい | `==`（比較）／ `=`（代入） |
| `≠` | "not equal" / 「等しくない」 | 等しくない | `!=` |
| `≈` | "approximately equal" / 「ほぼ等しい」 | 近似的に等しい | `np.isclose(a, b)` |
| `≡` | "identical / equivalent" / 「合同」「定義」 | 定義する、または恒等的に等しい | コメントで表現 |
| `:=` | "is defined as" / 「定義する」 | 左辺を右辺で定義 | `=`（代入） |
| `<`, `>` | "less / greater than" | 小なり、大なり | `<`, `>` |
| `≤`, `≥` | "less / greater than or equal" | 以下、以上 | `<=`, `>=` |
| `≪`, `≫` | "much less / greater than" | はるかに小さい / 大きい | （コメントで表現） |

### Python 例

```python
import numpy as np

a = 0.1 + 0.2
b = 0.3
print(a == b)                  # False（浮動小数点誤差）
print(np.isclose(a, b))        # True（≈ の Python 版）
```

## 数の集合（最頻出）

| 記号 | 読み方 | 意味 | Python での扱い |
|---|---|---|---|
| `ℕ` | "natural numbers" / 自然数 | 0, 1, 2, 3, ... | `int`（0以上） |
| `ℤ` | "integers" / 整数 | ..., -2, -1, 0, 1, 2, ... | `int` |
| `ℚ` | "rationals" / 有理数 | 分数で表せる数 | `fractions.Fraction` |
| `ℝ` | "real numbers" / 実数 | すべての実数 | `float`（近似） |
| `ℂ` | "complex numbers" / 複素数 | a + bi の形 | `complex` |
| `ℝⁿ` | "R-n" / n次元実空間 | n個の実数の組 | `np.ndarray` shape (n,) |

### Python 例

```python
import numpy as np

# ℝ³（3次元実空間）の元
x: np.ndarray = np.array([1.0, 2.0, 3.0])  # shape: (3,)

# ℂ の元
z: complex = 2 + 3j
print(z.real, z.imag)  # 2.0 3.0
```

## 無限・極限系

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `∞` | "infinity" / 無限大 | 無限 | `float('inf')`, `np.inf` |
| `-∞` | "minus infinity" / 負の無限大 | 負の無限 | `-np.inf` |
| `lim` | "limit" / 極限 | 極限を取る | `sympy.limit(...)` |

```python
import numpy as np
import sympy as sp

print(np.inf > 1e100)          # True
print(1.0 / np.inf)            # 0.0

x = sp.Symbol("x")
print(sp.limit(1/x, x, sp.oo)) # 0  (lim x→∞ 1/x = 0)
```

## その他の頻出記号

| 記号 | 読み方 | 意味 |
|---|---|---|
| `±` | "plus minus" / 「プラスマイナス」 | 正負両方 |
| `∝` | "proportional to" / 「比例する」 | 比例 |
| `∴` | "therefore" / 「ゆえに」 | 結論 |
| `∵` | "because" / 「なぜなら」 | 理由 |
| `□`, `∎`, `QED` | "Q.E.D." / 「証明終わり」 | 証明終了 |

## 関連: `/project:explain-symbol`

理解が曖昧な記号があれば、Claude Code で次のように質問:

```
/project:explain-symbol ≡
```
