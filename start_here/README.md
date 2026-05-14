# start_here — まずはここから（数学を全く知らない人向け）

「数学って学校でやって以来、実生活でなんの役に立つのかわからない」
「記号を見るだけで頭が拒否する」
「でも、生成AI・スマホ・GPSの裏側で数学が動いてるらしい」

そんな方のための**超ベビーステップ**章です。

## この章の方針

- **数式より、たとえ話と絵を優先**
- **「これって私たちの生活のどこにあるの？」を毎回示す**
- **数学の歴史や偉人エピソード**で人間味を持たせる（→ `columns/`）
- **Jupyter Lab でスライダーをいじりながら遊べる**（→ `notebooks/`）
- 疲れたら、まずコラムだけ読むのもOK

## ⚠️ ターミナルもプログラミングも触ったことがない方へ

**真っ黒な画面 (ターミナル) や Python という単語に拒否反応がある** 方は、まずここから:

→ **[`00_pet_terminal/`](00_pet_terminal/README.md)** — ペンギンの **ペンタ** と一緒に、ターミナル基礎をゼロから学ぶ章

ここを終えてから下記の数学パートに進めば、`uv run lab.py` などの呪文も理解した上で実行できます。

## 学習順序

| ファイル | 何がわかる？ | どのくらい時間がかかる？ |
|---|---|---|
| [`00_pet_terminal/`](00_pet_terminal/README.md) | ターミナル・CLI・Python・uv・AI CLI（必要な人だけ） | 約3時間 |
| [`01_why_math.md`](01_why_math.md) | そもそも数学って何の役に立つ？ | 15分 |
| [`02_pythagoras.md`](02_pythagoras.md) | ピタゴラスの定理（家・GPS・モニタの基礎） | 30分 |
| [`03_trigonometry.md`](03_trigonometry.md) | 三角関数（スマホ・音楽・アニメの基礎） | 45分 |
| [`04_logarithm.md`](04_logarithm.md) | 対数（地震・音のデシベル・pH） | 30分 |

## コラム欄（読み物・疲れたとき用）

`columns/` フォルダの中に。

| ファイル | 話のジャンル |
|---|---|
| [`00_what_is_math.md`](columns/00_what_is_math.md) | 数学はどこから来たのか（歴史ざっくり） |
| [`01_pythagoras_story.md`](columns/01_pythagoras_story.md) | ピタゴラスの謎の宗教団体の話 |
| [`02_trig_in_real_world.md`](columns/02_trig_in_real_world.md) | 三角関数が現代社会で使われている場所 |
| [`03_zero_invention.md`](columns/03_zero_invention.md) | 「ゼロ」を発明した人類の物語 |
| [`04_e_and_pi.md`](columns/04_e_and_pi.md) | π（円周率）と e（自然対数の底）の不思議 |
| [`05_math_in_ai.md`](columns/05_math_in_ai.md) | 今のAIは数学のどこで動いているか |

## Jupyter ノートブック（遊んでみる）

`notebooks/` の中に。Jupyter Lab で開いてセルを実行・編集できる。

| ノートブック | 何で遊べる？ |
|---|---|
| [`01_pythagoras.ipynb`](notebooks/01_pythagoras.ipynb) | 直角三角形の辺の長さをスライダーで動かす |
| [`02_trigonometry.ipynb`](notebooks/02_trigonometry.ipynb) | sin/cos の波を動かしてみる |
| [`03_trig_usecases.ipynb`](notebooks/03_trig_usecases.ipynb) | 音波・GPS・アニメ・フーリエ変換のデモ |

### Jupyter Lab を起動する

```bash
# プロジェクトルートで（Windows・Mac・Linux共通）
uv sync                  # 初回のみ
uv run lab.py
```

ブラウザが自動で開きます。`start_here/notebooks/01_pythagoras.ipynb` を開いて、上から順にセルを実行（Shift + Enter）してみてください。

## CLI で動的に学ぶ（Claude Code / Codex / Gemini CLI）

この章には**3つの専用コマンド**があります:

```
/project:teach-baby <なんでも>   # 数式ゼロ・たとえ話だけで説明
/project:column <トピック>        # 歴史 + 現代の使われ方を読み物風に
/project:visualize <概念>         # matplotlib で可視化するコードを生成
```

たとえば:
- `/project:teach-baby ベクトルって何？`
- `/project:column フーリエ変換`
- `/project:visualize sin と cos の関係`

CLI から「歩きながら散歩感覚で」学べるよう設計してあります。

## 次の章へ

`start_here/` を終えたら、[`../00_notation/`](../00_notation/README.md)（記号の読み解き）に進むのがおすすめです。
詳しい順序は [`../docs/learning_path.md`](../docs/learning_path.md) を参照。

---

## 📚 さらに学ぶ

数学に親しむ「読み物」 から始めるのが王道:

- 📕 **[数学ガール シリーズ](../appendix/books.md#数学ガール)** (結城浩) — 物語仕立てで数学を体感
- 📕 **[プログラマの数学 第2版](../appendix/books.md#プログラマの数学)** (結城浩) — プログラマー向け数学入門
- 🌐 **[3Blue1Brown](../appendix/online.md#3blue1brown)** — 数学を動画で直感的に (英語、字幕あり)
- 🌐 **[ヨビノリたくみ](../appendix/online.md#ヨビノリたくみ)** — 日本語で大学数学を分かりやすく

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`../appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [プロジェクト ROOT](../README.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | [`00_pet_terminal/README.md`](00_pet_terminal/README.md) |
