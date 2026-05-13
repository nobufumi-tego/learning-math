"""勾配降下法 (Gradient Descent) のデモ.

更新式: θ ← θ − η ∇L(θ)
"""
from __future__ import annotations

from typing import Callable

import numpy as np


LEARNING_RATE: float = 0.1  # η: 学習率
N_ITERATIONS: int = 50      # 反復回数
CONVERGENCE_THRESHOLD: float = 1e-6  # 収束判定の閾値


def gradient_descent(
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    learning_rate: float = LEARNING_RATE,
    n_iterations: int = N_ITERATIONS,
) -> tuple[np.ndarray, list[np.ndarray]]:
    """勾配降下法で最小値を探す.

    Args:
        grad_f: 勾配 ∇f を返す関数。
        x0: 初期点。shape: (d,)
        learning_rate: 学習率 η。
        n_iterations: 反復回数。

    Returns:
        (最終点, 軌跡のリスト)
    """
    x = x0.copy()
    history: list[np.ndarray] = [x.copy()]

    for _ in range(n_iterations):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        history.append(x_new.copy())

        # 収束判定
        if np.linalg.norm(x_new - x) < CONVERGENCE_THRESHOLD:
            break
        x = x_new

    return x, history


def demo_1d() -> None:
    """1次元: f(x) = (x − 3)² の最小値を探す.

    解析解: x* = 3, f(x*) = 0
    """
    print("--- 1次元: f(x) = (x − 3)² ---")

    def grad_f(x: np.ndarray) -> np.ndarray:
        """∇f = 2(x − 3)."""
        return 2 * (x - 3)

    x0 = np.array([0.0])
    x_star, history = gradient_descent(grad_f, x0)
    print(f"初期値: {x0}")
    print(f"収束先: {x_star}  （理論値: [3]）")
    print(f"反復回数: {len(history) - 1}")


def demo_2d() -> None:
    """2次元: f(x, y) = (x − 3)² + (y + 2)² の最小値を探す.

    解析解: (x*, y*) = (3, −2), f(x*, y*) = 0
    """
    print("\n--- 2次元: f(x, y) = (x − 3)² + (y + 2)² ---")

    def grad_f(p: np.ndarray) -> np.ndarray:
        """∇f = (2(x − 3), 2(y + 2)).

        Args:
            p: shape (2,)

        Returns:
            勾配。shape (2,)
        """
        return np.array([2 * (p[0] - 3), 2 * (p[1] + 2)])

    x0 = np.array([0.0, 0.0])
    x_star, history = gradient_descent(grad_f, x0)
    print(f"初期値: {x0}")
    print(f"収束先: {x_star}  （理論値: [3, −2]）")
    print(f"反復回数: {len(history) - 1}")


def main() -> None:
    demo_1d()
    demo_2d()


if __name__ == "__main__":
    main()
