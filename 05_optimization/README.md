# 05. 最適化 (Optimization)

**ゴール**: 勾配降下法を中心に、関数の最小値・最大値を求める手法を理解する。
**機械学習の訓練 = 損失関数の最小化** なので、ML を学ぶならここは必須。

## なぜ重要か
- ニューラルネットワークの訓練は**勾配降下法**そのもの
- 損失関数の形状（凸 / 非凸、局所最適）が学習に直結
- 学習率・モーメンタム・Adam などの理解に必要

## 学習ステップ

| ファイル | 内容 | 所要時間 |
|---|---|---|
| `01_basic_concepts.md` | 最小化問題、凸関数 | 1.5時間 |
| `02_gradient_descent.md` | 勾配降下法、学習率、収束 | 2時間 |

## キーとなる Python ツール

```python
import numpy as np
from scipy.optimize import minimize

def f(x: np.ndarray) -> float:
    """目的関数: f(x) = (x[0] - 3)² + (x[1] + 2)²."""
    return (x[0] - 3) ** 2 + (x[1] + 2) ** 2

# 最小化
x0 = np.array([0.0, 0.0])  # 初期値
result = minimize(f, x0)
print(result.x)  # ≈ [3, -2]
```

## 重要な記法

| 記号 | 読み方 | 意味 |
|---|---|---|
| `argmin f(x)` | argmin | f を最小にする x |
| `argmax f(x)` | argmax | f を最大にする x |
| `min f(x)` | min | f の最小値（値） |
| `s.t.` | subject to | 制約付き最適化の条件 |

更新式（勾配降下法）:
```
θ_{t+1} = θ_t − η ∇L(θ_t)
```

| 記号 | 意味 |
|---|---|
| `θ` | パラメータ |
| `η` | 学習率 (learning rate) |
| `∇L` | 損失関数の勾配 |

## ML への接続
- SGD, Momentum, Adam（学習アルゴリズム）
- 学習率スケジューリング
- バッチ正規化、勾配クリッピング
- 凸最適化 → SVM, ロジスティック回帰

## サンプル
- `examples/gradient_descent_demo.py`: 勾配を**手で導出**して降下（標準形式）
- `examples/gradient_descent_demo_jax.py`: `jax.grad` で**自動微分**して降下（JAX形式）

### この章で JAX が効くポイント

複雑な目的関数の勾配を**手で導出する手間が消える**:

```python
# 標準形式: 目的関数が変わるたびに勾配を手で書き直す
def grad_f(p): return np.array([2*(p[0]-3), 2*(p[1]+2)])

# JAX形式: 目的関数だけ書けば勾配は自動
def f(p): return (p[0]-3)**2 + (p[1]+2)**2
grad_f = jax.grad(f)
```

これに `@jit` を付けると更に高速化されるので、現代の研究コードはこちらが標準。
