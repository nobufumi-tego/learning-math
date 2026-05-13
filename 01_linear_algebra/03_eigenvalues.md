# 01-3. 固有値・固有ベクトル — 行列の「魂」を見る

**このページのゴール**: 固有値・固有ベクトルの直感的な意味、対角化、そしてこれが PCA・Google PageRank・量子力学にどう繋がるかを理解する。

---

## 💡 このページのコードを動かすには

```bash
uv run jupyter lab
```

ファイルツリーから `01_linear_algebra/notebooks/03_eigenvalues.ipynb` を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_matrices.md`](02_matrices.md) — 行列と線形変換の基本
> - [`01_vectors.md`](01_vectors.md) — ベクトルの内積とノルム

---

## 1. ひと言で

> **固有ベクトル** = 「**その行列で変換しても、向きが変わらない特別なベクトル**」
> **固有値** = 「**変換後にどれだけ伸び縮みするか**」のスカラー

数式で書くと、行列 `A` に対して:

```
A v = λ v
```

ここで:
- `v` = 固有ベクトル (eigenvector)
- `λ` (ラムダ) = 固有値 (eigenvalue)

意味: 「A という変換を v に適用すると、**v が λ 倍に伸びるだけで、向きは変わらない**」

## 2. 直感のために、絵で考える

普通のベクトルは、行列で変換すると**向きが変わる**:

```
変換前: ↗
変換後: ↘    （向きも長さも変わった）
```

ところが、ある特別なベクトル `v` だけは:

```
変換前: ↗
変換後: ↗↗    （向きそのまま、長さだけ変わった）
```

この「**向きが変わらない方向**」が **固有ベクトル**、そのときの伸び率が **固有値**。

行列はこの「**特別な方向**」を持っていて、それを知ると、**行列の本質的な動き**が見える。

## 3. 計算例

行列 `A = [[2, 1], [0, 3]]` の固有値・固有ベクトルは?

### 数式で
特性方程式 `det(A − λI) = 0` を解く:

```
det([[2-λ, 1], [0, 3-λ]]) = (2-λ)(3-λ) − 1×0 = 0
                          = (2-λ)(3-λ) = 0
                          → λ = 2, 3
```

各 λ について `(A − λI)v = 0` を解いて固有ベクトルを得る:

```
λ = 2: v = (1, 0) （x軸方向）
λ = 3: v = (1, 1) を正規化したもの
```

### Python で
```python
import numpy as np

A = np.array([[2.0, 1.0],
              [0.0, 3.0]])

eigvals, eigvecs = np.linalg.eig(A)
print('固有値:', eigvals)
# [2. 3.]

print('固有ベクトル (列ベクトル):')
print(eigvecs)
# [[1.         0.70710678]
#  [0.         0.70710678]]
```

`eigvecs[:, i]` が `eigvals[i]` に対応する固有ベクトル。
各列が独立な固有ベクトル。

### JAX 形式

```python
import jax.numpy as jnp

A_j = jnp.array([[2.0, 1.0], [0.0, 3.0]])
eigvals_j, eigvecs_j = jnp.linalg.eig(A_j)
```

---

## 4. なぜ重要か — 機械学習・科学での役割

### (1) 主成分分析 (PCA) — データの「主要な方向」

PCA は、データの **共分散行列の固有ベクトル** = データが**最も広がっている方向** を見つけるアルゴリズム。

```
データ → 共分散行列 C → 固有値分解 → 大きい固有値の固有ベクトル = 「重要な軸」
```

これで何ができるか:
- **次元削減**: 1万次元のデータを 50次元に圧縮
- **可視化**: 100次元のデータを 2次元に落として散布図
- **ノイズ除去**: 小さい固有値の方向は捨てる

### (2) Google PageRank — Web の重要度

1998年、Google を作った Larry Page と Sergey Brin は、Webページの重要度を**「リンクの行列の最大固有ベクトル」**として定義しました。

> 「**重要なページからリンクされているページは、重要**」

これを行列方程式で表すと、重要度ベクトル `r` は:

```
r = M r       （Mはリンク確率行列）
```

これは固有値 1 の固有ベクトルを求める問題。
**Google の検索エンジンの基礎**は、固有ベクトル計算でした。

### (3) 量子力学

量子力学では、物理量 (エネルギー・運動量など) は**演算子 (行列)** で表され、観測される値は**その演算子の固有値**になります。
水素原子のエネルギー準位は、ハミルトニアン演算子の固有値そのもの。

### (4) 振動の共振周波数

橋やビルが揺れるとき、特定の周波数で振動が**共鳴**します。
それは、構造の「**固有モード**」(固有ベクトル) に対応する固有振動数。
タコマナローズ橋の崩落 (1940) はこの共振現象の典型例。

### (5) 機械学習の最適化分析

損失関数の **ヘッセ行列 (二階微分の行列)** の固有値を見ると:
- 全部正 → 最小値 (ボウル形)
- 全部負 → 最大値 (山形)
- 正負混在 → 鞍点 (峠形)

ニューラルネット訓練で「**鞍点に引っかかる**」現象は、固有値の話。

---

## 5. 対角化 (diagonalization)

n 個の独立な固有ベクトルがあれば、行列 `A` を**対角行列**に変換できます:

```
A = P D P⁻¹
```

ここで:
- `P` = 固有ベクトルを列に並べた行列
- `D` = 対角に固有値を並べた行列

これを **対角化** と呼びます。

### なぜ嬉しい?

対角化できると、`A` の **べき乗** が一瞬で計算できる:

```
Aⁿ = P Dⁿ P⁻¹
```

`Dⁿ` は対角要素を n 乗するだけ。
これがマルコフ連鎖や微分方程式の解法を**激変**させます。

### Python

```python
A = np.array([[2.0, 1.0], [0.0, 3.0]])

eigvals, P = np.linalg.eig(A)
D = np.diag(eigvals)
P_inv = np.linalg.inv(P)

# A = P D P⁻¹ になっているか確認
print(P @ D @ P_inv)
# [[2. 1.]
#  [0. 3.]]   ← 元の A と一致

# A^10 を一瞬で
A_pow_10 = P @ np.diag(eigvals ** 10) @ P_inv
print(A_pow_10)
```

---

## 6. 対称行列の特別な性質

特に **対称行列 (`A = Aᵀ`)** は、固有値・固有ベクトルが**美しい性質**を持ちます:

| 性質 | 内容 |
|---|---|
| 実数性 | 固有値はすべて**実数** (複素数にならない) |
| 直交性 | 異なる固有値の固有ベクトルは**互いに直交** |
| 対角化可能 | 必ず対角化できる |

これを**スペクトル分解 (spectral decomposition)** と呼びます:
```
A = Q Λ Qᵀ      （Q は直交行列、Λ は対角の固有値行列）
```

```python
# 対称行列を作る
A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
print(np.allclose(A, A.T))           # True ← 対称

eigvals, Q = np.linalg.eigh(A)        # eigh は対称行列専用 (高速・安定)
print('固有値:', eigvals)              # [1.38... 3.61...]

# 直交性の確認
print('Q^T Q ≈ I:', np.allclose(Q.T @ Q, np.eye(2)))    # True

# 復元
print('復元:\n', Q @ np.diag(eigvals) @ Q.T)
# 元の A に一致
```

> 💡 **`np.linalg.eig` vs `np.linalg.eigh`**:
> 対称行列なら **`eigh`** が圧倒的に高速で精度も高い。
> 機械学習では、共分散行列・カーネル行列など対称行列が多いので、`eigh` の出番が多い。

---

## 7. 機械学習でのフル活用例: PCA

実際に PCA を実装してみます。

```python
import numpy as np

def pca(X: np.ndarray, n_components: int) -> tuple[np.ndarray, np.ndarray]:
    """主成分分析.

    Args:
        X: データ行列。shape: (n_samples, n_features)
        n_components: 削減後の次元数

    Returns:
        X_pca: 変換後のデータ。shape: (n_samples, n_components)
        components: 主成分。shape: (n_components, n_features)
    """
    # 1. 中心化
    X_centered = X - X.mean(axis=0)

    # 2. 共分散行列
    cov = np.cov(X_centered, rowvar=False)

    # 3. 固有値分解 (対称行列なので eigh)
    eigvals, eigvecs = np.linalg.eigh(cov)

    # 4. 大きい順にソート
    order = np.argsort(eigvals)[::-1]
    eigvals = eigvals[order]
    eigvecs = eigvecs[:, order]

    # 5. 上位 n_components 個の固有ベクトルで変換
    components = eigvecs[:, :n_components].T   # shape: (n_components, n_features)
    X_pca = X_centered @ components.T           # shape: (n_samples, n_components)

    return X_pca, components


# 使用例
rng = np.random.default_rng(seed=42)
X = rng.standard_normal((100, 5)) @ rng.standard_normal((5, 5))   # 5次元データ

X_2d, comps = pca(X, n_components=2)
print(f'元データ shape: {X.shape}')
print(f'2次元化後 shape: {X_2d.shape}')
print(f'主成分 shape: {comps.shape}')
```

これを使うと、高次元データを2次元に落として可視化できます。
詳しい実演は notebook で。

---

## 8. ハマりポイント

### (1) 複素数になることがある

非対称行列の場合、固有値が**複素数**になることがあります:

```python
A = np.array([[0, -1], [1, 0]])     # 90度回転行列
eigvals, _ = np.linalg.eig(A)
print(eigvals)
# [0.+1.j 0.-1.j]   ← 複素数
```

回転は「向きが変わらない方向」が**ない**ので、実数の固有ベクトルが存在しない、と解釈できます。

### (2) 固有ベクトルは正規化されている

NumPy の `eig` が返す固有ベクトルは、**ノルム1に正規化**されています。
ただし**符号は不定** (`v` も `-v` も固有ベクトル)。

### (3) 数値計算の不安定さ

固有値が**ほぼ等しい**ケースでは、固有ベクトルが**数値的に不安定**になります。
特に対称行列なら必ず `eigh` を使う。

---

## まとめ

| 概念 | 数式 | Python | 意味 |
|---|---|---|---|
| 固有値・固有ベクトル | `Av = λv` | `np.linalg.eig(A)` | 向きが変わらない方向と倍率 |
| 対称行列の固有値 | – | `np.linalg.eigh(A)` | 実数・直交、安定計算 |
| 対角化 | `A = PDP⁻¹` | `P @ diag(λ) @ inv(P)` | べき乗が一発 |
| スペクトル分解 | `A = QΛQᵀ` | (eigh で取得) | 対称行列の美しい構造 |

**この章のキー**:
- 固有値・固有ベクトル = 行列の「魂」、その変換の本質
- PCA・Google PageRank・量子力学 — 多分野で使われる
- 対称行列なら `eigh`、それ以外は `eig`

## 次へ

→ [`04_decompositions.md`](04_decompositions.md) — LU・QR・SVD など、行列を分解する技

## 関連
- [`05_optimization/`](../05_optimization/) — ヘッセ行列の固有値と最適化
- [`06_ml_math_bridge/`](../06_ml_math_bridge/) — PCA を使った特徴量設計

---

## 🔍 ググってみよう

- **PCA (主成分分析)** — 機械学習の前処理の定番
- **Google PageRank** — 1998年の論文「The Anatomy of a Large-Scale Hypertextual Web Search Engine」
- **スペクトル定理 (spectral theorem)** — 対称行列の固有値分解の正式名
- **ヘッセ行列 (Hessian)** — 2階微分の行列、最適化で使う
- **スペクトラル クラスタリング** — グラフを固有ベクトルで分割する
- **Power Iteration (べき乗法)** — 最大固有値を求める素朴な方法、PageRank の実装
- **タコマナローズ橋** — 共振現象で崩壊した有名な橋 (1940)
- **量子力学のシュレーディンガー方程式** — Hψ = Eψ という固有値問題
- **Diffusion Map** — 高次元データの構造を固有ベクトルで捉える
- **Lanczos algorithm** — 大規模疎行列の固有値計算手法
