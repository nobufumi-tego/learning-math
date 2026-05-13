# 03. `jit` で高速化、`vmap` でベクトル化

JAX の3大変換 (`grad`, `jit`, `vmap`) のうち、残り2つを扱う。

## `jit`: JITコンパイルで爆速に

`@jax.jit` を関数につけるだけで、初回呼び出し時に XLA でコンパイルされ、2回目以降は機械語レベルで高速実行される。

```python
import jax
import jax.numpy as jnp

def slow_f(x):
    """素朴な実装."""
    y = x
    for _ in range(100):
        y = y * 2 + jnp.sin(y)
    return jnp.sum(y)

@jax.jit
def fast_f(x):
    """JIT版 (中身は同じ)."""
    y = x
    for _ in range(100):
        y = y * 2 + jnp.sin(y)
    return jnp.sum(y)

x = jnp.ones(1000)

# 初回は JIT コンパイルがかかるので遅い
_ = fast_f(x).block_until_ready()

# 2回目以降は爆速
%timeit slow_f(x).block_until_ready()    # 例: 8ms
%timeit fast_f(x).block_until_ready()    # 例: 0.1ms  ← 80倍速い
```

### `jit` のお作法

#### (1) 形状 (shape) が同じ呼び出しのみキャッシュが効く
```python
fast_f(jnp.zeros(100))   # shape (100,) でコンパイル
fast_f(jnp.zeros(200))   # shape (200,) で再コンパイル
```

#### (2) `if` の中身が値依存だと使えない
```python
@jax.jit
def bad(x):
    if x > 0:        # ❌ x はトレース時の "抽象値" なので比較できない
        return x
    else:
        return -x

@jax.jit
def good(x):
    return jnp.where(x > 0, x, -x)   # ✅ jnp.where を使う
```

#### (3) 副作用は書かない
- `print` は OK（トレース時に1回だけ実行される）
- ファイル書き込み・グローバル変数変更はやらない

### `static_argnums`: 値依存の引数を許す
```python
@functools.partial(jax.jit, static_argnums=(1,))
def f(x, n):
    """n は Python int として固定値扱い、x はトレースされる."""
    return x ** n
```

## `vmap`: バッチ次元を自動で追加

「1サンプルに対する処理」を書くと、`vmap` でバッチ処理に変換できる。
明示的な for ループ・reshape が不要になる。

### 例: 1サンプル用の関数 → バッチ対応

```python
import jax
import jax.numpy as jnp

def loss_one(w, x, y):
    """1サンプルの平均二乗誤差.
    
    w: shape (d,)
    x: shape (d,)
    y: scalar
    """
    y_pred = jnp.dot(w, x)
    return (y_pred - y) ** 2

# バッチ対応版を自動生成
# in_axes=(None, 0, 0): w はバッチしない、x と y は0軸でバッチ
batched_loss = jax.vmap(loss_one, in_axes=(None, 0, 0))

w = jnp.array([0.5, -0.3])               # shape (2,)
X = jnp.array([[1.0, 2.0], [3.0, 4.0]])  # shape (2, 2): バッチサイズ2
y = jnp.array([1.0, 2.0])                # shape (2,)

losses = batched_loss(w, X, y)           # shape (2,)
print(losses)  # 各サンプルの損失
```

### `in_axes` の意味

| 値 | 意味 |
|---|---|
| `0` | この引数の 0 軸目をバッチ次元として展開 |
| `1`, `2`, ... | 指定軸をバッチ次元として展開 |
| `None` | この引数はバッチしない（全サンプルで共通） |

### `out_axes` で出力の軸も指定可
通常は `0`（出力の0軸目にバッチ次元が来る）でOK。

## `grad` + `jit` + `vmap` の合体

JAXの真価。3つの変換を**任意の順で**組み合わせられる。

```python
# 1. 1サンプル損失関数
def loss(w, x, y):
    return (jnp.dot(w, x) - y) ** 2

# 2. バッチ全体での平均損失
def batch_loss(w, X, y):
    losses = jax.vmap(loss, in_axes=(None, 0, 0))(w, X, y)
    return jnp.mean(losses)

# 3. 勾配を計算する関数
grad_fn = jax.grad(batch_loss)

# 4. JITで高速化
fast_grad_fn = jax.jit(grad_fn)

# これで「バッチ全体の損失に対する w の勾配」が
# 高速・自動微分・ベクトル化された形で手に入る
```

これが現代の ML 訓練コードの骨格。

## まとめ

| 変換 | 役割 |
|---|---|
| `jax.grad` | 自動微分（勾配計算） |
| `jax.jit` | JITコンパイルによる高速化 |
| `jax.vmap` | バッチ次元の自動追加（ベクトル化） |
| `jax.pmap` | 複数デバイス（GPU/TPU）への分散 |

これら4つで、現代の機械学習研究コードの大部分が書ける。

## サンプル
- [`examples/jit_vmap_demo.py`](examples/jit_vmap_demo.py) で実際の速度差を体感できる

---

## 📍 ナビゲーション

| ← 前 | 🏠 目次 | 次の章 → |
|---|---|---|
| [`02_autodiff.md`](02_autodiff.md) | [章 TOP](README.md) | [`../04_discrete_math/README.md`](../04_discrete_math/README.md) |

🎉 JAX 章卒業！残るは離散数学のみ (補助章)。
