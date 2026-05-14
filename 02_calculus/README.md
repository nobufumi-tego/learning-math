# 02. 微積分 (Calculus / Analysis)

**ゴール**: 微分・積分、特に**多変数の勾配 (gradient)** を理解する。
機械学習の最適化はすべて勾配の話なので、ML を学ぶなら必須。

## なぜ重要か
- 機械学習の損失関数を**最小化**する = 微分してゼロになる点を探す
- 誤差逆伝播は**連鎖律**（合成関数の微分）の応用
- 期待値・確率密度関数は**積分**で定義される

---

## 💡 動かす前に

このフォルダのコードは **Jupyter Lab** で対話的に動かすのが推奨です。

```bash
uv run lab.py
```

ブラウザが開いたら、左のファイルツリーから `02_calculus/notebooks/` を開いて、`01_limits.ipynb` から順に。

> 🐧 **「`uv` ってなに?」「ターミナルがわからない」方** は、まず以下を:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎
> - 特に [`08_uv_keeps_pet_healthy.md`](../start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) — uv の使い方
>
> **数学に苦手意識のある方** は:
> - [`start_here/`](../start_here/README.md) — 数式ゼロから始める数学
> - [`00_notation/`](../00_notation/README.md) — 数学記号の読み解き

---

## 学習ステップ

| md (解説) | ipynb (動かす) | 内容 | 所要時間 |
|---|---|---|---|
| [`01_limits.md`](01_limits.md) | [`notebooks/01_limits.ipynb`](notebooks/01_limits.ipynb) | 極限、連続性、e の定義 | 1時間 |
| [`02_derivatives.md`](02_derivatives.md) | [`notebooks/02_derivatives.ipynb`](notebooks/02_derivatives.ipynb) | 微分、3 形式 (SymPy/数値/JAX)、連鎖律 | 2時間 |
| [`03_integrals.md`](03_integrals.md) | [`notebooks/03_integrals.ipynb`](notebooks/03_integrals.ipynb) | 積分、リーマン和、期待値との関係 | 2時間 |
| [`04_multivariable.md`](04_multivariable.md) | [`notebooks/04_multivariable.ipynb`](notebooks/04_multivariable.ipynb) | 多変数関数、偏微分、勾配ベクトル | 2時間 |
| [`05_gradient_jacobian.md`](05_gradient_jacobian.md) | [`notebooks/05_gradient_jacobian.ipynb`](notebooks/05_gradient_jacobian.ipynb) | ∇f, Jf, Hf — ML微分の総合編 | 3時間 |

各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進めるのが効果的**です。

## キーとなる Python ツール

```python
import sympy as sp
import jax

# 記号微分 (厳密)
x = sp.Symbol('x')
df_dx = sp.diff(x**2, x)       # 2x

# 数値微分 (中央差分)
def df_central(f, x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)

# JAX 自動微分 (本命)
df = jax.grad(lambda x: x**2)
print(df(3.0))                 # 6.0

# 多変数の勾配
grad_f = jax.grad(lambda p: p[0]**2 + p[1]**2)

# ヤコビアン
J = jax.jacrev(lambda p: jnp.array([p[0]+p[1], p[0]*p[1]]))

# ヘッシアン
H = jax.hessian(lambda p: p[0]**2 + p[1]**2)
```

## ML への接続
- 勾配降下法: `θ ← θ − η ∇L(θ)`
- 誤差逆伝播: 連鎖律でレイヤごとの勾配を計算
- 自動微分 (autograd, PyTorch, JAX): 計算グラフを使った効率的な微分
- ニュートン法: ヘッシアンを使う2次最適化

## CLI 実行用サンプル (Jupyter を使わない場合)

`uv run python` で直接実行できる .py ファイルも置いてあります:
- [`examples/derivative_demo.py`](examples/derivative_demo.py) — 標準形式 (SymPy/数値)
- [`examples/derivative_demo_jax.py`](examples/derivative_demo_jax.py) — JAX 形式 (`jax.grad`)

```bash
uv run python 02_calculus/examples/derivative_demo.py
```

### この章で JAX が一番効く場面

**自動微分** こそ JAX の最大の価値:

```python
# 標準形式: 関数と勾配を別々に書く
def f(x): return x**3 + 2*x**2 + x + 1
def df(x): return 3*x**2 + 4*x + 1   # ← 自分で計算

# JAX形式: 関数だけ書けばよい
def f(x): return x**3 + 2*x**2 + x + 1
df = jax.grad(f)                       # ← 自動
```

複雑な損失関数になればなるほど、JAX のありがたみが増す。

---

## 📚 さらに学ぶ

- 📕 **[やさしく学べる微分積分](../appendix/books.md#やさしく学べる微分積分)** (石村園子) — 計算重視の入門
- 📕 **[微分積分学](../appendix/books.md#微分積分学-高木貞治)** (高木貞治) — 100 年読まれる古典
- 🌐 **[3Blue1Brown: Essence of Calculus](../appendix/online.md#3blue1brown)** — 微積分の直感を動画で
- 🌐 **[ヨビノリたくみ](../appendix/online.md#ヨビノリたくみ)** — 大学微積分を日本語で

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`../01_linear_algebra/04_decompositions.md`](../01_linear_algebra/04_decompositions.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`01_limits.md`](01_limits.md) |
