# 06. 機械学習との橋渡し (ML Math Bridge)

**ゴール**: ここまで学んだ数学（線形代数・微積分・確率・最適化）が、機械学習でどう統合されるかを見る。
**「数学を学ぶ目的地」** として、最後にここに到達することを意識する。

## なぜこの章を作るか
- 個々の数学を学んでも、「これが何の役に立つの？」が見えないと続かない
- 機械学習の論文・コードを読み解くには、複数分野の知識を**同時に**使う必要がある
- AI への指示・生成された数式コードを理解するには、全体像が要る

## 学習ステップ

| ファイル | 内容 | 前提 |
|---|---|---|
| `01_loss_functions.md` | 損失関数（MSE, クロスエントロピー） | 02, 03 |
| `02_backprop.md` | 誤差逆伝播（連鎖律の応用） | 01, 02 |

## 損失関数の数学的構造

### 平均二乗誤差 (MSE)
```
L(θ) = (1/n) Σᵢ (yᵢ − f(xᵢ; θ))²
```
- `Σ` (00章) と `(...)²` (02章の微分対象) の組合せ
- 連続値の回帰問題で使う

### クロスエントロピー
```
L(θ) = − Σᵢ yᵢ log p(xᵢ; θ)
```
- 確率分布の対数 (03章) を使う
- 分類問題で使う
- 最尤推定の対数尤度関数と同じもの

### Python 実装

```python
import numpy as np

def mse_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """平均二乗誤差.

    Args:
        y_true: 真の値。shape: (n,)
        y_pred: 予測値。shape: (n,)
    """
    return float(np.mean((y_true - y_pred) ** 2))


def cross_entropy_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """クロスエントロピー損失.

    Args:
        y_true: ワンホット表現の真のラベル。shape: (n, k)
        y_pred: 予測確率（softmax 出力）。shape: (n, k)
    """
    EPSILON = 1e-12  # log(0) を避けるための数値安定化
    return float(-np.mean(np.sum(y_true * np.log(y_pred + EPSILON), axis=1)))
```

## 誤差逆伝播 (Backpropagation)

連鎖律 (chain rule) を多層のニューラルネットに適用したもの。

### 連鎖律のおさらい
```
y = f(g(x))
dy/dx = (df/dg)(dg/dx)
```

### ニューラルネット1層の場合
```
入力:    x ∈ ℝⁿ
線形変換: z = W x + b      (Wは行列、bはバイアス)
活性化:   a = σ(z)         (σは活性化関数)
損失:     L = L(a, y)
```

各パラメータの勾配:
```
∂L/∂W = (∂L/∂a)(∂a/∂z)(∂z/∂W)
```

## サンプル
- `examples/loss_and_gradient.py`: 線形回帰 + クロスエントロピー（**標準形式 / 勾配は手で導出**）
- `examples/loss_and_gradient_jax.py`: 同じ問題を **JAX + jax.value_and_grad + jit** で（**JAX形式 / 自動微分**）

### この章で JAX が真価を発揮するポイント

これまで手で書いていた:
```python
# 標準形式: 線形回帰の勾配を手で導出
grad_w = (2.0 / n) * X.T @ (X @ w + b - y)
grad_b = (2.0 / n) * np.sum(X @ w + b - y)
```

JAX 形式では:
```python
# 損失関数を書くだけ
def mse_loss(params, X, y):
    y_pred = X @ params["w"] + params["b"]
    return jnp.mean((y - y_pred) ** 2)

# 勾配は自動で取得
loss_val, grads = jax.value_and_grad(mse_loss)(params, X, y)
```

ニューラルネットワークのように損失関数が深くなる程、この差は圧倒的になる。
ここで「JAX に行くか」「PyTorch に行くか」の分岐点。本リポジトリは JAX を採用。

## 学習を終えた後
ここまで来たら、以下に挑戦するとよい:
- 線形回帰を NumPy だけで実装
- 単純なニューラルネットを NumPy で実装（PyTorch/JAXに頼らず）
- 論文の1段落を読んで、出てくる数式に対応する Python コードを書く
