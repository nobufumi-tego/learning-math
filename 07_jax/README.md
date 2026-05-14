# 07. JAX — 標準Pythonから「自動微分・JIT・vmap」へ

> ⚠️ **未検証の個人学習教材**: 本章は AI 協働で作成され、専門家の監修を受けていません。誤りを含む可能性があるため、必ず一次情報源で検証してください ([詳細](../DISCLAIMER.md))。

**ゴール**: NumPy で書ける人が JAX を使えるようになる。
**到達点**: ニューラルネットワークや拡散モデルの最新論文コードを読めるレベル。

## なぜ JAX を学ぶか

機械学習の最先端実装は、いま **PyTorch / JAX** の2強。
- JAX = 「関数型に書かれた、自動微分とJITが効く NumPy」
- Google DeepMind の研究（Gemini, AlphaFold）、Anthropic、多くのアカデミア論文が JAX

NumPy との対応:

| NumPy | JAX |
|---|---|
| `np.array([1,2,3])` | `jnp.array([1,2,3])` |
| `np.sum(x)` | `jnp.sum(x)` |
| `np.random.normal(...)` | `jax.random.normal(key, ...)` |
| 自分で勾配を導出 | `jax.grad(f)` |
| 速度のため Cython 等 | `@jax.jit` |
| forループ | `jax.vmap(f)` |

## 学習ステップ

| ファイル | 内容 | 所要時間 |
|---|---|---|
| `01_basics.md` | `jax.numpy`, 配列の不変性, PRNGキー | 1時間 |
| `02_autodiff.md` | `grad`, `value_and_grad`, 高階微分 | 1.5時間 |
| `03_jit_vmap.md` | `jit` で高速化, `vmap` でベクトル化 | 1.5時間 |

## キーとなるAPI

```python
import jax
import jax.numpy as jnp

# 1. jax.numpy: NumPyとほぼ同じAPI
x = jnp.array([1.0, 2.0, 3.0])

# 2. 自動微分
def f(x): return jnp.sum(x ** 2)
grad_f = jax.grad(f)
print(grad_f(x))                      # [2, 4, 6]

# 3. 値と勾配を同時に
val, g = jax.value_and_grad(f)(x)

# 4. JIT コンパイル
fast_f = jax.jit(f)

# 5. ベクトル化
batched_f = jax.vmap(f)               # 入力にバッチ次元が増えてもそのまま
```

## JAX の4つのお作法

### (1) 配列は不変 (immutable)
```python
# NumPy
x[0] = 99                # OK

# JAX
x = x.at[0].set(99)      # 新しい配列を返す
```

### (2) 乱数は明示的なキー (PRNGKey)
```python
key = jax.random.PRNGKey(42)
key, subkey = jax.random.split(key)
x = jax.random.normal(subkey, shape=(3,))
```

### (3) 純粋関数を書く
- 引数だけで出力が決まり、副作用がない
- グローバル変数を変更しない、ファイル書き込みしない
- 同じ入力 → 必ず同じ出力

### (4) `jit` の中ではトレース可能な形を書く
- Python の `if` は値依存だと使えない → `jnp.where` や `jax.lax.cond` を使う
- `for` は固定回数なら OK、可変なら `jax.lax.scan` を使う

## ML への接続
- ニューラルネット: Flax / Haiku / Equinox
- 最適化器: Optax
- 確率プログラミング: NumPyro
- 大規模学習: pmap, jax.distributed

## サンプル
- `examples/jax_basics.py`: jax.numpy の基本
- [`examples/grad_demo.py`](examples/grad_demo.py): 自動微分の威力
- [`examples/jit_vmap_demo.py`](examples/jit_vmap_demo.py): JIT と vmap の効果

---

## 📚 さらに学ぶ

- 📕 **[Probabilistic Machine Learning](../appendix/books.md#probabilistic-machine-learning-murphy)** (Murphy) — JAX で実装された最新 ML 教科書、**無料 PDF**
- 🌐 **[JAX 公式ドキュメント](../appendix/online.md#jax-公式)** — `jit`, `grad`, `vmap` の真髄
- 🌐 [Optax 公式](https://optax.readthedocs.io/) — JAX 用最適化ライブラリ
- 🌐 [Flax 公式](https://flax.readthedocs.io/) — JAX 用ニューラルネットライブラリ

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`../06_ml_math_bridge/README.md`](../06_ml_math_bridge/README.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`01_basics.md`](01_basics.md) |
