# 00. 数学記号と論理 — 最優先章

> ⚠️ **未検証の個人学習教材**: 本章は AI 協働で作成され、専門家の監修を受けていません。誤りを含む可能性があるため、必ず一次情報源で検証してください ([詳細](../DISCLAIMER.md))。
> 📜 **ライセンス**: 文書 [CC BY-NC-SA 4.0](../LICENSE-DOCS) / コード [MIT](../LICENSE-CODE) — 商用利用 (書籍化・有料講座・企業研修等) は[要相談](../DISCLAIMER.md#-商用利用について--commercial-use)
> 🧪 **Jupyter Lab で読むのがおすすめ**: 起動方法と使い方 (Shift+Enter 等) は [`docs/jupyter_lab_guide.md`](../docs/jupyter_lab_guide.md) を参照。.md ファイルが整形プレビューで読めます。

**ゴール**: 数学論文・教科書・生成AIの出力に出てくる**記号を恐れずに読める**ようになる。

## なぜここから始めるか

大学院レベルの数学が難しく感じる最大の理由は、内容ではなく**記号**です。
記号の読み方さえ知れば、英語論文も生成AIの説明も「翻訳」できるようになります。

## 学習順序

| md (読む) | ipynb (動かす) | 内容 | 所要時間目安 |
|---|---|---|---|
| [`01_basic_symbols.md`](01_basic_symbols.md) | [`notebooks/01_basic_symbols.ipynb`](notebooks/01_basic_symbols.ipynb) | 等号・不等号・無限・± | 30 分 |
| [`02_set_theory.md`](02_set_theory.md) | [`notebooks/02_set_theory.ipynb`](notebooks/02_set_theory.ipynb) | 集合 ∈ ∉ ⊂ ⊆ ∪ ∩ ∅ | 1 時間 |
| [`03_logic_symbols.md`](03_logic_symbols.md) | [`notebooks/03_logic_symbols.ipynb`](notebooks/03_logic_symbols.ipynb) | 論理 ∀ ∃ ⇒ ⇔ ∧ ∨ ¬ | 1 時間 |
| [`04_function_notation.md`](04_function_notation.md) | [`notebooks/04_function_notation.ipynb`](notebooks/04_function_notation.ipynb) | 関数記法 f: A → B, ↦ | 30 分 |
| [`05_summation_product.md`](05_summation_product.md) | [`notebooks/05_summation_product.ipynb`](notebooks/05_summation_product.ipynb) | Σ・Π・∫・$n!$・$\binom{n}{k}$ | 1 時間 |
| [`06_greek_letters.md`](06_greek_letters.md) | [`notebooks/06_greek_letters.ipynb`](notebooks/06_greek_letters.ipynb) | ギリシャ文字 + LaTeX 記法 | 30 分 |

合計約 4〜5 時間で「読める目」 が手に入ります。各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進める** のが効果的です。

---

## 💡 動かす前に

このフォルダのコードは **Jupyter Lab** で対話的に動かすのが推奨です。

🚀 **起動方法** (リポジトリのルートで実行):
- 🪟 **Windows**: [`start.bat`](../start.bat) を **ダブルクリック** ⭐
- 🍎 **Mac** / 🐧 **Linux**: ターミナルで `./start.sh`
- 🪟 **PowerShell 派**: `.\start.ps1`
- 🛠️ **すでに環境がある人**: `uv run lab.py`

> ⏰ **初回起動は 5〜15 分かかります**。詳細・トラブルシューティングは ROOT [`README.md`](../README.md#step-2--ワンショットスクリプトで起動-推奨) 参照。
> 🧪 **Jupyter Lab の使い方** (Shift+Enter でセル実行など) は [`docs/jupyter_lab_guide.md`](../docs/jupyter_lab_guide.md) を参照。

---

## 学習方法

各ファイルで:
1. 記号一覧を眺める（暗記不要、雰囲気をつかむ）
2. **読み方**と**意味**を確認
3. `examples/notation_to_python.py` で実行して感触をつかむ
4. わからなくなったら `/project:explain-symbol <記号>` で再質問

## 実践

このセクション終了後、以下を試してください:
- 機械学習の論文の Abstract を読む
- `np.sum(x)` と `Σx_i` の対応を説明する
- ChatGPT/Claude に「行列の固有値分解」を質問して、出てきた数式を読み解く

---

## 📚 さらに学ぶ

- 📕 **[プログラマの数学 第2版](../appendix/books.md#プログラマの数学)** (結城浩) — 記号と論理を物語形式で
- 📕 **[数学ガール](../appendix/books.md#数学ガール)** (結城浩) — 記号と数式に親しむ
- 🌐 **[高校数学の美しい物語](../appendix/online.md#高校数学の美しい物語)** — 記号の意味を辞書的に検索

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`../start_here/04_logarithm.md`](../start_here/04_logarithm.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`01_basic_symbols.md`](01_basic_symbols.md) |
