# 01. 線形代数 (Linear Algebra)

> ⚠️ **未検証の個人学習教材**: 本章は AI 協働で作成され、専門家の監修を受けていません。誤りを含む可能性があるため、必ず一次情報源で検証してください ([詳細](../DISCLAIMER.md))。
> 📜 **ライセンス**: 文書 [CC BY-NC-SA 4.0](../LICENSE-DOCS) / コード [MIT](../LICENSE-CODE) — 商用利用 (書籍化・有料講座・企業研修等) は[要相談](../DISCLAIMER.md#-商用利用について--commercial-use)

**ゴール**: ベクトル・行列の演算を、数式と Python の両方で扱えるようになる。
機械学習の論文・コードを読むうえで**最重要**の分野。

## なぜ重要か
- 機械学習のデータは基本的に**行列**（行 = サンプル、列 = 特徴量）
- ニューラルネットワークの順伝播・逆伝播は**行列の積**
- 主成分分析・推薦システムは**固有値分解・SVD**

---

## 💡 動かす前に

このフォルダのコードは **Jupyter Lab** で対話的に動かすのが推奨です。

🚀 **起動方法** (リポジトリのルートで実行):
- 🪟 **Windows**: [`start.bat`](../start.bat) を **ダブルクリック** ⭐
- 🍎 **Mac** / 🐧 **Linux**: ターミナルで `./start.sh`
- 🪟 **PowerShell 派**: `.\start.ps1`
- 🛠️ **すでに環境がある人**: `uv run lab.py`

uv のインストールから依存関係取得、Jupyter Lab 起動まで全部自動です。
詳細・トラブルシューティングは ROOT [`README.md`](../README.md#step-2--ワンショットスクリプトで起動-推奨) 参照。

ブラウザが開いたら、左のファイルツリーから `01_linear_algebra/notebooks/` を開いて、`01_vectors.ipynb` から順に。

> 🐧 **「`uv` ってなに?」「ターミナルがわからない」方** は、まず以下を:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎
> - 特に [`08_uv_keeps_pet_healthy.md`](../start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) — uv の使い方
>
> **数学に苦手意識のある方** は:
> - [`start_here/`](../start_here/README.md) — 数式ゼロから始める数学
> - [`00_notation/`](../00_notation/README.md) — 数学記号の読み解き

---

## 学習ステップ

| md (解説) | ipynb (動かす) | 内容 | 所要時間 |
|---|---|---|---|
| [`01_vectors.md`](01_vectors.md) | [`notebooks/01_vectors.ipynb`](notebooks/01_vectors.ipynb) | ベクトル、内積、ノルム、コサイン類似度 | 1時間 |
| [`02_matrices.md`](02_matrices.md) | [`notebooks/02_matrices.ipynb`](notebooks/02_matrices.ipynb) | 行列、行列積、転置、逆行列、線形変換 | 2時間 |
| [`03_eigenvalues.md`](03_eigenvalues.md) | [`notebooks/03_eigenvalues.ipynb`](notebooks/03_eigenvalues.ipynb) | 固有値・固有ベクトル、PCA、Power Iteration | 2時間 |
| [`04_decompositions.md`](04_decompositions.md) | [`notebooks/04_decompositions.ipynb`](notebooks/04_decompositions.ipynb) | LU、QR、Cholesky、SVD（圧縮・推薦） | 2時間 |

各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進めるのが効果的**です。

## キーとなる Python ツール

```python
import numpy as np

# ベクトル
x = np.array([1, 2, 3])              # shape: (3,)

# 行列
A = np.array([[1, 2], [3, 4]])       # shape: (2, 2)

# 行列積（@ または np.matmul）
y = A @ x[:2]                        # shape: (2,)

# 連立方程式（推奨: inv より高速・安定）
x = np.linalg.solve(A, b)

# 固有値分解
eigvals, eigvecs = np.linalg.eig(A)         # 一般行列
eigvals, eigvecs = np.linalg.eigh(A)        # 対称行列専用 (安定)

# SVD
U, s, Vt = np.linalg.svd(A)
```

## ML への接続
- **線形回帰**: `y = Xβ + ε` （行列方程式）
- **ニューラルネット1層**: `h = σ(Wx + b)`
- **主成分分析 (PCA)**: 共分散行列の固有値分解
- **推薦システム**: 行列分解（NMF, SVD）
- **Transformer の Attention**: `softmax(QKᵀ/√d) V`

## CLI 実行用サンプル (Jupyter を使わない場合)

`uv run python` で直接実行できる .py ファイルも置いてあります:

- `examples/vectors_and_matrices.py` — ベクトル・行列の基本演算（**標準形式 / NumPy**）
- `examples/vectors_and_matrices_jax.py` — 同じ内容（**JAX形式 / jax.numpy**）

```bash
uv run python 01_linear_algebra/examples/vectors_and_matrices.py
```

### NumPy vs JAX の対応（線形代数）
ほとんどのAPIが同名で使える:
```python
np.linalg.inv(A)      ↔   jnp.linalg.inv(A)
np.linalg.solve(A, b) ↔   jnp.linalg.solve(A, b)
np.linalg.eig(A)      ↔   jnp.linalg.eig(A)
np.linalg.svd(A)      ↔   jnp.linalg.svd(A)
```
違いは主に「配列が不変」「float32 デフォルト」「GPU/TPU自動対応」。

## この章で JAX が一番効く場面
- 大規模行列の **JIT コンパイル**で加速
- 行列演算を含む損失関数の **自動微分**
- バッチ処理を **`vmap`** で1行で書く

詳しくは → [`07_jax/`](../07_jax/README.md)

## 次の章へ

線形代数を終えたら → [`02_calculus/`](../02_calculus/README.md) (微積分)

## 📚 さらに学ぶ

この章を終えて「もっと深く」と思った方は:

- 📕 **[プログラミングのための線形代数](../appendix/books.md#プログラミングのための線形代数)** (平岡和幸・堀玄) — エンジニア向け本格解説
- 📕 **[Linear Algebra Done Right](../appendix/books.md#linear-algebra-done-right)** (Axler) — 無料 PDF、エレガントな構成
- 🌐 **[3Blue1Brown: Essence of Linear Algebra](../appendix/online.md#3blue1brown)** — 線形代数の直感を 3 時間で
- 🌐 **[Strang MIT 18.06](../appendix/online.md#strang-mit-1806-linear-algebra)** — MIT の伝説的講義 (英語、無料)

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`../00_notation/06_greek_letters.md`](../00_notation/06_greek_letters.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`01_vectors.md`](01_vectors.md) |
