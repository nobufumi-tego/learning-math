# 03-8. ベイズ推論 — 事後分布ひとつから、全部を取り出す

**このページのゴール**: $\pi(\theta \mid x) \propto L(\theta; x)\,\pi(\theta)$ という **1 本の式**を読めるようになり、
そこから点推定・区間・予測・意思決定を取り出せるようになる。

[`04_bayes.md`](04_bayes.md) では「$P(\theta \mid D) \propto P(D \mid \theta)P(\theta)$」という**式の形**を学びました。
この章では、それを**実際に計算する道具**（共役モデル）と、**答えの取り出し方**（信用区間・意思決定）を扱います。

---

## 💡 このページのコードを動かすには

このページのコード例は **Jupyter Lab** で対話的に試せます。

```bash
uv run lab.py
```

ブラウザが開いたら、左のファイルツリーから [`03_probability_statistics/notebooks/08_bayesian_inference.ipynb`](notebooks/08_bayesian_inference.ipynb) を開いて、上から順に **Shift+Enter** でセル実行してください。

> 🐧 **「`uv` って何?」「ブラウザが開かない」「ファイルツリーがわからない」方** は、まず以下を:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎
> - 特に [`08_uv_keeps_pet_healthy.md`](../start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) — uv の使い方
>
> 前提が不安なら:
> - [`04_bayes.md`](04_bayes.md) — ベイズの定理そのもの
> - [`02_distributions.md`](02_distributions.md) — ベータ分布・ポアソン分布・正規分布
> - [`06_estimation.md`](06_estimation.md) — MLE と MAP、信頼区間

---

## 0. この章で出てくる記号 — 先に「読み方」を配っておきます

ベイズの文献は**記号が読めれば 8 割読める**ので、最初に一覧を置きます。
分からなくなったらここに戻ってきてください。

| 記号 | 読み方 | 意味 |
|---|---|---|
| $\pi(\theta)$ | パイ・シータ | **事前分布** (prior)。データを見る前の $\theta$ の見立て。確率の $P$ と区別するため $\pi$ を使う慣習 |
| $\pi(\theta \mid x)$ | パイ・シータ・ギブン・エックス | **事後分布** (posterior)。データ $x$ を見た後の見立て |
| $L(\theta; x)$ | エル・オブ・シータ・セミコロン・エックス | **尤度** (likelihood)。$\theta$ の関数として見たデータの出やすさ |
| $\propto$ | proportional to / 比例する | 定数倍を無視して等しい。ベイズでは「正規化定数を省いた」の意味 |
| $\tilde{x}$ | **エックス・チルダ** | これから観測する**将来の**データ（既に見た $x$ と区別する） |
| $p(\tilde{x} \mid x)$ | – | **事後予測分布** (posterior predictive distribution) |
| $\alpha_0, \beta_0$ | アルファ・ノート / ベータ・ノート | 事前分布のパラメータ（**ハイパーパラメータ**）。添字 0 は「データ前」の印 |
| $\kappa_0$ | **カッパ・ノート** | 事前分布の**集中度** $\alpha_0 + \beta_0$。「どれくらい強く信じているか」 |
| $\mu_0$ | ミュー・ノート | 事前分布の中心 |
| $\tau_0^2, \tau_n^2$ | **タウ・ノート二乗 / タウ・エヌ二乗** | 事前 / 事後の分散（正規–正規モデル） |
| $\hat\theta_{\mathrm{MAP}}$ | シータ・ハット・マップ | **MAP 推定量**（事後密度が最大になる点） |
| $\gamma$ | ガンマ | 区間から外す確率。95% 区間なら $\gamma = 0.05$ |
| $m(x \mid H_i)$ | – | **周辺尤度** (marginal likelihood)。仮説 $H_i$ 全体でのデータの出やすさ |
| $BF_{01}$ | ベイズファクター・ゼロワン | $H_0$ と $H_1$ の周辺尤度の比 |
| $\Gamma(\cdot)$ | 大文字ガンマ | **ガンマ関数**（階乗を実数に拡張したもの）。$\Gamma(n) = (n-1)!$ |
| $B(\alpha, \beta)$ | ベータ関数 | $B(\alpha,\beta) = \dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$。ベータ分布の正規化定数 |

> ⚠️ **$\pi$ は円周率ではありません。** ベイズ統計では $\pi(\cdot)$ は「分布（密度関数）」を表す記号として使われます。
> 同じ 1 本の論文の中で円周率の $\pi$ と分布の $\pi$ が両方出ることもあります（$\frac{1}{\sqrt{2\pi}\sigma}$ の $\pi$ は円周率）。
> **括弧の中に引数があれば分布、なければ円周率**、と読み分けてください。

> ⚠️ **$\tilde{x}$（チルダ）は「まだ見ていないデータ」の印**です。
> $x$ は観測済みで**確定**、$\tilde{x}$ はこれから起こること。この 2 つを混同すると事後予測分布の式が読めません。
> 飾り記号全般は [`glossary/symbol_reference.md`](../glossary/symbol_reference.md#7-文字につく飾りハットバーチルダ) 参照。

---

## 1. 出発点は 1 本だけ — 事後 ∝ 尤度 × 事前

### 数式

$$
\pi(\theta \mid x) = \frac{L(\theta; x)\,\pi(\theta)}{\displaystyle\int L(t; x)\,\pi(t)\,dt}
\qquad\Longleftrightarrow\qquad
\underbrace{\pi(\theta \mid x)}_{\text{事後}} \;\propto\; \underbrace{L(\theta; x)}_{\text{尤度}} \times \underbrace{\pi(\theta)}_{\text{事前}}
$$

### 読み下し

「シータ・ギブン・エックスの事後分布は、尤度かける事前分布を、その積分で割ったもの」。

| 部分 | 名前 | 直感 |
|---|---|---|
| $\pi(\theta)$ | 事前分布 | **データを見る前の見立て**（山の位置と幅） |
| $L(\theta; x)$ | 尤度 | **観測データが、その $\theta$ の下でどれくらい出やすいか** |
| $\pi(\theta \mid x)$ | 事後分布 | **見立てをデータで更新した結果**。ベイズの成果物はこれ 1 つ |
| $\int L(t;x)\pi(t)\,dt$ | 正規化定数 | 全体の面積を 1 にするための割り算。**$\theta$ には依存しない** |

### なぜ $\propto$ で済ませてよいのか

分母の積分は $\theta$ を含みません（積分変数 $t$ で潰れている）。
つまり **$\theta$ を動かしても分母は変わらない**ので、「事後分布の形」を知るだけなら分子だけ見ればよい。

$$
\int L(t; x)\pi(t)\,dt \;=\; \text{定数}
$$

> 📌 **この積分が計算できないこと**が、次章 [`09_mcmc.md`](09_mcmc.md) で MCMC が必要になる理由です。
> $\propto$ という記号は、実は**後半への伏線**になっています。

### 頻度論との違い — 何に確率が乗っているか

これまでの章（[`06_estimation.md`](06_estimation.md), [`07_hypothesis_testing.md`](07_hypothesis_testing.md)）は**頻度論**の枠組みでした。

| | 頻度論 | ベイズ |
|---|---|---|
| $\theta$（パラメータ） | 固定された未知の**定数** | **確率分布**で表す（不確かさの持ち主） |
| $x$（データ） | 確率変数（標本ごとに変動） | 観測されて**確定**。条件付けの対象 |
| 記法 | $L(\theta; x)$ — $\theta$ の関数だが分布ではない | $\pi(\theta \mid x)$ — 縦棒の右にデータ |

> **一言でいうと**: 従来は「パラメータ固定・データが変動」、ベイズは「**データを固定してパラメータの分布を更新**」。

「データを元にパラメータを調整する」だけなら**最尤推定も同じ**です。ベイズ固有なのは次の 2 点:

1. **出発点（事前分布）を持っている** — 最尤推定は白紙から始める
2. **調整されるのが値ではなく分布そのもの** — 点が動くのではなく、山の位置と幅が同時に変わる

---

## 2. 事後予測分布 — 「次の 1 件」を予測する

### 数式

$$
p(\tilde{x} \mid x) = \int \underbrace{p(\tilde{x} \mid \theta)}_{\theta\text{ を固定したときの分布}} \; \underbrace{\pi(\theta \mid x)}_{\theta\text{ に残る不確実性}} \, d\theta
$$

### 読み下し

「$\theta$ を 1 つに**決め打ちしないで**、事後分布で平均した、次の観測の分布」。

### なぜ大事か

「推定値 $\hat\theta = 0.583$ を使って予測する」のは簡単ですが、それだと
**「$\theta$ がまだ分かっていない」という事実が予測に反映されません**。

事後予測分布は $\theta$ の不確実性ごと積分するので、**予測区間が正直に広くなります**。

> 💡 **不確実性は「分布」という器に載っている間だけ運ばれる。**
> 点推定に潰した瞬間、そこで途切れます。これがベイズの一貫した思想です。

---

## 3. 共役モデル① Bernoulli–Beta — 成功確率を推定する

### 場面

新 UI を 20 人に見せたら 12 人が成約した。成約率 $\theta$ はどれくらいか？

$$
n = 20, \quad y = 12, \quad \hat\theta = \frac{y}{n} = 0.60
$$

点だけなら 0.60。でも実務で知りたいのは「**$\theta$ はどの範囲か**」「**基準値 0.50 を上回る確率は**」です。

### 観測モデルと事前分布

$$
X_i \mid \theta \sim \mathrm{Bernoulli}(\theta), \qquad
Y = \sum_{i=1}^{n} X_i \;\Big|\; \theta \sim \mathrm{Binomial}(n, \theta)
$$

$$
\theta \sim \mathrm{Beta}(\alpha_0, \beta_0)
$$

### 事後分布（結論）

$$
\boxed{\;\theta \mid x \sim \mathrm{Beta}(\alpha_0 + y,\; \beta_0 + n - y)\;}
$$

**覚え方**: 事前分布の「**成功側に $y$、失敗側に $n-y$ を足すだけ**」。

$\mathrm{Beta}(2,2)$ に「20 人中 12 人成約」→ $\mathrm{Beta}(2+12,\, 2+8) = \mathrm{Beta}(14, 10)$。

### なぜこうなるのか（1 行で追える）

$$
\pi(\theta \mid x) \propto \underbrace{\theta^{y}(1-\theta)^{n-y}}_{\text{尤度}} \cdot \underbrace{\theta^{\alpha_0-1}(1-\theta)^{\beta_0-1}}_{\text{Beta 事前}}
= \theta^{(\alpha_0+y)-1}(1-\theta)^{(\beta_0+n-y)-1}
$$

指数を見比べると $\mathrm{Beta}(\alpha_0+y,\ \beta_0+n-y)$ の形そのもの。**掛けても Beta のまま**なので、更新が足し算で終わります。
この性質を**共役性 (conjugacy)** と呼びます。

### 事後予測分布

中心 $\mu_0$ と集中度 $\kappa_0$ を用意します:

$$
\kappa_0 = \alpha_0 + \beta_0, \qquad \mu_0 = \frac{\alpha_0}{\kappa_0}, \qquad \hat\theta = \frac{y}{n}
$$

次の 1 人について:

$$
\tilde{X} \mid x \sim \mathrm{Bernoulli}\!\left( \underbrace{\frac{\kappa_0}{\kappa_0 + n}\mu_0 + \frac{n}{\kappa_0 + n}\hat\theta}_{\text{事前平均と標本比率の「加重平均」}} \right)
$$

将来 $m$ 回の試行での成功回数 $\tilde{Y}$ は:

$$
\tilde{Y} \mid x \sim \mathrm{BetaBinomial}\!\left(m,\; \alpha_0 + y,\; \beta_0 + n - y\right)
$$

> 📌 **なぜ二項分布ではなく「ベータ二項分布」なのか。**
> 二項分布は成功確率を**固定**するので、「$\theta$ 自体がまだ分からない」という状況を表現できません。
> $\theta$ に Beta を重ねて積分したものがベータ二項分布で、**通常の二項分布より分散が大きくなります**（過分散）。

### Python（標準形式）

```python
import numpy as np
from scipy import stats

# --- 設定 (単位: 人) ---
ALPHA_0: float = 2.0   # 事前分布 Beta(α₀, β₀) の成功側
BETA_0: float = 2.0    # 失敗側
N: int = 20            # 試行数 n (人)
Y: int = 12            # 成功数 y (人)

# --- 事後分布: 成功側に y、失敗側に n−y を足すだけ ---
alpha_post: float = ALPHA_0 + Y          # 14
beta_post: float = BETA_0 + (N - Y)      # 10
posterior = stats.beta(alpha_post, beta_post)

print(f'事後分布      : Beta({alpha_post:.0f}, {beta_post:.0f})')
print(f'事後平均 E[θ|x]: {posterior.mean():.3f}')       # 0.583
print(f'事後 SD        : {posterior.std():.3f}')        # 0.099

# --- 95% 等裾信用区間 (γ = 0.05 を左右に 0.025 ずつ) ---
GAMMA: float = 0.05
lo, hi = posterior.ppf([GAMMA / 2, 1 - GAMMA / 2])
print(f'95% 等裾信用区間: [{lo:.3f}, {hi:.3f}]')        # [0.385, 0.768]

# --- しきい値超過確率 P(θ > 0.5 | x) ---
THRESHOLD: float = 0.50
print(f'P(θ > {THRESHOLD} | x) = {1 - posterior.cdf(THRESHOLD):.3f}')  # 0.798

# --- 事後予測: 次の 10 人のうち何人成約するか ---
M: int = 10
pred = stats.betabinom(M, alpha_post, beta_post)
print(f'次の{M}人の成約数の期待値: {pred.mean():.2f} 人')  # 5.83
```

---

## 4. 共役モデル② Poisson–Gamma — 発生率を推定する

### 場面

窓口の 1 日あたり問い合わせ件数。5 日間で $1, 3, 2, 4, 2$ 件だった。発生率 $\lambda$ は？

### 数式

$$
X_i \mid \lambda \sim \mathrm{Poisson}(\lambda), \quad i = 1,\dots,n
\qquad\qquad
\lambda \sim \mathrm{Gamma}(a_0, b_0)
$$

ここで $b_0$ は**率パラメータ** (rate parameter) です。

$$
\boxed{\;\lambda \mid x \sim \mathrm{Gamma}\!\left(a_0 + \sum_{i=1}^{n} x_i,\; b_0 + n\right)\;}
$$

**覚え方**: **合計回数を形状パラメータに、観測日数を率パラメータに足す**。

$\mathrm{Gamma}(2,1)$ に「5 日で合計 12 件」→ $\mathrm{Gamma}(14, 6)$、事後平均 $14/6 = 2.33$ 件/日。

### 事後予測分布

事後を $\mathrm{Gamma}(a, b)$ と書くと、翌日の件数は:

$$
\tilde{X} \mid x \sim \mathrm{NegativeBinomial}\!\left(a,\; \frac{b}{b+1}\right)
$$

> 📌 ここでも同じ構図です。$\lambda$ を決め打ちしないで平均すると、Poisson が**負の二項分布**に変わる。
> Poisson は「平均 = 分散」という強い制約がありますが、負の二項は**分散のほうが大きい**（過分散）。

### ⚠️ 率パラメータかスケールパラメータか

Gamma 分布は**2 通りの書き方**があり、論文でもライブラリでも混乱の元です。

| 流儀 | 密度 | 平均 | SciPy |
|---|---|---|---|
| **率** (rate) $\beta$ | $f(x) \propto x^{\alpha-1}e^{-\beta x}$ | $\alpha/\beta$ | `stats.gamma(a, scale=1/beta)` |
| **スケール** (scale) $\vartheta = 1/\beta$ | $f(x) \propto x^{\alpha-1}e^{-x/\vartheta}$ | $\alpha\vartheta$ | `stats.gamma(a, scale=theta)` |

**SciPy は scale 流儀**なので、率パラメータ $b$ を使うときは `scale=1/b` と書きます。**ここは事故が起きやすい**ので必ず確認を。

### Python（標準形式）

```python
import numpy as np
from scipy import stats

A_0: float = 2.0       # 事前 Gamma(a₀, b₀) の形状パラメータ
B_0: float = 1.0       # 率パラメータ (rate)
x = np.array([1, 3, 2, 4, 2])   # shape: (5,)  5日間の件数 (単位: 件/日)

a_post: float = A_0 + x.sum()   # 形状に「合計件数」を足す -> 14
b_post: float = B_0 + x.size    # 率に「日数」を足す       -> 6

# ⚠️ SciPy は scale 流儀なので scale = 1 / rate
posterior = stats.gamma(a=a_post, scale=1.0 / b_post)
print(f'事後分布      : Gamma({a_post:.0f}, {b_post:.0f})  ※第2引数は率')
print(f'事後平均 E[λ|x]: {posterior.mean():.3f} 件/日')   # 2.333 = 14/6

# 事後予測: 翌日の件数 ~ NegativeBinomial(a, b/(b+1))
pred = stats.nbinom(n=a_post, p=b_post / (b_post + 1))
print(f'翌日の件数の期待値: {pred.mean():.3f} 件')          # 2.333
print(f'翌日 5 件以上の確率: {1 - pred.cdf(4):.3f}')
```

---

## 5. 共役モデル③ 正規–正規 — 平均を推定する

### 場面

商品の 1 日あたり需要量。4 日間で $11, 12, 13, 12$ 個。平均需要 $\mu$ は？（$\sigma^2 = 4$ は既知とする）

### 数式

$$
X_i \mid \mu \sim N(\mu, \sigma^2) \;(\sigma^2\text{ 既知}), \qquad \mu \sim N(\mu_0, \tau_0^2)
$$

$$
\boxed{\;\mu \mid x \sim N(\mu_n, \tau_n^2), \qquad
\tau_n^2 = \left(\frac{1}{\tau_0^2} + \frac{n}{\sigma^2}\right)^{-1}, \qquad
\mu_n = \tau_n^2\left(\frac{\mu_0}{\tau_0^2} + \frac{n\bar{x}}{\sigma^2}\right)\;}
$$

### 加重平均として読み直す

$\tau_n^2$ の式を代入して整理すると、事後平均は**事前平均と標本平均の加重平均**だと分かります:

$$
\mu_n = \frac{\sigma^2}{\sigma^2 + n\tau_0^2}\,\mu_0 \;+\; \frac{n\tau_0^2}{\sigma^2 + n\tau_0^2}\,\bar{x}
$$

**$n$ が増えるほどデータ側 $\bar{x}$ の重みが上がる**。「どれだけ事前に寄せるか」を人が決めるのではなく、
**データ量と自信の強さの比で自動的に決まります**。

### 事後予測分布

$$
\tilde{X} \mid x \sim N(\mu_n,\; \underbrace{\sigma^2}_{\text{観測そのもののばらつき}} + \underbrace{\tau_n^2}_{\mu\text{ にまだ残る不確実性}})
$$

> 📌 **この足し算が「不確実性が予測へ運ばれる」の一番わかりやすい形**です。
> $\mu$ を推定値に決め打ちすると分散は $\sigma^2$ だけになり、$\tau_n^2$ の分だけ**予測を過信**することになります。

### 演習の答え合わせ

$\bar{x} = 12$, $\mu_0 = 10$, $\tau_0^2 = 1$, $\sigma^2 = 4$, $n = 4$ のとき:

$$
\tau_n^2 = \left(\frac{1}{1} + \frac{4}{4}\right)^{-1} = \frac{1}{2}, \qquad
\mu_n = \frac{1}{2}\left(\frac{10}{1} + \frac{4 \cdot 12}{4}\right) = 11
$$

$$
\mu \mid x \sim N\!\left(11, \tfrac{1}{2}\right), \qquad \tilde{X} \mid x \sim N\!\left(11, \tfrac{9}{2}\right)
$$

事前の 10 と標本平均 12 の**ちょうど真ん中**の 11 になりました（重みが半々だったため）。

### Python（標準形式）

```python
import numpy as np
from scipy import stats

SIGMA2: float = 4.0    # σ² 観測のばらつき (既知、単位: 個²)
MU_0: float = 10.0     # μ₀ 事前平均 (単位: 個)
TAU0_2: float = 1.0    # τ₀² 事前分散

x = np.array([11.0, 12.0, 13.0, 12.0])   # shape: (4,) 4日間の需要 (単位: 個)
n: int = x.size
x_bar: float = float(x.mean())           # x̄ 標本平均

tau_n2: float = 1.0 / (1.0 / TAU0_2 + n / SIGMA2)          # τn²
mu_n: float = tau_n2 * (MU_0 / TAU0_2 + n * x_bar / SIGMA2)  # μn

print(f'τn² = {tau_n2:.3f},  μn = {mu_n:.3f}')             # 0.500, 11.000

# 加重平均としての確認 (同じ値になる)
w_prior: float = SIGMA2 / (SIGMA2 + n * TAU0_2)   # 事前の重み
print(f'加重平均で再計算: {w_prior * MU_0 + (1 - w_prior) * x_bar:.3f}')

posterior = stats.norm(loc=mu_n, scale=np.sqrt(tau_n2))
predictive = stats.norm(loc=mu_n, scale=np.sqrt(SIGMA2 + tau_n2))  # 分散は「和」
print(f'μ の 95% 信用区間  : {posterior.interval(0.95)}')
print(f'翌日需要の 95% 予測区間: {predictive.interval(0.95)}')
```

---

## 6. 横断してみる — 変わるのは分布、変わらないのは構造

| 知りたい量 | 値の範囲 | 観測モデル | 共役事前分布 | 事後分布 | 事後予測分布 |
|---|---|---|---|---|---|
| 成功確率 $\theta$ | $0 < \theta < 1$ | Bernoulli／二項 | $\mathrm{Beta}(\alpha_0,\beta_0)$ | $\mathrm{Beta}(\alpha_0{+}y,\ \beta_0{+}n{-}y)$ | ベータ二項 |
| 発生率 $\lambda$ | $\lambda > 0$ | Poisson | $\mathrm{Gamma}(a_0,b_0)$ | $\mathrm{Gamma}(a_0{+}\textstyle\sum x_i,\ b_0{+}n)$ | 負の二項 |
| 平均 $\mu$ | $\mu \in \mathbb{R}$ | 正規（$\sigma^2$ 既知） | $N(\mu_0,\tau_0^2)$ | $N(\mu_n,\tau_n^2)$ | $N(\mu_n,\ \sigma^2{+}\tau_n^2)$ |

**共通の流れ**は 4 ステップだけ:

> 観測モデルを決める → 事前分布を置く → 事後分布へ更新 → 予測する

3 つのモデルは「**同じことを 3 回やっている**」だけです。違うのは分布名。ここに気づくと負担が一気に減ります。

### 分布の選び方は「値の範囲」で決まる

| 考えている事象 | 実現する分布 |
|---|---|
| 1 回の試行の成功・失敗 | Bernoulli |
| $n$ 回中の成功回数 | 二項 |
| $r$ 回成功するまでの失敗回数 | 負の二項 |
| 一定期間の発生回数 | Poisson |
| 0〜1 の割合 | Beta |
| 正の量・待ち時間 | Gamma |

> 💡 **判断する質問**: 「この分布は、私が見ているデータのような値を実際に**生成できる**か？」
> （値の範囲・裾の重さ・ばらつきの大きさ・ゼロの多さ）

---

## 7. 事前分布への感度 — 実務で一番突っ込まれるところ

**同じデータ（12 勝 8 敗）**に対して、事前分布だけを変えるとどうなるか。

| 事前分布 | 事前平均 $\mu_0$ | 集中度 $\kappa_0$ | 事後分布 | 事後平均 | 95% 等裾信用区間 |
|---|---|---|---|---|---|
| $\mathrm{Beta}(1,1)$ | 0.50 | 2 | $\mathrm{Beta}(13,9)$ | 0.591 | $[0.384,\ 0.782]$ |
| $\mathrm{Beta}(2,2)$ | 0.50 | 4 | $\mathrm{Beta}(14,10)$ | 0.583 | $[0.385,\ 0.768]$ |
| $\mathrm{Beta}(8,12)$ | 0.40 | 20 | $\mathrm{Beta}(20,20)$ | 0.500 | $[0.348,\ 0.652]$ |
| $\mathrm{Beta}(40,60)$ | 0.40 | 100 | $\mathrm{Beta}(52,68)$ | 0.433 | $[0.346,\ 0.523]$ |

### 集中度 $\kappa_0$ は「仮想的なデータ件数」

$\kappa_0 = \alpha_0 + \beta_0$ は**事前の自信の強さ**であり、事実上「**すでに何件見たのと同じ重みか**」を表します。

$\mathrm{Beta}(40,60)$ は $\kappa_0 = 100$、つまり「すでに 100 件見たのと同じ」重み。
だから 20 件の実データに**勝ってしまう**のです。

### ベータ分布は「中心 × 集中度」で読む

$$
\mu_0 = \frac{\alpha}{\alpha+\beta} \;(\text{中心}), \qquad
\kappa_0 = \alpha + \beta \;(\text{集中度}), \qquad
\mathrm{Var}(\theta) = \frac{\mu_0(1-\mu_0)}{\kappa_0 + 1}
$$

中心を固定すると、$\kappa_0$ が大きいほど分母が大きく → **分散が小さく → 分布が尖る**。

| 分布 | 平均 | 分散 |
|---|---|---|
| $\mathrm{Beta}(1,1)$ | 0.5 | 0.0833 |
| $\mathrm{Beta}(2,2)$ | 0.5 | 0.0500 |
| $\mathrm{Beta}(20,20)$ | 0.5 | 0.00610 |

**平均が同じでも「自信の強さ」は全然違う**。だから平均だけでは分布を説明できません。

> 💡 **判断する質問**: 「弱い事前分布をいくつか試して、結論は変わらないか？」
> 変わるなら**感度分析として明記する**のがベイズの作法です。
> 「ベイズは主観的でズルい」への回答は、**主観を隠さず明示して、依存性を報告すること**。

---

## 8. 事後分布から取り出す① — 点推定は「要約」にすぎない

$\theta \mid x \sim \mathrm{Beta}(14,10)$ のとき:

| 推定量 | 式 | 値 | 何の点か |
|---|---|---|---|
| **MLE** $\hat\theta_{\mathrm{MLE}}$ | $\dfrac{y}{n} = \dfrac{12}{20}$ | 0.600 | 尤度の頂点（事前を使わない） |
| **事後平均** $\mathbb{E}[\theta \mid x]$ | $\dfrac{\alpha}{\alpha+\beta} = \dfrac{14}{24}$ | 0.583 | 事後分布の**重心** |
| **MAP** $\hat\theta_{\mathrm{MAP}}$ | $\dfrac{\alpha-1}{\alpha+\beta-2} = \dfrac{13}{22}$ | 0.591 | 事後密度の**最大点**（山の頂上） |

3 つとも近いですが**意味が違います**。歪んだ分布では重心と頂上は大きくズレます。

> 📌 **点推定は事後分布の「要約」であって、本体ではありません。**
> 点に潰した瞬間に失われるもの: 自信の強さ／非対称性／$P(\theta > c \mid x)$ のような確率。

---

## 9. 事後分布から取り出す② — 信用区間（等裾と HPD）

### 等裾信用区間 (equal-tailed credible interval)

左右の裾に $\gamma/2$ ずつ残す:

$$
P(\theta < L \mid x) = P(\theta > U \mid x) = \frac{\gamma}{2}
$$

分位点（`ppf`）で機械的に作れるのが利点。

### HPD 区間 (Highest Posterior Density)

事後**密度の高いところから**確率 $1-\gamma$ を集める:

$$
C(c) = \{\theta : \pi(\theta \mid x) \ge c\}, \qquad P(\theta \in C(c) \mid x) = 1 - \gamma
$$

ここで $c$ は「切り取る高さ」で、領域の確率がちょうど $1-\gamma$ になるように選びます。

### 違い

| | 等裾 | HPD |
|---|---|---|
| 方針 | 左右の**確率**をそろえる | **密度の高い領域**を優先する |
| 比喩 | 両端から同じ人数ずつ切る | 人口密度の高い区画から詰めていく |
| 長さ | 一般に HPD より長い | **最短**になる（単峰の場合） |
| 一致するか | **対称な単峰分布なら一致する** | 同左 |

> ⚠️ **HPD が「1 本の最短区間」になるのは、事後分布が単峰 (unimodal) のときだけ**です。
> 山が 2 つある事後分布では、$C(c)$ は**互いに離れた複数の区間の和**になります
> （谷の部分は密度が低いので入らない）。ノートブックの実装も単峰を前提にしています。

歪んだ分布では、等裾は左右の裾確率をそろえるために**密度の低い側まで拾って**しまいます。

実例（$\mathrm{Beta}(2,8)$ という右に裾を引く分布）:

| 区間 | 下限 | 上限 | 幅 |
|---|---|---|---|
| 等裾 95% | 0.0281 | 0.4825 | 0.4544 |
| HPD 95% | 0.0086 | 0.4334 | **0.4248** |

### ⚠️ 信用区間 (credible interval) と信頼区間 (confidence interval) は読み方が違う

**この対比が今回いちばん大事な理解です。**

| | ベイズ**信用**区間 | 頻度論的**信頼**区間 |
|---|---|---|
| 確率が乗る対象 | 未知パラメータ $\theta$ | 標本ごとに変わる**区間のほう** |
| 読み方 | 「$\theta$ がこの区間に入る確率が 95%」と**言ってよい** | 「同じ手続きを繰り返すと 95% が真値を含む」 |
| 観測後の解釈 | 事後確率として直接読める | 今回の区間に入る確率とは**言えない** |
| 事前情報 | 事前分布として明示的に使える | 通常は使わない |
| 報告上の注意 | **使用した事前分布を明記する** | 手法と仮定を明記する |

[`06_estimation.md`](06_estimation.md) で「信頼区間を『真値が 95% の確率で入る』と読むのは誤り」と学びました。
その **"正しく読める版" がベイズの信用区間**です。頻度論で読めない理由は $\theta$ が定数で動かないから。
動いていたのは**区間のほう**でした。

---

## 10. 事後分布から取り出す③ — 損失を考えた意思決定

確率だけでは決められません。**外したときの損失**を入れます。

新 UI と従来 UI の成約率を $\theta_{\mathrm{new}}, \theta_{\mathrm{old}}$ とすると、誤判断は 2 種類:

- $\theta_{\mathrm{new}} \le \theta_{\mathrm{old}}$ なのに**導入する**: 損失 $C_{10}$
- $\theta_{\mathrm{new}} > \theta_{\mathrm{old}}$ なのに**導入しない**: 機会損失 $C_{01}$

期待損失を最小にするロールアウト条件:

$$
\boxed{\;P(\theta_{\mathrm{new}} > \theta_{\mathrm{old}} \mid x) \;>\; \frac{C_{10}}{C_{10} + C_{01}}\;}
$$

| 状況 | しきい値 | 意味 |
|---|---|---|
| 誤導入の損失 $C_{10}$ が大きい | 上がる | **高い確信が必要**（慎重に） |
| 見送りの機会損失 $C_{01}$ が大きい | 下がる | **低い確率でも踏み込む**のが合理的 |

> 📌 これが「5% 有意水準を全部の場面で使う」頻度論的な運用との一番の実務差です。
> **しきい値を業務の損失から決められる**。
>
> 💡 **判断する質問**: 「この判断、外したときにどっち向きの損失が大きい？」

### Python（標準形式）— A/B テストの比較確率

```python
import numpy as np
from scipy import stats

# 新旧 UI それぞれの事後分布 (一様事前 Beta(1,1) から更新)
post_new = stats.beta(1 + 12, 1 + 8)    # 20 人中 12 人成約
post_old = stats.beta(1 + 90, 1 + 110)  # 200 人中 90 人成約

# P(θ_new > θ_old | x) はモンテカルロで (積分を標本平均に置き換える)
K: int = 200_000                        # 標本数
rng = np.random.default_rng(42)
s_new = post_new.rvs(K, random_state=rng)   # shape: (200000,)
s_old = post_old.rvs(K, random_state=rng)
p_better: float = float((s_new > s_old).mean())
print(f'P(θ_new > θ_old | x) = {p_better:.3f}')

# 損失比からしきい値を決める (単位: 円などの共通尺度)
C_10: float = 100.0   # ダメなのに導入した損失
C_01: float = 50.0    # 良いのに見送った機会損失
threshold: float = C_10 / (C_10 + C_01)
print(f'必要な確信度 = {threshold:.3f} -> ロールアウト: {p_better > threshold}')
```

> この「標本平均で確率を出す」やり方が、次章 [`09_mcmc.md`](09_mcmc.md) の中心的な発想です。

---

## 11. 仮説を比べる — 周辺尤度とベイズファクター

$$
H_0: \theta = \theta_0, \qquad H_1: \theta \neq \theta_0
$$

### 周辺尤度 (marginal likelihood)

$$
m(x \mid H_i) = \int L(\theta; x, H_i)\,\pi(\theta \mid H_i)\,d\theta
$$

「その仮説が**事前に想定していた範囲全体**での、データの出やすさの平均」。
点仮説 $H_0$ では通常 $m(x \mid H_0) = L(\theta_0; x, H_0)$ になります。

### ベイズファクター (Bayes factor)

$$
BF_{01} = \frac{m(x \mid H_0)}{m(x \mid H_1)}, \qquad
\underbrace{\frac{P(H_0 \mid x)}{P(H_1 \mid x)}}_{\text{事後オッズ}} = BF_{01} \cdot \underbrace{\frac{P(H_0)}{P(H_1)}}_{\text{事前オッズ}}
$$

**事後オッズ = ベイズファクター × 事前オッズ**。ベイズの定理をオッズの形で書いただけです。

> ⚠️ **事前分布を広げすぎると周辺尤度は下がります。**
> データに合わない $\theta$ にも重みを配ってしまうため。
> 「とりあえず無情報事前で広く」がペナルティになる場面があります
> （**オッカムの剃刀が自動で効く**、と言われる現象）。

> 📌 事後オッズが 1 より大きくても、直ちに $H_0$ を採択することにはなりません。
> 実際の選択は、[第 10 節](#10-事後分布から取り出す③--損失を考えた意思決定)の**損失**も考慮して決めます。

---

## 12. JAX 形式 — `grad` で MAP を求める

共役モデルは代数で解けるので JAX の出番は薄いのですが、
「**対数事後密度を関数として書き、その勾配で山頂を探す**」という形は、
非共役モデル（次章）にそのまま繋がります。

```python
# === 標準形式 (NumPy / SciPy) — 閉じた式 ===
ALPHA_POST: float = 14.0
BETA_POST: float = 10.0
map_closed: float = (ALPHA_POST - 1) / (ALPHA_POST + BETA_POST - 2)
print(f'MAP (閉じた式) = {map_closed:.6f}')   # 0.590909

# === JAX 形式 (jax.grad で勾配上昇) ===
import jax
import jax.numpy as jnp

A0, B0, N, Y = 2.0, 2.0, 20.0, 12.0


def log_posterior(theta: jnp.ndarray) -> jnp.ndarray:
    """正規化定数を除いた対数事後密度 log π(θ|x) + const。

    Args:
        theta: 成約率 (スカラー、0 < theta < 1)。

    Returns:
        対数事後密度 (スカラー)。定義域外は -inf。
    """
    inside = (theta > 0) & (theta < 1)
    t = jnp.clip(theta, 1e-12, 1 - 1e-12)          # log(0) 回避
    lp = (A0 + Y - 1) * jnp.log(t) + (B0 + N - Y - 1) * jnp.log(1 - t)
    return jnp.where(inside, lp, -jnp.inf)


grad_log_post = jax.grad(log_posterior)   # 手で微分しなくてよい

LEARNING_RATE: float = 1e-3
N_STEPS: int = 500
theta = jnp.float32(0.5)                  # 初期値 (成約率なので中央)
for _ in range(N_STEPS):
    theta = theta + LEARNING_RATE * grad_log_post(theta)   # 勾配"上昇"

print(f'MAP (jax.grad)  = {float(theta):.6f}')   # 0.590909

# --- 検算: 標準形式と JAX 形式が一致するか ---
assert abs(float(theta) - map_closed) < 1e-4
print('✅ 標準形式と JAX 形式が一致')
```

> 💡 **ここでの JAX の価値**: `log_posterior` を書くだけで、微分は `jax.grad` が自動で出す。
> 事後分布の式が複雑になるほど（ベイズ・ロジスティック回帰など）この差が効いてきます。
> JAX 自体の入門は [`07_jax/`](../07_jax/README.md) を参照。

---

## 13. 付録: この章で使う分布の定義式

「$\mathrm{Beta}(14,10)$」と書かれたときに**中身の式**が言えると、論文が一段読みやすくなります。
$\Gamma$（ガンマ関数）と $B$（ベータ関数）の説明そのものは
[`00_notation/05_summation_product.md`](../00_notation/05_summation_product.md#γガンマ関数-階乗を実数へつなぐ) にあります。

### 離散（回数・個数を表す）

| 分布 | 確率関数 | 平均 | 分散 | SciPy |
|---|---|---|---|---|
| $\mathrm{Bernoulli}(p)$ | $P(X=1)=p,\ P(X=0)=1-p$ | $p$ | $p(1-p)$ | `stats.bernoulli` |
| $\mathrm{Binomial}(n,p)$ | $\dbinom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ | `stats.binom` |
| $\mathrm{NegativeBinomial}(r,p)$ | $\dbinom{k+r-1}{k}p^r(1-p)^k$ | $\dfrac{r(1-p)}{p}$ | $\dfrac{r(1-p)}{p^2}$ | `stats.nbinom` |
| $\mathrm{Poisson}(\lambda)$ | $\dfrac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ | `stats.poisson` |

$\mathrm{NegativeBinomial}(r,p)$ の $k$ は「$r$ 回成功するまでに起こる**失敗回数**」です。

### 連続（事前分布に使う）

**ベータ分布**（0〜1 の割合。成功確率の事前分布）:

$$
f(x) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\,x^{\alpha-1}(1-x)^{\beta-1}
= \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}, \quad 0<x<1
$$

$$
\mathbb{E}[X] = \frac{\alpha}{\alpha+\beta}, \qquad
\mathrm{Var}(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} = \frac{\mu_0(1-\mu_0)}{\kappa_0+1}
$$

**ガンマ分布**（正の量・発生率・待ち時間。$\beta$ は**率パラメータ**）:

$$
f(x) = \frac{\beta^{\alpha}}{\Gamma(\alpha)}\,x^{\alpha-1}e^{-\beta x}, \quad x>0
\qquad
\mathbb{E}[X] = \frac{\alpha}{\beta}, \qquad \mathrm{Var}(X) = \frac{\alpha}{\beta^2}
$$

### 事後予測に出てくる分布

**ベータ二項分布**（$\theta$ 自体が不確実な二項）:

$$
P(Y=k) = \binom{m}{k}\frac{B(k+\alpha,\; m-k+\beta)}{B(\alpha,\beta)}, \quad k = 0,1,\dots,m
$$

$$
\mathbb{E}[Y] = m\frac{\alpha}{\alpha+\beta}, \qquad
\mathrm{Var}(Y) = m\frac{\alpha\beta}{(\alpha+\beta)^2}\cdot\frac{\alpha+\beta+m}{\alpha+\beta+1}
$$

> 📌 **分散の最後の因子 $\dfrac{\alpha+\beta+m}{\alpha+\beta+1}$ が 1 より大きい**ことに注目してください。
> これが「二項分布より分散が大きい」（**過分散**）の正体です。
> $\kappa_0 = \alpha+\beta$ が大きい（＝$\theta$ に自信がある）ほど 1 に近づき、通常の二項分布に戻ります。

### 正規化定数はどこへ消えるのか

上の式で **$x$ を含まない部分**（$\Gamma$ や $B$ の塊、$\binom{n}{k}$）が正規化定数です。
だから [第 3 節](#3-共役モデル①-bernoullibeta--成功確率を推定する)の共役計算では:

$$
\pi(\theta \mid x) \propto \underbrace{\theta^{y}(1-\theta)^{n-y}}_{\text{尤度}}\cdot
\underbrace{\theta^{\alpha_0-1}(1-\theta)^{\beta_0-1}}_{\text{事前}}
$$

と、$\binom{n}{y}$ も $1/B(\alpha_0,\beta_0)$ も**書かずに済ませられます**。
指数だけ見比べれば分布が決まり、係数は最後に「$\mathrm{Beta}$ の形だから」と付け直せばよい。

> 💡 **$\propto$ で計算が軽くなる、という実感がここで得られます。**
> 逆に MCMC（[`09_mcmc.md`](09_mcmc.md)）では、この正規化定数が**そもそも計算できない**のに
> 比を取れば消えるので困らない、という話になります。

---

## 14. ハマりポイント

- **$\pi$ を円周率と読んでしまう** — 引数があれば分布。[第 0 節](#0-この章で出てくる記号--先に読み方を配っておきます)参照
- **Gamma 分布の率 / スケール取り違え** — SciPy は `scale=1/rate`。**最頻出の事故**
- **事後平均と MAP を混同する** — 重心と山頂は別物。歪んだ分布で顕著
- **信用区間を信頼区間の意味で読む（逆も）** — [第 9 節](#9-事後分布から取り出す②--信用区間等裾と-hpd)の表を毎回確認
- **「無情報事前なら中立」ではない** — どのスケールで一様かに仮定が入る。周辺尤度も下がる
- **強い事前を黙って使う** — $\kappa_0$ は仮想データ件数。**必ず報告する**
- **事後予測を「点推定を代入した分布」で済ませる** — 分散 $\tau_n^2$ の分だけ予測を過信する

---

## まとめ

| 概念 | 数式 |
|---|---|
| ベイズの一般原理 | $\pi(\theta \mid x) \propto L(\theta;x)\,\pi(\theta)$ |
| 事後予測分布 | $p(\tilde{x} \mid x) = \int p(\tilde{x} \mid \theta)\pi(\theta \mid x)\,d\theta$ |
| Bernoulli–Beta | $\theta \mid x \sim \mathrm{Beta}(\alpha_0 + y,\ \beta_0 + n - y)$ |
| Poisson–Gamma | $\lambda \mid x \sim \mathrm{Gamma}(a_0 + \sum x_i,\ b_0 + n)$ |
| 正規–正規 | $\mu \mid x \sim N(\mu_n, \tau_n^2)$、予測分散は $\sigma^2 + \tau_n^2$ |
| MAP（Beta） | $\hat\theta_{\mathrm{MAP}} = \dfrac{\alpha-1}{\alpha+\beta-2}$ |
| HPD 区間 | $C(c) = \{\theta : \pi(\theta \mid x) \ge c\}$ |
| 意思決定 | $P(\theta_{\mathrm{new}} > \theta_{\mathrm{old}} \mid x) > \dfrac{C_{10}}{C_{10}+C_{01}}$ |
| ベイズファクター | $BF_{01} = \dfrac{m(x \mid H_0)}{m(x \mid H_1)}$ |

**この章のキー**:

> **ベイズの成果物は事後分布ひとつ。**
> **点推定・区間・予測・意思決定は、すべてそこからの「取り出し方」の違いにすぎない。**

---

## 次へ

→ [`09_mcmc.md`](09_mcmc.md) — 事後分布に名前が付かないとき、どうやって計算するか

## 関連
- [`04_bayes.md`](04_bayes.md) — ベイズの定理そのもの
- [`02_distributions.md`](02_distributions.md) — Beta・Gamma・Poisson の形
- [`06_estimation.md`](06_estimation.md) — MLE / MAP、頻度論の信頼区間
- [`07_hypothesis_testing.md`](07_hypothesis_testing.md) — p 値とベイズファクターの対比
- [`glossary/symbol_reference.md`](../glossary/symbol_reference.md#10-7-ベイズ統計) — この章の記号の逆引き

---

## 🔍 ググってみよう

- **共役事前分布 (conjugate prior)** — 一覧表が Wikipedia にある。眺めるだけでも勉強になる
- **ベータ二項分布 / 過分散 (overdispersion)** — なぜ二項より分散が大きいのか
- **HPD 区間 (highest posterior density interval)** — ArviZ の `az.hdi` が定番実装
- **無情報事前 / ジェフリーズ事前 (Jeffreys prior)** — 「中立な事前」の難しさ
- **ベイズファクター / Lindley のパラドックス** — p 値とベイズが逆の結論を出す例
- **ベイズ A/B テスト** — `P(B > A)` を直接報告する運用
- **PyMC / NumPyro / Stan** — ベイズ推論の代表的ライブラリ（NumPyro は JAX ベース）

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`07_hypothesis_testing.md`](07_hypothesis_testing.md) | [章 TOP](README.md) | [📚 ROOT README](../README.md) | [`09_mcmc.md`](09_mcmc.md) |
