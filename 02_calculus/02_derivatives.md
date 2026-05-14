# 02-2. 微分・導関数 — 「変化の速さ」を測る

**このページのゴール**: 微分が「**ある点での傾き**」だと体感し、SymPy で記号微分・JAX で自動微分の両方を使えるようになる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`02_calculus/notebooks/02_derivatives.ipynb`](notebooks/02_derivatives.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`01_limits.md`](01_limits.md) — 微分の土台 (極限)
> - [`00_notation/04_function_notation.md`](../00_notation/04_function_notation.md) — `f(x)` の記法

---

## 1. ひと言で

> **微分** = 「**ある点での "変化の速さ" (傾き)** を測る道具」

具体例で:
- 走っている車の **速度メーター** = 位置の微分 (位置がどれくらい速く変化しているか)
- 山道を歩くときの **傾き** = 高度関数の微分
- 株価チャートの **モメンタム** = 株価の微分

すべて「**今この瞬間、どれくらいの勢いで変化してるか**」を表すのが微分です。

---

## 2. 数学の記号

`f(x)` の微分 (導関数) はいくつかの書き方があります:

| 記号 | 読み方 | 場面 |
|---|---|---|
| `f'(x)` | "f prime of x" / 「エフ プライム オブ エックス」 | 1変数で簡潔 |
| `df/dx` | "dee-f dee-x" | ライプニッツ記法。物理・工学で頻出 |
| `Df` | "D of f" | 演算子記法 |
| `∂f/∂x` | "partial f partial x" / 「ラウンド ディー」 | **多変数の場合** (偏微分、04章) |

定義式:
```
f'(x) = lim  (f(x+h) - f(x)) / h
        h→0
```

意味: 「**x から少し進んだときの y の変化を、x の変化で割った値**」 を、h を 0 に近づけた極限。
**「傾き」** そのものです。

---

## 3. 直感: 「割線」が「接線」になる

絵で考えるとシンプル:

```
        f(x+h)  ←─────●
                       │
                       │ f(x+h) - f(x)  (高さの差)
                       │
        f(x)    ●──────┘
                ↑       ↑
                x       x+h
                ←───h───→  (横の差)
```

「**(高さの差) / (横の差) = 傾き**」 = **割線 (secant line)** の傾き。

そして h を 0 に近づけると、割線は **接線 (tangent line)** になります。
これがその点の「**真の傾き**」 = **微分**。

---

## 4. 主要な公式 (覚えるべきもの)

| f(x) | f'(x) | 覚え方 |
|---|---|---|
| `定数 c` | `0` | 平らな線、傾きゼロ |
| `xⁿ` | `n·xⁿ⁻¹` | べき乗ルール (一番重要!) |
| `e^x` | `e^x` | 自分自身が微分! (`e` の特権) |
| `ln x` | `1/x` | 対数の微分 |
| `sin x` | `cos x` | sin と cos のペア |
| `cos x` | `-sin x` | (符号反転) |

例:
- `f(x) = x³` → `f'(x) = 3x²`
- `f(x) = 5x⁴` → `f'(x) = 20x³`
- `f(x) = 1/x = x⁻¹` → `f'(x) = -x⁻² = -1/x²`

---

## 5. Python で微分

### 標準形式 1: SymPy (記号計算 — 数学者の世界)

```python
import sympy as sp

x = sp.Symbol('x')
f = x**3 + 2*x**2 - 5*x + 7

df = sp.diff(f, x)
print(df)
# → 3*x**2 + 4*x - 5

# ある点での値
print(df.subs(x, 2))
# → 15  (x=2 における傾き)
```

SymPy は **「数式そのもの」** を扱うので、結果も数式で返してくれます。

### 標準形式 2: 数値微分 (中央差分)

```python
import numpy as np

def f(x: float) -> float:
    return x**3 + 2*x**2 - 5*x + 7

def df_numeric(f, x: float, h: float = 1e-5) -> float:
    """中央差分: (f(x+h) - f(x-h)) / (2h)
    
    前進差分 (f(x+h)-f(x))/h より精度が高い (誤差 O(h²))
    """
    return (f(x + h) - f(x - h)) / (2 * h)

print(df_numeric(f, 2.0))   # 14.999... (≈ 15)
```

> 💡 **前進差分 vs 中央差分**: 同じ精度でも中央差分の方が誤差が小さい (`O(h²)` vs `O(h)`)。**勾配確認には中央差分を使う**のがプロの作法。

### JAX 形式 (自動微分 — ML の本命)

```python
import jax
import jax.numpy as jnp

def f(x):
    return x**3 + 2*x**2 - 5*x + 7

# jax.grad は「微分する関数」を返す
df = jax.grad(f)
print(df(2.0))   # 15.0  ← 厳密!
```

**たった 1 行 `jax.grad(f)` で勾配計算できる**。これが ML の本命の道具。
詳しくは → [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md)

#### 3 形式の比較

| 方式 | 入力 | 出力 | 速度 | 向き不向き |
|---|---|---|---|---|
| SymPy | 数式 | 数式 | 遅い | 数学的に厳密に確認したい時 |
| 数値差分 | 関数 + 点 | 数値 | 速い | 簡易チェック、教育用 |
| JAX | 関数 | 関数 | 速い・高精度 | **ML 本番**、複雑な合成関数 |

---

## 6. 連鎖律 (chain rule) — 合成関数の微分

ML で **誤差逆伝播法** の根幹を成す超重要ルール:

> **`(g∘f)'(x) = g'(f(x)) · f'(x)`**

訳: 「**外の関数の微分** × **中の関数の微分**」。

### 例

`y = sin(x²)` を微分したい。
- 外の関数: `g(u) = sin(u)`、`g'(u) = cos(u)`
- 内の関数: `f(x) = x²`、`f'(x) = 2x`

連鎖律で:
```
dy/dx = cos(x²) · 2x = 2x cos(x²)
```

Python で確認:

```python
import sympy as sp

x = sp.Symbol('x')
y = sp.sin(x**2)
print(sp.diff(y, x))   # 2*x*cos(x**2)  ← 一致!

# JAX でも
import jax
import jax.numpy as jnp
df = jax.grad(lambda x: jnp.sin(x**2))
print(df(1.0))   # 2*cos(1) ≈ 1.0806
```

### なぜ ML で重要か

ニューラルネットの 3 層構造:
```
入力 x → [層1] → [層2] → [層3] → 損失 L
```

**「L を入力 x で微分したい」** ときは、連鎖律で**層を逆順に辿る**:
```
dL/dx = dL/d(層3出力) × d(層3出力)/d(層2出力) × d(層2出力)/d(層1出力) × d(層1出力)/dx
```

これが **誤差逆伝播法 (backpropagation)** の正体。
詳しくは → [`06_ml_math_bridge/02_backprop.md`](../06_ml_math_bridge/02_backprop.md)

---

## 7. 高階微分

微分を **何度も繰り返す** こともできます:

| 記号 | 意味 |
|---|---|
| `f''(x)` または `d²f/dx²` | 2 階微分 (微分の微分) |
| `f'''(x)` | 3 階微分 |
| `f^(n)(x)` | n 階微分 |

物理的解釈:
- 位置 → 1階微分: **速度**
- 位置 → 2階微分: **加速度**
- 位置 → 3階微分: **加加速度 (jerk)**

```python
import sympy as sp

x = sp.Symbol('x')
f = x**5

print(sp.diff(f, x))      # 5*x**4   (1階)
print(sp.diff(f, x, 2))   # 20*x**3  (2階)
print(sp.diff(f, x, 3))   # 60*x**2  (3階)
```

JAX で重ねがけ:
```python
import jax

def f(x): return x**5
df = jax.grad(f)
d2f = jax.grad(df)
d3f = jax.grad(d2f)

print(df(2.0))   # 80
print(d2f(2.0))  # 80
print(d3f(2.0))  # 60 * 4 = 240
```

ML では、**ヘッセ行列 (2階微分の行列)** が最適化の安定性分析や Newton 法で使われます。

---

## 8. 機械学習でのフル活用

### 線形回帰の損失関数の微分

```python
import sympy as sp

w, b, x, y = sp.symbols('w b x y')
loss = (y - (w * x + b))**2

# w で微分 (パラメータ更新の勾配)
print(sp.diff(loss, w))   # -2*x*(-b - w*x + y) = -2x(y - wx - b)

# b で微分
print(sp.diff(loss, b))   # -2*(-b - w*x + y) = -2(y - wx - b)
```

これらを使って **勾配降下法** で w, b を更新する → [`05_optimization/`](../05_optimization/README.md)

---

## 9. ハマりポイント

- **数値差分の誤差**: `h` が小さすぎると浮動小数点誤差で壊れる、大きすぎると近似が荒い → **sweet spot は `h = 1e-5 〜 1e-7`**
- **SymPy は遅い**: 大規模な計算には向かない (確認用)
- **JAX の grad はスカラー出力前提**: ベクトル出力には `jacrev` / `jacfwd` を使う (次の章で)
- **連鎖律の順序を間違えない**: `(g∘f)' = g'(f(x)) · f'(x)`、`g'(x) · f'(x)` ではない

---

## まとめ

| 概念 | 数式 | Python |
|---|---|---|
| 微分の定義 | `lim (f(x+h)-f(x))/h` | (差分計算) |
| 記号微分 | `f'(x)` | `sympy.diff(f, x)` |
| 数値微分 | – | `(f(x+h)-f(x-h))/(2h)` |
| 自動微分 | – | `jax.grad(f)` |
| 連鎖律 | `(g∘f)' = g'(f(x))·f'(x)` | `jax.grad` が自動で適用 |
| 高階微分 | `f''`, `f'''` | `sympy.diff(f,x,n)` / `jax.grad` ネスト |

**この章のキー**: 微分 = ある点での傾き。`jax.grad(f)` で関数を渡すだけ。

---

## 次へ

→ [`03_integrals.md`](03_integrals.md) — 積分: 微分の逆操作、面積・期待値の道具

## 関連
- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX 自動微分の深掘り
- [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 微分を使った最適化

---

## 🔍 ググってみよう

- **チェーンルール (chain rule)** — 誤差逆伝播の心臓部
- **微分演算子** — `D`, `∂` などの記号文化
- **L'Hopital の定理** — `0/0` 形を微分で解く技
- **平均値の定理** — `f'(c) = (f(b)-f(a))/(b-a)` を保証する定理
- **テイラー展開** — 関数を微分から多項式で復元する技
- **自動微分 (autodiff)** — 数値微分でも記号微分でもない第3の道
- **dual number (双対数)** — JAX の forward-mode autodiff の理論的基礎

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`01_limits.md`](01_limits.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`03_integrals.md`](03_integrals.md) |
