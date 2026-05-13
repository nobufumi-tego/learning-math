"""微分・勾配のデモ（JAX版）.

標準形式の `derivative_demo.py` では:
- SymPy で記号微分（数式として扱う）
- 中央差分で数値微分（近似計算）

JAX版では:
- jax.grad で自動微分（記号でも近似でもなく、計算グラフを辿って厳密に計算）

3つを並べて結果が一致することを確認する。
"""
from __future__ import annotations

from typing import Callable

import jax
import jax.numpy as jnp
import numpy as np
import sympy as sp


def section_scalar_derivative() -> None:
    """1変数: f(x) = x³ + 2x² + x + 1."""
    print("--- 1変数の微分 ---")

    # === 標準形式 1: SymPy 記号微分 ===
    x_sym = sp.Symbol("x")
    f_sym = x_sym**3 + 2 * x_sym**2 + x_sym + 1
    df_sym = sp.diff(f_sym, x_sym)
    print(f"SymPy:  f'(x) = {df_sym}")
    print(f"        f'(2) = {df_sym.subs(x_sym, 2)}")

    # === 標準形式 2: 数値差分 ===
    def f(x: float) -> float:
        return x**3 + 2 * x**2 + x + 1

    def df_numeric(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
        return (f(x + h) - f(x - h)) / (2 * h)

    print(f"数値:   f'(2) ≈ {df_numeric(f, 2.0):.4f}")

    # === JAX形式: 自動微分 ===
    def f_jax(x):
        return x**3 + 2 * x**2 + x + 1

    df_jax = jax.grad(f_jax)
    print(f"JAX:    f'(2) = {df_jax(2.0)}")


def section_multivariable_gradient() -> None:
    """多変数: g(x, y) = x² + xy + y²."""
    print("\n--- 多変数の勾配 ∇g ---")

    # === 標準形式 1: SymPy ===
    x_sym, y_sym = sp.symbols("x y")
    g_sym = x_sym**2 + x_sym * y_sym + y_sym**2
    grad_sym = [sp.diff(g_sym, v) for v in (x_sym, y_sym)]
    print(f"SymPy:  ∇g = ({grad_sym[0]}, {grad_sym[1]})")
    print(f"        ∇g(1,2) = ({grad_sym[0].subs([(x_sym,1),(y_sym,2)])}, "
          f"{grad_sym[1].subs([(x_sym,1),(y_sym,2)])})")

    # === 標準形式 2: 数値差分 ===
    def g_np(p: np.ndarray) -> float:
        return float(p[0]**2 + p[0] * p[1] + p[1]**2)

    def numerical_gradient(
        f: Callable[[np.ndarray], float], x: np.ndarray, h: float = 1e-5
    ) -> np.ndarray:
        grad = np.zeros_like(x, dtype=float)
        for i in range(len(x)):
            xp, xm = x.copy(), x.copy()
            xp[i] += h
            xm[i] -= h
            grad[i] = (f(xp) - f(xm)) / (2 * h)
        return grad

    p = np.array([1.0, 2.0])
    print(f"数値:   ∇g(1,2) ≈ {numerical_gradient(g_np, p)}")

    # === JAX形式: 自動微分 ===
    def g_jax(p):
        return p[0]**2 + p[0] * p[1] + p[1]**2

    grad_jax = jax.grad(g_jax)
    p_j = jnp.array([1.0, 2.0])
    print(f"JAX:    ∇g(1,2) = {np.array(grad_jax(p_j))}")


def section_higher_order() -> None:
    """高階微分: JAX なら grad をネストするだけ."""
    print("\n--- 高階微分 (JAX が圧倒的に楽) ---")

    # === 標準形式: SymPy ===
    x_sym = sp.Symbol("x")
    f_sym = x_sym**5
    print(f"SymPy: f'(x)     = {sp.diff(f_sym, x_sym)}")
    print(f"       f''(x)    = {sp.diff(f_sym, x_sym, 2)}")
    print(f"       f'''(x)   = {sp.diff(f_sym, x_sym, 3)}")

    # === JAX形式 ===
    def f(x):
        return x**5

    df = jax.grad(f)
    d2f = jax.grad(df)
    d3f = jax.grad(d2f)

    x0 = 2.0
    print(f"JAX:   f'(2)     = {df(x0)}    (理論 5x⁴=80)")
    print(f"       f''(2)    = {d2f(x0)}   (理論 20x³=160)")
    print(f"       f'''(2)   = {d3f(x0)}   (理論 60x²=240)")


def main() -> None:
    section_scalar_derivative()
    section_multivariable_gradient()
    section_higher_order()


if __name__ == "__main__":
    main()
