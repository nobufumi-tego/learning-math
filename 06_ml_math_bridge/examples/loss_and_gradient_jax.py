"""損失関数と勾配（JAX版）.

標準版 `loss_and_gradient.py` では、線形回帰の勾配を **手で導出** した:
    ∂L/∂w = (2/n) Xᵀ(Xw + b − y)
    ∂L/∂b = (2/n) Σ(Xw + b − y)

JAX版では同じ訓練を **jax.value_and_grad で自動微分** する。
- 損失関数の式を書くだけ → 勾配は自動
- @jit で高速化
- vmap で1サンプル関数からバッチ対応

これが現代の機械学習研究コードの「典型形」。
"""
from __future__ import annotations

import jax
import jax.numpy as jnp
import numpy as np


EPSILON: float = 1e-12


# === 損失関数 (標準形式と同じ式、ただし jnp で書く) ===

def mse_loss(params: dict, X: jnp.ndarray, y: jnp.ndarray) -> jnp.ndarray:
    """平均二乗誤差 L = (1/n) Σ(yᵢ − ŷᵢ)².

    Args:
        params: {"w": shape (d,), "b": scalar} のパラメータ辞書。
        X: 特徴量行列。shape (n, d)
        y: 真のラベル。shape (n,)

    Returns:
        スカラー損失。
    """
    y_pred = X @ params["w"] + params["b"]   # shape (n,)
    return jnp.mean((y - y_pred) ** 2)


def cross_entropy_loss(y_true: jnp.ndarray, y_pred: jnp.ndarray) -> jnp.ndarray:
    """クロスエントロピー L = − Σ y log(ŷ).

    Args:
        y_true: ワンホット。shape (n, k)
        y_pred: ソフトマックス出力。shape (n, k)
    """
    return -jnp.mean(jnp.sum(y_true * jnp.log(y_pred + EPSILON), axis=1))


def softmax(z: jnp.ndarray) -> jnp.ndarray:
    """数値安定化されたソフトマックス."""
    z_shifted = z - z.max(axis=1, keepdims=True)
    exp_z = jnp.exp(z_shifted)
    return exp_z / exp_z.sum(axis=1, keepdims=True)


# === 訓練ループ ===

@jax.jit
def update_step(
    params: dict, X: jnp.ndarray, y: jnp.ndarray, learning_rate: float
) -> tuple[dict, jnp.ndarray]:
    """1ステップ分の更新を返す.

    勾配は jax.value_and_grad で自動取得。
    手で ∂L/∂w や ∂L/∂b を書く必要が一切ない。
    """
    loss_val, grads = jax.value_and_grad(mse_loss)(params, X, y)
    new_params = {
        "w": params["w"] - learning_rate * grads["w"],
        "b": params["b"] - learning_rate * grads["b"],
    }
    return new_params, loss_val


def demo_linear_regression_jax() -> None:
    """JAX で線形回帰を勾配降下法で学習."""
    print("--- 線形回帰の勾配降下法 (JAX 版) ---")

    # データ生成（NumPy で）
    rng = np.random.default_rng(seed=42)
    n_samples = 100
    X_np = rng.uniform(-5, 5, size=(n_samples, 1))
    noise = rng.normal(0, 0.5, size=n_samples)
    y_np = 2 * X_np[:, 0] + 1 + noise

    # JAX 配列に変換
    X = jnp.array(X_np)            # shape (100, 1)
    y = jnp.array(y_np)            # shape (100,)

    # 初期パラメータ
    params = {"w": jnp.zeros(1), "b": 0.0}
    learning_rate = 0.01
    n_epochs = 200

    for epoch in range(n_epochs):
        params, loss_val = update_step(params, X, y, learning_rate)
        if epoch % 50 == 0:
            print(f"epoch={epoch:3d}  loss={float(loss_val):.4f}  "
                  f"w={float(params['w'][0]):.4f}  b={float(params['b']):.4f}")

    print(f"\n学習結果: w ≈ {float(params['w'][0]):.4f} (真値 2), "
          f"b ≈ {float(params['b']):.4f} (真値 1)")
    print("→ 勾配導出は一切書かず、損失関数の式だけで学習できた")


def demo_softmax_cross_entropy_jax() -> None:
    """ソフトマックスとクロスエントロピー (JAX 版)."""
    print("\n--- ソフトマックスとクロスエントロピー (JAX 版) ---")

    logits = jnp.array([[2.0, 1.0, 0.1],
                        [0.5, 2.5, 0.3]])
    y_true = jnp.array([[1, 0, 0],
                        [0, 1, 0]], dtype=jnp.float32)

    probs = softmax(logits)
    print(f"確率分布:\n{np.array(probs)}")
    print(f"各行の和: {np.array(probs.sum(axis=1))}")

    loss = cross_entropy_loss(y_true, probs)
    print(f"損失: {float(loss):.4f}")

    # 勾配も自動計算できる
    def total_loss(logits):
        return cross_entropy_loss(y_true, softmax(logits))

    grad_logits = jax.grad(total_loss)(logits)
    print(f"\n∂L/∂logits（自動微分）:\n{np.array(grad_logits)}")


def main() -> None:
    demo_linear_regression_jax()
    demo_softmax_cross_entropy_jax()


if __name__ == "__main__":
    main()
