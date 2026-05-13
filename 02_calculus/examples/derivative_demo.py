"""微分・勾配のデモ.

記号微分 (SymPy) と数値微分 (NumPy) の両方を扱う。
"""
from __future__ import annotations

from typing import Callable

import numpy as np
import sympy as sp


def symbolic_derivative_demo() -> None:
    """SymPy で記号微分."""
    print("--- 記号微分 (SymPy) ---")
    x = sp.Symbol("x")
    f = x**3 + 2 * x**2 + x + 1

    df = sp.diff(f, x)
    d2f = sp.diff(f, x, 2)  # 2階微分

    print(f"f(x)   = {f}")
    print(f"f'(x)  = {df}")    # 3x² + 4x + 1
    print(f"f''(x) = {d2f}")   # 6x + 4

    # x=2 での値
    print(f"f'(2)  = {df.subs(x, 2)}")  # 21


def numerical_derivative_demo() -> None:
    """中央差分による数値微分."""
    print("\n--- 数値微分 (中央差分) ---")

    def f(x: float) -> float:
        """f(x) = x³ + 2x² + x + 1."""
        return x**3 + 2 * x**2 + x + 1

    def df_numeric(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
        """中央差分: (f(x+h) − f(x−h)) / (2h)."""
        return (f(x + h) - f(x - h)) / (2 * h)

    x0 = 2.0
    print(f"f'(2) ≈ {df_numeric(f, x0):.4f}")  # 21.0 に近い


def multivariable_gradient_demo() -> None:
    """多変数の勾配 ∇f を計算する."""
    print("\n--- 多変数の勾配 ∇f ---")

    # 記号計算
    x, y = sp.symbols("x y")
    g = x**2 + x * y + y**2

    # ∇g = (∂g/∂x, ∂g/∂y)
    grad_sym = [sp.diff(g, v) for v in (x, y)]
    print(f"g(x, y)  = {g}")
    print(f"∇g(x,y)  = ({grad_sym[0]}, {grad_sym[1]})")
    print(f"∇g(1, 2) = ({grad_sym[0].subs([(x,1),(y,2)])}, "
          f"{grad_sym[1].subs([(x,1),(y,2)])})")

    # 数値計算
    def g_np(p: np.ndarray) -> float:
        """g(x, y) = x² + xy + y². p shape: (2,)."""
        return float(p[0]**2 + p[0] * p[1] + p[1]**2)

    def numerical_gradient(
        f: Callable[[np.ndarray], float],
        x: np.ndarray,
        h: float = 1e-5,
    ) -> np.ndarray:
        """中央差分による数値勾配."""
        grad = np.zeros_like(x, dtype=float)
        for i in range(len(x)):
            x_plus = x.copy()
            x_minus = x.copy()
            x_plus[i] += h
            x_minus[i] -= h
            grad[i] = (f(x_plus) - f(x_minus)) / (2 * h)
        return grad

    p = np.array([1.0, 2.0])  # shape: (2,)
    grad_num = numerical_gradient(g_np, p)
    print(f"数値勾配 ∇g(1,2) = {grad_num}")  # ≈ (4, 5)


def main() -> None:
    symbolic_derivative_demo()
    numerical_derivative_demo()
    multivariable_gradient_demo()


if __name__ == "__main__":
    main()
