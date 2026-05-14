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
> - [`00_notation/04_function_notation.md`](../00_notation/04_function_notation.md) — $f(x)$ の記法

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

$f(x)$ の微分 (導関数) はいくつかの書き方があります:

| 記号 | 読み方 | 場面 |
|---|---|---|
| $f'(x)$ | "f prime of x" | 1変数で簡潔 |
| $\dfrac{df}{dx}$ | "dee-f dee-x" | ライプニッツ記法。物理・工学で頻出 |
| $Df$ | "D of f" | 演算子記法 |
| $\dfrac{\partial f}{\partial x}$ | "partial f partial x" | **多変数の場合** (偏微分、04章) |

定義式:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

意味: 「**$x$ から少し進んだときの $y$ の変化を、$x$ の変化で割った値**」 を、$h$ を $0$ に近づけた極限。
**「傾き」** そのものです。

---

## 3. 直感: 「割線」が「接線」になる

$\dfrac{f(x+h) - f(x)}{h}$ は **割線 (secant line)** の傾き。
$h \to 0$ にすると、割線は **接線 (tangent line)** になります。
これがその点の「**真の傾き**」 = **微分**。

---

## 4. 主要な公式 (覚えるべきもの)

| $f(x)$ | $f'(x)$ | 覚え方 |
|---|---|---|
| $c$ (定数) | $0$ | 平らな線、傾きゼロ |
| $x^n$ | $n \cdot x^{n-1}$ | べき乗ルール (一番重要!) |
| $e^x$ | $e^x$ | 自分自身が微分! ($e$ の特権) |
| $\ln x$ | $\dfrac{1}{x}$ | 対数の微分 |
| $\sin x$ | $\cos x$ | sin と cos のペア |
| $\cos x$ | $-\sin x$ | (符号反転) |

例:
- $f(x) = x^3 \implies f'(x) = 3x^2$
- $f(x) = 5x^4 \implies f'(x) = 20x^3$
- $f(x) = \dfrac{1}{x} = x^{-1} \implies f'(x) = -x^{-2} = -\dfrac{1}{x^2}$

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

SymPy は **「数式そのもの」** を扱うので、結果も数式で返してくれます:

$$
f(x) = x^3 + 2x^2 - 5x + 7 \implies f'(x) = 3x^2 + 4x - 5
$$

### 標準形式 2: 数値微分 (中央差分)

中央差分の定義:

$$
f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
$$

```python
import numpy as np

def f(x: float) -> float:
    return x**3 + 2*x**2 - 5*x + 7

def df_numeric(f, x: float, h: float = 1e-5) -> float:
    """中央差分 (誤差 O(h²) で前進差分より高精度)."""
    return (f(x + h) - f(x - h)) / (2 * h)

print(df_numeric(f, 2.0))   # 14.999... (≈ 15)
```

> 💡 **前進差分 vs 中央差分**: 前進差分 $\dfrac{f(x+h)-f(x)}{h}$ は誤差 $O(h)$、中央差分は $O(h^2)$。**勾配確認には中央差分を使う**のがプロの作法。

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

$$
(g \circ f)'(x) = g'(f(x)) \cdot f'(x)
$$

訳: 「**外の関数の微分** $\times$ **中の関数の微分**」。

### 例

$y = \sin(x^2)$ を微分したい。
- 外の関数: $g(u) = \sin(u)$、$g'(u) = \cos(u)$
- 内の関数: $f(x) = x^2$、$f'(x) = 2x$

連鎖律で:

$$
\frac{dy}{dx} = \cos(x^2) \cdot 2x = 2x \cos(x^2)
$$

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

ニューラルネットの 3 層構造を考えると:

$$
\text{入力} \; x \to \text{層1} \to \text{層2} \to \text{層3} \to \text{損失} \; L
$$

**「$L$ を入力 $x$ で微分したい」** ときは、連鎖律で**層を逆順に辿る**:

$$
\frac{\partial L}{\partial x}
= \frac{\partial L}{\partial h_3} \cdot \frac{\partial h_3}{\partial h_2} \cdot \frac{\partial h_2}{\partial h_1} \cdot \frac{\partial h_1}{\partial x}
$$

これが **誤差逆伝播法 (backpropagation)** の正体。
詳しくは → [`06_ml_math_bridge/02_backprop.md`](../06_ml_math_bridge/02_backprop.md)

---

## 7. 高階微分

微分を **何度も繰り返す** こともできます:

| 記号 | 意味 |
|---|---|
| $f''(x)$ または $\dfrac{d^2 f}{dx^2}$ | 2 階微分 (微分の微分) |
| $f'''(x)$ | 3 階微分 |
| $f^{(n)}(x)$ | $n$ 階微分 |

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

線形回帰: $\hat{y} = wx + b$、損失: $L(w, b) = (y - \hat{y})^2$

$$
\frac{\partial L}{\partial w} = -2x(y - wx - b)
$$

$$
\frac{\partial L}{\partial b} = -2(y - wx - b)
$$

```python
import sympy as sp

w, b, x, y = sp.symbols('w b x y')
loss = (y - (w * x + b))**2

print(sp.diff(loss, w))   # ← 上の式と一致
print(sp.diff(loss, b))
```

これらを使って **勾配降下法** で $w, b$ を更新する → [`05_optimization/`](../05_optimization/README.md)

---

## 9. ハマりポイント

- **数値差分の誤差**: $h$ が小さすぎると浮動小数点誤差で壊れる、大きすぎると近似が荒い → **sweet spot は $h = 10^{-5} \sim 10^{-7}$**
- **SymPy は遅い**: 大規模な計算には向かない (確認用)
- **JAX の grad はスカラー出力前提**: ベクトル出力には `jacrev` / `jacfwd` を使う (次の章で)
- **連鎖律の順序を間違えない**: $(g \circ f)' = g'(f(x)) \cdot f'(x)$、$g'(x) \cdot f'(x)$ ではない

---

## まとめ

| 概念 | 数式 | Python |
|---|---|---|
| 微分の定義 | $\lim_{h\to 0} \dfrac{f(x+h)-f(x)}{h}$ | (差分計算) |
| 記号微分 | $f'(x)$ | `sympy.diff(f, x)` |
| 数値微分 | $\dfrac{f(x+h)-f(x-h)}{2h}$ | (実装) |
| 自動微分 | – | `jax.grad(f)` |
| 連鎖律 | $(g \circ f)' = g'(f(x)) \cdot f'(x)$ | `jax.grad` が自動適用 |
| 高階微分 | $f''$, $f'''$ | `sympy.diff(f,x,n)` / `jax.grad` ネスト |

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
- **微分演算子** — $D$, $\partial$ などの記号文化
- **L'Hôpital の定理** — $\frac{0}{0}$ 形を微分で解く技
- **平均値の定理** — $f'(c) = \frac{f(b)-f(a)}{b-a}$ を保証する定理
- **テイラー展開** — 関数を微分から多項式で復元する技
- **自動微分 (autodiff)** — 数値微分でも記号微分でもない第3の道
- **dual number (双対数)** — JAX の forward-mode autodiff の理論的基礎

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`01_limits.md`](01_limits.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`03_integrals.md`](03_integrals.md) |
