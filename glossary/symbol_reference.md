# 数学記号リファレンス

論文・教科書・生成AIの出力で出てきた記号を逆引きする用。
学習を進めながら**新しい記号に出会ったら必ずここに追記**する。

## 1. 関係・等号

| 記号 | 読み方（英/日） | 意味 | Python |
|---|---|---|---|
| `=` | equals / 等しい | 等しい | `==` / `=` |
| `≠` | not equal / 等しくない | 等しくない | `!=` |
| `≈` | approximately / ほぼ等しい | 近似 | `np.isclose` |
| `≡` | identical / 合同・定義 | 定義する / 恒等的に等しい | コメントで |
| `:=` | defined as / 定義する | 左辺を右辺で定義 | `=` |
| `∝` | proportional to / 比例 | 比例 | – |

## 2. 数の集合

| 記号 | 意味 | Python |
|---|---|---|
| `ℕ` | 自然数 | `int` (≥0) |
| `ℤ` | 整数 | `int` |
| `ℚ` | 有理数 | `fractions.Fraction` |
| `ℝ` | 実数 | `float` |
| `ℂ` | 複素数 | `complex` |
| `ℝⁿ` | n次元実空間 | `np.ndarray` shape (n,) |

## 3. 集合

| 記号 | 意味 | Python |
|---|---|---|
| `∈` | 属する | `in` |
| `∉` | 属さない | `not in` |
| `⊂` `⊊` | 真部分集合 | `<` |
| `⊆` | 部分集合 | `<=` |
| `∪` | 和集合 | `\|` |
| `∩` | 共通部分 | `&` |
| `\` | 差集合 | `-` |
| `∅` | 空集合 | `set()` |
| `\|A\|` | 濃度 | `len(A)` |
| `×` | 直積 | `itertools.product` |

## 4. 論理

| 記号 | 意味 | Python |
|---|---|---|
| `∀` | すべての | `all(...)` |
| `∃` | 存在する | `any(...)` |
| `∧` | かつ | `and` / `&` |
| `∨` | または | `or` / `\|` |
| `¬` | 否定 | `not` / `~` |
| `⇒` | ならば | `not P or Q` |
| `⇔` | 同値 | `P == Q` |
| `s.t.` | such that | `if` |

## 5. 関数

| 記号 | 意味 | Python |
|---|---|---|
| `f: A → B` | f は A から B への関数 | `def f(...) -> B:` |
| `x ↦ f(x)` | x を f(x) に写す | `lambda x: ...` |
| `f ∘ g` | 合成関数 | `lambda x: f(g(x))` |
| `f⁻¹` | 逆関数 | – |
| `\|x\|` | 絶対値 | `abs(x)` |
| `\|\|x\|\|` | ノルム | `np.linalg.norm(x)` |
| `⌊x⌋` | 床 | `math.floor` |
| `⌈x⌉` | 天井 | `math.ceil` |

## 6. 総和・総乗・積分

| 記号 | 意味 | Python |
|---|---|---|
| `Σ` | 総和 | `np.sum`, `sum` |
| `Π` | 総乗 | `np.prod`, `math.prod` |
| `∫` | 積分（定積分は `∫_a^b`） | `scipy.integrate.quad` / `sympy.integrate` |
| `∬` | 二重積分 | `scipy.integrate.dblquad` |
| `d/dx`, `'` | 微分 | `sympy.diff` |
| `∂/∂x` | 偏微分 | `sympy.diff(f, x)` |
| `∇` | 勾配（ナブラ） | `[sp.diff(f, v) for v in vars]` |

## 7. 線形代数

| 記号 | 意味 | Python |
|---|---|---|
| `Aᵀ` または `A'` | 転置 | `A.T` |
| `A⁻¹` | 逆行列 | `np.linalg.inv(A)` |
| `det(A)`, `\|A\|` | 行列式 | `np.linalg.det(A)` |
| `tr(A)` | トレース | `np.trace(A)` |
| `rank(A)` | ランク | `np.linalg.matrix_rank(A)` |
| `A ⊗ B` | クロネッカー積 | `np.kron(A, B)` |
| `⟨u, v⟩` | 内積 | `u @ v` |

## 8. 確率・統計

| 記号 | 意味 | Python |
|---|---|---|
| `P(A)` | A の確率 | – |
| `P(A\|B)` | 条件付き確率 | – |
| `E[X]` | 期待値 | `np.mean` |
| `Var[X]` | 分散 | `np.var` |
| `Cov[X, Y]` | 共分散 | `np.cov` |
| `X ~ D` | X は分布 D に従う | `rng.<dist>(...)` |
| `N(μ, σ²)` | 正規分布 | `stats.norm` |
| `Bin(n, p)` | 二項分布 | `stats.binom` |
| `iid` | independent and identically distributed | – |

## 9. 最適化

| 記号 | 意味 | Python |
|---|---|---|
| `argmin f(x)` | f を最小にする x | `scipy.optimize.minimize` |
| `argmax f(x)` | f を最大にする x | `-` を使って最小化 |
| `min f(x)` | 最小値（値） | – |
| `s.t.` | 制約条件 | `constraints=...` |

## 10. その他よく見るもの

| 記号 | 意味 |
|---|---|
| `∞` | 無限大 |
| `∴` | ゆえに |
| `∵` | なぜなら |
| `□`, `∎`, `QED` | 証明終わり |
| `≜` | 定義する |

---

## 追記方法

新しい記号に出会ったら:
1. このファイルの該当セクションに行を追加
2. 同じ意味の Python があれば必ず併記
3. わからなければ Claude Code で `/project:explain-symbol <記号>`
