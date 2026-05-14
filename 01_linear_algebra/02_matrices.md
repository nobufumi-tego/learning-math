# 01-2. 行列 — ベクトルを並べた、世界の主役

**このページのゴール**: 行列の演算（積・転置・逆行列）を、数式・Python・幾何学的意味の3面で理解する。

---

## 💡 このページのコードを動かすには

```bash
uv run jupyter lab
```

ファイルツリーから `01_linear_algebra/notebooks/02_matrices.ipynb` を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前に読むと理解が早い**:
> - [`01_vectors.md`](01_vectors.md) — このページの基礎（ベクトル）
> - [`00_notation/05_summation_product.md`](../00_notation/05_summation_product.md) — Σ 記号

---

## 1. 行列とは — ベクトルの並び

### 直感

行列 (matrix) とは、**数を縦横に並べた表**:

```
A = [ 1  2  3 ]
    [ 4  5  6 ]
```

これは **2行 × 3列** の行列。書き方は **`(2, 3) 行列`** または **`2×3 行列`**。

### 何の役に立つか

| 解釈 | 例 |
|---|---|
| **データセット** | 行=サンプル、列=特徴量 |
| **画像** | 縦×横 のピクセル値 (グレースケールなら1枚の行列) |
| **線形変換** | 「**ベクトルを別のベクトルに変換**」する操作 |
| **連立方程式** | `Ax = b` の形 |
| **グラフ (頂点間の繋がり)** | 隣接行列 |
| **マルコフ連鎖** | 状態遷移確率 |

機械学習では、**データもパラメータも、ほぼ全部行列**。
ニューラルネットの「層」は、**1つの行列の掛け算**で表されます。

### 記号

```
A ∈ ℝᵐˣⁿ      ← 「A は m行n列の実数行列」
```

要素は `A[i, j]` または `aᵢⱼ` と書きます (i行目、j列目)。

⚠️ **数学は1始まり**, **Python は0始まり**。これがバグの最頻出原因。

---

## 2. Python での行列

```python
# === 標準形式 (NumPy) ===
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6]])
print(A.shape)         # (2, 3) ← 2行3列
print(A.ndim)          # 2 (2次元配列)
print(A[0, 1])         # 2 ← 0行目、1列目（数学だと A[1, 2]）

# === JAX形式 ===
import jax.numpy as jnp
A_j = jnp.array([[1, 2, 3], [4, 5, 6]])
```

> 💡 **頻出操作**:
> ```python
> A.shape         # 行列の形
> A.T             # 転置 (後述)
> A[0, :]         # 0行目すべて (ベクトル)
> A[:, 1]         # 1列目すべて (ベクトル)
> A[0:2, 1:3]     # 部分行列を切り出し
> ```

---

## 3. 特別な行列たち

### ゼロ行列・1行列

```python
np.zeros((2, 3))      # 全要素0
np.ones((2, 3))       # 全要素1
np.full((2, 3), 7)    # 全要素7
```

### 単位行列 (identity matrix) `I`

対角線が1、他は0。**「掛け算の単位元」**:

```
I₃ = [ 1  0  0 ]
     [ 0  1  0 ]
     [ 0  0  1 ]
```

```python
np.eye(3)            # 3×3 単位行列
```

性質: 任意の行列 `A` に対し `A I = I A = A`。
数の世界で「× 1 は何も変えない」のと同じ。

### 対角行列 (diagonal matrix)

対角だけに値があり、他は0:

```python
np.diag([2, 3, 5])
# [[2 0 0]
#  [0 3 0]
#  [0 0 5]]
```

### 対称行列 (symmetric matrix)

`A = Aᵀ` を満たす行列。
共分散行列やカーネル行列など、機械学習で頻出。

```python
A = np.array([[1, 2, 3],
              [2, 5, 6],
              [3, 6, 9]])
print(np.allclose(A, A.T))    # True ← 対称
```

---

## 4. 転置 (transpose) — 行と列を入れ替える

```
A = [ 1  2  3 ]            Aᵀ = [ 1  4 ]
    [ 4  5  6 ]                  [ 2  5 ]
                                 [ 3  6 ]
```

shape は `(2, 3)` → `(3, 2)` に。

```python
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]
print(A.T.shape)     # (3, 2)

# JAX
print(jnp.array(A).T)
```

> 💡 **頻出**: 「**A の転置と A の積**」は、機械学習の「**正規方程式**」「**ガラムリン法**」「**自己相関行列**」など、あちこちで出てきます:
> ```python
> AtA = A.T @ A   # shape: (3, 3)
> ```

---

## 5. 行列とベクトルの積

行列 `A` (m×n) とベクトル `x` (n次元) の積 `Ax` は、**m次元ベクトル**を返す。

### 計算ルール

```
[ 1  2 ] [ 5 ]   [ 1×5 + 2×6 ]   [ 17 ]
[ 3  4 ] [ 6 ] = [ 3×5 + 4×6 ] = [ 39 ]
```

つまり「**A の各行と x の内積**」を並べたもの。

### Python

```python
A = np.array([[1, 2],
              [3, 4]])
x = np.array([5, 6])

print(A @ x)         # [17 39]
print(A.dot(x))      # 同じ

# JAX
print(jnp.array(A) @ jnp.array(x))
```

### 幾何学的解釈: 「線形変換」

`Ax` は **「x をAで変換した結果」**と解釈できます。
A は「変換の法則」。

```python
# 例: 反時計回りに 90 度回転する行列
import math
theta = math.pi / 2
R = np.array([[math.cos(theta), -math.sin(theta)],
              [math.sin(theta),  math.cos(theta)]])

x = np.array([1.0, 0.0])     # x軸方向の単位ベクトル
y = R @ x
print(y)                     # [0. 1.] ← 90度回って、y軸方向に
```

機械学習の「**ニューラルネットの1層**」は、結局この変換。
**`y = Wx + b`** の `Wx` の部分です。

---

## 6. 行列同士の積 — 線形代数のキング

### ルール

`A` (m×n) と `B` (n×p) の積 `AB` は、**(m×p) の行列**:

```
(A B)[i, j] = Σₖ A[i, k] × B[k, j]
```

つまり「**A の i行目と B の j列目の内積**」を、すべての (i, j) について計算。

### 重要: shape が合わないと計算できない

```
(2, 3) × (3, 4)  → (2, 4)   ✅ 中の3が一致
(2, 3) × (4, 3)  → ❌ エラー
```

> 💡 **覚え方**: **「内側が一致、外側が結果の shape」**

### Python

```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])         # shape: (2, 3)
B = np.array([[7,  8],
              [9,  10],
              [11, 12]])           # shape: (3, 2)

C = A @ B                          # shape: (2, 2)
print(C)
# [[ 58  64]
#  [139 154]]
print(C.shape)                     # (2, 2)
```

### 行列積の性質

| 性質 | 例 |
|---|---|
| **結合法則** | `(AB)C = A(BC)` ✅ |
| **分配法則** | `A(B + C) = AB + AC` ✅ |
| **可換じゃない** | 一般に `AB ≠ BA` ⚠️ |
| **転置と積** | `(AB)ᵀ = BᵀAᵀ` (順序が逆!) |

`AB ≠ BA` という事実は、線形代数の最大の罠の一つ。
普通の数の掛け算とは違うことを、**何度も自分に言い聞かせる**必要があります。

---

## 7. 逆行列 (inverse matrix)

### 定義

正方行列 `A` (n×n) に対して、`A⁻¹` という行列があれば:
```
A A⁻¹ = A⁻¹ A = I
```

これを **逆行列** と呼ぶ。
数の世界の「**逆数 (1/x)**」に対応します。

### 計算

```python
A = np.array([[1.0, 2.0],
              [3.0, 4.0]])

A_inv = np.linalg.inv(A)
print(A_inv)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# 確認: A × A⁻¹ ≈ I
print(A @ A_inv)
# [[1. 0.]
#  [0. 1.]]
```

### 連立方程式を解く

「`Ax = b` を `x` について解く」=「`x = A⁻¹ b`」。

```python
# 2x + y = 5
#  x + 3y = 10
A = np.array([[2.0, 1.0],
              [1.0, 3.0]])
b = np.array([5.0, 10.0])

x = np.linalg.inv(A) @ b
print(x)             # [1. 3.]   ← x=1, y=3

# でも実は np.linalg.solve のほうが推奨 (速くて精度高い)
x2 = np.linalg.solve(A, b)
print(x2)            # [1. 3.]
```

> ⚠️ **逆行列を直接計算するのはなるべく避ける**:
> 数値的に不安定で遅い。`np.linalg.solve` のほうが、内部でもっと賢いアルゴリズム（LU分解など）を使うので、**速くて精度も高い**。
> 機械学習でも「実装上は逆行列を計算しない」のが定石です。

### 逆行列が存在しない場合

すべての行列に逆行列があるわけではありません。
**行列式 (determinant)** が 0 だと逆行列なし。
これを **特異 (singular)** または **退化 (degenerate)** と言います。

```python
A = np.array([[1.0, 2.0],
              [2.0, 4.0]])         # 2行目 = 1行目 × 2 (情報が重複)
print(np.linalg.det(A))            # 0.0 ← 特異
# np.linalg.inv(A) はエラーになる
```

---

## 8. 行列式 (determinant) — 「拡大率」

### 直感

行列式は、**「その行列による線形変換が、空間をどれだけ拡大するか」** を表すスカラー。

- `det(A) = 2` → 面積 (2D) や体積 (3D) が 2倍
- `det(A) = 1` → 大きさは変わらない (回転など)
- `det(A) = -1` → 鏡映 (反転)
- `det(A) = 0` → 潰れて次元が下がる (情報の損失)

### Python

```python
A = np.array([[1.0, 2.0],
              [3.0, 4.0]])
print(np.linalg.det(A))            # -2.0  (1×4 − 2×3 = −2)
```

### 機械学習との接点

行列式は、**正規分布の確率密度関数** や **VAE (Variational AutoEncoder)** の **ヤコビアン項** で出てきます:

```
p(x) = (1 / √((2π)ⁿ |Σ|)) × exp(-½ (x-μ)ᵀ Σ⁻¹ (x-μ))
                  ↑
               これが行列式
```

---

## 9. ランク (rank) — 「行列が持つ情報量」

ランクとは、**行列の独立な行 (or 列) の数**。
- フル ランク = `min(m, n)` → 最大限の情報
- ランク不足 = 行や列に重複・依存があり、情報が減っている

```python
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(np.linalg.matrix_rank(A))    # 2 ← 3行あるが、独立なのは2つ
```

機械学習では、データの**有効な次元数**を測るのに使います (例: PCA、SVD)。

---

## 10. 機械学習でのフル活用例

### (1) ニューラルネット1層

```python
# 入力 x (10次元) → 出力 y (5次元)
import numpy as np

W = np.random.randn(5, 10)         # 重み行列 shape: (5, 10)
b = np.random.randn(5)              # バイアス shape: (5,)
x = np.random.randn(10)             # 入力 shape: (10,)

y = W @ x + b                       # shape: (5,)
print(y.shape)                      # (5,)
```

### (2) ミニバッチ処理 (32サンプルを同時に処理)

```python
batch = np.random.randn(32, 10)    # shape: (32, 10) 32サンプル
out = batch @ W.T + b               # shape: (32, 5)
print(out.shape)                    # (32, 5)
```

GPU はこれを並列で**爆速**実行します。だから現代AIは行列が大好き。

### (3) 推薦システム

```python
# ユーザー × アイテム の評価行列 (一部欠損)
R = np.array([
    [5, 4, 0, 1],   # ユーザー1
    [4, 0, 0, 1],   # ユーザー2
    [1, 1, 0, 5],   # ユーザー3
    [0, 0, 5, 4],   # ユーザー4
])
# これを R ≈ U × V^T と分解して、欠損を埋める
# (詳しくは 04_decompositions.md の SVD)
```

→ 詳細は [`04_decompositions.md`](04_decompositions.md) の SVD セクション

### (4) Transformer の Attention

```
Attention(Q, K, V) = softmax(Q Kᵀ / √d) V
```
すべて行列の積。ChatGPT/Claude/Gemini の中核も、行列。

---

## まとめ

| 概念 | 数式 | Python | shape変化 |
|---|---|---|---|
| 行列の作成 | A ∈ ℝᵐˣⁿ | `np.array([[..],..])` | – |
| 転置 | Aᵀ | `A.T` | (m,n) → (n,m) |
| 行列×ベクトル | Ax | `A @ x` | (m,n) × (n,) → (m,) |
| 行列×行列 | AB | `A @ B` | (m,n) × (n,p) → (m,p) |
| 逆行列 | A⁻¹ | `np.linalg.inv(A)` | (n,n) → (n,n) |
| 連立方程式 | Ax=b | `np.linalg.solve(A, b)` | – |
| 行列式 | det(A) | `np.linalg.det(A)` | スカラー |
| ランク | rank(A) | `np.linalg.matrix_rank(A)` | スカラー |

**この章のキー**: 行列はベクトルを別のベクトルに変換する装置。機械学習のすべての層は、結局行列の積。

## 次へ

→ [`03_eigenvalues.md`](03_eigenvalues.md) — 行列の「**深い構造**」を見る固有値・固有ベクトル

## 関連

- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — 行列演算の自動微分
- [`06_ml_math_bridge/`](../06_ml_math_bridge/) — 行列が損失関数に居る場面

---

## 🔍 ググってみよう

- **BLAS / LAPACK** — 線形代数演算の標準ライブラリ、NumPy/SciPy/JAX の裏側で動いている
- **GEMM** (General Matrix Multiplication) — 行列積の標準名
- **Strassen のアルゴリズム** — 行列積を O(n²·⁸¹) で計算する魔法
- **疎行列 (sparse matrix)** — 0が多い行列の効率的扱い、`scipy.sparse`
- **ブロードキャスト (NumPy)** — 形状の違う配列同士の演算規則
- **Einsum (`np.einsum`)** — 任意の行列演算を1行で書ける魔法
- **PyTorch / TensorFlow** — 行列演算を GPU で高速化するフレームワーク
- **CUDA** — NVIDIA の GPU 計算プラットフォーム
- **TPU** — Google が作った行列計算特化のハードウェア

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`01_vectors.md`](01_vectors.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`03_eigenvalues.md`](03_eigenvalues.md) |
