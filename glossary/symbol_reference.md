# 数学記号リファレンス

論文・教科書・生成AIの出力で出てきた記号を逆引きする用。
学習を進めながら**新しい記号に出会ったら必ずここに追記**する。

> 💡 **読み方も載せています。** 記号は「声に出して読めない」と頭に残りません。
> $\hat{y}$ は「ワイ・ハット」、$\bar{x}$ は「エックス・バー」。英語論文を読むとき、頭の中で読み上げられるかどうかで理解速度が変わります。

## 目次

| # | セクション | 主な内容 |
|---|---|---|
| 1 | [関係・等号](#1-関係等号) | `=` `≈` `∝` `≪` |
| 2 | [数の集合](#2-数の集合) | `ℝ` `ℕ` `ℝⁿ` `ℝ^{m×n}` |
| 3 | [集合](#3-集合) | `∈` `∪` `∩` `∅` |
| 4 | [論理](#4-論理) | `∀` `∃` `⇒` `⇔` |
| 5 | [関数](#5-関数) | `f: A → B` `f∘g` `‖x‖` |
| 6 | [総和・総乗・積分](#6-総和総乗積分) | `Σ` `Π` `∫` `∇` `n!` `C(n,k)` |
| 7 | [**文字につく飾り**](#7-文字につく飾りハットバーチルダ) | **`x̂` `x̄` `x̃` `x*` `ẋ`** ← 推定のハットはここ |
| 8 | [**書体の違い**](#8-書体の違い) | **`ℝ` `ℒ` `𝐱` `θ`** |
| 9 | [線形代数](#9-線形代数) | `Aᵀ` `A⁻¹` `I` `λ` `⊙` `‖x‖₂` |
| 10 | [確率・統計](#10-確率統計) | `P` `𝔼` `Var` `σ` `⊥⊥` `𝒩` |
| 11 | [最適化](#11-最適化) | `argmin` `s.t.` `η` `≽` |
| 12 | [機械学習で頻出](#12-機械学習で頻出) | `θ` `ℒ` `𝒟` `∇θ` `ŷ` |
| 13 | [その他](#13-その他よく見るもの) | `∞` `O(·)` `∴` `∎` |

---

## 1. 関係・等号

| 記号 | 読み方（英/日） | 意味 | Python |
|---|---|---|---|
| `=` | equals / 等しい | 等しい | `==` / `=` |
| `≠` | not equal / 等しくない | 等しくない | `!=` |
| `≈` | approximately / ほぼ等しい | 近似 | `np.isclose` |
| `≡` | identical / 合同・定義 | 定義する / 恒等的に等しい | コメントで |
| `:=` | defined as / 定義する | 左辺を右辺で定義 | `=` |
| `∝` | proportional to / 比例 | 比例（定数倍を無視）。ベイズの $P(\theta \mid D) \propto P(D \mid \theta)P(\theta)$ で頻出 | – |
| `≪` `≫` | much less / much greater | 桁違いに小さい / 大きい | – |
| `∼` | tilde / チルダ | 「同程度」または「分布に従う」（文脈による） | – |
| `→` | tends to / 収束する | 極限で近づく | – |

---

## 2. 数の集合

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `ℕ` | natural numbers | 自然数 | `int` (≥0) |
| `ℤ` | integers（ドイツ語 Zahlen） | 整数 | `int` |
| `ℚ` | rationals（Quotient） | 有理数 | `fractions.Fraction` |
| `ℝ` | reals / 実数 | 実数 | `float` |
| `ℂ` | complex | 複素数 | `complex` |
| `ℝⁿ` | R n / アール・エヌ | n 次元実ベクトル空間 | `np.ndarray` shape `(n,)` |
| `ℝ^{m×n}` | R m by n | m 行 n 列の実行列全体 | `np.ndarray` shape `(m, n)` |
| `[0, 1]` | closed interval | 閉区間（両端を含む） | – |
| `(0, 1)` | open interval | 開区間（両端を含まない） | – |

> 📌 **$\mathbf{x} \in \mathbb{R}^n$ は「shape 宣言」です。** 論文でこれを見たら
> 「$\mathbf{x}$ は要素数 $n$ の配列」と読み替えてください。$W \in \mathbb{R}^{m \times n}$ なら `W.shape == (m, n)`。
> **形状の不一致は最頻出のバグ源**なので、数式を読む段階で shape を把握する習慣が効きます。

---

## 3. 集合

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `∈` | element of / 属する | 属する | `in` |
| `∉` | not element of | 属さない | `not in` |
| `⊂` `⊊` | proper subset | 真部分集合 | `<` |
| `⊆` | subset | 部分集合 | `<=` |
| `∪` | union / 和 | 和集合 | `\|` |
| `∩` | intersection / 積 | 共通部分 | `&` |
| `\` | set minus | 差集合 | `-` |
| `∅` | empty set | 空集合 | `set()` |
| `\|A\|` | cardinality / 濃度 | 要素数 | `len(A)` |
| `×` | Cartesian product | 直積 | `itertools.product` |
| `{x \| P(x)}` | set-builder | 条件 P を満たす x の集合 | 内包表記 |

詳しくは [`00_notation/02_set_theory.md`](../00_notation/02_set_theory.md)。

---

## 4. 論理

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `∀` | for all / すべての | 全称量化 | `all(...)` |
| `∃` | there exists / 存在する | 存在量化 | `any(...)` |
| `∃!` | exists unique | ただ1つ存在する | – |
| `∧` | and / かつ | 論理積 | `and` / `&` |
| `∨` | or / または | 論理和 | `or` / `\|` |
| `¬` | not / 否定 | 否定 | `not` / `~` |
| `⇒` | implies / ならば | 含意 | `not P or Q` |
| `⇔` | if and only if / 同値 | 同値（iff） | `P == Q` |
| `s.t.` | such that | 「〜であるような」 | `if` |

詳しくは [`00_notation/03_logic_symbols.md`](../00_notation/03_logic_symbols.md)。

---

## 5. 関数

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `f: A → B` | f from A to B | f は A から B への関数 | `def f(...) -> B:` |
| `x ↦ f(x)` | x maps to f(x) | x を f(x) に写す | `lambda x: ...` |
| `f ∘ g` | f composed with g | 合成関数 $f(g(x))$ | `lambda x: f(g(x))` |
| `f⁻¹` | f inverse | 逆関数 | – |
| `f⁽ⁿ⁾(x)` | n-th derivative of f | n 階微分。**`f²` の「2乗」とは別物** | `sp.diff(f, x, n)` |
| `\|x\|` | absolute value | 絶対値 | `abs(x)` |
| `‖x‖` | norm of x | ノルム（長さ） | `np.linalg.norm(x)` |
| `⌊x⌋` | floor | 床（切り捨て） | `math.floor` |
| `⌈x⌉` | ceiling | 天井（切り上げ） | `math.ceil` |
| `1[条件]`, `𝟙` | indicator function | 条件が真なら 1、偽なら 0 | `int(cond)` / `(arr > 0).astype(float)` |
| `sgn(x)` | sign | 符号（−1, 0, +1） | `np.sign` |

詳しくは [`00_notation/04_function_notation.md`](../00_notation/04_function_notation.md)。

---

## 6. 総和・総乗・積分

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `Σ` | sigma / 総和 | すべて足す | `np.sum`, `sum` |
| `Π` | pi (product) / 総乗 | すべて掛ける | `np.prod`, `math.prod` |
| `∫` | integral | 積分（定積分は `∫_a^b`） | `scipy.integrate.quad` / `sympy.integrate` |
| `∬` | double integral | 二重積分 | `scipy.integrate.dblquad` |
| `d/dx`, `'` | derivative / プライム | 微分 | `sympy.diff` |
| `∂/∂x` | partial / パーシャル | 偏微分 | `sympy.diff(f, x)` |
| `∇` | nabla / del / ナブラ | 勾配（全偏微分を並べたベクトル） | `jax.grad(f)` |
| `∇²`, `Δ` | Laplacian | ラプラシアン（2階微分の和） | – |
| `n!` | n factorial | 階乗 n×(n−1)×…×1、`0! = 1` | `math.factorial(n)` |
| `C(n,k)`, `ₙCₖ` | n choose k | 二項係数（組合せ） | `math.comb(n, k)` |

二項係数は論文では縦に積んだ形で書かれます:

$$
\binom{n}{k} = \frac{n!}{k!\,(n-k)!}
$$

読み方は「エヌ・チューズ・ケー」。分数ではないので横線を書かないことに注意。

詳しくは [`00_notation/05_summation_product.md`](../00_notation/05_summation_product.md)、[`02_calculus/`](../02_calculus/README.md)。

---

## 7. 文字につく飾り（ハット・バー・チルダ）

**このセクションが記号読解の最大の関門です。**

同じ文字 $x$ でも、上に何が乗っているかで**まったく別のもの**を指します。
そして飾りの意味は**分野によって変わります**。

| 記号 | 読み方 | 主な意味 | Python での対応 |
|---|---|---|---|
| `x̂` | **x hat** / エックス・ハット | **推定値・予測値**（データから求めた値） | 計算結果の変数 |
| `x̄` | **x bar** / エックス・バー | **標本平均**（データの平均） | `x.mean()` |
| `x̃` | **x tilde** / エックス・チルダ | 修正版・近似版・別バージョン | – |
| `x*` | **x star** / エックス・スター | 最適値・真の値・共役 | 最適化の解 |
| `ẋ` | **x dot** / エックス・ドット | 時間微分 $dx/dt$（物理でよく使う） | – |
| `x₀` | x naught / x zero | 初期値・特定の点 | 初期化した変数 |
| `x⁽ⁱ⁾` | x superscript i | **i 番目のサンプル**（ML の慣習。累乗ではない） | `X[i]` |
| `xᵢ` | x sub i | i 番目の**成分** | `x[i]` |

### 7-1. ハットが最重要 — 「真の値」と「推定した値」を区別する記号

統計学と機械学習では、次の 2 つを厳密に区別します:

| | 記号 | 何か | 知っているか |
|---|---|---|---|
| **真の値** | $\theta$（シータ） | 神様だけが知っている本当の値 | ❌ 知りえない |
| **推定値** | $\hat{\theta}$（シータ・ハット） | 手元のデータから計算した値 | ✅ 計算できる |

この区別こそが統計学の出発点です。

> **ハットは「これはデータから推定したものであって、本物ではない」という宣言**です。

だから統計学の問いは、いつもこの形になります:

$$
\hat{\theta} \text{ は } \theta \text{ にどれくらい近いのか?}
$$

そしてこの「近さ」を分解したものが、[`03_probability_statistics/03_expectation_variance.md`](../03_probability_statistics/03_expectation_variance.md) で扱うバイアス-バリアンス分解です:

$$
\mathrm{MSE}(\hat{f}) = \underbrace{\mathrm{Var}[\hat{f}]}_{\text{推定のブレ}} + \underbrace{\mathrm{Bias}^2[\hat{f}]}_{\text{系統的なズレ}} + \underbrace{\sigma^2}_{\text{どうにもならないノイズ}}
$$

### 7-2. ⚠️ 同じハットが分野で違う意味になる

**このリポジトリの中だけでも、ハットは 3 つの意味で登場します。**

| 記号 | 出てくる場所 | 意味 |
|---|---|---|
| $\hat{\mathbf{v}} = \dfrac{\mathbf{v}}{\|\mathbf{v}\|}$ | [`01_linear_algebra/01_vectors.md`](../01_linear_algebra/01_vectors.md) | **単位ベクトル**（長さ 1 に正規化したベクトル） |
| $\hat{f}$, $\hat{\theta}$ | [`03_probability_statistics/`](../03_probability_statistics/README.md) | **推定量**（データから推定した関数・パラメータ） |
| $\hat{y}$ | [`06_ml_math_bridge/01_loss_functions.md`](../06_ml_math_bridge/01_loss_functions.md) | **予測値**（モデルの出力。正解 $y$ と対比される） |

線形代数のハットは「長さ 1 にした」、統計の帽子は「推定した」。**まったく無関係の意味**です。

見分け方: **ベクトル（太字）に付いていれば単位ベクトル、パラメータや予測に付いていれば推定値**。文脈で判断するしかありません。

> 💡 これは記号読解の重要な教訓です。**記号の意味は記号自体には書かれていません。**
> 「この論文のこの文脈では何を指すか」を、定義が書かれた箇所まで戻って確認する癖をつけてください。
> 同種の罠に $\|x\|$（ノルム / 絶対値 / 集合の濃度）、$O(\cdot)$（テイラーの剰余 / 計算量）があります。

### 7-3. Python で書くとどうなるか

数式のハットやバーは、コードでは**ただの変数名**になります。慣習的な書き方:

```python
import numpy as np

# 真の値 (シミュレーションなので今回は知っている)
theta_true: float = 2.5          # θ    真のパラメータ

# データ
x: np.ndarray = np.array([2.3, 2.7, 2.4, 2.6, 2.5])  # shape: (5,)

# 推定値・標本統計量
x_bar: float = float(x.mean())    # x̄    標本平均
theta_hat: float = x_bar          # θ̂    推定量 (ここでは標本平均を推定に使う)

print(f'θ  (真の値) = {theta_true}')
print(f'x̄ (標本平均) = {x_bar}')
print(f'θ̂ (推定値)  = {theta_hat}')
print(f'推定誤差     = {abs(theta_hat - theta_true):.4f}')
```

命名の慣習は `theta_hat` / `x_bar` / `theta_star`。
コメントに元の記号（`# θ̂`）を書いておくと、数式とコードを行き来しやすくなります。

---

## 8. 書体の違い

**なぜ `R` と `ℝ` を書き分けるのか。**

数式では**同じアルファベットを書体で区別**します。論文を読むとき、書体の違いは意味の違いです。

| 書体 | 例 | 名前 | 何を表すか | LaTeX |
|---|---|---|---|---|
| 黒板太字 | $\mathbb{R}$, $\mathbb{E}$, $\mathbb{N}$ | blackboard bold | **数の集合**、期待値 | `\mathbb{R}` |
| 花文字 | $\mathcal{L}$, $\mathcal{N}$, $\mathcal{D}$ | calligraphic / script | **損失関数・分布・データ集合** | `\mathcal{L}` |
| 太字（ローマン） | $\mathbf{x}$, $\mathbf{A}$ | bold | **ベクトル・行列** | `\mathbf{x}` |
| 太字（ギリシャ） | $\boldsymbol{\theta}$, $\boldsymbol{\mu}$ | bold symbol | **ベクトルになったパラメータ** | `\boldsymbol{\theta}` |
| 立体（ローマン） | $\mathrm{Var}$, $\mathrm{d}x$ | roman | **関数名・演算子**（変数でないことを示す） | `\mathrm{Var}` |
| 斜体 | $x$, $n$ | italic | **スカラー変数**（デフォルト） | `x` |

### 太字かどうかで shape が変わる

これは実務上いちばん効く区別です:

| 数式 | 読み | Python の shape |
|---|---|---|
| $x$ | スカラー | `float` / `()` |
| $\mathbf{x}$ | ベクトル | `(n,)` |
| $\mathbf{A}$ | 行列 | `(m, n)` |
| $\theta$ | スカラーのパラメータ | `float` |
| $\boldsymbol{\theta}$ | パラメータをまとめたベクトル | `(d,)` |

$\mathbf{y} = \mathbf{A}\mathbf{x}$ を見たら「行列 × ベクトル = ベクトル」、
つまり `y = A @ x` で `(m,n) @ (n,) -> (m,)` だと即座に読めるのが目標です。

> ⚠️ **手書きや一部の論文では太字が区別されないことがあります。**
> その場合は「$\mathbf{x} \in \mathbb{R}^n$」のような宣言文を探して shape を確認してください。

### 混同しやすいペア

| ペア | 違い |
|---|---|
| $N$ と $\mathcal{N}$ | 前者はサンプル数などの変数、後者は**正規分布** |
| $L$ と $\mathcal{L}$ | 前者は変数、後者は**損失関数 (Loss)** または**尤度 (Likelihood)** |
| $E$ と $\mathbb{E}$ | 前者は変数、後者は**期待値** |
| $\Sigma$ と $\sum$ | 前者は**共分散行列**、後者は**総和記号**（同じギリシャ文字シグマの大文字） |
| $\sigma$ と $\Sigma$ | 前者は標準偏差、後者は共分散行列（大文字か小文字か） |

ギリシャ文字そのものは [`00_notation/06_greek_letters.md`](../00_notation/06_greek_letters.md) を参照。

---

## 9. 線形代数

### 9-1. 行列の基本操作

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `Aᵀ`, `A'`, `Aᵗ` | A transpose | 転置（行と列を入れ替え） | `A.T` |
| `A⁻¹` | A inverse | 逆行列 | `np.linalg.inv(A)` |
| `A⁺` | A dagger / pseudo-inverse | 擬似逆行列（正方でなくても使える） | `np.linalg.pinv(A)` |
| `Aᴴ`, `A*` | A Hermitian / conjugate transpose | 共役転置（複素数版の転置） | `A.conj().T` |
| `det(A)`, `\|A\|` | determinant | 行列式（体積の拡大率） | `np.linalg.det(A)` |
| `tr(A)` | trace | トレース（対角成分の和） | `np.trace(A)` |
| `rank(A)` | rank | ランク（独立な行/列の数） | `np.linalg.matrix_rank(A)` |
| `I`, `Iₙ`, `E` | identity matrix | 単位行列（対角が 1） | `np.eye(n)` |
| `O`, `𝟎` | zero matrix | 零行列 | `np.zeros((m, n))` |
| `𝟏` | ones vector | 全要素が 1 のベクトル | `np.ones(n)` |
| `diag(a)` | diagonal | 対角行列を作る / 対角成分を取る | `np.diag(a)` |

### 9-2. 積の種類（混同注意）

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `AB`, `A·B` | matrix product | 行列積 | `A @ B` |
| `⟨u, v⟩`, `u·v` | inner product / dot | 内積（スカラーが出る） | `u @ v` / `np.dot(u, v)` |
| `u ⊙ v`, `u ∘ v` | Hadamard product / element-wise | **要素ごとの積**（形は変わらない） | `u * v` |
| `u ⊗ v`, `A ⊗ B` | Kronecker / outer product | クロネッカー積・外積 | `np.kron(A, B)` / `np.outer(u, v)` |
| `u × v` | cross product | 外積（3次元ベクトル、ベクトルが出る） | `np.cross(u, v)` |

> ⚠️ **NumPy の `*` は行列積ではありません。** `A * B` は要素ごとの積 $A \odot B$、
> 行列積は `A @ B` です。数式の $AB$ をそのまま `A * B` と書くのは最頻出のバグです。

### 9-3. ノルム（長さの測り方）

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `‖x‖`, `‖x‖₂` | L2 norm / Euclidean | ユークリッド距離 $\sqrt{\sum x_i^2}$ | `np.linalg.norm(x)` |
| `‖x‖₁` | L1 norm / Manhattan | 絶対値の和（Lasso で使う） | `np.linalg.norm(x, 1)` |
| `‖x‖∞` | L-infinity / max norm | 最大絶対値 | `np.linalg.norm(x, np.inf)` |
| `‖x‖₀` | L0 "norm" | 非ゼロ要素の数（厳密にはノルムでない） | `np.count_nonzero(x)` |
| `‖A‖_F` | Frobenius norm | 行列の全要素の二乗和の平方根 | `np.linalg.norm(A, 'fro')` |

### 9-4. 固有値・空間

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `λ` | lambda | 固有値 | `np.linalg.eigvals(A)` |
| `Av = λv` | – | 固有値方程式 | `np.linalg.eig(A)` |
| `σᵢ` | sigma i | 特異値（SVD） | `np.linalg.svd(A)` |
| `span{v₁,…}` | span | 張られる空間 | – |
| `dim(V)` | dimension | 次元 | – |
| `ker(A)`, `N(A)` | kernel / null space | 核・零空間（$A\mathbf{x}=\mathbf{0}$ の解） | `scipy.linalg.null_space(A)` |
| `im(A)`, `R(A)` | image / range | 像・列空間 | – |
| `u ⊥ v` | orthogonal / 直交 | 内積が 0 | `u @ v == 0` |
| `A ≻ 0` | positive definite | 正定値（固有値がすべて正） | `np.all(np.linalg.eigvals(A) > 0)` |
| `A ⪰ 0` | positive semi-definite | 半正定値（固有値がすべて 0 以上） | – |

詳しくは [`01_linear_algebra/`](../01_linear_algebra/README.md)（特に [`03_eigenvalues.md`](../01_linear_algebra/03_eigenvalues.md), [`04_decompositions.md`](../01_linear_algebra/04_decompositions.md)）。

---

## 10. 確率・統計

### 10-1. 確率

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `P(A)` | probability of A | A の確率 | – |
| `P(A \| B)` | P of A given B | 条件付き確率（`\|` は「〜が与えられたとき」） | – |
| `P(A ∩ B)`, `P(A, B)` | joint probability | 同時確率 | – |
| `X ~ D` | X follows D / X is distributed as D | X は分布 D に従う | `rng.<dist>(...)` |
| `X ⊥⊥ Y` | X independent of Y | 独立（$P(X,Y)=P(X)P(Y)$） | – |
| `X ⊥⊥ Y \| Z` | conditionally independent | Z を条件として独立 | – |
| `f(x)`, `p(x)` | probability density function | 確率密度関数 (PDF) | `stats.norm.pdf` |
| `F(x)` | cumulative distribution function | 累積分布関数 (CDF) | `stats.norm.cdf` |
| `Φ(x)`, `φ(x)` | Phi / phi | 標準正規分布の CDF / PDF | `stats.norm.cdf` / `.pdf` |

### 10-2. 期待値・ばらつき

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `𝔼[X]`, `E[X]` | expectation / expected value | 期待値（理論上の平均） | `np.mean`（標本で近似） |
| `𝔼[X \| Y]` | conditional expectation | 条件付き期待値 | – |
| `Var[X]`, `σ²` | variance | 分散（ばらつきの二乗） | `np.var` |
| `SD[X]`, `σ` | standard deviation | 標準偏差（分散の平方根） | `np.std` |
| `Cov[X, Y]` | covariance | 共分散 | `np.cov` |
| `Σ` (大文字) | covariance matrix | 共分散行列（総和記号と別物） | `np.cov(X.T)` |
| `ρ`, `corr` | rho / correlation | 相関係数（−1 〜 +1） | `np.corrcoef` |
| `μ` | mu | 母平均（真の平均） | – |
| `x̄` | x bar | 標本平均（データの平均） | `x.mean()` |
| `s²` | sample variance | 標本分散（不偏分散は `ddof=1`） | `np.var(x, ddof=1)` |

> 📌 **$\mu$ と $\bar{x}$ の違いが統計学の核心です。**
> $\mu$ は「本当の平均」（知りえない）、$\bar{x}$ は「手元のデータの平均」（計算できる）。
> $\bar{x}$ を使って $\mu$ を推定する、というのが統計的推測の基本構造です。[第 7 節](#7-文字につく飾りハットバーチルダ)も参照。

### 10-3. 推定

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `θ` | theta | 真のパラメータ（未知） | – |
| `θ̂` | **theta hat** | **推定量**（データから計算した値） | 計算結果 |
| `θ̂_MLE` | MLE | 最尤推定量 | `scipy.optimize.minimize`（負の対数尤度） |
| `θ̂_MAP` | MAP | 事後確率最大化推定量 | – |
| `L(θ)`, `ℒ(θ)` | likelihood | 尤度（そのパラメータでデータが出る確率） | – |
| `ℓ(θ)` | log-likelihood | 対数尤度（計算しやすくした尤度） | – |
| `Bias[θ̂]` | bias | 偏り（推定量の系統的なズレ） | – |
| `MSE` | mean squared error | 平均二乗誤差 = 分散 + バイアス² | – |
| `CI` | confidence interval | 信頼区間 | `stats.norm.interval` |
| `p 値` | p-value | 帰無仮説のもとでの「珍しさ」 | `stats.ttest_1samp` |

### 10-4. 主な分布

| 記号 | 読み方 | 分布 | Python |
|---|---|---|---|
| `𝒩(μ, σ²)`, `N(μ, σ²)` | normal / Gaussian | 正規分布 | `stats.norm` |
| `Bin(n, p)` | binomial | 二項分布 | `stats.binom` |
| `Bern(p)` | Bernoulli | ベルヌーイ分布（コイン 1 回） | `stats.bernoulli` |
| `Pois(λ)` | Poisson | ポアソン分布（稀な事象の回数） | `stats.poisson` |
| `U(a, b)` | uniform | 一様分布 | `stats.uniform` |
| `Exp(λ)` | exponential | 指数分布（待ち時間） | `stats.expon` |
| `Beta(α, β)` | beta | ベータ分布（確率の確率、ベイズで頻出） | `stats.beta` |
| `χ²(k)` | chi-squared | カイ二乗分布 | `stats.chi2` |
| `t(ν)` | Student's t | t 分布（小標本の検定） | `stats.t` |

### 10-5. 情報理論（ML で頻出）

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `H(X)` | entropy | エントロピー（不確実さの量） | `stats.entropy` |
| `H(p, q)` | cross entropy | 交差エントロピー（分類の損失関数） | `jax.nn.log_softmax` と組み合わせ |
| `D_KL(p ‖ q)` | KL divergence | KL ダイバージェンス（分布間の「ズレ」） | `stats.entropy(p, q)` |
| `I(X; Y)` | mutual information | 相互情報量 | `sklearn.metrics.mutual_info_score` |

> ⚠️ KL ダイバージェンスの `‖` は**ノルムではなく区切り記号**です。$D_{KL}(p \,\|\, q)$ は
> 「p から見た q のズレ」。$D_{KL}(p\|q) \ne D_{KL}(q\|p)$ で**対称ではありません**（距離ではない）。

詳しくは [`03_probability_statistics/`](../03_probability_statistics/README.md)。

---

## 11. 最適化

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `argmin f(x)` | arg min | f を最小にする **x**（値ではない） | `scipy.optimize.minimize` |
| `argmax f(x)` | arg max | f を最大にする x | `-` を付けて最小化 |
| `min f(x)` | min | 最小**値** | – |
| `s.t.` | subject to | 制約条件 | `constraints=...` |
| `η` | eta | 学習率 (learning rate) | `lr` |
| `α` | alpha | 学習率 or 正則化係数（分野で違う） | – |
| `λ` | lambda | 正則化係数 or ラグランジュ乗数 or 固有値 | – |
| `∇f = 0` | – | 停留点の条件（一階の必要条件） | – |
| `θ ← θ − η∇L` | – | 勾配降下法の更新式 | `params -= lr * grads` |
| `≼`, `≽` | preceq / succeq | 半順序（凸最適化の制約） | – |

> ⚠️ **`argmin` と `min` の違い**: $\min_x f(x)$ は「最小値そのもの」、
> $\arg\min_x f(x)$ は「最小値を与える $x$」。ML で欲しいのはたいてい **argmin**（最適なパラメータ）です。

詳しくは [`05_optimization/`](../05_optimization/README.md)。

---

## 12. 機械学習で頻出

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `θ`, `𝛉` | theta | モデルのパラメータ（重みの総称） | `params` |
| `w`, `𝐰` | w / weights | 重みベクトル | `w` |
| `b` | bias | バイアス項（切片） | `b` |
| `ŷ` | **y hat** | **モデルの予測値**（正解 `y` と対比） | `y_pred` |
| `y` | y | 正解ラベル (ground truth) | `y_true` |
| `ℒ(θ)`, `J(θ)` | loss / cost | 損失関数・目的関数 | `loss` |
| `𝒟` | data set | データセット | – |
| `x⁽ⁱ⁾`, `xᵢ` | i-th sample | i 番目のサンプル（**累乗ではない**） | `X[i]` |
| `N`, `n` | – | サンプル数 | `len(X)` |
| `d`, `D` | – | 特徴量の次元 | `X.shape[1]` |
| `∇_θ ℒ` | grad of L w.r.t. theta | θ に関する勾配 | `jax.grad(loss)` |
| `η`, `lr` | eta | 学習率 | `lr` |
| `σ(·)` | sigmoid | シグモイド関数（活性化） | `jax.nn.sigmoid` |
| `softmax(·)` | – | 確率化する関数 | `jax.nn.softmax` |
| `ReLU(·)` | rectified linear unit | $\max(0, x)$ | `jax.nn.relu` |
| `𝔼_{x∼𝒟}[·]` | expectation over D | データ分布での期待値 | データ平均で近似 |

> 📌 **$x^{(i)}$ の上付きカッコは「i 番目のサンプル」で、累乗ではありません。**
> ML 論文の慣習で、$x_i$（成分）との衝突を避けるために使われます。
> [第 5 節](#5-関数)の $f^{(n)}$（n 階微分）とも別物なので、文脈で判断してください。

詳しくは [`06_ml_math_bridge/`](../06_ml_math_bridge/README.md)、[`07_jax/`](../07_jax/README.md)。

---

## 13. その他よく見るもの

| 記号 | 読み方 | 意味 |
|---|---|---|
| `∞` | infinity | 無限大 |
| `O(·)` | big O | ランダウの記号。テイラー展開では「これ以降の項を省略」、計算量では「増え方の上界」。**分野で意味が変わる代表例** → [`02_calculus/06_taylor_series.md`](../02_calculus/06_taylor_series.md) |
| `o(·)`, `Θ(·)`, `Ω(·)` | little o / theta / omega | それぞれ「真に小さい」「同オーダー」「下界」 |
| `∴` | therefore | ゆえに |
| `∵` | because | なぜなら |
| `□`, `∎`, `QED` | – | 証明終わり |
| `≜` | defined as | 定義する |
| `⋯`, `⋮`, `⋱` | dots | 省略（横・縦・斜め） |
| `w.r.t.` | with respect to | 「〜に関して」（微分の対象を示す） |
| `i.e.` / `e.g.` | id est / exempli gratia | 「すなわち」/「たとえば」 |
| `WLOG` | without loss of generality | 一般性を失わずに |

---

## つまずいたときの調べ方

記号が読めないときの手順:

1. **このファイルを Ctrl+F** で検索（記号そのもの、または「ハット」「バー」などの読み方で）
2. **飾り**（ハット等）なら [第 7 節](#7-文字につく飾りハットバーチルダ)、**書体**の違いなら [第 8 節](#8-書体の違い)
3. 載っていなければ Claude Code で `/explain-symbol <記号>`
4. **論文中でその記号が最初に定義された箇所まで戻る**（記号の意味は分野・著者によって変わるため、これが最も確実）

## 追記方法

新しい記号に出会ったら:

1. このファイルの該当セクションに行を追加
2. **読み方**（英語での読み上げ方）を必ず入れる
3. 同じ意味の Python があれば必ず併記
4. 分野で意味が変わる記号なら、その旨を明記

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [用語集 TOP](README.md) | [用語集 TOP](README.md) | [📚 ROOT README](../README.md) | [`jp_en_terms.md`](jp_en_terms.md) |
