# 01. JAX 基本 — `jax.numpy` と配列の不変性、PRNGキー

NumPy ユーザーが最初に違和感を覚える 3 つのポイントを押さえる。

## 1. `jax.numpy` は NumPy の APIと同じ感覚

```python
import numpy as np
import jax.numpy as jnp

# ほぼ同じ
np.array([1, 2, 3])         # NumPy
jnp.array([1, 2, 3])        # JAX

np.sum(x)                   ;  jnp.sum(x)
np.mean(x)                  ;  jnp.mean(x)
np.dot(a, b)                ;  jnp.dot(a, b)
a @ b                       ;  a @ b  # 行列積も同じ
```

### 違うところ
- 配列はデフォルトで **float32**（NumPy は float64）
  - `jax.config.update("jax_enable_x64", True)` で 64bit を有効化可
- デバイスが GPU/TPU なら自動で使う
- 演算は遅延評価される（実際に値が必要なときに実行）

## 2. 配列は不変 (immutable)

NumPy では普通の代入が、JAX ではエラーになる。

```python
# NumPy
import numpy as np
x = np.array([1, 2, 3])
x[0] = 99
print(x)   # [99, 2, 3]   ← OK

# JAX
import jax.numpy as jnp
x = jnp.array([1, 2, 3])
x[0] = 99    # TypeError: '<class 'jaxlib.xla_extension.ArrayImpl'>' object does not support item assignment
```

### 解決: `.at[...]`構文（新しい配列を返す）

```python
x = jnp.array([1, 2, 3])

x2 = x.at[0].set(99)       # 0番目を99に
print(x2)                  # [99, 2, 3]
print(x)                   # [1, 2, 3] ← 元は変わらない（重要）

# 他の更新操作
x.at[0].add(10)            # 加算
x.at[0].multiply(2)        # 乗算
x.at[1:3].set(0)           # スライスで設定
```

### なぜ不変か
- 自動微分のために計算履歴を追える必要がある
- JIT コンパイルが副作用を嫌う
- 関数型プログラミング・並列化に有利

## 3. 乱数は明示的な PRNGキー

NumPy のグローバル状態 `np.random.seed(42)` のような暗黙のシード管理はしない。

```python
# NumPy
import numpy as np
rng = np.random.default_rng(seed=42)
x = rng.normal(size=(3,))
y = rng.normal(size=(3,))   # 同じ rng を使い回し → 別の乱数

# JAX
import jax
key = jax.random.PRNGKey(42)

# 同じキーを使うと同じ乱数が返る（再現性のため）
x = jax.random.normal(key, shape=(3,))
y = jax.random.normal(key, shape=(3,))
# x と y は同じ ← 普通これは欲しくない

# 正しいやり方: 毎回キーを分割 (split)
key, sub1 = jax.random.split(key)
x = jax.random.normal(sub1, shape=(3,))

key, sub2 = jax.random.split(key)
y = jax.random.normal(sub2, shape=(3,))    # x と異なる
```

### split を使う理由
- すべての乱数発生点で「どのキーを使ったか」が明示的に追える
- 並列化・分散学習時に乱数の衝突がない
- 完全再現可能（実験のリプロダクションに重要）

### キー使い回しの典型パターン

```python
key = jax.random.PRNGKey(0)
keys = jax.random.split(key, num=10)   # 10個のキーを一気に作る
# keys[0], keys[1], ... を各箇所で使う
```

## まとめ

| やりたいこと | NumPy | JAX |
|---|---|---|
| 配列を作る | `np.array(...)` | `jnp.array(...)` |
| 配列要素を更新 | `x[i] = v` | `x = x.at[i].set(v)` |
| 乱数を取る | `rng.normal(...)` | `jax.random.normal(key, ...)` |
| シード設定 | `np.random.seed(42)` | `jax.random.PRNGKey(42)` |

## 練習

```python
# 演習: 以下を NumPy と JAX の両方で実装し、結果が一致することを確認
# 1. shape (5,) の正規乱数ベクトル x を作る
# 2. その最大要素を 0 に置き換える
# 3. 二乗和を計算
```

`examples/jax_basics.py` で答え合わせができる。
