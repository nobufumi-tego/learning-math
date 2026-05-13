"""JIT と vmap のデモ.

- jit で速度差を体感する
- vmap で「1サンプル関数 → バッチ対応」を体感する
"""
from __future__ import annotations

import time

import jax
import jax.numpy as jnp
import numpy as np


def benchmark(f, x, n_runs: int = 100) -> float:
    """関数の実行時間を計測（ミリ秒）.

    Args:
        f: 計測対象の関数。
        x: 引数。
        n_runs: 試行回数。

    Returns:
        平均実行時間 (ms)。
    """
    # ウォームアップ（JIT コンパイル含む）
    _ = f(x)
    if isinstance(_, jnp.ndarray):
        _.block_until_ready()

    start = time.perf_counter()
    for _ in range(n_runs):
        result = f(x)
        if isinstance(result, jnp.ndarray):
            result.block_until_ready()
    elapsed_ms = (time.perf_counter() - start) / n_runs * 1000
    return elapsed_ms


def jit_speedup_demo() -> None:
    """jit による高速化を確認."""
    print("--- JIT 高速化のデモ ---")

    def heavy_compute(x):
        """繰り返し計算で重い処理を擬似的に作る."""
        y = x
        for _ in range(100):
            y = y * 2.0 + jnp.sin(y)
        return jnp.sum(y)

    heavy_compute_jit = jax.jit(heavy_compute)

    x = jnp.ones(10_000)

    t_no_jit = benchmark(heavy_compute, x, n_runs=20)
    t_jit = benchmark(heavy_compute_jit, x, n_runs=20)

    print(f"JIT なし:  {t_no_jit:.3f} ms / 呼び出し")
    print(f"JIT あり:  {t_jit:.3f} ms / 呼び出し")
    print(f"高速化倍率: {t_no_jit / t_jit:.1f}x")


def vmap_demo() -> None:
    """vmap でバッチ次元を自動追加."""
    print("\n--- vmap デモ ---")

    def predict_one(w: jnp.ndarray, x: jnp.ndarray) -> jnp.ndarray:
        """1サンプルでの線形予測 ŷ = wᵀx.

        Args:
            w: 重み。shape (d,)
            x: 入力。shape (d,)

        Returns:
            予測値 (スカラー)
        """
        return jnp.dot(w, x)

    # === 方法1: 素朴な for ループ ===
    w = jnp.array([0.5, -0.3, 0.2])
    X = jnp.array([[1.0, 2.0, 3.0],
                   [4.0, 5.0, 6.0],
                   [7.0, 8.0, 9.0]])  # shape (3, 3)

    preds_loop = jnp.array([predict_one(w, x_i) for x_i in X])
    print(f"for ループ版:  {preds_loop}")

    # === 方法2: vmap で一発 ===
    predict_batch = jax.vmap(predict_one, in_axes=(None, 0))
    preds_vmap = predict_batch(w, X)
    print(f"vmap 版:       {preds_vmap}")
    print(f"一致:          {jnp.allclose(preds_loop, preds_vmap)}")


def combined_demo() -> None:
    """jit + grad + vmap の合体（ML訓練の骨格）."""
    print("\n--- jit + grad + vmap の合体 ---")

    def loss_one(w, x, y):
        """1サンプルでの二乗誤差."""
        return (jnp.dot(w, x) - y) ** 2

    def batch_loss(w, X, y):
        """バッチ全体での平均損失."""
        losses = jax.vmap(loss_one, in_axes=(None, 0, 0))(w, X, y)
        return jnp.mean(losses)

    # 勾配 + JIT
    fast_grad = jax.jit(jax.grad(batch_loss))

    rng = jax.random.PRNGKey(0)
    rng, k1, k2 = jax.random.split(rng, 3)
    X = jax.random.normal(k1, shape=(100, 5))    # 100サンプル、5特徴
    w_true = jnp.array([1.0, -2.0, 0.5, 3.0, -1.0])
    y = X @ w_true                                 # 正解

    w = jnp.zeros(5)
    grad_val = fast_grad(w, X, y)
    print(f"バッチ全体の勾配 shape: {grad_val.shape}")
    print(f"勾配値: {grad_val}")
    print("→ この勾配で w を更新するだけで学習が回る")


def main() -> None:
    jit_speedup_demo()
    vmap_demo()
    combined_demo()


if __name__ == "__main__":
    main()
