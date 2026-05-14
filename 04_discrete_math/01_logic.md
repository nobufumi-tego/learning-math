# 04-1. 命題論理 — 真と偽だけの世界

**このページのゴール**: 命題論理の基本演算 (AND, OR, NOT, →, ⇔) と真理表を理解し、Python で論理式を扱えるようになる。

---

## 💡 このページのコードを動かすには

```bash
uv run lab.py
```

ファイルツリーから [`04_discrete_math/notebooks/01_logic.ipynb`](notebooks/01_logic.ipynb) を開いて、上から順に **Shift+Enter**。

> 🐧 **CLI/Jupyter が初めての方** → [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **このページの前提**:
> - [`00_notation/03_logic_symbols.md`](../00_notation/03_logic_symbols.md) — ∀, ∃, ⇒ の記号

---

## 1. 命題とは — 「真か偽が決まる文」

### 例

| 文 | 命題か? | 真偽 |
|---|---|---|
| 「2 + 2 = 4」 | ✅ | 真 |
| 「東京は日本の首都である」 | ✅ | 真 |
| 「3 は偶数である」 | ✅ | 偽 |
| 「彼は背が高い」 | ❌ | 主観的 → 命題ではない |
| 「明日は雨が降る」 | △ | 未確定だが時点で確定する |

**命題 = 真偽が客観的に判定できる文**。

---

## 2. 論理演算子

### 否定 (NOT) $\neg$

| $P$ | $\neg P$ |
|---|---|
| 真 | 偽 |
| 偽 | 真 |

「否定する」だけ。

### 論理積 (AND) $\land$

| $P$ | $Q$ | $P \land Q$ |
|---|---|---|
| 真 | 真 | 真 |
| 真 | 偽 | 偽 |
| 偽 | 真 | 偽 |
| 偽 | 偽 | 偽 |

「**両方真**のときだけ真」。

### 論理和 (OR) $\lor$

| $P$ | $Q$ | $P \lor Q$ |
|---|---|---|
| 真 | 真 | 真 |
| 真 | 偽 | 真 |
| 偽 | 真 | 真 |
| 偽 | 偽 | 偽 |

「**少なくとも 1 つ真**なら真」(包括的 or)。

### 含意 (Implication) $\Rightarrow$

「$P$ ならば $Q$」:

| $P$ | $Q$ | $P \Rightarrow Q$ |
|---|---|---|
| 真 | 真 | 真 |
| 真 | 偽 | **偽** ⚠️ |
| 偽 | 真 | 真 |
| 偽 | 偽 | 真 |

> ⚠️ **注意**: 「偽 → 何でも = 真」。これは数学的な約束で、日常会話の「〜なら」とはニュアンスが違う。

### 同値 (Biconditional) $\Leftrightarrow$

「$P$ かつ $Q$ が同じ真偽」:

| $P$ | $Q$ | $P \Leftrightarrow Q$ |
|---|---|---|
| 真 | 真 | 真 |
| 真 | 偽 | 偽 |
| 偽 | 真 | 偽 |
| 偽 | 偽 | 真 |

---

## 3. Python で論理演算

```python
P, Q = True, False

# NOT
print(not P)        # False

# AND
print(P and Q)      # False

# OR
print(P or Q)       # True

# 含意 (Python に直接ないので、論理的に等価な式で)
print((not P) or Q)   # = P → Q

# 同値
print(P == Q)         # = P ⇔ Q
```

ヘルパー:

```python
def implies(p: bool, q: bool) -> bool:
    """p ⇒ q."""
    return (not p) or q

def equiv(p: bool, q: bool) -> bool:
    """p ⇔ q."""
    return p == q
```

---

## 4. 真理表 (Truth Table)

すべての可能な入力組み合わせと、結果の真偽を表にしたもの。

例: $\neg(P \land Q)$ vs $\neg P \lor \neg Q$ (**ド・モルガンの法則**):

```python
import itertools

def print_truth_table(formula, var_names):
    """formula は変数辞書を受け取り bool を返す関数."""
    print(' | '.join(var_names) + ' || formula')
    print('-' * 30)
    for vals in itertools.product([True, False], repeat=len(var_names)):
        env = dict(zip(var_names, vals))
        result = formula(**env)
        print(' | '.join(str(v)[:5].rjust(5) for v in vals)
              + ' || ' + str(result))

# ¬(P ∧ Q)
print_truth_table(lambda P, Q: not (P and Q), ['P', 'Q'])

# ¬P ∨ ¬Q (これも同じになるはず)
print()
print_truth_table(lambda P, Q: (not P) or (not Q), ['P', 'Q'])
```

両方の真理表が一致 → **論理的に同値** $\neg(P \land Q) \equiv \neg P \lor \neg Q$。

---

## 5. 重要な恒真式 (Tautology)

すべての入力で**必ず真**になる論理式:

| 名前 | 数式 |
|---|---|
| **排中律** | $P \lor \neg P$ |
| **二重否定** | $\neg \neg P \Leftrightarrow P$ |
| **ド・モルガン** | $\neg(P \land Q) \Leftrightarrow \neg P \lor \neg Q$ |
| **ド・モルガン (2)** | $\neg(P \lor Q) \Leftrightarrow \neg P \land \neg Q$ |
| **対偶** | $(P \Rightarrow Q) \Leftrightarrow (\neg Q \Rightarrow \neg P)$ |
| **含意の分解** | $(P \Rightarrow Q) \Leftrightarrow (\neg P \lor Q)$ |

これらを使うと、複雑な論理式を簡略化できる。

---

## 6. 推論規則

論理から論理を導く正しい操作:

### モーダス・ポネンス (Modus Ponens)
「$P$ かつ $P \Rightarrow Q$ なら、$Q$」

$$
\frac{P, \quad P \Rightarrow Q}{Q}
$$

### モーダス・トレンス (Modus Tollens)
「$\neg Q$ かつ $P \Rightarrow Q$ なら、$\neg P$」

$$
\frac{\neg Q, \quad P \Rightarrow Q}{\neg P}
$$

これは**対偶**を使った推論。

---

## 7. ML / AI への接続

### ブール演算と機械学習

ニューラルネットの初期研究 (Perceptron, 1957) は、論理演算 (AND, OR, NOT) を学習できることを目指した。
1969 年の **「Perceptron は XOR を学習できない」** 衝撃が「冬」を招き、後の多層 NN の研究につながる。

### ファジィ論理 (Fuzzy Logic)

「真 or 偽」だけでなく、$[0, 1]$ の連続値で扱う論理。
- t-norm (AND の拡張): $\min(p, q)$ や $p \cdot q$
- t-conorm (OR の拡張): $\max(p, q)$ や $p + q - pq$

ニューラルネットのアテンション機構や VAE の確率的推論で、ファジィ論理的な操作が暗に使われている。

### 論理プログラミング (Prolog)

事実とルールを宣言的に書く言語:
```prolog
parent(tom, alice).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

最近の **NeSy (Neuro-Symbolic AI)** で再注目。

---

## 8. ハマりポイント

- **含意の真理表**: $P=偽 \Rightarrow Q=真$ も「真」になる ← 最も混乱しやすい
- **「または」の意味**: 数学の OR は**包括的** (両方真もOK)、日常会話は排他的なことも
- **論理的同値の証明**: 真理表で全パターン一致を確認 (`==`)

---

## まとめ

| 演算 | 記号 | Python |
|---|---|---|
| 否定 | $\neg P$ | `not p` |
| 論理積 | $P \land Q$ | `p and q` |
| 論理和 | $P \lor Q$ | `p or q` |
| 含意 | $P \Rightarrow Q$ | `(not p) or q` |
| 同値 | $P \Leftrightarrow Q$ | `p == q` |

**この章のキー**: 命題論理は「真/偽」 の世界。真理表で論理式の同値性を機械的に判定できる。

## 次へ

→ [`02_proof_techniques.md`](02_proof_techniques.md) — 数学的証明の技法

## 関連
- [`00_notation/03_logic_symbols.md`](../00_notation/03_logic_symbols.md) — 論理記号の読み方
- [`03_combinatorics.md`](03_combinatorics.md) — 組合せ論

---

## 🔍 ググってみよう

- **命題論理 vs 述語論理** — $\forall, \exists$ が入ると述語論理
- **ブール代数 (Boolean algebra)** — 1854 年、George Boole の業績
- **NAND ゲート** — 1 つの演算で全論理を表現可能
- **Karnaugh map** — 論理式を視覚的に簡略化する技法
- **充足可能性問題 (SAT)** — 計算理論で最重要
- **Prolog / Datalog** — 論理プログラミング言語
- **記述論理 (Description Logic)** — オントロジーで使う
- **Curry-Howard 同型対応** — 「命題 = 型、証明 = プログラム」

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [章 TOP](README.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`02_proof_techniques.md`](02_proof_techniques.md) |
