"""ベクトル・行列の基本演算（JAX版）.

`vectors_and_matrices.py`（NumPy版）と並べて読むこと。
ほとんどのAPIは同じだが、配列が不変・float32がデフォルトという違いがある。
"""
from __future__ import annotations

import jax.numpy as jnp


def demo_vectors() -> None:
    """ベクトル: 加減算、内積、ノルム."""
    print("--- ベクトル (JAX) ---")
    u: jnp.ndarray = jnp.array([1.0, 2.0, 3.0])  # shape: (3,)
    v: jnp.ndarray = jnp.array([4.0, 5.0, 6.0])  # shape: (3,)

    print(f"u + v          = {u + v}")
    print(f"3 * u          = {3 * u}")
    print(f"u · v (内積)   = {u @ v}")
    print(f"||u|| (ノルム) = {jnp.linalg.norm(u):.4f}")


def demo_matrices() -> None:
    """行列: 積、転置、逆行列、行列式."""
    print("\n--- 行列 (JAX) ---")
    A = jnp.array([[1.0, 2.0],
                   [3.0, 4.0]])
    B = jnp.array([[5.0, 6.0],
                   [7.0, 8.0]])

    print(f"A @ B =\n{A @ B}")
    print(f"A.T  =\n{A.T}")
    print(f"det(A)  = {jnp.linalg.det(A):.4f}")
    print(f"A⁻¹  =\n{jnp.linalg.inv(A)}")


def demo_linear_system() -> None:
    """連立方程式 Ax = b の解."""
    print("\n--- 連立方程式 Ax = b (JAX) ---")
    A = jnp.array([[2.0, 1.0],
                   [1.0, 3.0]])
    b = jnp.array([5.0, 10.0])

    x = jnp.linalg.solve(A, b)
    print(f"解 x = {x}")
    print(f"検算 A@x − b = {A @ x - b}")


def demo_immutability() -> None:
    """JAXならではのトピック: 配列の不変性."""
    print("\n--- JAX 固有: 配列の不変性 ---")
    x = jnp.array([1.0, 2.0, 3.0])

    # NumPy なら x[0] = 99 が動くが、JAXでは下のように書く
    x2 = x.at[0].set(99.0)
    print(f"元 x   = {x}")
    print(f"新 x2  = {x2}  ← 新しい配列。元は不変")


def main() -> None:
    demo_vectors()
    demo_matrices()
    demo_linear_system()
    demo_immutability()


if __name__ == "__main__":
    main()
