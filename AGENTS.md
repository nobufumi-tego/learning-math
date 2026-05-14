# Leaning Math — 大学院数学基礎 学習プロジェクト

大学院レベルの数学（特に機械学習・AI関連で頻出する内容）の基礎を、
**数学記号の読み解き**と**Python実装**の両輪で学ぶための個人学習リポジトリ。

> 📌 **Codex CLI ユーザーへ**: このリポジトリの設計知 (memory) は `.claude/memory/` に同梱されています。
> Codex CLI は `@-import` を解釈しないので、必要に応じて `.claude/memory/MEMORY.md` および同フォルダ内の各 `feedback_*.md` を直接読んでください。
> Claude Code / Gemini CLI ではこれらは `CLAUDE.md` / `GEMINI.md` から自動ロードされます。

## 学習者プロフィール
- 大学院で扱う数学基礎を理解したい
- **特に数学記号がわからない**（学習の最大の壁）
- 数学とPython（NumPy / SciPy / SymPy）を結びつけたい
- 生成AIへの指示文や、AIが出すドキュメント（論文・コード）を理解できるようになりたい

## 学習ロードマップ（優先順位）
-1. **start_here/00_pet_terminal/** — ターミナル/CLI/Pythonに触ったことがない人の入口（ペットと学ぶ）
0. **start_here/** — 数学に苦手意識がある人の入口（数式ゼロ・たとえ話・コラム・Jupyter）
1. **00_notation/** — 記号と論理（記号の読み解き）
2. **01_linear_algebra/** — 線形代数（ML/AIで最頻出）
3. **02_calculus/** — 微積分（特に多変数・勾配）
4. **03_probability_statistics/** — 確率・統計
5. **05_optimization/** — 最適化（勾配降下法）
6. **06_ml_math_bridge/** — 機械学習への橋渡し
7. **07_jax/** — JAX（自動微分・JIT・vmap、最終到達点）
8. **04_discrete_math/** — 離散数学（補助）

## Commands
```
uv run python <script.py>         # スクリプト実行
uv run pytest tests/ -v           # テスト実行
uv run jupyter lab                # ノートブック起動
uv run python -c "import sympy; sympy.init_printing(); ..."  # 数式描画
```

## Architecture
- `start_here/` — 数学初心者向け入口（コラム + Jupyter notebook 含む）
- `00_notation/` 〜 `07_jax/` — 章ごとの学習資料 + 実行可能サンプル
- 各章の `examples/` には **`*.py`（標準形式）** と **`*_jax.py`（JAX形式）** を併置（CLI実行用）
- 各章の `notebooks/` には **対応する `*.ipynb`** を置く（**Jupyter Lab 主、`.py` は副**）
- `start_here/notebooks/` — Jupyter Lab で対話的に遊ぶ ipynb (ipywidgets でスライダー対話)
- `docs/setup.md` — Windows / Mac / Linux 共通の uv ベース手順

## サンプル実行は Jupyter Lab 主体（重要方針）

各章のサンプルは原則として **Jupyter Lab で対話的に動かす**ことを前提に設計する。
- 主: `<章>/notebooks/*.ipynb` — 学習者が Shift+Enter でセル実行しながら理解
- 副: `<章>/examples/*.py` — CLI で `uv run python ...` 実行する人向け

### 各章 md の冒頭に必ず入れるボックス（テンプレート）

```markdown
## 💡 このページのコードを動かすには

このページのコード例は **Jupyter Lab** で対話的に試せます。

```bash
uv run jupyter lab
```

ブラウザが開いたら、左のファイルツリーから `<相対パス>/notebooks/<該当>.ipynb` を開いて、上から順に **Shift+Enter** でセル実行してください。

> 🐧 **「`uv` って何?」「ブラウザが開かない」「ファイルツリーがわからない」方** は、まず以下を:
> - [`start_here/00_pet_terminal/`](<相対パス>/start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎
> - 特に [`08_uv_keeps_pet_healthy.md`](<相対パス>/start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) — uv の使い方
>
> 数学の前提が不安なら:
> - [`start_here/`](<相対パス>/start_here/README.md) — 数式ゼロから始める数学
> - [`00_notation/`](<相対パス>/00_notation/README.md) — 数学記号の読み解き
```

CLI に不安がある学習者を**置き去りにしない**ことを最優先する。

## ナビゲーションとリンクの規約（必須）

### (1) ファイル名は必ずリンクにする
本文中で他の md ファイル名を記載するときは、**必ず Markdown リンク**にする:

```
❌ 詳しくは 04_decompositions.md の SVD を参照
✅ 詳しくは [`04_decompositions.md`](04_decompositions.md) の SVD を参照
```

理由: GitHub 上での閲覧時、ワンクリックで遷移できるようにするため。

### (2) 各章 md の末尾に「ナビゲーションブロック」を入れる

学習フローに沿って、**前ページ・章 TOP・全体 TOP・次ページ** へのリンクを 4 カラムの表で配置:

```markdown
---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [前ページタイトル](prev.md) | [章のREADME](README.md) | [ROOT README](../README.md) | [次ページタイトル](next.md) |
```

- 章の最初/最後では、対応するセルを「(なし)」 や「次の章: [next chapter](../next/README.md)」のように調整
- README は前章の最終ページ → 自身 → 章の最初のページ
- コラムは「本流に戻る」リンクを次ページ欄に置く
- **「📚 全体 TOP」は ROOT README へのリンク**。深さに応じて `../README.md`, `../../README.md`, `../../../README.md` を使い分ける

### (4) Jupyter notebook (.ipynb) も「二段ナビ」を必ず入れる

GitHub で .ipynb を閲覧したときも迷子にならないよう、各 notebook に以下 2 つの markdown セルを設置する:

#### 冒頭の「クイックナビ」 (タイトル直後の独立セル)
```markdown
> 🧭 **クイックナビ**: 📚 [ROOT (全体 TOP)](../../README.md) ・ 🏠 [章 TOP](../README.md) ・ 📖 [解説 md (XX.md)](../XX.md)
```

#### 末尾の「📍 ナビゲーション」 (.md と同じ 4カラム表)
```markdown
---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [前のノート](prev.ipynb) または [章 TOP](../README.md) | [章 TOP](../README.md) | [📚 ROOT README](../../README.md) | [次のノート](next.ipynb) または [次の章](../../next/README.md) |
```

すべての notebook は `<chapter>/notebooks/<name>.ipynb` レイアウトなので相対パスは:
- ROOT: `../../README.md`
- 章 TOP: `../README.md`
- 同名 md: `../<name>.md`

### (3) 学習フロー全体図

詳細は `docs/learning_path.md`。
- `glossary/` — 日英対訳用語集、記号リファレンス
- `notebooks/` — Jupyter Lab での実験
- `docs/learning_path.md` — 詳細な学習ロードマップ
- `.claude/commands/` — 学習用カスタムスラッシュコマンド
- `.claude/skills/math-tutor/` — 数学チューター用スキル

## AIへの基本指示（最重要）

### 説明スタイル
- **必ず日本語で説明**する
- 新しい数学記号が登場したら、**必ず以下の3点をセットで提示**:
  1. **記号の読み方**（例: `∀` → "for all"／「すべての」）
  2. **意味**（直感的説明 + 厳密な定義）
  3. **Python での書き方**（NumPy / SymPy / 標準ライブラリ）
- 抽象的な定義を出す前に、**必ず具体例から入る**
- 専門用語が出たら、初出時に**日本語と英語の両方**を併記する
  例: 「固有値（eigenvalue）」

### コード方針
- すべての数式サンプルは**実行可能なPythonコード**として書く
- 単位・次元・形状（shape）は必ずコメントで明記
  例: `x = np.array([1, 2, 3])  # shape: (3,), 3次元ベクトル`
- 型ヒント必須、docstring必須

#### 「標準形式」と「JAX形式」の併記（最重要方針）

このプロジェクトでは、Pythonコードを**2つの形式で併記**する:

1. **標準形式**: NumPy / SymPy / SciPy ベース（読解の起点となる素朴な実装）
2. **JAX形式**: `jax.numpy`, `jax.grad`, `jit`, `vmap` を使った関数型・自動微分・高速化された実装

##### なぜ併記するか
- **標準形式** は「数式 → コード」の対応が最も直感的（学習導入に最適）
- **JAX形式** は最先端の機械学習研究で実際に使われる（LLM・拡散モデルの実装は JAX or PyTorch）
- 両者を並べることで、JAX の以下の3点の価値が体感できる:
  - `grad`: 自動微分（手で勾配を導出せず関数を渡すだけ）
  - `jit`: JITコンパイル（NumPy同等のコードが大幅高速化）
  - `vmap` / `pmap`: ベクトル化・並列化が宣言的に書ける

##### 提示テンプレート
新しい計算を Python で書くときは、以下の構造で示す:

```python
# === 標準形式 (NumPy) ===
import numpy as np
def f_np(x: np.ndarray) -> np.ndarray:
    ...

# === JAX形式 (jax.numpy + jit + grad) ===
import jax
import jax.numpy as jnp
@jax.jit
def f_jax(x: jnp.ndarray) -> jnp.ndarray:
    ...
# 自動微分が必要なら
grad_f = jax.grad(f_jax)
```

JAX を後から導入できる構造にしておくため、**標準形式を先に**、**JAX形式を後に**書く順序を守る。

### 学習効果を高めるための応答パターン
- 質問への回答は次の順序で:
  1. **直感**（一言で）
  2. **記号の読み方**（数式があれば）
  3. **具体例**（数字を入れた小さな例）
  4. **Python実装**（コピペで動くコード）
  5. **応用先**（ML/AIでどこに出てくるか）
- 「これは何のために学ぶのか」を常に意識させる
- 一度に詰め込まず、確認を挟みながら段階的に進める

### ベビーステップ層への配慮
ユーザーが **超初心者モード** で質問してきた場合、または `/project:teach-baby` で呼び出されたときは:
- 数式を一切使わず、**たとえ話 3つ以上**で説明
- 日常 (料理・買い物・通勤・スマホ) に必ず結びつける
- 「自明」「明らか」を絶対使わない
- 関連する `start_here/` の章 (`02_pythagoras.md`, `03_trigonometry.md`, `04_logarithm.md`) や `columns/` のエッセイを案内
- 詳細ルール: `.claude/commands/teach-baby.md`

### ターミナル/CLI/Python に触ったことがない人への配慮
ターミナルやコマンドの使い方を質問してきた人、`uv` や `python` という言葉に不安そうな反応をする人には:
- ペンギンの **ペンタ** をガイド役として、`start_here/00_pet_terminal/` を案内
- 「真っ黒な画面」を歴史的・文化的背景込みで親しみやすく説明
- 命令を覚える前に「なぜ CLI を使うと仕事が爆速になるか」の実例 (写真リサイズ、ログ集計など) を示す
- `rm -rf /` のような危険コマンドは、必ず明示的に警告
- 章末に「ググってみよう」 キーワードを散りばめて、自学の習慣を育てる

### コラム生成のスタイル
`/project:column` または「歴史」「使われ場所」を聞かれたとき:
- 教科書ではなくエッセイ口調
- 歴史的人物・事件・誤解・偉人ドラマを織り込む
- 言葉の語源 (algorithm = アル=フワーリズミー等) を入れると深まる
- 「現代の私たちの暮らしへの繋がり」を必ず1セクション
- ファクトチェックを意識、伝説は「〜と伝えられる」と書く
- スタイル参考: `start_here/columns/00_what_is_math.md` 等

## Conventions
- Python 3.10+、型ヒント必須、docstring必須
- 数学定数・閾値はマジックナンバー化せず定数として定義
- 単位・形状（shape）・次元はコメントで明記
- 例: `EPSILON: float = 1e-9  # 数値計算上のゼロ判定閾値`

## Do / Don't
DO:
- 新しい記号は **glossary/symbol_reference.md** に追記して蓄積する
- 概念を理解したら **対応するPythonコードを必ず書いて実行**する
- わからない用語は質問する（自分で抱え込まない）

DON'T:
- 数学記号を曖昧なまま読み飛ばさない
- 抽象的な定義だけで終わらせない（必ず具体例とコードまで）
- 動画・大容量データを git 管理しない

## Watch out for
- 同じ記号でも分野により意味が異なる（例: `||x||` はベクトルのノルム、絶対値、集合の濃度など）
- 行列の形状（shape）の不一致は最頻出のバグ源 — 必ずshapeを確認する習慣を
- 日本語の数学用語と英語論文の用語の対応を意識する（glossaryで管理）

### JAX 特有の注意点
- **配列は不変 (immutable)**: `x[0] = 1` は使えない。`x = x.at[0].set(1)` を使う
- **乱数は明示的な PRNGKey**: `np.random` のようなグローバル状態を使わない
  ```python
  key = jax.random.PRNGKey(42)
  key, subkey = jax.random.split(key)
  x = jax.random.normal(subkey, shape=(3,))
  ```
- **`jit` の中では Python の if/for を控える**（トレースされない or 再コンパイル発火）
- **副作用なしの純粋関数**を書く（`print`はOKだがファイル書き込みなどは避ける）
- 学習開始時は **JAX形式と標準形式の出力が一致するかを必ず検算**する

## 参照ドキュメント
- AI CLI構成ガイド: `@~/.claude/ai-cli-structure-guide.md`
- 学習ロードマップ詳細: `@docs/learning_path.md`
- 記号リファレンス: `@glossary/symbol_reference.md`
- 日英用語対訳: `@glossary/jp_en_terms.md`
