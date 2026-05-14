# 01-4. 行列分解 — LU・QR・SVD・Cholesky

**このページのゴール**: 「行列を、より扱いやすい部品に分解する」 4 つの主要技法を理解し、SVD が機械学習でどう使われるかを掴む。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから `01_linear_algebra/notebooks/04_decompositions.ipynb` を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_matrices.md`](02_matrices.md) — 行列演算の基本
> - [`03_eigenvalues.md`](03_eigenvalues.md) — 固有値分解 (SVD の親戚)

---

## 1. なぜ行列を「分解」するのか

「分解する」とは、ある行列 $A$ を、**シンプルな行列の積に書き直す**こと:

$$
A = B \times C \quad \text{(例: } B \text{ が三角、} C \text{ が対角、など特殊形)}
$$

なぜ嬉しいか:

1. **方程式を解くのが速くなる** (LU, Cholesky)
2. **数値安定性が上がる** (QR)
3. **データの本質的な構造が見える** (SVD)
4. **データの圧縮ができる** (SVD)
5. **逆行列の代用で安定** (擬似逆行列)

機械学習では特に **SVD** が圧倒的に重要。
このページでは 4 つを並べて、特性の違いを掴みます。

---

## 2. LU 分解 — 連立方程式の高速解法

### 何をするか

正方行列 $A$ を、**下三角行列 $L$** と **上三角行列 $U$** の積に分解:

$$
A = L U
$$

$$
L = \begin{pmatrix}
1 & 0 & 0 \\
\ell_{21} & 1 & 0 \\
\ell_{31} & \ell_{32} & 1
\end{pmatrix},
\qquad
U = \begin{pmatrix}
u_{11} & u_{12} & u_{13} \\
0 & u_{22} & u_{23} \\
0 & 0 & u_{33}
\end{pmatrix}
$$

### なぜ嬉しいか

連立方程式 $A\mathbf{x} = \mathbf{b}$ を解くとき:
- $LU\mathbf{x} = \mathbf{b}$ ⇒ まず $L\mathbf{y} = \mathbf{b}$ を解く (前進代入)、次に $U\mathbf{x} = \mathbf{y}$ (後退代入)
- 三角行列なら**爆速**で解ける

`np.linalg.solve` は内部でこれをやっています。

### Python

```python
import numpy as np
from scipy.linalg import lu

A = np.array([[2.0, 1.0, 1.0],
              [4.0, 3.0, 3.0],
              [8.0, 7.0, 9.0]])

P, L, U = lu(A)        # 実は P (置換行列) もある: PA = LU
print('L:'); print(L)
print('U:'); print(U)
print('検算 P @ A ≈ L @ U:', np.allclose(P @ A, L @ U))
```

### 実用

ほとんどの線形代数ライブラリ (NumPy, SciPy, MATLAB) の `solve` が、内部で LU を使っています。
**直接ユーザーが LU を呼ぶことは少ない** ですが、「**裏で動いているのは LU**」と知っておくと安心。

---

## 3. QR 分解 — 数値安定性の王様

### 何をするか

任意の ($m \times n$, $m \geq n$) 行列 $A$ を、**直交行列 $Q$** と **上三角行列 $R$** の積に:

$$
A = Q R
$$

$Q$ は $Q^\top Q = I$ を満たす (列が正規直交)。
**回転 + 反転だけ** の変換、つまり「**長さや角度を変えない**」変換。

### なぜ嬉しいか

- **最小二乗法**: 「$A\mathbf{x} \approx \mathbf{b}$ を一番うまく満たす $\mathbf{x}$ を求める」のに数値安定
- **線形回帰の解法**: 内部で QR が使われる
- **直交化**: グラム＝シュミットの手続きの一般化

### Python

```python
A = np.array([[1.0, 2.0],
              [3.0, 4.0],
              [5.0, 6.0]])

Q, R = np.linalg.qr(A)
print('Q (直交):'); print(Q)
print('R (上三角):'); print(R)
print('検算 A ≈ Q @ R:', np.allclose(A, Q @ R))
print('検算 Q^T Q ≈ I:', np.allclose(Q.T @ Q, np.eye(Q.shape[1])))
```

### 線形回帰での使い方

最小二乗法: $\|\mathbf{y} - X\boldsymbol{\beta}\|^2$ を最小化する $\boldsymbol{\beta}$ を求める

| 解法 | 数式 | 安定性 |
|---|---|---|
| 解析解 | $\boldsymbol{\beta} = (X^\top X)^{-1} X^\top \mathbf{y}$ | ⚠️ 数値的に不安定 |
| QR で | $\boldsymbol{\beta} = R^{-1} Q^\top \mathbf{y}$ | ✅ 数値的に安定 |

scikit-learn の `LinearRegression` は内部で SVD/QR を使います (理由はこの安定性のため)。

---

## 4. Cholesky 分解 — 対称正定値行列の高速処理

### 何をするか

**対称正定値行列** (固有値が全部正の対称行列) $A$ を、**下三角行列 $L$** だけで:

$$
A = L L^\top
$$

LU 分解の特殊版で、**LU の半分の計算量**で済む。

### どこで出てくるか

- **共分散行列** (常に対称半正定値)
- **カーネル行列** (ガウス過程・SVM)
- **ハミルトニアンモンテカルロ** (ベイズ推論)

### Python

```python
A = np.array([[4.0, 1.0, 2.0],
              [1.0, 5.0, 0.0],
              [2.0, 0.0, 6.0]])     # 対称

L = np.linalg.cholesky(A)
print('L:'); print(L)
print('検算 A ≈ L Lᵀ:', np.allclose(A, L @ L.T))
```

> ⚠️ **正定値でないと失敗します**。
> 「半正定値だけど特異値0がある」ような行列だと Cholesky はエラー。
> その場合は SVD を使う。

---

## 5. SVD (特異値分解) — 線形代数の "King of Decompositions"

### 何をするか

**任意の ($m \times n$) 行列** を 3 つの行列に分解:

$$
A = U \Sigma V^\top
$$

- $U \in \mathbb{R}^{m \times m}$ — 左特異ベクトル、直交行列
- $\Sigma \in \mathbb{R}^{m \times n}$ — 対角成分が**特異値** (singular values)、降順、非負
- $V \in \mathbb{R}^{n \times n}$ — 右特異ベクトル、直交行列

特異値は「**$A$ の "強さ"** をいくつかの方向に分解した値」。

### 何が偉大か

1. **任意の長方行列に適用できる** (固有値分解は正方限定)
2. **常に存在する** (特異性に依存しない)
3. **数値的に超安定**
4. **ランクが分かる** (非ゼロ特異値の数 = ランク)
5. **データ圧縮ができる** (大きい特異値だけ残す)
6. **疑似逆行列が得られる** ($A^+ = V \Sigma^+ U^\top$)

### Python

```python
A = np.array([[1.0, 2.0, 3.0],
              [4.0, 5.0, 6.0]])     # (2, 3)

U, s, Vt = np.linalg.svd(A, full_matrices=False)
print('U:'); print(U)
print('s (特異値):', s)
print('Vᵀ:'); print(Vt)

# 復元
Sigma = np.diag(s)
reconstructed = U @ Sigma @ Vt
print('\n復元:'); print(reconstructed)
print('一致:', np.allclose(A, reconstructed))
```

### JAX 形式

```python
import jax.numpy as jnp
A_j = jnp.array(A)
U_j, s_j, Vt_j = jnp.linalg.svd(A_j, full_matrices=False)
```

### 低ランク近似 — データ圧縮

特異値が**急速に減衰する**ことが多いので、上位 $k$ 個だけ残せば近似できる:

$$
A \approx U_{:, :k} \cdot \mathrm{diag}(\sigma_{1:k}) \cdot V^\top_{:k, :}
$$

これが**画像圧縮**・**推薦システム**・**潜在意味解析**の基本原理。

```python
# 画像 (簡略例) を SVD で圧縮
img = np.random.standard_normal((100, 100))    # 仮の画像
U, s, Vt = np.linalg.svd(img, full_matrices=False)

# 上位 10 個の特異値だけで近似 (元データの 10% 未満で済む)
k = 10
img_approx = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]

# 誤差
relative_error = np.linalg.norm(img - img_approx) / np.linalg.norm(img)
print(f'k=10 での相対誤差: {relative_error:.4f}')
```

### 推薦システム

ユーザー × アイテム の評価行列 $R$ (大半が欠損) に対して:
1. SVD で $R \approx U \Sigma V^\top$
2. **$U$** がユーザーの潜在的な好み、**$V$** がアイテムの潜在的な特徴
3. 欠損部分の予測 = $U \cdot \mathrm{diag}(\sigma) \cdot V^\top$ の対応位置

Netflix の伝説的な「Netflix Prize コンテスト」(2006-2009) で、上位チームは全員 SVD 系のアルゴリズムを使っていました。

### 機械学習の用途まとめ

| 用途 | 使い方 |
|---|---|
| **PCA** | 共分散行列の SVD = 主成分 |
| **画像圧縮** | 低ランク近似 |
| **推薦システム** | 評価行列の補完 |
| **潜在意味解析 (LSA)** | 文書 × 単語行列を分解 |
| **疑似逆行列** | $A^+ = V \Sigma^+ U^\top$ |
| **正則化最小二乗** | 小さい特異値を切り捨て |
| **ノイズ除去** | 小さい特異値を切る |

---

## 6. 分解の選び方チートシート

| 状況 | 使う分解 |
|---|---|
| 連立方程式を解きたい (一般正方行列) | LU (np.linalg.solve が裏でやる) |
| 線形回帰・最小二乗 | QR または SVD |
| 共分散・カーネル行列の処理 | Cholesky |
| データの本質的な構造を見たい | **SVD** |
| データを圧縮したい | **SVD** |
| 行列のランクを知りたい | SVD (非ゼロ特異値の数) |
| 主成分分析 (PCA) | 固有値分解 (eigh) または SVD |
| 疑似逆行列が欲しい | SVD |

**迷ったら SVD**。汎用性と安定性が最強。

---

## まとめ

| 分解 | 形 | 適用条件 | 主な用途 |
|---|---|---|---|
| LU | $A = LU$ | 正方 | 連立方程式 |
| QR | $A = QR$ | 任意 ($m \geq n$) | 最小二乗、直交化 |
| Cholesky | $A = LL^\top$ | 対称正定値 | 共分散・ベイズ |
| SVD | $A = U\Sigma V^\top$ | 任意 | 圧縮・推薦・PCA・疑似逆 |
| 固有値 | $A = PDP^{-1}$ | 正方 | PCA、PageRank、力学 |

**この章のキー**:
- 行列を分解すると「速く」「安定に」「本質が見える」
- 機械学習で一番使うのは **SVD**
- ライブラリの裏側でも、これらが**毎日何兆回**動いている

## 次へ

→ [`02_calculus/README.md`](../02_calculus/README.md) — いよいよ微積分へ

## 関連
- [`03_eigenvalues.md`](03_eigenvalues.md) — SVD は固有値分解の親戚
- [`06_ml_math_bridge/`](../06_ml_math_bridge/) — SVD で推薦システム

---

## 🔍 ググってみよう

- **Netflix Prize** — 2006-2009 のコンテスト、SVD 系手法が大活躍
- **Latent Semantic Analysis (LSA)** — 文書を SVD で意味解析
- **Truncated SVD** — 大規模疎行列の SVD、`scipy.sparse.linalg.svds`
- **Randomized SVD** — 確率的に高速化したSVD
- **Eckart-Young theorem** — 「**SVD の上位 $k$ 項は最良の $k$ ランク近似**」を保証する定理
- **Pseudo-inverse (Moore-Penrose)** — 疑似逆行列、SVD で構築
- **Cholesky decomposition** — 1924 年に André-Louis Cholesky が発明
- **LAPACK** — 線形代数アルゴリズムの標準実装、Fortran 製
- **CUSOLVER** — NVIDIA GPU 上の線形代数ソルバ
- **Krylov subspace methods** — 大規模疎行列専用のソルバ群 (CG, GMRES, Lanczos)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`03_eigenvalues.md`](03_eigenvalues.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`../02_calculus/README.md`](../02_calculus/README.md) |
