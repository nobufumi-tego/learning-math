# 04-3. 組合せ論 — 順列・組合せ・二項係数

**このページのゴール**: 「何通りあるか?」を数える組合せ論を、Python で計算しながら身につける。確率論・アルゴリズム解析の基礎。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`04_discrete_math/notebooks/03_combinatorics.ipynb`](notebooks/03_combinatorics.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`01_logic.md`](01_logic.md), [`02_proof_techniques.md`](02_proof_techniques.md) — 論理・証明
> - [`03_probability_statistics/02_distributions.md`](../03_probability_statistics/02_distributions.md) — 二項分布

---

## 1. 階乗 (Factorial)

### 定義

$$
n! = n \cdot (n-1) \cdot (n-2) \cdots 2 \cdot 1
$$

特別な約束: $0! = 1$

| $n$ | $n!$ |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 10 | 3,628,800 |
| 20 | $\approx 2.4 \times 10^{18}$ |

### 意味

「$n$ 個の異なるものを **一列に並べる** 方法の数」。

### Python

```python
import math

print(math.factorial(5))   # 120
print(math.factorial(20))  # 2432902008176640000

# 自前実装
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

---

## 2. 順列 (Permutation)

### 定義

「$n$ 個から $r$ 個を選んで**並べる**」方法の数:

$$
P(n, r) = \frac{n!}{(n-r)!} = n \cdot (n-1) \cdots (n-r+1)
$$

別記法: $_nP_r$

### 例

5 人から 3 人を選んで一列に並べる:

$$
P(5, 3) = \frac{5!}{2!} = 5 \cdot 4 \cdot 3 = 60
$$

### Python

```python
import math
from itertools import permutations

# 公式
print(math.perm(5, 3))   # 60

# 全列挙 (確認用)
print(len(list(permutations([1, 2, 3, 4, 5], 3))))   # 60

# 例
print(list(permutations(['A', 'B', 'C'], 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

---

## 3. 組合せ (Combination)

### 定義

「$n$ 個から $r$ 個を選ぶ」方法の数 (**順序を区別しない**):

$$
\binom{n}{r} = \frac{n!}{r!(n-r)!} = \frac{P(n, r)}{r!}
$$

別記法: $_nC_r$, $C(n, r)$

これを **二項係数** とも呼ぶ。

### 例

5 人から 3 人を選ぶ (順序問わず):

$$
\binom{5}{3} = \frac{5!}{3! \cdot 2!} = \frac{120}{6 \cdot 2} = 10
$$

### 順列との違い

- 順列: $A, B, C$ と $B, A, C$ は別 → $\frac{5!}{2!} = 60$
- 組合せ: $A, B, C$ と $B, A, C$ は同じ (集合として) → $\frac{60}{3!} = 10$

### Python

```python
import math
from itertools import combinations

print(math.comb(5, 3))   # 10
print(len(list(combinations([1, 2, 3, 4, 5], 3))))   # 10

print(list(combinations(['A', 'B', 'C', 'D'], 2)))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
```

### 重要な性質

#### (1) 対称性
$$
\binom{n}{r} = \binom{n}{n-r}
$$

(残す $n-r$ 個を選ぶのも同じこと)

#### (2) パスカルの公式
$$
\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}
$$

(「特定の 1 個を選ぶ場合」と「選ばない場合」に分割)

#### (3) 全パターンの和
$$
\sum_{r=0}^n \binom{n}{r} = 2^n
$$

(「各要素を選ぶか選ばないかの自由」 = 部分集合の数)

---

## 4. パスカルの三角形

二項係数 $\binom{n}{r}$ を並べたもの:

```
n=0:                1
n=1:              1   1
n=2:            1   2   1
n=3:          1   3   3   1
n=4:        1   4   6   4   1
n=5:      1   5  10  10   5   1
n=6:    1   6  15  20  15   6   1
```

各数 = 上の 2 つの数の和 (パスカルの公式)。

### Python で生成

```python
import math

def pascal(n):
    return [math.comb(n, r) for r in range(n + 1)]

for n in range(7):
    row = pascal(n)
    print(' '.join(f'{v:>4}' for v in row).center(40))
```

---

## 5. 二項定理 (Binomial Theorem)

$$
(x + y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r
$$

例: $n = 3$ なら
$$
(x + y)^3 = x^3 + 3x^2 y + 3xy^2 + y^3
$$

係数 $1, 3, 3, 1$ が**パスカルの三角形の 3 行目**と一致。

### SymPy で確認

```python
import sympy as sp

x, y = sp.symbols('x y')
expr = (x + y)**5
print(sp.expand(expr))
# x**5 + 5*x**4*y + 10*x**3*y**2 + 10*x**2*y**3 + 5*x*y**4 + y**5
```

---

## 6. 重複を許す組合せ (Multiset Combination)

「$n$ 種類から重複 OK で $r$ 個選ぶ」 = $\binom{n+r-1}{r}$

例: ドーナツ屋で 5 種類から 3 個買う (重複 OK):
$$
\binom{5+3-1}{3} = \binom{7}{3} = 35 \text{ 通り}
$$

```python
import math
from itertools import combinations_with_replacement

print(math.comb(5 + 3 - 1, 3))   # 35
print(len(list(combinations_with_replacement(range(5), 3))))   # 35
```

---

## 7. 確率との接続

### コインを 10 回投げて表が $k$ 回出る確率

二項分布 $\mathrm{Bin}(10, 0.5)$ で:

$$
P(X = k) = \binom{10}{k} (0.5)^k (0.5)^{10-k} = \binom{10}{k} \cdot 0.5^{10}
$$

例: 5 回表が出る確率
$$
P(X = 5) = \binom{10}{5} \cdot 0.5^{10} = \frac{252}{1024} \approx 0.246
$$

```python
import math

n, p = 10, 0.5
for k in range(11):
    prob = math.comb(n, k) * p**k * (1-p)**(n-k)
    bar = '█' * int(prob * 100)
    print(f'P(X={k:>2}) = {prob:.4f}  {bar}')
```

### スターリングの公式

大きい $n$ での階乗の近似:

$$
n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n
$$

確率論や情報理論の理論解析で必須。

```python
import math

def stirling(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e) ** n

for n in [10, 20, 50, 100]:
    actual = math.factorial(n)
    approx = stirling(n)
    print(f'n={n:>3}: 実際 = {actual:.4e},  近似 = {approx:.4e},  比 = {approx/actual:.6f}')
```

---

## 8. ML / AI への接続

### Transformer のアテンション

$n$ 個のトークンに対し、すべてのペア $(i, j)$ について類似度を計算:

$$
\text{総ペア数} = n^2 \quad (\text{重複 OK の順列})
$$

これが Transformer が長いシーケンスで遅い理由 ($O(n^2)$ メモリ・計算)。

### 決定木 / ランダムフォレスト

$d$ 次元の特徴量から $k$ 個選ぶ方法 → $\binom{d}{k}$ 通り。
ランダムフォレストは各木でランダムに特徴を選ぶ。

### 自然言語処理の N-gram

連続する $N$ 語の組合せ:
- 1-gram (unigram): 単語単体
- 2-gram (bigram): 連続 2 語
- 3-gram (trigram): 連続 3 語

語彙数 $V$ なら $V^N$ 通りの組合せがある (組合せ爆発)。

---

## 9. ハマりポイント

- **順列と組合せの区別**: 「並べる」か「選ぶ」か
- **階乗のオーバーフロー**: $20! \approx 2 \times 10^{18}$ で int64 限界。$30!$ で float の精度を失う
- **対称性を活用**: $\binom{100}{99}$ を直接計算せず、$\binom{100}{1} = 100$ を使う
- **`math.comb` は Python 3.8+** で利用可、それ以前は自前で

---

## まとめ

| 概念 | 数式 | Python |
|---|---|---|
| 階乗 | $n!$ | `math.factorial(n)` |
| 順列 | $P(n, r) = \dfrac{n!}{(n-r)!}$ | `math.perm(n, r)` |
| 組合せ | $\binom{n}{r} = \dfrac{n!}{r!(n-r)!}$ | `math.comb(n, r)` |
| 二項定理 | $(x+y)^n = \sum_r \binom{n}{r}x^{n-r}y^r$ | `sympy.expand` |
| パスカル | $\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$ | – |
| スターリング | $n! \approx \sqrt{2\pi n}(n/e)^n$ | (上記関数) |

**この章のキー**: 「**順序を区別する → 順列**」「**区別しない → 組合せ**」。確率・アルゴリズムの基礎で必須。

## 離散数学章 完了 🎉

これで本リポジトリの全章を読破!
**お疲れさまでした**。

→ ROOT README に戻る: [`../README.md`](../README.md)

## 関連
- [`03_probability_statistics/02_distributions.md`](../03_probability_statistics/02_distributions.md) — 二項分布
- [`02_proof_techniques.md`](02_proof_techniques.md) — 組合せ論の証明には帰納法が頻出

---

## 🔍 ググってみよう

- **二項定理 (binomial theorem)** — Newton による一般化形 (実数指数版)
- **多項定理 (multinomial theorem)** — 二項定理の拡張
- **包除原理 (inclusion-exclusion)** — 「少なくとも 1 つ」の数え方
- **カタラン数 (Catalan number)** — 組合せ論の頻出数列
- **スターリング数** — 集合分割の数
- **生成関数 (generating function)** — 数列を関数で表す技法
- **ベル数 (Bell number)** — 集合を分割する方法の数
- **モビウス反転** — 数論と組合せ論の交差点

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`02_proof_techniques.md`](02_proof_techniques.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | 全章卒業 🎉 [ROOT に戻る](../README.md) |
