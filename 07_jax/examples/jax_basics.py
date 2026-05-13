"""JAX 基本: jax.numpy・配列の不変性・PRNGキー.

NumPy と JAX を併記して、対応関係を体感する。
"""
from __future__ import annotations

import jax
import jax.numpy as jnp
import numpy as np


def section_array_basics() -> None:
    """配列作成と基本演算: NumPy と JAX で同じ感覚."""
    print("--- 配列の基本（NumPy / JAX） ---")

    # NumPy
    x_np: np.ndarray = np.array([1.0, 2.0, 3.0])  # shape: (3,)
    y_np = np.sum(x_np ** 2)
    print(f"NumPy:  x = {x_np},  Σx² = {y_np}")

    # JAX
    x_jax: jnp.ndarray = jnp.array([1.0, 2.0, 3.0])  # shape: (3,)
    y_jax = jnp.sum(x_jax ** 2)
    print(f"JAX:    x = {x_jax},  Σx² = {y_jax}")

    # 検算: 値は一致
    print(f"検算 NumPy ≈ JAX:  {np.isclose(float(y_np), float(y_jax))}")


def section_immutability() -> None:
    """配列の不変性: NumPy では x[0]=v、JAX では x.at[0].set(v)."""
    print("\n--- 配列の不変性 ---")

    # NumPy: 直接代入で更新できる
    x_np = np.array([1, 2, 3])
    x_np[0] = 99
    print(f"NumPy (代入で更新): {x_np}")

    # JAX: 新しい配列を返す
    x_jax = jnp.array([1, 2, 3])
    x_jax2 = x_jax.at[0].set(99)
    print(f"JAX (.at[0].set):   元={x_jax}, 新={x_jax2}")
    # 元の配列は変わらない（重要）


def section_prng() -> None:
    """乱数: グローバル状態 vs 明示的キー."""
    print("\n--- 乱数生成 ---")

    # NumPy
    rng = np.random.default_rng(seed=42)
    x_np = rng.normal(size=(3,))
    y_np = rng.normal(size=(3,))   # 別の乱数（rngの内部状態が進む）
    print(f"NumPy x: {x_np}")
    print(f"NumPy y: {y_np}")

    # JAX
    key = jax.random.PRNGKey(42)

    # 注意: 同じキーを使い回すと同じ乱数が返る
    same1 = jax.random.normal(key, shape=(3,))
    same2 = jax.random.normal(key, shape=(3,))
    print(f"JAX (同じキー): {same1} == {same2}  → {jnp.allclose(same1, same2)}")

    # 正しいやり方: split でキーを分割
    key, sub1 = jax.random.split(key)
    x_jax = jax.random.normal(sub1, shape=(3,))
    key, sub2 = jax.random.split(key)
    y_jax = jax.random.normal(sub2, shape=(3,))
    print(f"JAX x: {x_jax}")
    print(f"JAX y: {y_jax}")
    print(f"x と y は異なる:  {not jnp.allclose(x_jax, y_jax)}")


def section_practice_answer() -> None:
    """01_basics.md の練習問題の答え合わせ.

    1. shape (5,) の正規乱数ベクトル x を作る
    2. 最大要素を 0 に置き換える
    3. 二乗和を計算
    """
    print("\n--- 練習問題の答え合わせ ---")

    # === 標準形式 (NumPy) ===
    rng = np.random.default_rng(seed=0)
    x_np: np.ndarray = rng.normal(size=(5,))     # shape: (5,)
    idx_np = int(np.argmax(x_np))
    x_np[idx_np] = 0                              # 直接書き換え
    result_np = float(np.sum(x_np ** 2))
    print(f"NumPy: 結果 = {result_np:.4f}")

    # === JAX形式 ===
    key = jax.random.PRNGKey(0)
    x_jax = jax.random.normal(key, shape=(5,))   # shape: (5,)
    idx_jax = jnp.argmax(x_jax)
    x_jax = x_jax.at[idx_jax].set(0.0)            # .at[i].set() で更新
    result_jax = float(jnp.sum(x_jax ** 2))
    print(f"JAX:   結果 = {result_jax:.4f}")
    # 注: NumPy と JAX は乱数生成器が違うので値そのものは一致しない


def main() -> None:
    section_array_basics()
    section_immutability()
    section_prng()
    section_practice_answer()


if __name__ == "__main__":
    main()
