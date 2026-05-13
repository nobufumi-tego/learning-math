"""確率分布のサンプリングと統計量計算デモ."""
from __future__ import annotations

import numpy as np
from scipy import stats


def normal_distribution_demo() -> None:
    """正規分布 N(μ, σ²) のサンプリングと統計量."""
    print("--- 正規分布 N(μ=0, σ=1) ---")

    rng = np.random.default_rng(seed=42)
    samples: np.ndarray = rng.normal(loc=0.0, scale=1.0, size=10_000)  # shape: (10000,)

    print(f"サンプル平均 μ̂      = {np.mean(samples):.4f}")
    print(f"サンプル標準偏差 σ̂  = {np.std(samples):.4f}")
    print(f"サンプル分散 σ̂²    = {np.var(samples):.4f}")

    # PDF 値: f(0) = 1/√(2π) ≈ 0.3989
    print(f"PDF f(0)            = {stats.norm.pdf(0.0):.4f}")

    # CDF 値: P(X ≤ 1.96) ≈ 0.975
    print(f"P(X ≤ 1.96)         = {stats.norm.cdf(1.96):.4f}")


def binomial_distribution_demo() -> None:
    """二項分布 Bin(n, p): n回試行で成功した回数の分布."""
    print("\n--- 二項分布 Bin(n=10, p=0.5) ---")

    n, p = 10, 0.5  # 10回コインを投げて表の回数
    # E[X] = np, Var[X] = np(1-p)
    print(f"理論期待値 E[X] = np = {n * p}")
    print(f"理論分散 Var[X] = np(1−p) = {n * p * (1 - p)}")

    # 確率質量関数 P(X = k)
    for k in [0, 5, 10]:
        prob = stats.binom.pmf(k, n, p)
        print(f"P(X = {k}) = {prob:.4f}")


def bayes_demo() -> None:
    """ベイズの定理: P(A|B) = P(B|A) P(A) / P(B).

    例: 病気の検査
    - 病気の事前確率 P(D) = 1%
    - 検査の感度 P(陽性|病気) = 99%
    - 検査の特異度 P(陰性|健康) = 99%
    - 陽性のとき、本当に病気である確率 P(病気|陽性) は？
    """
    print("\n--- ベイズの定理（検査の例） ---")

    P_disease = 0.01          # P(D)
    P_pos_given_disease = 0.99  # P(+|D)
    P_neg_given_healthy = 0.99  # P(−|¬D)
    P_pos_given_healthy = 1 - P_neg_given_healthy  # P(+|¬D)

    # 全確率 P(+) = P(+|D)P(D) + P(+|¬D)P(¬D)
    P_positive = (
        P_pos_given_disease * P_disease
        + P_pos_given_healthy * (1 - P_disease)
    )

    # ベイズの定理 P(D|+) = P(+|D)P(D) / P(+)
    P_disease_given_pos = P_pos_given_disease * P_disease / P_positive

    print(f"事前確率 P(病気)           = {P_disease:.2%}")
    print(f"感度 P(+|病気)             = {P_pos_given_disease:.2%}")
    print(f"陽性確率 P(+)              = {P_positive:.4%}")
    print(f"事後確率 P(病気|+)         = {P_disease_given_pos:.2%}")
    print("→ 「99% 正確な検査」でも陽性のとき本当に病気な確率はわずか 50%")


def main() -> None:
    normal_distribution_demo()
    binomial_distribution_demo()
    bayes_demo()


if __name__ == "__main__":
    main()
