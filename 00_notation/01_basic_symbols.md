# 基本記号

数値・関係を表す基本記号。中学・高校で見たものから、大学院でも使うものまで。

## 等号・不等号系

| 記号 | 読み方（英 / 日） | 意味 | Python |
|---|---|---|---|
| `=` | "equals" / 「等しい」 | 等しい | `==`（比較）／ `=`（代入） |
| `≠` | "not equal" / 「等しくない」 | 等しくない | `!=` |
| `≈` | "approximately equal" / 「ほぼ等しい」 | 近似的に等しい | `np.isclose(a, b)` |
| `≡` | "identical / equivalent" / 「合同」「定義」 | 定義する、または恒等的に等しい | コメントで表現 |
| `:=` | "is defined as" / 「定義する」 | 左辺を右辺で定義 | `=`（代入） |
| `<`, `>` | "less / greater than" | 小なり、大なり | `<`, `>` |
| `≤`, `≥` | "less / greater than or equal" | 以下、以上 | `<=`, `>=` |
| `≪`, `≫` | "much less / greater than" | はるかに小さい / 大きい | （コメントで表現） |

> ### ✒️ この記号の生まれ — `=`
>
> 等号 `=` は **1557 年**、ウェールズの医師 **ロバート・レコード**が考案しました。
> それまでは「等しい」を毎回 `is equalle to` と**単語で書いていた**のです。
>
> 彼が平行線を選んだ理由が洒落ています。
> **「2 本の平行線ほど、互いに等しいものはないから」**。
>
> なお普及までには約 150 年かかり、あのデカルトは別の記号を使い続けました。
>
> 📖 続き → [`columns/00_birth_of_equals.md`](columns/00_birth_of_equals.md)（Python の `=` と `==` が食い違う理由も、ここに繋がります）

### Python 例

```python
import numpy as np

a = 0.1 + 0.2
b = 0.3
print(a == b)                  # False（浮動小数点誤差）
print(np.isclose(a, b))        # True（≈ の Python 版）
```

## 数の集合（最頻出）

| 記号 | 読み方 | 意味 | Python での扱い |
|---|---|---|---|
| `ℕ` | "natural numbers" / 自然数 | 0, 1, 2, 3, ... | `int`（0以上） |
| `ℤ` | "integers" / 整数 | ..., -2, -1, 0, 1, 2, ... | `int` |
| `ℚ` | "rationals" / 有理数 | 分数で表せる数 | `fractions.Fraction` |
| `ℝ` | "real numbers" / 実数 | すべての実数 | `float`（近似） |
| `ℂ` | "complex numbers" / 複素数 | a + bi の形 | `complex` |
| `ℝⁿ` | "R-n" / n次元実空間 | n個の実数の組 | `np.ndarray` shape (n,) |

### Python 例

```python
import numpy as np

# ℝ³（3次元実空間）の元
x: np.ndarray = np.array([1.0, 2.0, 3.0])  # shape: (3,)

# ℂ の元
z: complex = 2 + 3j
print(z.real, z.imag)  # 2.0 3.0
```

## 無限・極限系

| 記号 | 読み方 | 意味 | Python |
|---|---|---|---|
| `∞` | "infinity" / 無限大 | 無限 | `float('inf')`, `np.inf` |
| `-∞` | "minus infinity" / 負の無限大 | 負の無限 | `-np.inf` |
| `lim` | "limit" / 極限 | 極限を取る | `sympy.limit(...)` |

```python
import numpy as np
import sympy as sp

print(np.inf > 1e100)          # True
print(1.0 / np.inf)            # 0.0

x = sp.Symbol("x")
print(sp.limit(1/x, x, sp.oo)) # 0  (lim x→∞ 1/x = 0)
```

## その他の頻出記号

| 記号 | 読み方 | 意味 |
|---|---|---|
| `±` | "plus minus" / 「プラスマイナス」 | 正負両方 |
| `∝` | "proportional to" / 「比例する」 | 比例（**定数倍の違いを無視する**） |
| `\|` | "given" / 「〜が与えられたとき」 | 条件（縦棒の**右が既知**、左が知りたいこと） |
| `∴` | "therefore" / 「ゆえに」 | 結論 |
| `∵` | "because" / 「なぜなら」 | 理由 |
| `□`, `∎`, `QED` | "Q.E.D." / 「証明終わり」 | 証明終了 |

### ⚠️ `∝` は「どうでもいい定数を捨てた」の合図

$y \propto x$ は「$y = cx$ となる定数 $c$ がある」という意味です。**$c$ が何かは言っていません。**

なぜわざわざこう書くかというと、**その定数を計算するのが大変（または不要）だから**です。
ベイズ統計がその代表例で、

$$
\pi(\theta \mid x) \propto L(\theta; x)\,\pi(\theta)
$$

と書いたら「本当は右辺をある積分で割るのだが、その積分は $\theta$ に依存しないので、
**分布の形を知るだけなら無視してよい**」と宣言しています。

> 📌 論文で $\propto$ を見たら「**ここで何かを省略した**」と読み、
> 「省略されたのは何で、なぜ省いてよいのか」を探す癖をつけてください。
> → [`03_probability_statistics/08_bayesian_inference.md`](../03_probability_statistics/08_bayesian_inference.md)

### ⚠️ 縦棒 `|` は「これは既に分かっている」の宣言

$P(A \mid B)$ は「B が起きたと**分かっている**ときの A の確率」。**縦棒の右側は確定した情報**です。

| 表記 | 読み | 何が既知か |
|---|---|---|
| $P(A \mid B)$ | "P of A given B" | $B$ |
| $\pi(\theta \mid x)$ | "pi of theta given x" | データ $x$（＝観測済み） |
| $X_i \mid \theta \sim \mathrm{Bernoulli}(\theta)$ | – | $\theta$ を固定したときの $X_i$ の分布 |

> ⚠️ **$P(A \mid B)$ と $P(B \mid A)$ はまったく別物です。**
> 「病気なら陽性が出る確率」と「陽性なら病気である確率」は数値が全然違います。
> この 2 つを行き来する道具がベイズの定理 → [`03_probability_statistics/04_bayes.md`](../03_probability_statistics/04_bayes.md)
>
> なお、同じ縦棒でも $|x|$（絶対値）、$\|x\|$（ノルム）、$\{x \mid P(x)\}$（集合の「〜であるような」）、
> $a \mid b$（整除）は**別の意味**です。**両側に何があるか**で判断してください。

## 関連: `/project:explain-symbol`

理解が曖昧な記号があれば、Claude Code で次のように質問:

```
/project:explain-symbol ≡
```

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [章 TOP](README.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`02_set_theory.md`](02_set_theory.md) |
