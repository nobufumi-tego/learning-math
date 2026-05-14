# 02-1. 極限 (limit) — 「近づく」を数学にする

**このページのゴール**: 極限の直感を掴み、Python で実際に「近づける」操作ができるようになる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`02_calculus/notebooks/01_limits.ipynb`](notebooks/01_limits.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`start_here/04_logarithm.md`](../start_here/04_logarithm.md) — 「e って何?」を素朴に理解
> - [`00_notation/01_basic_symbols.md`](../00_notation/01_basic_symbols.md) — `lim` `∞` の記号
> - [`00_notation/05_summation_product.md`](../00_notation/05_summation_product.md) — Σ の感覚

---

## 1. 極限とは — 「ぴったりは無理だけど、いくらでも近づく」

### 直感

「**コップの水を半分ずつ飲む**」を想像してください。
- 1回目: $\frac{1}{2}$ 残る
- 2回目: $\frac{1}{4}$ 残る
- 3回目: $\frac{1}{8}$ 残る
- ...

永遠に **「ゼロにはならない」** けど、**「いくらでもゼロに近づく」**。

数学ではこれを次のように書きます:

$$
\lim_{n \to \infty} \left(\frac{1}{2}\right)^n = 0
$$

読み方: 「**$n$ が無限大に近づくとき、$\left(\frac{1}{2}\right)^n$ の極限は $0$**」。

**極限 (limit)** とは、「**到達しないけど、いくらでも近づける値**」のことです。

### もう1つの例: $0$ で割る話

$f(x) = \dfrac{\sin(x)}{x}$ という関数。
$x = 0$ を入れると $\frac{0}{0}$ になるので、本当は計算できないはず。

でも、**$x$ をどんどん $0$ に近づけていく** と…

| $x$ | $\sin(x) / x$ |
|---|---|
| $1.0$ | $0.8415$ |
| $0.1$ | $0.9983$ |
| $0.01$ | $0.99998$ |
| $0.001$ | $0.9999998$ |
| ... | ... |

→ **どんどん $1$ に近づく** ことが分かります。これを数学では:

$$
\lim_{x \to 0} \frac{\sin(x)}{x} = 1
$$

と書きます。これが **極限の威力**: **そのままでは計算できないものに、意味を与える** ことができる。

---

## 2. 記号と読み方

| 記号 | 読み方 | 意味 |
|---|---|---|
| $\lim_{x \to a} f(x)$ | "the limit of f(x) as x approaches a" | $x$ が $a$ に限りなく近づくときの値 |
| $\lim_{x \to \infty}$ | "as x approaches infinity" | $x$ が無限大に近づくとき |
| $\lim_{x \to 0^+}$ | "approaches 0 from the right" | 右から $0$ に近づく (正の側) |
| $\lim_{x \to 0^-}$ | "approaches 0 from the left" | 左から $0$ に近づく (負の側) |

> 💡 **$x \to a$ は $x = a$ ではない**。「**$a$ に近づくが、$a$ そのものは含まない**」がポイント。

---

## 3. Python で「近づける」を体感

### 標準形式 (NumPy で数値的に)

```python
import numpy as np

# sin(x) / x の x → 0 を観察
xs = np.array([1.0, 0.1, 0.01, 0.001, 0.0001, 0.00001])
ys = np.sin(xs) / xs

for x, y in zip(xs, ys):
    print(f"x = {x:.6f}  →  sin(x)/x = {y:.10f}")
```

**$1$ にどんどん近づく** のが見えます。

### 標準形式 (SymPy で記号的に厳密計算)

NumPy は数値近似ですが、**SymPy** は数学者と同じ「**厳密な記号計算**」をしてくれます:

```python
import sympy as sp

x = sp.Symbol('x')
result = sp.limit(sp.sin(x) / x, x, 0)
print(result)
# → 1   (厳密に 1 と分かる)
```

便利な極限の例:

```python
import sympy as sp
from sympy import oo  # ∞ の記号

x = sp.Symbol('x')

# lim x→∞ 1/x = 0
print(sp.limit(1/x, x, sp.oo))

# lim x→0 (1+x)^(1/x) = e (← e の定義そのもの!)
print(sp.limit((1 + x)**(1/x), x, 0))

# lim x→∞ (1 + 1/x)^x = e (← e のもう1つの定義)
print(sp.limit((1 + 1/x)**x, x, sp.oo))
```

最後の 2 行、感動しませんか? **$e$ (ネイピア数) は極限から定義される** という事実が Python で確かめられます:

$$
e = \lim_{x \to 0} (1 + x)^{1/x} = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n
$$

詳しくは → [`start_here/columns/04_e_and_pi.md`](../start_here/columns/04_e_and_pi.md)

### JAX 形式 (自動微分・JIT 用の数値計算)

```python
import jax.numpy as jnp
import jax

# JAX で数値的に近づける (NumPy とほぼ同じ)
xs = jnp.array([1.0, 0.1, 0.01, 0.001, 0.0001])
ys = jnp.sin(xs) / xs
print(ys)
```

> 💡 JAX は「数値計算の高速化」が得意で、**SymPy のような厳密記号計算は不向き**。極限の確認には NumPy + SymPy を、ML で実際に勾配を計算するときに JAX を使う、という使い分けが定石です。

---

## 4. 連続性 — 「グラフを書くときに筆を離さなくていい」関数

ある関数 $f(x)$ が **「$x = a$ で連続」** とは、ざっくり:

> **$a$ の近くで $f(x)$ が "ジャンプ" しないこと**

数式で書くと:

$$
\lim_{x \to a} f(x) = f(a)
$$

「$x$ を $a$ に近づけたときの値」と「$x = a$ を直接代入した値」が **一致する** こと。

### 連続じゃない例

階段関数 (床関数 $\lfloor x \rfloor$):

$x = 1$ の前後で:
- $x \to 1^-$ (左から近づく): $f(0.999) = 0$
- $x \to 1^+$ (右から近づく): $f(1.001) = 1$

→ **左右で値が違う = 不連続**。

### Python で確かめる

```python
import numpy as np

# floor 関数は x = 1 で不連続
print(np.floor(0.9999))   # 0.0
print(np.floor(1.0))      # 1.0
print(np.floor(1.0001))   # 1.0
# 0 から 1 に "ジャンプ" している
```

機械学習では、**損失関数を連続にすること** が訓練を安定させるのに重要 (不連続だと勾配が定義できない)。

---

## 5. ML / AI への接続

### 勾配降下法は「極限」から生まれる

ニューラルネットの学習で頻出する **勾配** は:

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

これは「**$h$ を限りなく $0$ に近づけたときの差分**」、つまり**極限**。
**極限がなければ微分も存在しない、微分がなければ機械学習も存在しない** わけです。

### ソフトマックスの正規化定数

ソフトマックスでよく見る $Z = \sum_i \exp(z_i)$ も、極限的に「どの $z$ が支配的か」を見るときに、**温度パラメータ $\tau$** を変化させて極限を考えます:

- $\tau \to \infty$: すべて一様 (どれも同じ確率)
- $\tau \to 0$: 最大値だけ確率 $1$ ($\arg\max$ と同じ)

これも極限の応用です。

---

## 6. ハマりポイント

- **「近づく」≠「等しい」**: $\lim_{x \to a} f(x) = L$ でも $f(a) \neq L$ のことがある (関数の値が定義されてない場合など)
- **左右の極限が違うことがある**: 階段関数のように、左から近づくか右から近づくかで値が変わる
- **数値計算は精度に注意**: あまりに小さい $h$ を使うと、浮動小数点誤差で逆に精度が落ちる (例: $h = 10^{-30}$ だと壊れる)

---

## まとめ

| 概念 | 数式 | Python |
|---|---|---|
| 極限 | $\lim_{x \to a} f(x)$ | `sympy.limit(f, x, a)` |
| 無限大 | $\infty$ | `numpy.inf` / `sympy.oo` |
| 連続 | $\lim_{x \to a} f(x) = f(a)$ | グラフがジャンプしない |
| 自然対数 $e$ の定義 | $\lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n$ | `(1+1/n)**n` |

**この章のキー**: 極限は「ぴったりは無理だけど近づく」を数学にする道具。微分の土台。

---

## 次へ

→ [`02_derivatives.md`](02_derivatives.md) — 微分: 極限を使って「変化の速さ」を測る

## 関連
- [`start_here/columns/04_e_and_pi.md`](../start_here/columns/04_e_and_pi.md) — 極限から定義される $e$
- [`07_jax/02_autodiff.md`](../07_jax/02_autodiff.md) — JAX なら勾配を一瞬で

---

## 🔍 ググってみよう

- **ε-δ 論法** — 極限の厳密な定義 (大学初年度の難所)
- **連続関数 (continuous function)** — 微分・積分の前提
- **コーシー列 (Cauchy sequence)** — 極限の現代的な定義の出発点
- **解析学 (analysis)** — 極限を中心に発展した数学の分野
- **e (ネイピア数)** — $\lim_{n\to\infty}(1+1/n)^n$ で定義される自然対数の底
- **L'Hôpital の定理** — $\frac{0}{0}$ 形の極限を解く必殺技
- **Taylor 展開** — 関数を多項式の極限で表現する技法

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [章 TOP](README.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`02_derivatives.md`](02_derivatives.md) |
