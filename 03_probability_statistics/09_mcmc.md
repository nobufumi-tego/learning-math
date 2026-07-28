# 03-9. モンテカルロと MCMC — 解けない積分を、標本で置き換える

**このページのゴール**: 事後分布に**名前が付かない**とき何が起こるかを理解し、
$\mathbb{E}[g(\theta) \mid x] \approx \frac{1}{K}\sum_k g(\theta^{(k)})$ という **1 行の発想転換**を自分の道具にする。

前章 [`08_bayesian_inference.md`](08_bayesian_inference.md) の共役モデルは、**代数で解けた特別な場合**でした。
この章では、その「閉じた形」が失われたときにどうするかを扱います。

---

## 💡 このページのコードを動かすには

このページのコード例は **Jupyter Lab** で対話的に試せます。

```bash
uv run lab.py
```

ブラウザが開いたら、左のファイルツリーから [`03_probability_statistics/notebooks/09_mcmc.ipynb`](notebooks/09_mcmc.ipynb) を開いて、上から順に **Shift+Enter** でセル実行してください。

> 🐧 **「`uv` って何?」「ブラウザが開かない」「ファイルツリーがわからない」方** は、まず以下を:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎
> - 特に [`08_uv_keeps_pet_healthy.md`](../start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) — uv の使い方
>
> 前提が不安なら:
> - [`08_bayesian_inference.md`](08_bayesian_inference.md) — 事後分布・共役モデル（**この章の直接の前提**）
> - [`01_probability_basics.md`](01_probability_basics.md) — 大数の法則（標本平均が期待値に近づく理由）

---

## 0. この章で出てくる記号

| 記号 | 読み方 | 意味 |
|---|---|---|
| $\theta^{(k)}$ | **シータ・スーパースクリプト・ケー** | $k$ 番目の**標本**（累乗ではない。上付きカッコは「番号」の印） |
| $\theta^{*}$ | シータ・スター | MCMC が出した**候補点**（ここでは最適値の意味ではない） |
| $K$ | – | 標本数（MCMC の反復回数） |
| $g(\theta)$ | – | 知りたい量を作る関数（平均なら $g(\theta)=\theta$） |
| $I(\cdot)$, $\mathbb{1}[\cdot]$ | **indicator function / 指示関数** | 条件が真なら 1、偽なら 0 |
| $\dfrac{\pi(\theta^{*} \mid x)}{\pi(\theta^{(k)} \mid x)}$ | – | 2 地点の事後密度の**比**。MCMC が使う唯一の情報 |
| $q(\cdot \mid \cdot)$ | – | **提案分布** (proposal distribution)。次の候補を出す分布 |
| $\|\beta\|^2$ | ノルムの二乗 | $\sum_j \beta_j^2$。正規事前から出てくる正則化項 |
| $x_i^{\top}\beta$ | エックス・アイ・トランスポーズ・ベータ | 内積（$\sum_j x_{ij}\beta_j$） |

> ⚠️ **$\theta^{(k)}$ の上付きカッコは「$k$ 乗」ではありません。**
> 「$k$ 番目のサンプル」を表す ML / MCMC の慣習です。$\theta_k$（成分）との衝突を避けるための記法。
> [`glossary/symbol_reference.md`](../glossary/symbol_reference.md#7-文字につく飾りハットバーチルダ) 参照。

---

## 1. 壁 — 複雑なモデルでは事後分布に名前が付かない

ベイズ・ロジスティック回帰を例にします（[`06_ml_math_bridge/`](../06_ml_math_bridge/README.md) のロジスティック回帰のベイズ版）。

$$
p_i := P(y_i = 1 \mid \beta, x_i) = \frac{1}{1 + e^{-x_i^{\top}\beta}}, \qquad \beta \sim N(0, \tau^2 I)
$$

事後分布は:

$$
\pi(\beta \mid y, X) \;\propto\; \prod_{i=1}^{n} p_i^{\,y_i}(1 - p_i)^{1 - y_i} \cdot \exp\!\left(-\frac{\|\beta\|^2}{2\tau^2}\right)
$$

**この式には、通常の分布名が付きません**（非共役 / non-conjugate）。
Beta でも Gamma でも正規でもない。だから `stats.beta(...)` のように「呼び出す」ことができません。

それでも知りたいのは:

$$
\mathbb{E}[\beta_j \mid y, X], \qquad 95\%\text{ 信用区間}, \qquad P(\beta_j > 0 \mid y, X)
$$

> 📌 共役の 3 モデルは「**たまたま**うまくいく特別な場合」です。
> 実務のモデルはたいてい閉じた形になりません。

---

## 2. 発想の転換 — 欲しいものは、ほとんど全部「積分」

$$
\begin{aligned}
\text{事後平均}&: & \mathbb{E}[g(\theta) \mid x] &= \int g(\theta)\,\pi(\theta \mid x)\,d\theta \\[4pt]
\text{事後確率}&: & P(\theta > c \mid x) &= \int I(\theta > c)\,\pi(\theta \mid x)\,d\theta \\[4pt]
\text{予測分布}&: & p(\tilde{x} \mid x) &= \int p(\tilde{x} \mid \theta)\,\pi(\theta \mid x)\,d\theta
\end{aligned}
$$

**3 つとも「$\pi(\theta \mid x)$ で重み付けした平均」の形**をしています。

> 💡 補足: 積分は**加重和**、期待値は**確率による加重平均**です。
> $\int_a^b f(x)dx \approx \sum_i f(x_i)\Delta x_i$（値 $= f(x_i)$、重み $= \Delta x_i$）。
> この見方をしておくと、次の置き換えがすんなり入ります。

### ここが今日イチの発想

$$
\boxed{\;\text{積分が解けなくても、事後分布から「標本」さえ取れれば、標本平均で置き換えられる}\;}
$$

$\theta^{(1)}, \dots, \theta^{(K)} \sim \pi(\theta \mid x)$ が得られれば:

$$
\mathbb{E}[g(\theta) \mid x] \;\approx\; \frac{1}{K}\sum_{k=1}^{K} g\!\left(\theta^{(k)}\right)
$$

$$
P(\theta > c \mid x) \;\approx\; \frac{1}{K}\sum_{k=1}^{K} I\!\left(\theta^{(k)} > c\right) \quad(\text{= 標本のうち } c \text{ を超えた割合})
$$

**信用区間**は標本を並べて 2.5% 点と 97.5% 点を取るだけ。

> 標本さえあれば、平均・確率・区間・予測を**すべて同じ計算原理**（並べて数える）で求められます。
> 「数学で解く問題」を「サンプリングで解く問題」に**置き換えた**わけです。

これを **モンテカルロ法 (Monte Carlo method)** と呼びます。根拠は[大数の法則](01_probability_basics.md)です。

---

## 3. でも「事後分布から標本を取る」のが難しい

事後分布に名前が付かないので、`rng.beta(...)` のような乱数生成器がありません。
そこで数値的な方法が 3 つ登場します。

| 方法 | 基本発想 | 事前に用意するもの |
|---|---|---|
| **受容・棄却法** (rejection sampling) | 別の分布から候補をまとめて生成し、要らないものを捨てる | 事後分布全体を**上から覆う**良い提案分布 |
| **重点サンプリング** (importance sampling) | 別の分布から生成し、事後に近い標本に**重み**を付ける | 重要な領域を**全部覆う**良い提案分布 |
| **MCMC** | 現在地の**近く**に候補を出し、もっともらしい方へ少しずつ動く | 各地点の事後密度の**相対的な高さ**だけ |

### 決定的な違い

前 2 つには**自己矛盾**があります。「事後分布全体に合う提案分布」を作るには、
**事後分布の全体像を先に知っている必要がある**。それが分からないから困っているのに。

MCMC は**全体地図が要りません**。現在地の周りだけ比較しながら歩けばよい。

---

## 4. MCMC — 地図を持たずに山を歩く

事後分布を**山の地形**（高いところ＝もっともらしい $\theta$）だと思ってください。

```
現在地 θ^(k) → 近くに候補を出す θ* → どちらがもっともらしい? → 次の現在地 θ^(k+1)
```

1. 現在地の近くに候補を 1 つ出す
2. 現在地と候補地点の事後密度を**比べる**
3. 高い方向へは移動しやすく、**低い方向へも一定確率で移動する**
4. これを繰り返すと、密度の高い領域を頻繁に訪れる

**滞在時間の分布が、そのまま事後分布になる** — これが MCMC の本質です。

> 📌 ステップ 3 の「低い方へも一定確率で動く」が肝です。
> 山を降りられないと局所的な山に閉じ込められ、分布全体を覆えません。

### なぜ複雑な事後分布でも使えるのか — 正規化定数が消える

使うのは **2 地点の比**だけ:

$$
\frac{\pi(\theta^{*} \mid x)}{\pi(\theta^{(k)} \mid x)}
= \frac{L(\theta^{*};x)\pi(\theta^{*}) \big/ \displaystyle\int L(t;x)\pi(t)dt}{L(\theta^{(k)};x)\pi(\theta^{(k)}) \big/ \displaystyle\int L(t;x)\pi(t)dt}
= \frac{L(\theta^{*};x)\pi(\theta^{*})}{L(\theta^{(k)};x)\pi(\theta^{(k)})}
$$

**割り算で、あの解けない積分（正規化定数）が消えます。**

> 📌 [`08_bayesian_inference.md`](08_bayesian_inference.md) の $\propto$ という記号が、ここで回収されます。
> 「$\propto$ しか分からない」ことが、MCMC では**まったく困らない**。
>
> 比喩: 標高の絶対値を知らなくても、「今より高いか低いか」だけ分かれば山歩きはできる。

---

## 5. Metropolis 法 — 一番シンプルな MCMC

### アルゴリズム

現在地 $\theta^{(k)}$ に対して:

1. **提案**: $\theta^{*} \sim N(\theta^{(k)},\ s^2)$（$s$ = 一歩の大きさ）
2. **比を計算**: $r = \dfrac{\pi(\theta^{*} \mid x)}{\pi(\theta^{(k)} \mid x)}$
3. **採否**: $u \sim U(0,1)$ を引いて、$u < r$ なら $\theta^{(k+1)} = \theta^{*}$、さもなくば $\theta^{(k+1)} = \theta^{(k)}$

### 実装上の 2 つの定石

**(1) 対数で比較する**

確率の積は簡単にアンダーフローします（$0.001^{100}$ は 0 になる）。だから対数を取って**引き算**にします:

$$
\log r = \log \pi(\theta^{*} \mid x) - \log \pi(\theta^{(k)} \mid x), \qquad \log u < \log r \;\Rightarrow\; \text{採択}
$$

**(2) 棄却されたら、現在値をもう一度記録する**

同じ値が連続して並ぶのは**バグではなく仕様**です。滞在時間が確率になるので、
「動かなかった」ことも 1 標本として数えなければいけません。

### バーンイン (burn-in)

初期値は人が勝手に決めた場所なので、連鎖の最初のほうには**初期値の影響**が残ります。
最初の一定回数（例: 1,000 回）を捨てるのが **バーンイン**です。

### Python（標準形式 / NumPy）

$\mathrm{Beta}(2,2)$ の事前 × 「20 人中 12 人成約」で、**答えが $\mathrm{Beta}(14,10)$ と分かっている問題**を
あえて MCMC で解きます。これは無駄ではなく **道具の検定**です。

```python
import numpy as np
from scipy import stats

# --- モデルの設定 ---
A0: float = 2.0      # 事前分布 Beta(α₀, β₀)
B0: float = 2.0
N: int = 20          # 試行数 (人)
Y: int = 12          # 成功数 (人)

# --- アルゴリズムの設定 (モデルではない: 事後分布そのものは変えない) ---
N_ITER: int = 11_000     # 連鎖の総ステップ数
BURN_IN: int = 1_000     # 捨てる先頭ステップ数
PROPOSAL_SD: float = 0.08  # 一歩の大きさ s
INIT: float = 0.5        # 初期値 (成約率なので中央)


def log_posterior(theta: float) -> float:
    """正規化定数を除いた対数事後密度 log π(θ|x) + const。

    Args:
        theta: 成約率 (0 < theta < 1)。

    Returns:
        対数事後密度。定義域の外は -inf (= 絶対に採択されない)。
    """
    if theta <= 0.0 or theta >= 1.0:
        return -np.inf
    return (A0 + Y - 1) * np.log(theta) + (B0 + N - Y - 1) * np.log(1 - theta)


rng = np.random.default_rng(42)
samples = np.empty(N_ITER)      # shape: (11000,)
samples[0] = INIT
n_accept: int = 0

for s in range(1, N_ITER):
    current: float = samples[s - 1]
    proposal: float = rng.normal(current, PROPOSAL_SD)      # 現在地の近くに候補

    log_ratio: float = log_posterior(proposal) - log_posterior(current)  # 比を対数で

    if np.log(rng.uniform()) < log_ratio:
        samples[s] = proposal
        n_accept += 1
    else:
        samples[s] = current      # ⚠️ 棄却されたら現在値をもう一度記録 (仕様)

samples = samples[BURN_IN:]       # shape: (10000,) バーンインを捨てる

# --- 厳密解と比べる (答えが分かっている問題で検算する) ---
exact = stats.beta(A0 + Y, B0 + N - Y)    # Beta(14, 10)

print(f'受容率            : {n_accept / (N_ITER - 1):.3f}')       # 0.758
print(f'MCMC 事後平均     : {samples.mean():.4f}')                # 0.5865
print(f'厳密な事後平均    : {exact.mean():.4f}')                  # 0.5833
print(f'MCMC 95% 信用区間 : {np.percentile(samples, [2.5, 97.5]).round(3)}')
print(f'厳密 95% 信用区間 : {exact.ppf([0.025, 0.975]).round(3)}')
print(f'MCMC P(θ>0.5|x)   : {(samples > 0.5).mean():.3f}')        # 0.810
print(f'厳密 P(θ>0.5|x)   : {1 - exact.cdf(0.5):.3f}')            # 0.798
```

**3 桁目まで一致します。** MCMC が正しく動いていることを、答えの分かる問題で確認できました。

### 壊してみる — アルゴリズムのパラメータの意味

| いじる | 極端に小さくすると | 極端に大きくすると |
|---|---|---|
| `PROPOSAL_SD` | ちょろちょろしか動かず、分布全体を覆えない（受容率↑だが移動しない） | 候補が端に飛んで**棄却だらけ**（受容率↓） |
| `BURN_IN` | 初期値 0.5 の影響が残る | 標本が減るだけ（実害は小さい） |
| `N_ITER` | 推定がガタつく | 時間がかかるだけ |

> 📌 **これらは「モデルのパラメータ」ではなく「アルゴリズムのパラメータ」**です。
> 事後分布そのものは変えません。結果がズレて見えたら、モデルが変わったのではなく
> **収束していない**という診断情報です。
>
> レポートでの書き分け: モデル・事前分布 = 「**何を仮定したか**」（結論に責任）、
> `PROPOSAL_SD` など = 「**どう計算したか**」（再現性に責任）。

---

## 6. JAX 形式 — `jit` + `lax.scan` + `vmap`

MCMC は「同じ更新を何万回も繰り返す」処理なので、JAX の得意分野です。

- **`lax.scan`**: Python の `for` ループを 1 つの計算グラフに畳み込む
- **`jit`**: コンパイルして高速化
- **`vmap`**: **複数の連鎖を同時に**走らせる（収束診断に必須）

```python
# === JAX 形式 (jax.numpy + jit + lax.scan + vmap) ===
import functools

import jax
import jax.numpy as jnp
from jax import lax

A0, B0, N, Y = 2.0, 2.0, 20.0, 12.0
PROPOSAL_SD: float = 0.08


def log_posterior(theta: jnp.ndarray) -> jnp.ndarray:
    """正規化定数を除いた対数事後密度 (JAX 版)。

    Args:
        theta: 成約率 (スカラー)。

    Returns:
        対数事後密度 (スカラー)。定義域外は -inf。
    """
    inside = (theta > 0) & (theta < 1)
    t = jnp.clip(theta, 1e-12, 1 - 1e-12)     # log(0) 回避 (トレース可能な形で)
    lp = (A0 + Y - 1) * jnp.log(t) + (B0 + N - Y - 1) * jnp.log(1 - t)
    return jnp.where(inside, lp, -jnp.inf)    # if 文は使わない (jit の中では where)


@functools.partial(jax.jit, static_argnames=("n_iter",))
def metropolis(key: jnp.ndarray, n_iter: int, init: float = 0.5) -> jnp.ndarray:
    """Metropolis 法で対数事後密度からサンプリングする。

    Args:
        key: jax.random.PRNGKey。
        n_iter: 連鎖の総ステップ数 (static: 変えると再コンパイル)。
        init: 連鎖の初期値。

    Returns:
        標本。shape: (n_iter,)
    """
    def step(carry, k):
        current, current_lp = carry
        k_prop, k_unif = jax.random.split(k)                # 乱数は明示的に分割
        proposal = current + PROPOSAL_SD * jax.random.normal(k_prop)
        proposal_lp = log_posterior(proposal)

        accept = jnp.log(jax.random.uniform(k_unif)) < proposal_lp - current_lp
        new = jnp.where(accept, proposal, current)          # 棄却なら現在値を維持
        new_lp = jnp.where(accept, proposal_lp, current_lp)
        return (new, new_lp), new

    init_arr = jnp.float32(init)
    keys = jax.random.split(key, n_iter)                    # shape: (n_iter, 2)
    _, out = lax.scan(step, (init_arr, log_posterior(init_arr)), keys)
    return out                                              # shape: (n_iter,)


N_ITER: int = 11_000
BURN_IN: int = 1_000

# --- 1 本の連鎖 ---
chain = metropolis(jax.random.PRNGKey(42), N_ITER)
print(f'JAX MCMC 事後平均: {float(chain[BURN_IN:].mean()):.4f}')   # 0.5851
print(f'厳密な事後平均   : {14 / 24:.4f}')                          # 0.5833

# --- vmap で 4 本の連鎖を同時に (収束診断用) ---
N_CHAINS: int = 4
keys = jax.random.split(jax.random.PRNGKey(0), N_CHAINS)   # shape: (4, 2)
chains = jax.vmap(lambda k: metropolis(k, N_ITER))(keys)   # shape: (4, 11000)

chain_means = chains[:, BURN_IN:].mean(axis=1)             # shape: (4,)
print(f'4 連鎖の事後平均: {[f"{m:.4f}" for m in chain_means]}')

# --- 検算: 連鎖どうしがそろっていれば収束したと判断できる ---
TOLERANCE: float = 0.02          # 許容するばらつき
assert float(chain_means.max() - chain_means.min()) < TOLERANCE
print('✅ 4 本の連鎖が一致 -> 収束したとみなせる')
```

> 💡 **ここでの JAX の価値**:
> - `jit` + `lax.scan`: Python の逐次ループを 1 回のコンパイル済み処理にできる
> - `vmap`: 「4 本の連鎖」を**書き直さずに 1 行で**並列化できる

### ⚠️ ただし「JAX なら何でも速い」ではありません

このおもちゃ問題（$\theta$ がスカラー 1 個）で実測すると、手元の CPU では:

| | NumPy | JAX | 比 |
|---|---|---|---|
| 連鎖 1 本 | 約 20 ms | 約 60 ms | **0.3 倍 — JAX のほうが遅い** |
| 連鎖 32 本 | 約 600 ms | 約 110〜170 ms | **4〜6 倍 — JAX が速い** |
| 連鎖 128 本 | 約 2.4 秒 | 約 0.3 秒 | **約 8 倍** |

**1 本だけなら JAX のほうが遅い**。スカラー 1 個ずつの計算では、`jit` / `lax.scan` の間接費が勝ってしまうからです。
連鎖を増やすと `vmap` が効いて逆転します。

> 📌 **JAX の強みは「同じ計算をたくさん」に出ます。**
> 連鎖を何十本も走らせる／パラメータが数百〜数万個ある（ベイズ・ロジスティック回帰、ニューラルネット）／GPU・TPU を使う。
> 逆に「小さいスカラー計算を 1 回」なら素の NumPy が速い。**道具は測って選ぶ**のが正解です。
> （ノートブックに実測セルを置いてあります）

> ⚠️ **JAX 特有の注意**: `jit` の中で `if theta <= 0` は書けません（トレースされない）。
> `jnp.where` を使います。乱数も `PRNGKey` を明示的に `split` する必要があります。
> 詳しくは [`07_jax/`](../07_jax/README.md)。

---

## 7. 収束をどう確かめるか

MCMC は「十分長く回せば」正しい分布に収束しますが、**十分かどうかは自動では分かりません**。

| 診断 | 見るもの | 危険信号 |
|---|---|---|
| **トレースプロット** | 標本を反復順に折れ線で描く | 一方向にドリフトする、太い帯にならない |
| **受容率** | 採択された割合 | 極端に低い（<10%）／極端に高い（>95%）。1 次元なら 0.3〜0.5 が目安 |
| **複数連鎖** | 別々の初期値から走らせて重ねる | 連鎖どうしが**別の場所に居座る** |
| **$\hat{R}$**（R ハット） | 連鎖間分散 ÷ 連鎖内分散 | 1.01 より大きい |
| **有効標本数** (ESS) | 自己相関を考慮した実質的な標本数 | 数百未満 |

> 📌 **段が上がるごとに「正しさをどう担保するか」の手段が変わります。**
>
> | 段 | 何を扱う | 正しさの担保 |
> |---|---|---|
> | 1 | 共役・名前の付く分布 | **手計算で検算できる** |
> | 2 | 同じ問題を MCMC で | **段 1 の答えと一致するか** |
> | 3 | 名前の付かない事後（ベイズ・ロジスティック回帰） | 手順への信頼 + 収束診断 |
> | 4 | 階層モデル・入れ子 | 事後予測チェックで経験的に |
>
> **単純で検算できるものを踏み台にして複雑側へ渡る**。いきなり段 3 から入ると、
> 「モデルが違うのか、計算が失敗しているのか」を切り分けられなくなります。

---

## 8. 階層モデルと縮小 — n の小さいグループを守る

### 2 店舗の例

| 店舗 | 成約 / 訪問 | 観測比率 |
|---|---|---|
| A | 2 / 2 | **1.00** |
| B | 50 / 100 | 0.50 |

店舗 A は 2 件しかないのに「成約率 100% の店」になってしまいます。これは明らかにおかしい。
かといって全部まとめると店舗差が消えます。**その中間**が欲しい。

### 階層モデル (hierarchical model)

店舗 $j = 1,\dots,J$ について:

$$
Y_j \mid \theta_j \sim \mathrm{Bin}(n_j, \theta_j), \qquad \theta_j \mid \alpha, \beta \sim \mathrm{Beta}(\alpha, \beta)
$$

$$
\frac{\alpha}{\alpha+\beta} = \text{全店舗に共通する平均的な成約率}
$$

$\theta_j$ は店舗ごとに別々ですが、$\alpha, \beta$ は**共通**で、全店舗のデータから推定します。
これを **部分プーリング (partial pooling)** といいます。

### 縮小 (shrinkage)

その結果、**データの少ない店舗ほど、全体平均へ強く引っぱられます**。

| 店舗 | 観測比率 | 推定値 | 引っぱられ方 |
|---|---|---|---|
| A (n=2) | 1.00 | 0.50 寄りへ**大きく**調整 | 情報が少ないので全体を借りる |
| B (n=100) | 0.50 | ほぼ 0.50 のまま | 自分のデータで十分 |

> 💡 これは実務の直感そのものです。
> 「**2 件で 10 割の営業マンより、100 件で 5 割の方が信用できる**」。
> それをモデルとして書けるのが階層モデルの良いところ。
>
> **判断する質問**: 「この数字、$n$ がいくつのときの割合か？」

### モデルパラメータは 3 層ある

混ぜると混乱するので分けて持ちます。

| 層 | 何か | 例 | 誰が決めるか |
|---|---|---|---|
| 1 | **モデルパラメータ** $\theta$ | 成約率 $\theta$、発生率 $\lambda$、回帰係数 $\beta$ | データから推定 |
| 2 | **ハイパーパラメータ** | $\mathrm{Beta}(\alpha_0,\beta_0)$ の $\alpha_0, \beta_0$ | **分析者が置く**（報告必須） |
| 3 | **アルゴリズムのパラメータ** | `PROPOSAL_SD`, `N_ITER`, `BURN_IN` | 計算の都合（事後分布は変えない） |

> 📌 **階層モデルがやっているのは、層 2 を層 1 へ格上げすること**です。
> $\theta_j \sim \mathrm{Beta}(\alpha,\beta)$ の $\alpha,\beta$ を**データから推定する**ので、
> 店舗間で情報を融通でき、縮小が起きます。
>
> 「どこまでを固定の設定とし、どこからをデータに決めさせるか」の線引きが、モデリングの設計判断そのものです。

---

## 9. 事後予測チェック — 推定できても、モデルが正しいとは限らない

事後標本 $\theta^{(s)}$ ごとに**模擬データ**を生成します:

$$
\theta^{(s)} \sim \pi(\theta \mid x), \qquad \tilde{x}^{(s)} \sim p(\tilde{x} \mid \theta^{(s)})
$$

そして、観測データ $x$ と模擬データ $\tilde{x}$ を**特徴量**で比べます（平均・最大値・外れ値の数など）。

> **問い**: モデルから生成したデータは、実データの重要な特徴を再現しているか？
> 再現しないなら、**モデルを見直す**。

「パラメータが推定できた ＝ モデルが正しい」ではありません。
[`07_hypothesis_testing.md`](07_hypothesis_testing.md) の検定や、分類の混同行列・AUC と同じく、
**当てはめた後の検証**の枠です。

### Python（標準形式）

```python
import numpy as np
from scipy import stats

# 事後分布 Beta(14, 10) から θ を引き、そのつど「20 人分」の模擬データを作る
A_POST, B_POST = 14.0, 10.0
N_OBS: int = 20            # 実データと同じ試行数 (人)
Y_OBS: int = 12            # 実際に観測された成功数 (人)
N_REP: int = 5_000         # 模擬データセットの本数

rng = np.random.default_rng(0)
theta_draws = stats.beta(A_POST, B_POST).rvs(N_REP, random_state=rng)  # shape: (5000,)
y_rep = rng.binomial(N_OBS, theta_draws)                                # shape: (5000,)

# 特徴量 (ここでは成功数そのもの) の分布に、実データが収まっているか
p_lower: float = float((y_rep <= Y_OBS).mean())
print(f'模擬データの平均成功数: {y_rep.mean():.2f} 人 (実データ: {Y_OBS} 人)')
print(f'事後予測 p 値相当     : {min(p_lower, 1 - p_lower) * 2:.3f}')
print('※ 0 に近いとモデルが実データを再現できていない')
```

---

## 10. 逐次更新 — 昨日の事後分布が、今日の事前分布になる

独立なデータのまとまり $x_1, x_2$ が順に届くとき:

$$
\pi(\theta \mid x_1) \propto f(x_1 \mid \theta)\,\pi(\theta), \qquad
\pi(\theta \mid x_1, x_2) \propto f(x_2 \mid \theta)\,\underbrace{\pi(\theta \mid x_1)}_{\text{昨日の事後 = 今日の事前}}
$$

Bernoulli–Beta なら、これは単に**足し算を続ける**だけです:

$$
\mathrm{Beta}(\alpha_0, \beta_0) \xrightarrow{\;y_1/n_1\;} \mathrm{Beta}(\alpha_0+y_1,\ \beta_0+n_1-y_1) \xrightarrow{\;y_2/n_2\;} \cdots
$$

**用途**:
- オンライン A/B テスト
- 障害率の継続監視
- センサ・時系列の状態推定
- 人手評価が追加されていく ML システム

> 📌 頻度論の検定は「あらかじめ $n$ を決めて 1 回判定する」のが原則です
> （途中で覗き見して逐次に検定すると $\alpha$ 水準が壊れる → [`07_hypothesis_testing.md`](07_hypothesis_testing.md) の p ハッキング）。
> **ベイズは更新が構造的に定義されている**のが強みです。
>
> 新しい情報が来るたびに、**不確実性を保ったまま**学習を継続できる。

---

## 11. 頻度論とベイズの使い分け

| 頻度論的統計が向いている場面 | ベイズ統計が向いている場面 |
|---|---|
| 客観的な手順で検定・推定を行いたい | 事前情報や専門家判断を明示的に入れたい |
| 事前情報を入れたくない／入れにくい | **データが少なく**、不確実性を丁寧に扱いたい |
| 大量データがあり、標本の反復を考えやすい | パラメータや将来予測の**確率を直接知りたい** |
| $p$ 値・信頼区間・仮説検定で説明したい | データ更新に応じて**逐次的に**判断したい |

> **頻度論は「手順の長期的な性質」、ベイズは「観測後に残る不確実性」**を重視します。
> どちらが常に優れているというより、**目的に応じて使い分ける**。
>
> 💡 **判断する質問**: 「知りたいのは『手続きの信頼性』か、『いま手元のデータを見た後の自分の確からしさ』か？」

---

## 12. ハマりポイント

- **棄却されたときに記録し忘れる** — 同じ値の連続は仕様。忘れると分布が歪む
- **対数を取らずに確率の積で比べる** — アンダーフローして全部 0 になる
- **バーンインを取らない** — 初期値の影響が残る
- **1 本の連鎖だけで判断する** — 別の山に閉じ込められていても気づけない。必ず複数連鎖
- **受容率を見ない** — 0.9 超えは「動いていない」、0.05 未満は「跳びすぎ」のサイン
- **`jit` の中で Python の `if`** — トレースされない。`jnp.where` を使う
- **`np.random` を JAX で使う** — 再現性が壊れる。`jax.random.PRNGKey` を明示的に分割する
- **収束＝正しいモデル、と思う** — 収束は「計算が終わった」だけ。モデルの妥当性は事後予測チェックで

---

## まとめ

| 概念 | 数式 |
|---|---|
| モンテカルロ近似 | $\mathbb{E}[g(\theta) \mid x] \approx \dfrac{1}{K}\sum_{k=1}^{K} g(\theta^{(k)})$ |
| 事後確率の近似 | $P(\theta > c \mid x) \approx \dfrac{1}{K}\sum_{k=1}^{K} I(\theta^{(k)} > c)$ |
| MCMC が使う情報 | $\dfrac{\pi(\theta^{*} \mid x)}{\pi(\theta^{(k)} \mid x)}$（**正規化定数は不要**） |
| Metropolis の採否 | $\log u < \log \pi(\theta^{*}\mid x) - \log \pi(\theta^{(k)}\mid x)$ |
| 階層モデル | $Y_j \mid \theta_j \sim \mathrm{Bin}(n_j,\theta_j)$, $\theta_j \sim \mathrm{Beta}(\alpha,\beta)$ |
| 事後予測チェック | $\theta^{(s)} \sim \pi(\theta\mid x)$, $\tilde{x}^{(s)} \sim p(\tilde{x} \mid \theta^{(s)})$ |
| 逐次更新 | $\pi(\theta \mid x_1,x_2) \propto f(x_2\mid\theta)\,\pi(\theta \mid x_1)$ |

**この章のキー**:

> **解けない積分を、標本平均に置き換える。**
> **しかも使うのは 2 地点の「比」だけなので、正規化定数は要らない。**

---

## 次へ

→ 次の章: [`../05_optimization/README.md`](../05_optimization/README.md) — 最適化: 損失を最小にするパラメータを見つける

🎉 **確率・統計章、卒業です！**
確率 → 分布 → 期待値 → ベイズ → 記述統計 → 推定 → 検定 → ベイズ推論 → MCMC と辿ってきました。

## 関連
- [`08_bayesian_inference.md`](08_bayesian_inference.md) — 事後分布・共役モデル（この章の前提）
- [`07_hypothesis_testing.md`](07_hypothesis_testing.md) — 逐次に検定すると壊れる話
- [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 「山を登る」つながり
- [`07_jax/`](../07_jax/README.md) — `jit` / `vmap` / `lax.scan` の詳細
- [`glossary/symbol_reference.md`](../glossary/symbol_reference.md#10-7-ベイズ統計) — この章の記号の逆引き

---

## 🔍 ググってみよう

- **Metropolis-Hastings 法** — 提案分布が非対称なときの一般形
- **ギブスサンプリング (Gibbs sampling)** — 条件付き分布から順に引く MCMC
- **ハミルトニアンモンテカルロ / NUTS** — 勾配を使う現代的な MCMC（Stan・NumPyro の既定）
- **$\hat{R}$ (R-hat) / 有効標本数 (ESS)** — 収束診断の標準指標
- **ArviZ** — MCMC の診断・可視化ライブラリ
- **NumPyro / BlackJAX** — JAX ベースのベイズ推論ライブラリ
- **変分推論 (variational inference)** — MCMC の代わりに最適化で事後を近似する
- **Stein の縮小推定量 / James-Stein estimator** — 「縮小」の古典的な驚き
- **メトロポリス・ウラム・フォンノイマン** — マンハッタン計画とモンテカルロ法の誕生

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`08_bayesian_inference.md`](08_bayesian_inference.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`../05_optimization/README.md`](../05_optimization/README.md) |
