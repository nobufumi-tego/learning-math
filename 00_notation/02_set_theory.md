# 集合論の記号

集合 (set) は数学の最も基礎的な概念。すべての分野で出てくる。

## 基本記号

| 記号 | 読み方（英 / 日） | 意味 | Python |
|---|---|---|---|
| `{ }` | "set" / 集合 | 集合の表記 | `set()` または `{1, 2, 3}` |
| `∈` | "in / element of" / 「に属する」 | 要素である | `in` 演算子 |
| `∉` | "not in" / 「属さない」 | 要素でない | `not in` |
| `⊂`, `⊊` | "subset" / 「真部分集合」 | 真部分集合（含まれて等しくない） | `<` |
| `⊆` | "subset or equal" / 「部分集合」 | 部分集合（等しくてもよい） | `<=` |
| `⊃`, `⊇` | "superset" / 「上位集合」 | 上位集合 | `>`, `>=` |
| `∪` | "union" / 「和集合」 | 和集合 A or B | `\|` または `.union()` |
| `∩` | "intersection" / 「共通部分」 | 共通部分 A and B | `&` または `.intersection()` |
| `\` or `−` | "set minus" / 「差集合」 | A から B を除く | `-` または `.difference()` |
| `∅` | "empty set" / 「空集合」 | 要素がない集合 | `set()` |
| `\|A\|` | "cardinality" / 「濃度」 | 集合の要素数 | `len(A)` |
| `Aᶜ` or `A'` | "complement" / 「補集合」 | 補集合 | `universe - A` |
| `A × B` | "Cartesian product" / 「直積」 | 直積 | `itertools.product(A, B)` |

## Python での実例

```python
"""集合論の記号 → Python 対応."""

# A = {1, 2, 3, 4}, B = {3, 4, 5, 6}
A: set[int] = {1, 2, 3, 4}
B: set[int] = {3, 4, 5, 6}

# 3 ∈ A
print(3 in A)              # True

# 7 ∉ A
print(7 not in A)          # True

# A ∪ B = {1, 2, 3, 4, 5, 6}
print(A | B)               # {1, 2, 3, 4, 5, 6}

# A ∩ B = {3, 4}
print(A & B)               # {3, 4}

# A \ B = {1, 2}
print(A - B)               # {1, 2}

# |A| = 4
print(len(A))              # 4

# A × B（直積）
from itertools import product
print(list(product(A, B))[:3])  # [(1, 3), (1, 4), (1, 5), ...]

# {1, 2} ⊂ A
print({1, 2} < A)          # True（真部分集合）

# {1, 2} ⊆ {1, 2}
print({1, 2} <= {1, 2})    # True
print({1, 2} < {1, 2})     # False（等しいので真部分集合ではない）
```

## 集合の内包表記（set-builder notation）

数学:
```
S = { x ∈ ℕ | x² < 20 }
```

読み方: 「S は、自然数 x のうち、x² が 20 未満であるもの全体の集合」

Python:
```python
S = {x for x in range(100) if x**2 < 20}
print(S)  # {0, 1, 2, 3, 4}
```

`|` は数学では「such that（〜であるような）」、Python の set内包では `if` に対応。

## ハマりポイント

- `∈` と `⊂` を混同しない:
  - `1 ∈ {1, 2}` ✅（1 は要素）
  - `{1} ⊂ {1, 2}` ✅（{1} は部分集合）
  - `{1} ∈ {1, 2}` ❌（{1} は要素ではない、1 が要素）
- `∅` は何の部分集合でもある: `∅ ⊆ A` は常に真
- Python の `set` は順序を持たない、重複を許さない

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`01_basic_symbols.md`](01_basic_symbols.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`03_logic_symbols.md`](03_logic_symbols.md) |
