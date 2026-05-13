# 02. 微積分 (Calculus / Analysis)

**ゴール**: 微分・積分、特に**多変数の勾配 (gradient)** を理解する。
機械学習の最適化はすべて勾配の話なので、ML を学ぶなら必須。

## なぜ重要か
- 機械学習の損失関数を**最小化**する = 微分してゼロになる点を探す
- 誤差逆伝播は**連鎖律**（合成関数の微分）の応用
- 期待値・確率密度関数は**積分**で定義される

## 学習ステップ

| ファイル | 内容 | 所要時間 |
|---|---|---|
| `01_limits.md` | 極限 lim、連続性 | 1時間 |
| `02_derivatives.md` | 微分、導関数、連鎖律 | 2時間 |
| `03_integrals.md` | 積分、不定積分・定積分 | 2時間 |
| `04_multivariable.md` | 偏微分、多変数関数 | 2時間 |
| `05_gradient_jacobian.md` | 勾配 ∇f、ヤコビアン、ヘッシアン | 3時間 |

## キーとなる Python ツール

```python
import numpy as np
import sympy as sp

# 記号微分
x = sp.Symbol("x")
f = x**2 + 3*x + 1
df_dx = sp.diff(f, x)                # 2x + 3

# 偏微分（多変数）
x, y = sp.symbols("x y")
g = x**2 + x*y + y**2
print(sp.diff(g, x))                 # ∂g/∂x = 2x + y
print(sp.diff(g, y))                 # ∂g/∂y = x + 2y

# 勾配 ∇g = (∂g/∂x, ∂g/∂y)
grad_g = [sp.diff(g, v) for v in (x, y)]

# 数値微分
def numerical_gradient(f, x: np.ndarray, h: float = 1e-5) -> np.ndarray:
    """前進差分による数値勾配."""
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus = x.copy()
        x_plus[i] += h
        grad[i] = (f(x_plus) - f(x)) / h
    return grad
```

## ML への接続
- 勾配降下法: `θ ← θ − η ∇L(θ)`
- 誤差逆伝播: 連鎖律でレイヤごとの勾配を計算
- 自動微分 (autograd, PyTorch, JAX): 計算グラフを使った効率的な微分

## サンプル
- `examples/derivative_demo.py`: 微分の **記号計算 (SymPy)** と **数値計算 (NumPy)**（標準形式）
- `examples/derivative_demo_jax.py`: 同じ問題を **自動微分 (jax.grad)** で（JAX形式）

### この章で JAX が一番効くポイント

**自動微分** こそ JAX の最大の価値:

```python
# 標準形式: 関数と勾配を別々に書く（手で導出する必要）
def f(x): return x**3 + 2*x**2 + x + 1
def df(x): return 3*x**2 + 4*x + 1   # ← 自分で計算

# JAX形式: 関数だけ書けばよい
def f(x): return x**3 + 2*x**2 + x + 1
df = jax.grad(f)                       # ← 自動
```

複雑な損失関数になればなるほど、JAX のありがたみが増す。
