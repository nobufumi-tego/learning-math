"""ベクトル・行列の基本演算サンプル.

線形代数の最頻出演算を NumPy で実行する。
"""
from __future__ import annotations

import numpy as np


def demo_vectors() -> None:
    """ベクトル: 加減算、スカラー倍、内積、ノルム."""
    print("--- ベクトル ---")
    u: np.ndarray = np.array([1.0, 2.0, 3.0])  # shape: (3,)
    v: np.ndarray = np.array([4.0, 5.0, 6.0])  # shape: (3,)

    print(f"u + v          = {u + v}")               # 加算
    print(f"3 * u          = {3 * u}")               # スカラー倍
    print(f"u · v (内積)   = {u @ v}")               # 内積 Σuᵢvᵢ
    print(f"||u|| (ノルム) = {np.linalg.norm(u):.4f}")  # √(Σuᵢ²)


def demo_matrices() -> None:
    """行列: 積、転置、逆行列、行列式."""
    print("\n--- 行列 ---")
    A: np.ndarray = np.array([[1.0, 2.0],
                              [3.0, 4.0]])  # shape: (2, 2)
    B: np.ndarray = np.array([[5.0, 6.0],
                              [7.0, 8.0]])  # shape: (2, 2)

    print(f"A @ B (行列積) =\n{A @ B}")
    print(f"A.T (転置) =\n{A.T}")
    print(f"det(A) (行列式) = {np.linalg.det(A):.4f}")  # 1*4 − 2*3 = −2
    print(f"A⁻¹ (逆行列) =\n{np.linalg.inv(A)}")


def demo_linear_system() -> None:
    """連立一次方程式 Ax = b を解く.

    数学:
        A = [[2, 1], [1, 3]], b = [5, 10]
        2x + y = 5
        x + 3y = 10
    """
    print("\n--- 連立方程式 Ax = b ---")
    A = np.array([[2.0, 1.0],
                  [1.0, 3.0]])
    b = np.array([5.0, 10.0])

    x = np.linalg.solve(A, b)
    print(f"解 x = {x}")               # [1, 3]
    print(f"検算 A@x − b = {A @ x - b}")  # ほぼ0


def main() -> None:
    demo_vectors()
    demo_matrices()
    demo_linear_system()


if __name__ == "__main__":
    main()
