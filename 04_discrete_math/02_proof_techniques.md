# 04-2. 証明の技法 — 直接証明・背理法・帰納法

**このページのゴール**: 数学的な証明の 3 大技法を理解し、定理を読めるようになる。論文の "Proof" セクションがブラックボックスでなくなる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`04_discrete_math/notebooks/02_proof_techniques.ipynb`](notebooks/02_proof_techniques.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`01_logic.md`](01_logic.md) — 命題論理

---

## 1. 証明とは — 「論理の連鎖で真であることを示す」

### 直感

「**ある命題が真である**」 ことを、**既に認められた命題 (公理・定理)** から**論理規則**で導く文章。

例:
- 命題: 「$\sqrt{2}$ は無理数である」
- 証明: ピタゴラス教団のヒッパソスが発見 (背理法)

数学では証明されたものだけが「**定理**」と呼ばれる。

---

## 2. 直接証明 (Direct Proof)

### 構造

「$P \Rightarrow Q$」を証明したいとき:
1. $P$ を仮定する
2. 論理を積み重ねて $Q$ を導く

### 例: 「$n$ が偶数なら $n^2$ も偶数」

**定理**: $n \in \mathbb{Z}$ が偶数なら、$n^2$ も偶数である。

**証明**:
- $n$ が偶数なので、$n = 2k$ ($k \in \mathbb{Z}$) と書ける。
- すると $n^2 = (2k)^2 = 4k^2 = 2 \cdot (2k^2)$。
- $2k^2 \in \mathbb{Z}$ なので、$n^2$ は $2 \times$ 整数。
- ゆえに $n^2$ は偶数。 $\blacksquare$

### Python で例を確認

```python
import numpy as np

# 多くの偶数で確認
for n in range(2, 21, 2):
    print(f'{n}² = {n**2},  偶数? {n**2 % 2 == 0}')
```

> 💡 **重要**: コンピュータでいくつ確認しても**証明にはならない**。100 万個の例で成り立っても、$n = 10^9$ で破れる可能性が残る。**論理的に普遍を示す**のが証明。

---

## 3. 背理法 (Proof by Contradiction)

### 構造

「$P$ である」を示したいとき:
1. $\neg P$ を仮定する
2. 矛盾を導く
3. ゆえに $\neg P$ は偽 → $P$ は真

### 例: 「$\sqrt{2}$ は無理数である」

**定理**: $\sqrt{2}$ は無理数である (= 整数の比 $a/b$ で表せない)。

**証明 (背理法)**:
- $\sqrt{2}$ が有理数だと仮定。すると $\sqrt{2} = a/b$ ($a, b \in \mathbb{Z}$, **既約分数**, $b > 0$) と書ける。
- 両辺を2乗: $2 = a^2 / b^2 \implies a^2 = 2 b^2$。
- よって $a^2$ は偶数 → $a$ も偶数 (前節の対偶)。
- $a = 2k$ と書けて、$4k^2 = 2b^2 \implies b^2 = 2k^2$ → $b^2$ は偶数 → $b$ も偶数。
- $a, b$ がどちらも偶数だと、**既約分数**の仮定に矛盾。
- ゆえに $\sqrt{2}$ は有理数ではない、つまり無理数。$\blacksquare$

ピタゴラス教団のヒッパソスが命懸けで発見した話 → [`start_here/columns/01_pythagoras_story.md`](../start_here/columns/01_pythagoras_story.md)

### Python でシミュレーション

```python
import numpy as np
from fractions import Fraction

# 多くの分数を試して √2 に一致するか確認
sqrt2 = np.sqrt(2)

for denom in range(1, 1000):
    for num in range(1, denom * 2):
        if abs(num / denom - sqrt2) < 1e-15:
            print(f'発見: {num}/{denom}')
            break
    else:
        continue
    break
else:
    print('1000 までの分母では一致なし → 無理数の証拠 (証明ではない)')
```

---

## 4. 数学的帰納法 (Mathematical Induction)

### 構造

「すべての $n \in \mathbb{N}$ で $P(n)$ が真」を示したいとき:
1. **基底**: $P(1)$ (または $P(0)$) が真であることを示す
2. **帰納ステップ**: $P(k)$ が真と仮定して、$P(k+1)$ も真と示す
3. ゆえに任意の $n$ で $P(n)$ が真

「**ドミノ倒し**」のイメージ:
- 最初のドミノが倒れる (基底)
- $k$ 番目が倒れたら $k+1$ 番目も倒れる (帰納ステップ)
- → すべてのドミノが倒れる

### 例: 「$1 + 2 + \dots + n = \dfrac{n(n+1)}{2}$」

**定理**: 任意の $n \in \mathbb{N}$ について、

$$
\sum_{i=1}^n i = \frac{n(n+1)}{2}
$$

**証明 (帰納法)**:

**(基底)** $n = 1$ のとき:

$$
\text{左辺} = 1, \quad \text{右辺} = \frac{1 \cdot 2}{2} = 1
$$

→ 一致 ✅

**(帰納ステップ)** $P(k)$ が成り立つと仮定。つまり $1 + 2 + \dots + k = \frac{k(k+1)}{2}$ とする。

$P(k+1)$ を示したい:

$$
1 + 2 + \dots + k + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}
$$

→ $P(k+1)$ が成り立つ ✅

ゆえに任意の $n$ で $P(n)$ は真。$\blacksquare$

### Python で確認

```python
def sum_formula(n):
    return n * (n + 1) // 2

for n in [1, 5, 10, 100, 1_000_000]:
    actual = sum(range(1, n + 1))
    formula = sum_formula(n)
    print(f'n={n:>10}: 直接和={actual:>20},  公式={formula:>20},  一致={actual == formula}')
```

これも「シミュレーション」であり証明ではない。**証明は数式のみで行う**。

---

## 5. 対偶による証明 (Proof by Contrapositive)

「$P \Rightarrow Q$」 と $\neg Q \Rightarrow \neg P$ は**同値** (対偶) なので、後者を証明してもよい。

### 例

**定理**: $n^2$ が偶数なら $n$ も偶数 (前節の逆)。

**直接証明は難しい**。対偶を取ると:

「$n$ が奇数なら $n^2$ は奇数」

これなら直接証明できる:
- $n = 2k + 1$ と書ける。
- $n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$ → 奇数。$\blacksquare$

---

## 6. 構成的証明 vs 非構成的証明

### 構成的 (Constructive)

「**実際に作って見せる**」証明。例: $\sqrt{2}$ より大きい無理数を見つけよ → $\sqrt{3}$ を提示。

### 非構成的 (Non-constructive)

「**存在は分かるが、具体的なものは作れない**」証明。

例: **「$x^y$ が有理数となる無理数 $x, y$ が存在する」**

**証明**:
- $\sqrt{2}^{\sqrt{2}}$ が有理数ならOK ($x = y = \sqrt{2}$)
- 無理数なら、$x = \sqrt{2}^{\sqrt{2}}$, $y = \sqrt{2}$ とおく
  - $x^y = (\sqrt{2}^{\sqrt{2}})^{\sqrt{2}} = \sqrt{2}^2 = 2$ → 有理数!
- どちらの場合も存在する。$\blacksquare$

実は $\sqrt{2}^{\sqrt{2}}$ が有理数か無理数か、この証明では**分からない**。
それでも「存在する」とは結論できる。

---

## 7. ML / AI への接続

### 帰納法と再帰

帰納法は**再帰関数**の正しさの証明と密接:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

「$\text{factorial}(n) = n!$」 を**帰納法で証明**できる:
- 基底: $\text{factorial}(0) = 1 = 0!$
- 帰納: $\text{factorial}(k) = k!$ なら $\text{factorial}(k+1) = (k+1) \cdot k! = (k+1)!$

### 形式的検証 (Formal Verification)

Coq、Lean、Isabelle などの**証明支援系**で、ソフトウェアやハードウェアの正しさを数学的に証明する分野。
航空機の制御系、暗号システムなどで使われる。

### ML 理論

**学習理論** (PAC learning, VC dimension など) は厳密な証明で構築される。
「サンプル数がいくつなら誤差 ε 以下で学習できるか」 を保証する**汎化境界**などが定理として証明されている。

---

## 8. ハマりポイント

- **シミュレーション ≠ 証明**: 100 万個成り立っても証明にはならない
- **「明らかに」を多用しない**: 自分には明らかでも、読者にはそうでないことが多い
- **基底を忘れない**: 帰納法では $P(1)$ または $P(0)$ の確認が必要
- **対偶と裏 (converse) を混同しない**: $P \Rightarrow Q$ の対偶は $\neg Q \Rightarrow \neg P$、裏は $\neg P \Rightarrow \neg Q$ (これは別物!)

---

## まとめ

| 技法 | 構造 | 例 |
|---|---|---|
| 直接証明 | $P \Rightarrow $ 計算 $\Rightarrow Q$ | 偶数の 2 乗は偶数 |
| 背理法 | $\neg P$ 仮定 → 矛盾 | $\sqrt{2}$ は無理数 |
| 帰納法 | 基底 + 帰納ステップ | $\sum i = n(n+1)/2$ |
| 対偶 | $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$ | 「平方が奇数なら〜」 |

**この章のキー**: 証明は「論理の連鎖」。3 大技法 (直接・背理法・帰納法) を覚えれば論文の Proof セクションが読める。

## 次へ

→ [`03_combinatorics.md`](03_combinatorics.md) — 組合せ論 (順列・組合せ・二項係数)

## 関連
- [`01_logic.md`](01_logic.md) — 命題論理の基礎
- [`start_here/columns/01_pythagoras_story.md`](../start_here/columns/01_pythagoras_story.md) — $\sqrt{2}$ 無理数事件

---

## 🔍 ググってみよう

- **ユークリッド原論** — 紀元前 300 年、最古の体系的証明書
- **ZFC 公理系** — 現代数学の標準的な公理体系
- **ゲーデルの不完全性定理** — 「証明できないが真の命題が存在する」 衝撃の定理
- **構成主義 (constructive mathematics)** — 「存在を主張するなら作って見せろ」 派
- **形式的証明 (Coq, Lean, Isabelle)** — コンピュータで証明を機械的に検証
- **帰納法のバリエーション** — 強帰納法、超限帰納法、構造的帰納法
- **逆数学 (reverse mathematics)** — 「ある定理を証明するには何の公理が必要か」
- **証明論 (proof theory)** — 証明そのものを数学的に研究する分野

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`01_logic.md`](01_logic.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`03_combinatorics.md`](03_combinatorics.md) |
