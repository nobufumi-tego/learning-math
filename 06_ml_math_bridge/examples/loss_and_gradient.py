"""損失関数と勾配のデモ.

これまで学んだ数学（線形代数・微積分・確率）が ML で統合される様子を見る。
"""
from __future__ import annotations

import numpy as np


EPSILON: float = 1e-12  # log(0) を避けるための数値安定化定数


def mse_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """平均二乗誤差 L = (1/n) Σ(yᵢ − ŷᵢ)².

    Args:
        y_true: 真の値。shape: (n,)
        y_pred: 予測値。shape: (n,)

    Returns:
        スカラー損失。
    """
    return float(np.mean((y_true - y_pred) ** 2))


def mse_gradient(
    X: np.ndarray, y_true: np.ndarray, w: np.ndarray, b: float
) -> tuple[np.ndarray, float]:
    """線形回帰 ŷ = Xw + b の MSE 勾配.

    ∂L/∂w = (2/n) Xᵀ (Xw + b − y)
    ∂L/∂b = (2/n) Σ(Xw + b − y)

    Args:
        X: 特徴量行列。shape: (n, d)
        y_true: 真のラベル。shape: (n,)
        w: 重み。shape: (d,)
        b: バイアス。スカラー。

    Returns:
        (∂L/∂w shape: (d,), ∂L/∂b スカラー)
    """
    n = X.shape[0]
    y_pred = X @ w + b              # shape: (n,)
    error = y_pred - y_true         # shape: (n,)
    grad_w = (2.0 / n) * X.T @ error  # shape: (d,)
    grad_b = float((2.0 / n) * np.sum(error))
    return grad_w, grad_b


def cross_entropy_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """クロスエントロピー損失 L = − Σ y log(ŷ).

    Args:
        y_true: ワンホット表現。shape: (n, k)
        y_pred: ソフトマックス出力。shape: (n, k)
    """
    return float(-np.mean(np.sum(y_true * np.log(y_pred + EPSILON), axis=1)))


def softmax(z: np.ndarray) -> np.ndarray:
    """ソフトマックス関数 σ(z)ᵢ = exp(zᵢ) / Σ exp(zⱼ).

    Args:
        z: ロジット。shape: (n, k)

    Returns:
        確率分布。shape: (n, k), 各行が和1。
    """
    # 数値安定化: 各行から最大値を引く
    z_shifted = z - z.max(axis=1, keepdims=True)
    exp_z = np.exp(z_shifted)
    return exp_z / exp_z.sum(axis=1, keepdims=True)


def demo_linear_regression_gradient_descent() -> None:
    """線形回帰を勾配降下法で学習する.

    人工データ: y = 2x + 1 + ノイズ
    """
    print("--- 線形回帰の勾配降下法による学習 ---")

    rng = np.random.default_rng(seed=42)
    n_samples = 100
    X = rng.uniform(-5, 5, size=(n_samples, 1))     # shape: (100, 1)
    noise = rng.normal(0, 0.5, size=n_samples)      # shape: (100,)
    y_true = (2 * X[:, 0] + 1 + noise)              # shape: (100,)

    # 初期パラメータ
    w = np.array([0.0])  # shape: (1,)
    b = 0.0

    learning_rate = 0.01
    n_epochs = 200

    for epoch in range(n_epochs):
        loss = mse_loss(y_true, X @ w + b)
        grad_w, grad_b = mse_gradient(X, y_true, w, b)
        w = w - learning_rate * grad_w
        b = b - learning_rate * grad_b

        if epoch % 50 == 0:
            print(f"epoch={epoch:3d}  loss={loss:.4f}  w={w[0]:.4f}  b={b:.4f}")

    print(f"\n学習結果: w ≈ {w[0]:.4f} (真値 2), b ≈ {b:.4f} (真値 1)")


def demo_softmax_cross_entropy() -> None:
    """ソフトマックス + クロスエントロピー（分類の基本）."""
    print("\n--- ソフトマックスとクロスエントロピー ---")

    # 3クラス分類、2サンプル
    logits = np.array([[2.0, 1.0, 0.1],
                       [0.5, 2.5, 0.3]])  # shape: (2, 3)
    y_true = np.array([[1, 0, 0],
                       [0, 1, 0]])         # shape: (2, 3) ワンホット

    probs = softmax(logits)
    print(f"確率分布:\n{probs}")
    print(f"各行の和: {probs.sum(axis=1)}")  # [1.0, 1.0]

    loss = cross_entropy_loss(y_true, probs)
    print(f"クロスエントロピー損失: {loss:.4f}")


def main() -> None:
    demo_linear_regression_gradient_descent()
    demo_softmax_cross_entropy()


if __name__ == "__main__":
    main()
