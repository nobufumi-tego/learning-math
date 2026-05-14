# 06. 機械学習との橋渡し (ML Math Bridge)

> ⚠️ **未検証の個人学習教材**: 本章は AI 協働で作成され、専門家の監修を受けていません。誤りを含む可能性があるため、必ず一次情報源で検証してください ([詳細](../DISCLAIMER.md))。
> 📜 **ライセンス**: 文書 [CC BY-NC-SA 4.0](../LICENSE-DOCS) / コード [MIT](../LICENSE-CODE) — 商用利用 (書籍化・有料講座・企業研修等) は[要相談](../DISCLAIMER.md#-商用利用について--commercial-use)

**ゴール**: ここまで学んだ数学（線形代数・微積分・確率・最適化）が、機械学習でどう統合されるかを見る。
**「数学を学ぶ目的地」** として、最後にここに到達することを意識する。

## なぜこの章を作るか
- 個々の数学を学んでも、「これが何の役に立つの？」が見えないと続かない
- 機械学習の論文・コードを読み解くには、複数分野の知識を**同時に**使う必要がある
- AI への指示・生成された数式コードを理解するには、全体像が要る

---

## 💡 動かす前に

このフォルダのコードは **Jupyter Lab** で対話的に動かすのが推奨です。

🚀 **起動方法** (リポジトリのルートで実行):
- 🪟 **Windows**: [`start.bat`](../start.bat) を **ダブルクリック** ⭐
- 🍎 **Mac** / 🐧 **Linux**: ターミナルで `./start.sh`
- 🪟 **PowerShell 派**: `.\start.ps1`
- 🛠️ **すでに環境がある人**: `uv run lab.py`

uv のインストールから依存関係取得、Jupyter Lab 起動まで全部自動です。

> ⏰ **初回起動は 5〜15 分かかります** (依存関係 500MB〜1GB のダウンロード)。途中で中断せず気長に待ってください。「応答なし」 と出ても OS 更新の遅延なので焦らず ☕
> 2 回目以降は 10〜20 秒で起動します。詳細は ROOT [`README.md`](../README.md#-待ち時間の目安--フリーズしてないと心配しないでください) の「待ち時間の目安」 参照。

詳細・トラブルシューティングは ROOT [`README.md`](../README.md#step-2--ワンショットスクリプトで起動-推奨) 参照。

ブラウザが開いたら、左のファイルツリーから `06_ml_math_bridge/notebooks/` を開いて、`01_loss_functions.ipynb` から順に。

> 🐧 **「`uv` ってなに?」「ターミナルがわからない」方** は:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md)
>
> **数学の前提**:
> - [`02_calculus/02_derivatives.md`](../02_calculus/02_derivatives.md) — 連鎖律
> - [`03_probability_statistics/02_distributions.md`](../03_probability_statistics/02_distributions.md) — 正規分布
> - [`05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) — 勾配降下法

---

## 学習ステップ

| md (解説) | ipynb (動かす) | 内容 | 所要時間 |
|---|---|---|---|
| [`01_loss_functions.md`](01_loss_functions.md) | [`notebooks/01_loss_functions.ipynb`](notebooks/01_loss_functions.ipynb) | MSE、クロスエントロピー、正則化 | 2時間 |
| [`02_backprop.md`](02_backprop.md) | [`notebooks/02_backprop.ipynb`](notebooks/02_backprop.ipynb) | 誤差逆伝播法、手書き vs JAX | 3時間 |

各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進めるのが効果的**です。

## 損失関数の数学的構造

### 平均二乗誤差 (MSE)

$$
L(\boldsymbol{\theta}) = \frac{1}{N} \sum_i \bigl(y_i - f(x_i; \boldsymbol{\theta})\bigr)^2
$$

連続値の回帰問題で使う。

### クロスエントロピー

$$
L(\boldsymbol{\theta}) = -\sum_i y_i \log p(x_i; \boldsymbol{\theta})
$$

確率分布の対数を使う。分類問題で使う。最尤推定の対数尤度関数と同じもの。

### Python 実装

```python
import jax.numpy as jnp

def mse_loss(y_true, y_pred):
    return jnp.mean((y_true - y_pred) ** 2)

def cross_entropy_loss(y_true, y_pred):
    """y_true: ワンホット (N, K), y_pred: ソフトマックス (N, K)."""
    EPSILON = 1e-12
    return -jnp.mean(jnp.sum(y_true * jnp.log(y_pred + EPSILON), axis=1))
```

## 誤差逆伝播 (Backpropagation)

連鎖律 (chain rule) を多層のニューラルネットに適用したもの。

### 連鎖律のおさらい

$$
y = f(g(x)), \qquad \frac{dy}{dx} = \frac{df}{dg} \cdot \frac{dg}{dx}
$$

### ニューラルネット1層の場合

$$
\mathbf{z} = W \mathbf{x} + \mathbf{b}, \quad \mathbf{a} = \sigma(\mathbf{z})
$$

各パラメータの勾配:

$$
\frac{\partial L}{\partial W} = \frac{\partial L}{\partial \mathbf{a}} \cdot \frac{\partial \mathbf{a}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial W}
$$

JAX なら `jax.grad(loss)` で完全自動化。

## CLI 実行用サンプル

```bash
uv run python 06_ml_math_bridge/examples/loss_and_gradient.py
```

- [`examples/loss_and_gradient.py`](examples/loss_and_gradient.py) — 標準形式 (NumPy で線形回帰)
- [`examples/loss_and_gradient_jax.py`](examples/loss_and_gradient_jax.py) — JAX 形式 (`jax.value_and_grad`)

## 学習を終えた後

ここまで来たら、以下に挑戦するとよい:
- 線形回帰を NumPy だけで実装
- 単純なニューラルネットを NumPy で実装（PyTorch/JAXに頼らず）
- 論文の1段落を読んで、出てくる数式に対応する Python コードを書く

---

## 📚 さらに学ぶ

- 📕 **[ゼロから作るDeep Learning](../appendix/books.md#ゼロから作るdeep-learning)** (斎藤康毅) — NumPy で NN 実装、シリーズ全 5 巻
- 📕 **[Pattern Recognition and Machine Learning (PRML)](../appendix/books.md#pattern-recognition-and-machine-learning-prml)** (Bishop) — ML 理論の決定版
- 📕 **[Deep Learning](../appendix/books.md#deep-learning)** (Goodfellow et al.) — **無料 PDF**
- 🌐 **[Karpathy: Neural Networks Zero to Hero](../appendix/online.md#karpathy-neural-networks-zero-to-hero)** — GPT を 1 から実装
- 🌐 [fast.ai](../appendix/online.md#fastai-practical-deep-learning-for-coders) — 実装ファースト DL 講座

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次の章 → |
|---|---|---|---|
| [`../05_optimization/02_gradient_descent.md`](../05_optimization/02_gradient_descent.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`../07_jax/README.md`](../07_jax/README.md) |
