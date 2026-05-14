# 🌳 学習ロードマップ — 本リポジトリの後どこへ進むか

本リポジトリ (Phase −1 〜 8) を全て理解した後、**どんな道に進むか** によって次の学びが変わります。
あなたの目標別に、**1 年〜数年単位の学習計画** を提案します。

---

## 🎯 目標別ロードマップ

### A. 🎓 大学院・研究の道

**目標**: 機械学習・数学系の研究者になる、論文を書く

| 期間 | 学ぶこと | 推奨教材 |
|---|---|---|
| Month 1-3 | 厳密な線形代数 | [Strang MIT 18.06](online.md#strang-mit) → [Axler "Linear Algebra Done Right"](books.md#linear-algebra-done-right) |
| Month 4-6 | 厳密な解析学 | [杉浦光夫「解析入門」](books.md#解析入門-i-ii) または [Rudin "Principles of Mathematical Analysis"] |
| Month 7-9 | 確率論 (測度論ベース) | 舟木直久「確率論」 / Williams "Probability with Martingales" |
| Month 10-12 | 関数解析・凸最適化 | [Boyd "Convex Optimization"](books.md#convex-optimization) → Bertsekas |
| Year 2 | 機械学習理論 | Mohri "Foundations of Machine Learning" |
| Year 2 | ベイズ統計の理論 | 渡辺澄夫「ベイズ統計の理論と方法」 |
| Year 2-3 | **論文を読み書く** | arXiv で関心領域を絞り、週 5 本ペースで読む |

**到達点**: トップ会議 (NeurIPS, ICML, ICLR) の論文が読めて、自分でも書ける

---

### B. 🛠️ ML エンジニア / MLOps の道

**目標**: 企業で ML システムを設計・運用する

| 期間 | 学ぶこと | 推奨教材 |
|---|---|---|
| Month 1-2 | Python + データ分析実務 | [Pythonによるデータ分析入門](books.md#pythonによるデータ分析入門) |
| Month 3-4 | 古典 ML マスター | [scikit-learn 公式](online.md#scikit-learn-ユーザーガイド) + [Pythonではじめる機械学習](books.md#pythonではじめる機械学習) |
| Month 5-6 | 深層学習基礎 | [ゼロから作るDeep Learning 1, 2](books.md#ゼロから作るdeep-learning) |
| Month 7-8 | フレームワーク (PyTorch) | [PyTorch 公式](online.md#pytorch-公式) + [fast.ai](online.md#fastai-practical-deep-learning-for-coders) |
| Month 9-10 | コンペで実力試し | [Kaggle](online.md#kaggle) で 1 つメダル獲得を目指す |
| Month 11-12 | MLOps | "Designing ML Systems" Chip Huyen / Made With ML |

**到達点**: 業務で end-to-end ML pipeline を一人で構築できる

---

### C. 🤖 AI / LLM 開発の道

**目標**: ChatGPT/Claude のような LLM や生成 AI を作る・活用する

| 期間 | 学ぶこと | 推奨教材 |
|---|---|---|
| Month 1-2 | NN 基礎 (実装) | [Karpathy: Zero to Hero](online.md#karpathy-neural-networks-zero-to-hero) |
| Month 3 | Transformer 完全理解 | Karpathy: "Let's build GPT" + [Vaswani et al. 2017 原論文](https://arxiv.org/abs/1706.03762) |
| Month 4-5 | LLM 訓練の実装 | nanoGPT, [llm.c](https://github.com/karpathy/llm.c) のコードリーディング |
| Month 6 | LLM の使い分け・評価 | OpenAI / Anthropic API 公式ドキュメント |
| Month 7-8 | RAG / Agents | LangChain, LlamaIndex ドキュメント |
| Month 9-10 | ファインチューニング | LoRA, QLoRA, Hugging Face PEFT |
| Month 11-12 | 最前線研究 | [Anthropic Research](online.md#anthropic-research), [OpenAI](online.md#openai-blog) ブログ |

**到達点**: 自社のデータで LLM をファインチューニングして本番運用できる

---

### D. 📊 データサイエンティストの道

**目標**: ビジネス課題をデータで解決する

| 期間 | 学ぶこと | 推奨教材 |
|---|---|---|
| Month 1-2 | 統計学基礎 | [統計学入門 (赤本)](books.md#統計学入門) |
| Month 3 | ベイズ統計実用 | [データ解析のための統計モデリング入門 (緑本)](books.md#データ解析のための統計モデリング入門) |
| Month 4 | 因果推論 | [Causal Inference: What If](books.md#causal-inference-what-if) |
| Month 5 | 効果検証・A/B テスト | 「効果検証入門」 安井翔太 + "Trustworthy Online Controlled Experiments" |
| Month 6-7 | SQL + ダッシュボード | dbt, Looker, Tableau 等 |
| Month 8-12 | ドメイン知識 + 実プロジェクト | 自分の業界で 1 つ end-to-end の分析プロジェクト |

**到達点**: ビジネス意思決定に直結する分析を自走できる

---

### E. 🏃 趣味・教養として「ゆっくり一生学ぶ」道

**目標**: 焦らず、知的好奇心を満たすペースで

| 期間 | 学ぶこと | 推奨 |
|---|---|---|
| 月 1〜2 冊 | 興味のある本を読む | [数学ガール シリーズ](books.md#数学ガール) (結城浩) |
| 週 1 本 | 動画を見る | [3Blue1Brown](online.md#3blue1brown), [ヨビノリたくみ](online.md#ヨビノリたくみ) |
| 月 1 つ | 簡単な実験 | Jupyter で何か可視化、Kaggle Notebook を読む |
| 年に 1 つ | 大きいテーマに挑戦 | 例: 「今年は確率論をやる」 のように |

**到達点**: 一生楽しめる「**数学・AI を読み解く目**」

---

## 🌟 分野別の名著リスト (もう一段深く)

### 線形代数 (深く)
1. [Linear Algebra Done Right](books.md#linear-algebra-done-right) (Axler)
2. [プログラミングのための線形代数](books.md#プログラミングのための線形代数) (平岡・堀)
3. **The Matrix Cookbook** (Petersen & Pedersen) - 行列計算の早見表 🆓

### 微積分・解析 (深く)
1. [解析入門 I, II](books.md#解析入門-i-ii) (杉浦光夫)
2. **Principles of Mathematical Analysis** (Walter Rudin) - "Baby Rudin"
3. **Calculus on Manifolds** (Spivak)

### 確率論 (深く)
1. **Probability with Martingales** (David Williams)
2. **Probability: Theory and Examples** (Rick Durrett)
3. **An Introduction to Probability Theory** (Geoffrey Grimmett)

### 最適化 (深く)
1. [Convex Optimization](books.md#convex-optimization) (Boyd & Vandenberghe)
2. [Numerical Optimization](books.md#numerical-optimization) (Nocedal & Wright)
3. **Nonlinear Programming** (Bertsekas)

### 機械学習理論 (深く)
1. **Foundations of Machine Learning** (Mohri, Rostamizadeh, Talwalkar)
2. **Understanding Machine Learning** (Shalev-Shwartz & Ben-David) 🆓
3. **High-Dimensional Statistics** (Wainwright)

### 深層学習理論 (最先端)
1. **Mathematics of Deep Learning** (E, Han, Jentzen 等)
2. **Theory of Deep Learning** (Arora et al.)
3. arXiv の "deep learning theory" カテゴリ

### LLM 専門
1. [Build a Large Language Model (From Scratch)](books.md#build-a-large-language-model-from-scratch) (Raschka)
2. [Speech and Language Processing](books.md#speech-and-language-processing) (Jurafsky & Martin) 🆓
3. The Illustrated Transformer (Jay Alammar) ✍️

---

## 💡 「ML エンジニアとして 1 年で成長する」 サンプル週次プラン

| 曜日 | 内容 |
|---|---|
| 月 | 動画 1 本 (Karpathy か StatQuest) |
| 火・水 | 書籍 1 章 (現在進行中の本) |
| 木 | 論文 1 本サマリー (arxiv) |
| 金 | Kaggle Notebook を 1 つ読む |
| 土 | 自分のプロジェクトに 4 時間 |
| 日 | 雑談・ML Twitter チェック |

→ 1 年で「**動画 50, 書籍 4 冊, 論文 50, ノート 50, プロジェクト 200 時間**」 達成可能。

---

## 🚦 「学習で挫折しないコツ」 まとめ

1. **完璧主義をやめる** — 70% 理解で次に進む。後で戻れば 100% になる
2. **手を動かす** — 読むだけは身につかない。`jupyter lab` で実際に試す
3. **AI を活用する** — 分からない箇所は ChatGPT/Claude に聞く
4. **アウトプット** — Twitter/blog/Zenn で学んだことを書く
5. **コミュニティ** — 1 人で学ばない。勉強会、Discord、Twitter で仲間を見つける
6. **メンター** — 可能なら 1 人見つける。ML 業界は LinkedIn 経由で会いやすい

---

## 🤖 「AI 時代の学習」 のヒント

- 教科書を読んで詰まったら、**ChatGPT/Claude にその段落を貼って質問** する
- コードが分からないなら、**そのコードを AI に貼って「行ごとに解説して」**
- 自分の理解を確認したいなら、**AI に「私が説明するから、間違いを指摘して」**
- 演習問題を作ってもらう: 「○○の章の内容で、5 問問題を作って解説付きで」

本リポジトリの [`/project:teach-baby`](../.claude/commands/teach-baby.md) や [`/project:explain-symbol`](../.claude/commands/explain-symbol.md) も、この目的のために用意してあります。

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`online.md`](online.md) | [章 TOP (Appendix)](README.md) | [📚 ROOT README](../README.md) | (Appendix 終了 → ROOT へ) |
