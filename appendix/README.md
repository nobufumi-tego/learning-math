# 📚 Appendix — もっと学びたい人のための参考リソース集

本リポジトリの内容を一通り理解した方、もっと深く学びたい方のための **書籍・オンライン教材ガイド**。
各章とリンクしているので、興味の出たトピックから次の一歩を踏み出せます。

---

## 📖 このフォルダの構成

| ファイル | 内容 |
|---|---|
| [`README.md`](README.md) (このファイル) | 章別おすすめ早見表 + 全体ガイド |
| [`books.md`](books.md) | **書籍** — 日本語/英語、初心者〜上級、有料/無料 を網羅 |
| [`online.md`](online.md) | **オンライン教材** — YouTube / MOOC / 公式ドキュメント / 論文サイト |
| [`learning_paths.md`](learning_paths.md) | 本リポジトリの**後どこへ進むか** — 進路別ロードマップ |

---

## 🎯 章別おすすめ早見表

各章を学んだ後、**最も評価の高い 1 冊と 1 サイト** だけ厳選すると:

| 本リポジトリの章 | 📕 おすすめ書籍 | 🌐 おすすめサイト/動画 |
|---|---|---|
| [`start_here/`](../start_here/README.md) (数学基礎) | [数学ガール](books.md#数学ガール) (結城浩) | [3Blue1Brown](online.md#3blue1brown) (動画で直感) |
| [`00_notation/`](../00_notation/README.md) (記号) | [プログラマの数学 第2版](books.md#プログラマの数学) | [高校数学の美しい物語](online.md#高校数学の美しい物語) |
| [`01_linear_algebra/`](../01_linear_algebra/README.md) | [プログラミングのための線形代数](books.md#プログラミングのための線形代数) | [3Blue1Brown: Essence of Linear Algebra](online.md#essence-of-linear-algebra) |
| [`02_calculus/`](../02_calculus/README.md) | [やさしく学べる微分積分](books.md#やさしく学べる微分積分) | [3Blue1Brown: Essence of Calculus](online.md#essence-of-calculus) |
| [`03_probability_statistics/`](../03_probability_statistics/README.md) | [統計学入門 (赤本)](books.md#統計学入門) (東大出版会) | [StatQuest with Josh Starmer](online.md#statquest) |
| [`05_optimization/`](../05_optimization/README.md) | [これなら分かる最適化数学](books.md#これなら分かる最適化数学) | [Boyd: Convex Optimization (講義動画)](online.md#boyd-convex-optimization) |
| [`06_ml_math_bridge/`](../06_ml_math_bridge/README.md) | [ゼロから作るDeep Learning](books.md#ゼロから作るdeep-learning) | [Karpathy: Neural Networks Zero to Hero](online.md#karpathy-neural-networks-zero-to-hero) |
| [`07_jax/`](../07_jax/README.md) | [JAX 公式チュートリアル (無料)](online.md#jax公式) | [Probabilistic ML by K. Murphy (無料PDF)](books.md#probabilistic-machine-learning) |
| [`04_discrete_math/`](../04_discrete_math/README.md) | [離散数学への招待](books.md#離散数学への招待) | [MIT OCW 6.042: Math for CS](online.md#mit-606042) |

→ より広く・深く知りたい方は次のセクションへ

---

## 🌳 学習ロードマップ別

### 🎓 大学院・研究の道へ

| 学ぶ順 | 内容 | 推奨 |
|---|---|---|
| 1 | 線形代数の厳密版 | Strang ([online.md](online.md#strang-mit)) → Axler「線型代数学への招待」 |
| 2 | 解析学 (微積分の厳密版) | 杉浦光夫「解析入門」 / Rudin "Principles of Mathematical Analysis" |
| 3 | 確率論 (測度論ベース) | 舟木直久「確率論」 / Williams "Probability with Martingales" |
| 4 | 関数解析・最適化 | Boyd "Convex Optimization" → Bertsekas |
| 5 | 機械学習理論 | Mohri "Foundations of Machine Learning" |

→ [`learning_paths.md`](learning_paths.md) でさらに詳しく

### 🛠️ ML エンジニアの道へ

| 学ぶ順 | 内容 | 推奨 |
|---|---|---|
| 1 | Python + NumPy/Pandas 実務 | 「Pythonによるデータ分析入門」 (McKinney) |
| 2 | 古典 ML | 「ゼロから作るDeep Learning」 1〜3巻 |
| 3 | フレームワーク | PyTorch ([公式チュートリアル](online.md#pytorch公式)) または JAX |
| 4 | 論文を読む | [Papers With Code](online.md#papers-with-code) → [arxiv-sanity](online.md#arxiv-sanity) |
| 5 | 実プロジェクト | Kaggle ([online.md](online.md#kaggle)) で手を動かす |

### 🤖 AI/LLM の道へ

| 学ぶ順 | 内容 | 推奨 |
|---|---|---|
| 1 | NN 基礎 (実装) | Karpathy: "Neural Networks: Zero to Hero" |
| 2 | Transformer 理解 | Karpathy: "Let's build GPT" + Vaswani 原論文 |
| 3 | LLM 訓練 | nanoGPT, miniGPT4 などの読み込み |
| 4 | RAG / Agents | LangChain, LlamaIndex ドキュメント |
| 5 | 最前線 | Anthropic / OpenAI / DeepMind のテクニカルブログ |

### 📊 データサイエンティストの道へ

| 学ぶ順 | 内容 | 推奨 |
|---|---|---|
| 1 | 統計学 | 東大出版会 「統計学入門」 (赤本) |
| 2 | ベイズ統計 | 久保拓弥「データ解析のための統計モデリング入門」 (緑本) |
| 3 | 因果推論 | Hernán & Robins "Causal Inference: What If" (無料 PDF) |
| 4 | 実験デザイン | "Trustworthy Online Controlled Experiments" |
| 5 | ビジネス応用 | 「効果検証入門」 安井翔太 |

---

## 💡 「この本/サイトを買って/読んで損したくない」 を避けるコツ

### 書籍選びの原則
1. **目次を必ず確認** (Amazon の「なか見!検索」 や出版社サイトで)
2. **レビューは星よりコメントを読む** — 「この層には合うが、別の層には合わない」 が分かる
3. **無料で公開されている書籍をまず試す** (Boyd "Convex Optimization", Goodfellow "Deep Learning" など)
4. **第一印象で「読めない」 と感じたら、別の本に切り替え**る — 自分のレベルに合わない本は時間の無駄

### オンライン教材の活用
- **動画 → 本 → 手を動かす** が王道
- 3Blue1Brown / StatQuest など**直感を作る動画** を最初に見る
- Coursera / edX は無料聴講可能 (証明書だけ有料)
- YouTube はすべて無料

### よくある勘違い
- ❌ 「分厚い本ほど良い」 → ❌ 自分のレベルに合うかが重要
- ❌ 「英語の本のほうが良い」 → 日本語の良書も多い、最初は日本語が効率的
- ❌ 「全部読まないといけない」 → 目次から興味のある章だけでも OK

---

## 🆕 更新履歴

このリストは継続的に更新されます。新しい良書や良サイトを見つけたら、PR で追加歓迎です。

最終更新: 2026-05

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [プロジェクト ROOT](../README.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`books.md`](books.md) |
