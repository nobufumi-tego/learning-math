"""JAX 自動微分のデモ.

「手で勾配を導出」と「jax.grad で自動」を併記し、一致を検証する。
"""
from __future__ import annotations

import jax
import jax.numpy as jnp
import numpy as np


def scalar_function_demo() -> None:
    """1変数: f(x) = x³ + 2x² + x + 1, f'(x) = 3x² + 4x + 1."""
    print("--- 1変数の微分 ---")

    # 標準形式: 手で導出した勾配
    def f_np(x: float) -> float:
        return x**3 + 2 * x**2 + x + 1

    def df_np(x: float) -> float:
        """手で導出: f'(x) = 3x² + 4x + 1."""
        return 3 * x**2 + 4 * x + 1

    # JAX形式: 自動微分
    def f_jax(x):
        return x**3 + 2 * x**2 + x + 1

    df_jax = jax.grad(f_jax)

    x0 = 2.0
    print(f"f(2)              = {f_np(x0)}")
    print(f"f'(2) 手動        = {df_np(x0)}")
    print(f"f'(2) jax.grad    = {df_jax(x0)}")
    print(f"一致              → {np.isclose(df_np(x0), float(df_jax(x0)))}")


def vector_function_demo() -> None:
    """多変数: g(x,y) = x² + xy + y², ∇g = (2x+y, x+2y)."""
    print("\n--- 多変数の勾配 ∇g ---")

    # 標準形式: 手で導出
    def grad_np(p: np.ndarray) -> np.ndarray:
        return np.array([2 * p[0] + p[1], p[0] + 2 * p[1]])

    # JAX形式: 自動微分
    def g_jax(p):
        return p[0]**2 + p[0] * p[1] + p[1]**2

    grad_jax = jax.grad(g_jax)

    p = np.array([1.0, 2.0])
    p_j = jnp.array([1.0, 2.0])

    print(f"∇g(1, 2) 手動     = {grad_np(p)}")
    print(f"∇g(1, 2) jax.grad = {np.array(grad_jax(p_j))}")
    print(f"一致              → {np.allclose(grad_np(p), grad_jax(p_j))}")


def value_and_grad_demo() -> None:
    """損失と勾配を同時に取得: value_and_grad."""
    print("\n--- value_and_grad（ML訓練ループで使う） ---")

    def loss(w, x, y):
        """二乗誤差損失: (wᵀx - y)²."""
        return (jnp.dot(w, x) - y) ** 2

    val_and_grad = jax.value_and_grad(loss)

    w = jnp.array([0.5, -0.3])
    x = jnp.array([1.0, 2.0])
    y = 1.0

    value, grad = val_and_grad(w, x, y)
    print(f"損失値:  {value:.4f}")
    print(f"∂L/∂w:  {grad}")


def higher_order_demo() -> None:
    """高階微分: jax.grad を重ねがけ."""
    print("\n--- 高階微分 ---")

    def f(x):
        return x ** 4

    df = jax.grad(f)        # f'  = 4x³
    d2f = jax.grad(df)      # f'' = 12x²
    d3f = jax.grad(d2f)     # f''' = 24x

    x0 = 2.0
    print(f"f(2)    = {f(x0)}        (理論値 16)")
    print(f"f'(2)   = {df(x0)}        (理論値 32)")
    print(f"f''(2)  = {d2f(x0)}       (理論値 48)")
    print(f"f'''(2) = {d3f(x0)}       (理論値 48)")


def hessian_demo() -> None:
    """ヘッシアン: 二階偏微分の行列."""
    print("\n--- ヘッシアン ---")

    def f(x):
        """f(x, y, z) = x² + 2y² + 3z² + xy."""
        return x[0]**2 + 2 * x[1]**2 + 3 * x[2]**2 + x[0] * x[1]

    hess = jax.hessian(f)
    H = hess(jnp.array([1.0, 1.0, 1.0]))
    print("ヘッシアン H:")
    print(np.array(H))
    print("(理論値: [[2,1,0],[1,4,0],[0,0,6]])")


def main() -> None:
    scalar_function_demo()
    vector_function_demo()
    value_and_grad_demo()
    higher_order_demo()
    hessian_demo()


if __name__ == "__main__":
    main()
