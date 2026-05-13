"""数学記号 → Python 対応 実行例集.

`uv run python 00_notation/examples/notation_to_python.py` で実行可能。
各セクションは独立しているので、上から順に読み進められる。
"""
from __future__ import annotations

import math
from itertools import product

import numpy as np


def section_1_basic_symbols() -> None:
    """1. 基本記号: =, ≈, ∞, etc."""
    print("=" * 50)
    print("Section 1: 基本記号")
    print("=" * 50)

    # ≈ 近似的に等しい
    a = 0.1 + 0.2
    b = 0.3
    print(f"0.1 + 0.2 == 0.3      → {a == b}")            # False
    print(f"np.isclose(a, b)      → {np.isclose(a, b)}")  # True (≈)

    # ∞ 無限大
    print(f"∞ > 1e308             → {np.inf > 1e308}")    # True
    print(f"1.0 / ∞               → {1.0 / np.inf}")      # 0.0


def section_2_set_theory() -> None:
    """2. 集合論: ∈, ∪, ∩, etc."""
    print("\n" + "=" * 50)
    print("Section 2: 集合論")
    print("=" * 50)

    A: set[int] = {1, 2, 3, 4}
    B: set[int] = {3, 4, 5, 6}

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"3 ∈ A                 → {3 in A}")
    print(f"A ∪ B                 → {A | B}")
    print(f"A ∩ B                 → {A & B}")
    print(f"A \\ B                 → {A - B}")
    print(f"|A| (濃度)            → {len(A)}")

    # 直積 A × B
    print(f"A × B の最初の5要素   → {list(product(A, B))[:5]}")


def section_3_logic() -> None:
    """3. 論理: ∀, ∃, ⇒."""
    print("\n" + "=" * 50)
    print("Section 3: 論理")
    print("=" * 50)

    xs = np.linspace(-10, 10, 1000)

    # ∀x ∈ ℝ, x² ≥ 0
    print(f"∀x, x² ≥ 0            → {all(x**2 >= 0 for x in xs)}")

    # ∃x s.t. x² ≈ 2
    print(f"∃x s.t. x² = 2 (近似) → "
          f"{any(np.isclose(x**2, 2.0, atol=0.01) for x in xs)}")

    # P ⇒ Q
    def implies(P: bool, Q: bool) -> bool:
        """P ⇒ Q の真理値."""
        return (not P) or Q

    print(f"True ⇒ False          → {implies(True, False)}")
    print(f"False ⇒ True          → {implies(False, True)}")


def section_4_functions() -> None:
    """4. 関数記法: f: ℝ → ℝ, f ∘ g, etc."""
    print("\n" + "=" * 50)
    print("Section 4: 関数")
    print("=" * 50)

    def f(x: float) -> float:
        """f: ℝ → ℝ, x ↦ x²."""
        return x ** 2

    def g(x: float) -> float:
        """g: ℝ → ℝ, x ↦ x + 1."""
        return x + 1

    # 合成 (g ∘ f)(x) = g(f(x))
    x = 2.0
    print(f"f(2) = 2²             → {f(x)}")
    print(f"g(2) = 2+1            → {g(x)}")
    print(f"(g ∘ f)(2) = g(f(2))  → {g(f(x))}")

    # 絶対値 |x|, 床関数 ⌊x⌋
    print(f"|−2.7|                → {abs(-2.7)}")
    print(f"⌊−2.7⌋                → {math.floor(-2.7)}")
    print(f"⌈−2.7⌉                → {math.ceil(-2.7)}")


def section_5_sum_prod() -> None:
    """5. Σ 総和、Π 総乗."""
    print("\n" + "=" * 50)
    print("Section 5: 総和・総乗")
    print("=" * 50)

    a = np.array([10, 20, 30, 40])  # shape: (4,)

    # Σ a_i
    print(f"Σ a_i                 → {np.sum(a)}")          # 100

    # Σ a_i²
    print(f"Σ a_i²                → {np.sum(a**2)}")       # 3000

    # 平均 = (1/n) Σ a_i
    print(f"平均 (1/n)Σa_i        → {np.mean(a)}")         # 25.0

    # Π a_i
    print(f"Π a_i                 → {np.prod(a)}")         # 240000

    # n! = Π i (i=1..n)
    print(f"5!                    → {math.factorial(5)}")  # 120

    # 内積 Σ w_i x_i
    w = np.array([0.1, 0.2, 0.3, 0.4])
    x = np.array([1.0, 2.0, 3.0, 4.0])
    print(f"Σ w_i x_i (内積)      → {w @ x}")              # 3.0


def section_6_greek_in_ml() -> None:
    """6. ML で使うギリシャ文字の典型例."""
    print("\n" + "=" * 50)
    print("Section 6: ギリシャ文字（ML 例）")
    print("=" * 50)

    # θ ← θ − η ∇L(θ) (勾配降下法の更新式)
    theta = np.array([1.0, 2.0])           # パラメータ θ
    eta = 0.1                              # 学習率 η
    grad_L = np.array([0.5, -0.3])         # 勾配 ∇L

    theta_new = theta - eta * grad_L
    print(f"θ_old                 → {theta}")
    print(f"η                     → {eta}")
    print(f"∇L                    → {grad_L}")
    print(f"θ_new = θ − η∇L       → {theta_new}")

    # 平均 μ と標準偏差 σ
    samples = np.random.default_rng(seed=42).normal(size=1000)
    mu = np.mean(samples)
    sigma = np.std(samples)
    print(f"μ (平均)              → {mu:.4f}")
    print(f"σ (標準偏差)          → {sigma:.4f}")


def main() -> None:
    """すべてのセクションを順に実行する."""
    section_1_basic_symbols()
    section_2_set_theory()
    section_3_logic()
    section_4_functions()
    section_5_sum_prod()
    section_6_greek_in_ml()


if __name__ == "__main__":
    main()
