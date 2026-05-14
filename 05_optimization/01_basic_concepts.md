# 05-1. 最適化の基本 — 最小化問題と凸性

**このページのゴール**: 最適化問題の枠組みと、ML を簡単にする「凸性」の概念を理解する。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`05_optimization/notebooks/01_basic_concepts.ipynb`](notebooks/01_basic_concepts.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`02_calculus/02_derivatives.md`](../02_calculus/02_derivatives.md) — 微分
> - [`02_calculus/04_multivariable.md`](../02_calculus/04_multivariable.md) — 偏微分・勾配

---

## 1. 最適化問題とは — 「一番良い答え」を探す

### 直感

私たちの日常は最適化だらけ:

- 一番安い往復ルートを探す (Google Maps)
- 一番美味しい組み合わせを選ぶ (献立)
- 一番幸せになる人生選択 (難問)
- **損失が一番小さくなるパラメータを探す (機械学習!)**

### 数式での定式化

最適化問題は次のように書きます:

$$
\min_{\mathbf{x} \in \mathcal{X}} f(\mathbf{x})
$$

意味: 「**集合 $\mathcal{X}$ の中で、関数 $f(\mathbf{x})$ を最小にする $\mathbf{x}$ を見つけよ**」

| 用語 | 意味 |
|---|---|
| $f(\mathbf{x})$ | **目的関数 (objective function)** — 最小化したい量 |
| $\mathbf{x}$ | **決定変数** — 動かせるパラメータ |
| $\mathcal{X}$ | **実行可能領域** — $\mathbf{x}$ が取れる範囲 |
| $\mathbf{x}^*$ | **最適解** — $f$ を最小化する $\mathbf{x}$ |

### 機械学習での例

ニューラルネットの訓練:

$$
\min_{\boldsymbol{\theta}} L(\boldsymbol{\theta}) = \min_{\boldsymbol{\theta}} \frac{1}{N} \sum_{i=1}^{N} \ell(\hat{y}(x_i; \boldsymbol{\theta}), y_i)
$$

「**パラメータ $\boldsymbol{\theta}$ を動かして、平均損失を最小化する**」。

最適化アルゴリズム (勾配降下法など) で $\boldsymbol{\theta}$ を更新する → これが**学習**そのもの。

---

## 2. 最大化と最小化は同じ問題

「収益を**最大化**したい」 = 「マイナス収益を**最小化**したい」:

$$
\max f(\mathbf{x}) \iff \min \bigl(-f(\mathbf{x})\bigr)
$$

なので最適化理論では、**最小化問題に統一**して扱います。
ML の「**尤度を最大化**」も内部では「**負の対数尤度を最小化**」しています。

---

## 3. 最適性の必要条件 — 「勾配 = 0」

### 1 変数の場合

$f'(x) = 0$ となる $x$ が**極値の候補**。

- **極小**: $f''(x) > 0$ (グラフが上に凸の谷)
- **極大**: $f''(x) < 0$ (グラフが下に凸の山)

### 多変数の場合

$\nabla f(\mathbf{x}) = \mathbf{0}$ が**極値の候補**。

ヘッセ行列 $H_f$ の固有値の符号で判定 (→ [`02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md)):

| 固有値 | 種類 |
|---|---|
| 全部正 | **極小点** (最適解候補) |
| 全部負 | 極大点 |
| 正負混在 | **鞍点** (saddle point) |

### Python で「勾配ゼロ」を確認

```python
import jax
import jax.numpy as jnp

def f(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2

grad_f = jax.grad(f)
print(grad_f(jnp.array([1.0, 2.0])))   # [0.0, 0.0]  ← 最小点!
print(grad_f(jnp.array([0.0, 0.0])))   # [-2.0, -4.0]  ← 最小点ではない
```

---

## 4. 局所最適 vs 大域最適

### 概念

| 種類 | 定義 |
|---|---|
| **局所最適 (local minimum)** | その近所で一番低い |
| **大域最適 (global minimum)** | 全体で一番低い |

ML では多くの場合、損失関数が**非凸**で多くの局所最適を持ちます。
「学習で収束した」 ≠ 「世界一良いパラメータが見つかった」。

### Python で確かめる

```python
import numpy as np

# 関数: f(x) = x⁴ - 4x² + x + 5
# 局所最適と大域最適を持つ
def f(x):
    return x**4 - 4*x**2 + x + 5

xs = np.linspace(-3, 3, 200)
ys = f(xs)

# どこに極小点があるか
import matplotlib.pyplot as plt
plt.plot(xs, ys)
plt.show()
# → 2つの谷 (異なる深さ) が見える
```

---

## 5. 凸関数 — 「綺麗な谷」を持つ関数

### 直感

**凸関数 (convex function)** は「**お椀型**」の関数:

- 局所最適 = 大域最適 (谷が1つしかない)
- 勾配降下で必ず最適解に到達できる
- ML 理論で**極めて重要**

### 数式での定義

任意の $\mathbf{x}_1, \mathbf{x}_2$ と $\lambda \in [0, 1]$ に対して:

$$
f\bigl(\lambda \mathbf{x}_1 + (1-\lambda) \mathbf{x}_2\bigr) \leq \lambda f(\mathbf{x}_1) + (1-\lambda) f(\mathbf{x}_2)
$$

意味: 「**2 点を結ぶ線分が、関数のグラフの上にある**」 = グラフが下に凸。

### よく見る凸関数

| 関数 | 凸? |
|---|---|
| $f(x) = x^2$ | ✅ 凸 (お椀) |
| $f(x) = e^x$ | ✅ 凸 |
| $f(x) = -\ln(x)$ ($x > 0$) | ✅ 凸 |
| $f(x) = x^4$ | ✅ 凸 |
| $\|\mathbf{x}\|^2$ (ユークリッドノルムの2乗) | ✅ 凸 |
| ロジスティック損失 | ✅ 凸 |
| $\sin(x)$ | ❌ 非凸 |
| ニューラルネットの損失 | ❌ ほぼ常に非凸 |

### 強凸 (strongly convex)

「**お椀の底が尖っている**」凸関数:

$$
f(\mathbf{y}) \geq f(\mathbf{x}) + \nabla f(\mathbf{x})^\top (\mathbf{y} - \mathbf{x}) + \frac{\mu}{2} \|\mathbf{y} - \mathbf{x}\|^2
$$

$\mu > 0$ が **強凸性パラメータ**。$\mu$ が大きいほど鋭く凹む。
強凸だと**収束速度の理論的保証**が得やすい。

### ヘッセ行列で判定

$f: \mathbb{R}^n \to \mathbb{R}$ が 2 階微分可能なら:

| ヘッセ行列の固有値 | $f$ の性質 |
|---|---|
| 全部 $\geq 0$ (半正定値) | **凸** |
| 全部 $> 0$ (正定値) | **強凸** |

```python
import jax
import jax.numpy as jnp

def f(x):
    return x[0]**2 + 2*x[1]**2

H = jax.hessian(f)(jnp.array([0.0, 0.0]))
eigvals = jnp.linalg.eigvalsh(H)
print(eigvals)  # [2., 4.] → 全部正 → 強凸 ✅
```

---

## 6. 制約付き最適化

### 制約あり問題

決定変数が動ける範囲 $\mathcal{X}$ に**制約**がある場合:

$$
\min f(\mathbf{x}) \quad \text{s.t.} \quad g_i(\mathbf{x}) \leq 0, \quad h_j(\mathbf{x}) = 0
$$

- $g_i \leq 0$: **不等式制約** (例: 予算上限)
- $h_j = 0$: **等式制約** (例: 確率の和=1)
- s.t. = "subject to" (〜という条件のもとで)

### ラグランジュ乗数法 (Lagrange multiplier)

等式制約付きの最適化を解く必殺技:

$$
\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_j \lambda_j h_j(\mathbf{x})
$$

$\nabla_{\mathbf{x}} \mathcal{L} = 0$ かつ $\nabla_{\boldsymbol{\lambda}} \mathcal{L} = 0$ を解く。

> 💡 **KKT 条件** (Karush-Kuhn-Tucker conditions) は不等式制約版の一般化。SVM などの理論的基礎。

---

## 7. 最適化アルゴリズムの分類

| 分類 | 代表 | 特徴 |
|---|---|---|
| **勾配を使う** | 勾配降下、Adam、SGD | ML の本命 (次の章) |
| **2階情報を使う** | Newton法、L-BFGS | 速いが計算重い |
| **勾配を使わない** | Nelder-Mead、CMA-ES | ノイズの多い目的関数向け |
| **離散最適化** | 整数計画、グラフ探索 | TSP、スケジューリング |
| **メタヒューリスティック** | 遺伝的アルゴリズム、焼きなまし法 | 大域探索 |

ML では**1次の勾配法 (SGD系)** が圧倒的に主流。次の章で詳しく。

---

## 8. ML / AI への接続

### 訓練 = 最適化問題

すべての ML は次の形に帰着:

$$
\min_{\boldsymbol{\theta}} \frac{1}{N} \sum_{i=1}^{N} \ell\bigl(f(x_i; \boldsymbol{\theta}), y_i\bigr) + \lambda R(\boldsymbol{\theta})
$$

| 項 | 意味 |
|---|---|
| $\ell$ | 損失関数 (MSE, クロスエントロピーなど) |
| $f$ | モデル (線形・ニューラルネット) |
| $\boldsymbol{\theta}$ | 学習するパラメータ |
| $\lambda R(\boldsymbol{\theta})$ | 正則化項 (過学習防止) |

これを最小化するのが**訓練 (training)**。
詳しくは → [`06_ml_math_bridge/01_loss_functions.md`](../06_ml_math_bridge/01_loss_functions.md)

### 凸性の夢と現実

| アルゴリズム | 損失関数の凸性 | 大域最適保証 |
|---|---|---|
| 線形回帰 (MSE) | ✅ 凸 | ✅ |
| ロジスティック回帰 | ✅ 凸 | ✅ |
| SVM | ✅ 凸 | ✅ |
| **ニューラルネット** | ❌ **非凸** | ❌ (実用上は十分良い解) |

NN が非凸なのに使えるのは、**勾配降下法が高次元空間ではほぼ良い解に辿り着く**経験的事実 (理由は研究中)。

---

## 9. ハマりポイント

- **「最適化収束」≠「真の最適解」**: 局所最適に捕まる可能性
- **凸性の確認は重要**: 凸ならアルゴリズム選びが楽
- **数値勾配 vs 解析勾配**: ML では `jax.grad` で解析勾配を必ず使う
- **学習率 (step size) の調整**: 大きすぎると発散、小さすぎると遅い (次の章で)

---

## まとめ

| 概念 | 数式 | 意味 |
|---|---|---|
| 最小化問題 | $\min_{\mathbf{x}} f(\mathbf{x})$ | 一番低い点を探す |
| 最適性条件 | $\nabla f(\mathbf{x}^*) = \mathbf{0}$ | 勾配ゼロが候補 |
| 凸関数 | $f(\lambda \mathbf{x}_1 + (1-\lambda)\mathbf{x}_2) \leq \lambda f(\mathbf{x}_1) + (1-\lambda)f(\mathbf{x}_2)$ | お椀型、局所=大域 |
| 強凸 | ヘッセ行列が正定値 | 谷の底が尖る |
| 制約付き | $\min f(\mathbf{x})$ s.t. $g_i \leq 0$ | 動ける範囲が限定 |

**この章のキー**: 最適化 = 一番良い答えを探す問題。凸関数なら勾配降下で確実に最適解に到達。

## 次へ

→ [`02_gradient_descent.md`](02_gradient_descent.md) — 勾配降下法 (ML の本命アルゴリズム)

## 関連
- [`02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md) — 勾配・ヘッセ行列
- [`06_ml_math_bridge/`](../06_ml_math_bridge/README.md) — 損失関数として何を使うか

---

## 🔍 ググってみよう

- **凸最適化 (convex optimization)** — Stephen Boyd の名著がある
- **CVXPY** — Python で凸最適化を直感的に書けるライブラリ
- **KKT 条件** — 不等式制約付き最適化の最適性条件
- **線形計画法 (Linear Programming, LP)** — 線形目的・線形制約の特殊ケース
- **二次計画法 (Quadratic Programming, QP)** — SVM の最適化問題はこれ
- **大域最適化 (global optimization)** — 局所最適を脱出する技法
- **ミニマックス (minimax)** — GAN や敵対的訓練で頻出
- **凸結合 (convex combination)** — 確率分布の混合などで頻出

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [章 TOP](README.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`02_gradient_descent.md`](02_gradient_descent.md) |
