# 用語集・記号リファレンス

学習中の「逆引き」用。論文・教科書・生成AI出力で出てきた記号や用語を即座に調べる。

## ファイル

- [`symbol_reference.md`](symbol_reference.md) — 数学記号と Python 対応の一覧
- [`jp_en_terms.md`](jp_en_terms.md) — 日英用語対訳（英語論文を読むときの辞書）

## 使い方

### 記号がわからないとき
1. [`symbol_reference.md`](symbol_reference.md) を Ctrl+F で検索
2. 載っていなければ Claude Code で `/project:explain-symbol <記号>`
3. 学んだら自分でこのファイルに追記

**よくあるつまずき別の入口**:

| こういうとき | 見るところ |
|---|---|
| $\hat{\theta}$ や $\bar{x}$ の**帽子や棒**が何なのかわからない | [文字につく飾り](symbol_reference.md#7-文字につく飾りハットバーチルダ) |
| $\mathbb{R}$ と $R$、$\mathcal{L}$ と $L$、太字の $\mathbf{x}$ の**違い**がわからない | [書体の違い](symbol_reference.md#8-書体の違い) |
| 行列の記号（$A^\top$, $\odot$, $\|x\|_2$, $\lambda$）を調べたい | [線形代数](symbol_reference.md#9-線形代数) |
| 統計の記号（$\mathbb{E}$, $\sigma$, $\perp\!\!\!\perp$, $\mathcal{N}$）を調べたい | [確率・統計](symbol_reference.md#10-確率統計) |
| 論文の $\theta$, $\hat{y}$, $\mathcal{D}$, $\nabla_\theta \mathcal{L}$ が読めない | [機械学習で頻出](symbol_reference.md#12-機械学習で頻出) |

### 英語の数学用語に出会ったとき
1. [`jp_en_terms.md`](jp_en_terms.md) を Ctrl+F で検索
2. なければ追記する習慣を

---

## 📚 関連: もっと深く学びたい方へ

本リポジトリの先に進みたい方は **Appendix** をご覧ください:

- 📂 [`../appendix/`](../appendix/README.md) — **書籍 + Web リソース集**
  - [`books.md`](../appendix/books.md) — 50 冊の厳選書籍 (日英・初級〜上級・有料/無料)
  - [`online.md`](../appendix/online.md) — YouTube・MOOC・公式ドキュメント・論文サイト
  - [`learning_paths.md`](../appendix/learning_paths.md) — 進路別 (研究/MLエンジニア/LLM開発/DS) ロードマップ

各章ごとのおすすめ書籍・サイトもまとめてあります。

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [プロジェクト ROOT](../README.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`symbol_reference.md`](symbol_reference.md) |
