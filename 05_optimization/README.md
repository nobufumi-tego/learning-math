# 05. 最適化 (Optimization)

> ⚠️ **未検証の個人学習教材**: 本章は AI 協働で作成され、専門家の監修を受けていません。誤りを含む可能性があるため、必ず一次情報源で検証してください ([詳細](../DISCLAIMER.md))。
> 📜 **ライセンス**: 文書 [CC BY-NC-SA 4.0](../LICENSE-DOCS) / コード [MIT](../LICENSE-CODE) — 商用利用 (書籍化・有料講座・企業研修等) は[要相談](../DISCLAIMER.md#-商用利用について--commercial-use)

**ゴール**: 勾配降下法を中心に、関数の最小値・最大値を求める手法を理解する。
**機械学習の訓練 = 損失関数の最小化** なので、ML を学ぶならここは必須。

## なぜ重要か
- ニューラルネットワークの訓練は**勾配降下法**そのもの
- 損失関数の形状（凸 / 非凸、局所最適）が学習に直結
- 学習率・モーメンタム・Adam などの理解に必要

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

ブラウザが開いたら、左のファイルツリーから `05_optimization/notebooks/` を開いて、`01_basic_concepts.ipynb` から順に。

> 🐧 **「`uv` ってなに?」「ターミナルがわからない」方** は:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎
>
> **数学の前提が不安なら**:
> - [`02_calculus/05_gradient_jacobian.md`](../02_calculus/05_gradient_jacobian.md) — 勾配・ヘッセ行列

---

## 学習ステップ

| md (解説) | ipynb (動かす) | 内容 | 所要時間 |
|---|---|---|---|
| [`01_basic_concepts.md`](01_basic_concepts.md) | [`notebooks/01_basic_concepts.ipynb`](notebooks/01_basic_concepts.ipynb) | 最小化問題、凸関数、ヘッセ行列 | 1.5時間 |
| [`02_gradient_descent.md`](02_gradient_descent.md) | [`notebooks/02_gradient_descent.ipynb`](notebooks/02_gradient_descent.ipynb) | GD/SGD/Mini-batch/Momentum/Adam | 2時間 |

各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進めるのが効果的**です。

## キーとなる Python ツール

```python
import jax
import jax.numpy as jnp
import optax

# JAX で勾配自動計算
loss_fn = lambda params: ...
grad_fn = jax.grad(loss_fn)

# 最適化器 (Optax)
optimizer = optax.adam(learning_rate=1e-3)
opt_state = optimizer.init(params)

# 訓練 1 ステップ
@jax.jit
def step(params, opt_state):
    grads = grad_fn(params)
    updates, opt_state = optimizer.update(grads, opt_state)
    params = optax.apply_updates(params, updates)
    return params, opt_state
```

## 重要な記法

| 記号 | 意味 |
|---|---|
| $\arg\min f(\mathbf{x})$ | $f$ を最小にする $\mathbf{x}$ |
| $\arg\max f(\mathbf{x})$ | $f$ を最大にする $\mathbf{x}$ |
| $\min f(\mathbf{x})$ | $f$ の最小値（値） |
| s.t. | subject to (制約条件) |

更新式（勾配降下法）:

$$
\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \eta \nabla L(\boldsymbol{\theta}_t)
$$

| 記号 | 意味 |
|---|---|
| $\boldsymbol{\theta}$ | パラメータ |
| $\eta$ | 学習率 (learning rate) |
| $\nabla L$ | 損失関数の勾配 |

## ML への接続
- SGD, Momentum, Adam（学習アルゴリズム）
- 学習率スケジューリング (warmup + cosine)
- バッチ正規化、勾配クリッピング
- 凸最適化 → SVM, ロジスティック回帰

## CLI 実行用サンプル

```bash
uv run python 05_optimization/examples/gradient_descent_demo.py
```

- [`examples/gradient_descent_demo.py`](examples/gradient_descent_demo.py) — 標準形式
- [`examples/gradient_descent_demo_jax.py`](examples/gradient_descent_demo_jax.py) — JAX形式

---

## 📚 さらに学ぶ

- 📕 **[これなら分かる最適化数学](../appendix/books.md#これなら分かる最適化数学)** (金谷健一) — 日本語の入門
- 📕 **[Convex Optimization](../appendix/books.md#convex-optimization)** (Boyd & Vandenberghe) — **無料 PDF**、世界標準
- 🌐 **[Boyd: Convex Optimization (Stanford)](../appendix/online.md#boyd-convex-optimization-stanford-ee364a)** — 講義動画も無料
- 🌐 [Optax 公式ドキュメント](https://optax.readthedocs.io/) — JAX 用 optimizer

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`../03_probability_statistics/04_bayes.md`](../03_probability_statistics/04_bayes.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`01_basic_concepts.md`](01_basic_concepts.md) |
