"""勾配降下法 (JAX版).

標準版 `gradient_descent_demo.py` では、勾配 ∇f を **手で導出** していた。
JAX版では `jax.grad` で自動導出する。

→ 「目的関数を書くだけで最適化が回る」が体感できる。
"""
from __future__ import annotations

from typing import Callable

import jax
import jax.numpy as jnp
import numpy as np


LEARNING_RATE: float = 0.1
N_ITERATIONS: int = 50
CONVERGENCE_THRESHOLD: float = 1e-6


def gradient_descent_jax(
    f: Callable[[jnp.ndarray], jnp.ndarray],
    x0: jnp.ndarray,
    learning_rate: float = LEARNING_RATE,
    n_iterations: int = N_ITERATIONS,
) -> tuple[jnp.ndarray, list[np.ndarray]]:
    """JAX 版勾配降下法.

    引数として目的関数 f を取り、勾配は jax.grad で自動導出する。

    Args:
        f: 目的関数。スカラーを返す純粋関数。
        x0: 初期点。
        learning_rate: 学習率 η。
        n_iterations: 反復回数。

    Returns:
        (最終点, 軌跡のリスト)
    """
    grad_f = jax.jit(jax.grad(f))  # 勾配計算をJITで高速化

    x = x0
    history: list[np.ndarray] = [np.array(x)]

    for _ in range(n_iterations):
        g = grad_f(x)
        x_new = x - learning_rate * g
        history.append(np.array(x_new))

        if jnp.linalg.norm(x_new - x) < CONVERGENCE_THRESHOLD:
            break
        x = x_new

    return x, history


def demo_1d() -> None:
    """1次元: f(x) = (x − 3)²."""
    print("--- 1次元: f(x) = (x − 3)² ---")

    def f(x):
        return (x[0] - 3) ** 2  # スカラーを返す

    x0 = jnp.array([0.0])
    x_star, history = gradient_descent_jax(f, x0)

    print(f"初期値: {np.array(x0)}")
    print(f"収束先: {np.array(x_star)}  （理論値: [3]）")
    print(f"反復: {len(history) - 1}")


def demo_2d() -> None:
    """2次元: f(x, y) = (x − 3)² + (y + 2)²."""
    print("\n--- 2次元: f(x, y) = (x − 3)² + (y + 2)² ---")

    def f(p):
        return (p[0] - 3) ** 2 + (p[1] + 2) ** 2

    x0 = jnp.array([0.0, 0.0])
    x_star, history = gradient_descent_jax(f, x0)

    print(f"初期値: {np.array(x0)}")
    print(f"収束先: {np.array(x_star)}  （理論値: [3, −2]）")
    print(f"反復: {len(history) - 1}")


def demo_complicated_function() -> None:
    """複雑な関数: 手で勾配を導出すると面倒な例.

    f(x, y, z) = sin(x) + cos(y) + exp(z/10) + (x*y*z)²
    """
    print("\n--- 複雑な関数（自動微分の威力） ---")

    def f(p):
        return (
            jnp.sin(p[0])
            + jnp.cos(p[1])
            + jnp.exp(p[2] / 10.0)
            + (p[0] * p[1] * p[2]) ** 2
        )

    x0 = jnp.array([1.0, 1.0, 1.0])
    x_star, history = gradient_descent_jax(f, x0, learning_rate=0.01, n_iterations=200)

    print(f"初期値: {np.array(x0)}")
    print(f"f(初期値) = {float(f(x0)):.4f}")
    print(f"収束先:   {np.array(x_star)}")
    print(f"f(収束先) = {float(f(x_star)):.4f}")
    print("→ 標準版なら勾配を手で導出する必要があるが、JAXは関数を渡すだけ")


def main() -> None:
    demo_1d()
    demo_2d()
    demo_complicated_function()


if __name__ == "__main__":
    main()
