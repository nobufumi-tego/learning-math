# Leaning Math — 大学院数学基礎 × Python × 生成AI

「数学を全く知らない人」から「最先端AIの数学を理解する人」まで、**1つの道のり** で学ぶための個人学習リポジトリです。

## このリポジトリでできること

- 数学記号アレルギーを克服する
- 数式と Python (NumPy / JAX) を行き来できるようになる
- 生成AIに賢く指示を出せるようになる
- 機械学習の論文・コードを読み解けるようになる

---

## 🚀 3分で始める (Windows / Mac / Linux 共通)

```bash
# 1. uv をインストール (初回のみ)
# Mac/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows:
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. リポジトリのフォルダに移動
cd path/to/learning-math

# 3. 依存関係のインストール
uv sync

# 4. Jupyter Lab を起動
uv run lab.py
```

ブラウザが自動で開いたら **[`start_here/notebooks/01_pythagoras.ipynb`](start_here/notebooks/01_pythagoras.ipynb)** を開いてください。
詳細な手順は [`docs/setup.md`](docs/setup.md) を参照。

---

## 🎯 どこから始めるか — 学習者のレベル別 入口

### 🐧 ターミナルもプログラミングも触ったことがない人

→ 最初の1ページ: **[`start_here/00_pet_terminal/README.md`](start_here/00_pet_terminal/README.md)**

ペンギンの **ペンタ** と一緒に、真っ黒な画面の正体・CLI・Python・uv・AI CLI を学ぶ (約3時間)。

### 🌱 数学が全くわからない・苦手意識が強い人

→ 最初の1ページ: **[`start_here/README.md`](start_here/README.md)**

数式ゼロ、たとえ話だけで「数学とは何か」を体感。ピタゴラス・三角関数・対数を「実生活の道具」として理解。

### 🌿 高校数学はやったけど忘れている人

→ 最初の1ページ: **[`00_notation/README.md`](00_notation/README.md)** で記号の読み解きから

### 🌳 ML/AIの実装ができるようになりたい人

→ [`01_linear_algebra/`](01_linear_algebra/README.md) → [`02_calculus/`](02_calculus/README.md) → [`06_ml_math_bridge/`](06_ml_math_bridge/README.md) → [`07_jax/`](07_jax/README.md)

詳しい順序は [`docs/learning_path.md`](docs/learning_path.md) を参照。

---

## 📚 全章ドキュメント案内 (すべてのページに直接アクセス)

### Phase −1: 🐧 ペットと学ぶターミナル基礎

📂 [`start_here/00_pet_terminal/`](start_here/00_pet_terminal/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_what_is_terminal.md`](start_here/00_pet_terminal/01_what_is_terminal.md) | 真っ黒な画面の正体 (歴史: テレタイプ→VT100) |
| 02 | [`02_meet_your_pet.md`](start_here/00_pet_terminal/02_meet_your_pet.md) | シェル (ペンタ) に挨拶 — bash/zsh/PowerShell |
| 03 | [`03_first_commands.md`](start_here/00_pet_terminal/03_first_commands.md) | 最初の3命令: `pwd` / `ls` / `cd` |
| 04 | [`04_files_and_folders.md`](start_here/00_pet_terminal/04_files_and_folders.md) | ファイル操作: `mkdir` / `touch` / `cp` / `mv` / `rm` |
| 05 | [`05_pipes_and_combine.md`](start_here/00_pet_terminal/05_pipes_and_combine.md) | パイプ `\|` の魔法 |
| 06 | [`06_why_cli_in_modern_work.md`](start_here/00_pet_terminal/06_why_cli_in_modern_work.md) | なぜ CLI で仕事が爆速になるのか |
| 07 | [`07_python_for_pets.md`](start_here/00_pet_terminal/07_python_for_pets.md) | ペンタが Python を覚える |
| 08 | [`08_uv_keeps_pet_healthy.md`](start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) | `uv` はペンタの世話係 |
| 09 | [`09_ai_cli_as_smart_pet.md`](start_here/00_pet_terminal/09_ai_cli_as_smart_pet.md) | AI CLI 時代 (Claude/Gemini/Codex) |

📖 コラム (読み物):
- [`columns/00_history_of_computer.md`](start_here/00_pet_terminal/columns/00_history_of_computer.md) — コンピュータ80年史
- [`columns/01_unix_philosophy.md`](start_here/00_pet_terminal/columns/01_unix_philosophy.md) — UNIX の哲学
- [`columns/02_keyboard_age.md`](start_here/00_pet_terminal/columns/02_keyboard_age.md) — キーボードがマウスより速い理由
- [`columns/03_open_source.md`](start_here/00_pet_terminal/columns/03_open_source.md) — オープンソースの物語

---

### Phase 0: 🌱 数学を全く知らない人向け

📂 [`start_here/`](start_here/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_why_math.md`](start_here/01_why_math.md) | そもそも数学って何の役に立つ？ |
| 02 | [`02_pythagoras.md`](start_here/02_pythagoras.md) | ピタゴラスの定理 (家・GPS・AI) |
| 03 | [`03_trigonometry.md`](start_here/03_trigonometry.md) | 三角関数 (スマホ・音楽・アニメ) |
| 04 | [`04_logarithm.md`](start_here/04_logarithm.md) | 対数 (地震・デシベル・pH) |

📖 コラム:
- [`columns/00_what_is_math.md`](start_here/columns/00_what_is_math.md) — 数学はどこから来たか (5000年史)
- [`columns/01_pythagoras_story.md`](start_here/columns/01_pythagoras_story.md) — ピタゴラスは数学者か宗教家か
- [`columns/02_trig_in_real_world.md`](start_here/columns/02_trig_in_real_world.md) — 三角関数が現代社会のどこに居るか
- [`columns/03_zero_invention.md`](start_here/columns/03_zero_invention.md) — ゼロの発明
- [`columns/04_e_and_pi.md`](start_here/columns/04_e_and_pi.md) — π と e の不思議
- [`columns/05_math_in_ai.md`](start_here/columns/05_math_in_ai.md) — 今のAIは数学のどこで動いているか

📓 Jupyter ノートブック (対話的に遊べる):
- [`notebooks/01_pythagoras.ipynb`](start_here/notebooks/01_pythagoras.ipynb) — ピタゴラスの定理
- [`notebooks/02_trigonometry.ipynb`](start_here/notebooks/02_trigonometry.ipynb) — 三角関数
- [`notebooks/03_trig_usecases.ipynb`](start_here/notebooks/03_trig_usecases.ipynb) — 音波・GPS・フーリエ

---

### Phase 1: 📐 数学記号と論理

📂 [`00_notation/`](00_notation/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_basic_symbols.md`](00_notation/01_basic_symbols.md) | 等号・不等号・無限・数の集合 (ℕℤℚℝℂ) |
| 02 | [`02_set_theory.md`](00_notation/02_set_theory.md) | 集合 ∈ ∉ ⊂ ⊃ ∪ ∩ |
| 03 | [`03_logic_symbols.md`](00_notation/03_logic_symbols.md) | 論理 ∀ ∃ ⇒ ⇔ ∧ ∨ ¬ |
| 04 | [`04_function_notation.md`](00_notation/04_function_notation.md) | 関数記法 f: A → B, ↦ |
| 05 | [`05_summation_product.md`](00_notation/05_summation_product.md) | Σ (総和) / Π (総乗) / ∫ (積分) |
| 06 | [`06_greek_letters.md`](00_notation/06_greek_letters.md) | ギリシャ文字一覧と慣習 |

🐍 サンプル:
- [`examples/notation_to_python.py`](00_notation/examples/notation_to_python.py) — 記号 → Python 対応例

---

### Phase 2: 📊 線形代数

📂 [`01_linear_algebra/`](01_linear_algebra/README.md) — 章 TOP

| # | 解説 (md) | 動かす (ipynb) | 内容 |
|---|---|---|---|
| 01 | [`01_vectors.md`](01_linear_algebra/01_vectors.md) | [`01_vectors.ipynb`](01_linear_algebra/notebooks/01_vectors.ipynb) | ベクトル・内積・ノルム・コサイン類似度 |
| 02 | [`02_matrices.md`](01_linear_algebra/02_matrices.md) | [`02_matrices.ipynb`](01_linear_algebra/notebooks/02_matrices.ipynb) | 行列・行列積・転置・逆行列・線形変換 |
| 03 | [`03_eigenvalues.md`](01_linear_algebra/03_eigenvalues.md) | [`03_eigenvalues.ipynb`](01_linear_algebra/notebooks/03_eigenvalues.ipynb) | 固有値・固有ベクトル・PCA・PageRank |
| 04 | [`04_decompositions.md`](01_linear_algebra/04_decompositions.md) | [`04_decompositions.ipynb`](01_linear_algebra/notebooks/04_decompositions.ipynb) | LU・QR・Cholesky・SVD (画像圧縮・推薦) |

🐍 CLI 実行サンプル:
- [`examples/vectors_and_matrices.py`](01_linear_algebra/examples/vectors_and_matrices.py) — 標準形式 (NumPy)
- [`examples/vectors_and_matrices_jax.py`](01_linear_algebra/examples/vectors_and_matrices_jax.py) — JAX形式

---

### Phase 3: 🌀 微積分 (骨格)

📂 [`02_calculus/`](02_calculus/README.md) — 章 TOP

> ⚠️ 本文 md は今後拡充予定 (現在は README + サンプルのみ)

🐍 サンプル:
- [`examples/derivative_demo.py`](02_calculus/examples/derivative_demo.py) — 標準形式 (SymPy / 数値差分)
- [`examples/derivative_demo_jax.py`](02_calculus/examples/derivative_demo_jax.py) — JAX形式 (`jax.grad`)

---

### Phase 4: 🎲 確率・統計 (骨格)

📂 [`03_probability_statistics/`](03_probability_statistics/README.md) — 章 TOP

> ⚠️ 本文 md は今後拡充予定 (現在は README + サンプルのみ)

🐍 サンプル:
- [`examples/distribution_demo.py`](03_probability_statistics/examples/distribution_demo.py) — 各種分布の可視化

---

### Phase 5: ⛰️ 最適化 (骨格)

📂 [`05_optimization/`](05_optimization/README.md) — 章 TOP

> ⚠️ 本文 md は今後拡充予定 (現在は README + サンプルのみ)

🐍 サンプル:
- [`examples/gradient_descent_demo.py`](05_optimization/examples/gradient_descent_demo.py) — 標準形式 (手で勾配導出)
- [`examples/gradient_descent_demo_jax.py`](05_optimization/examples/gradient_descent_demo_jax.py) — JAX形式 (`jax.grad`)

---

### Phase 6: 🌉 機械学習への橋渡し (骨格)

📂 [`06_ml_math_bridge/`](06_ml_math_bridge/README.md) — 章 TOP

> ⚠️ 本文 md は今後拡充予定 (現在は README + サンプルのみ)

🐍 サンプル:
- [`examples/loss_and_gradient.py`](06_ml_math_bridge/examples/loss_and_gradient.py) — 線形回帰 + クロスエントロピー (NumPy)
- [`examples/loss_and_gradient_jax.py`](06_ml_math_bridge/examples/loss_and_gradient_jax.py) — JAX で線形回帰 (自動微分)

---

### Phase 7: ⚡ JAX (自動微分・JIT・vmap)

📂 [`07_jax/`](07_jax/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_basics.md`](07_jax/01_basics.md) | `jax.numpy`・配列の不変性・PRNGキー |
| 02 | [`02_autodiff.md`](07_jax/02_autodiff.md) | `jax.grad`・`value_and_grad`・高階微分・ヤコビアン・ヘッシアン |
| 03 | [`03_jit_vmap.md`](07_jax/03_jit_vmap.md) | `@jit` で高速化・`vmap` でベクトル化 |

🐍 サンプル:
- [`examples/jax_basics.py`](07_jax/examples/jax_basics.py) — NumPy と JAX の対応
- [`examples/grad_demo.py`](07_jax/examples/grad_demo.py) — 自動微分の威力
- [`examples/jit_vmap_demo.py`](07_jax/examples/jit_vmap_demo.py) — JIT と vmap のベンチマーク

---

### Phase 8: 🔢 離散数学 (補助・骨格)

📂 [`04_discrete_math/`](04_discrete_math/README.md) — 章 TOP

> ⚠️ 本文 md は今後拡充予定 (現在は README のみ)

---

## 📖 用語集・リファレンス

📂 [`glossary/`](glossary/README.md)

- [`symbol_reference.md`](glossary/symbol_reference.md) — 数学記号 → Python 対応の逆引き辞書
- [`jp_en_terms.md`](glossary/jp_en_terms.md) — 日英用語対訳 (英語論文の辞書)

---

## 🛠️ Python 実装の方針: 「標準形式」 + 「JAX形式」 の併記

各章の `examples/` には以下の2形式を併置します:
- `xxx.py` — **標準形式** (NumPy / SymPy / SciPy): 数式 → コード対応が直感的
- `xxx_jax.py` — **JAX形式**: `jax.grad` で自動微分、`@jit` で高速化

JAX を最終到達点に据えることで、研究論文の最先端コード (Gemini, AlphaFold, etc.) が読める素養を獲得します。

---

## 🤖 AI CLI で動的に学ぶ

3つの CLI ツールすべてで、専用カスタムコマンドが使えます:

| コマンド | 効果 | 詳細 |
|---|---|---|
| `/project:teach-baby <なんでも>` | 数式ゼロ・たとえ話だけで超やさしく説明 | [.claude/commands/teach-baby.md](.claude/commands/teach-baby.md) |
| `/project:column <トピック>` | 歴史・偉人エピソード・現代の使われ方の読み物 | [.claude/commands/column.md](.claude/commands/column.md) |
| `/project:visualize <概念>` | matplotlib + ipywidgets で対話的可視化コード生成 | [.claude/commands/visualize.md](.claude/commands/visualize.md) |
| `/project:explain-symbol <記号>` | 数学記号を「読み方・意味・Python対応・例」の4点で解説 | [.claude/commands/explain-symbol.md](.claude/commands/explain-symbol.md) |
| `/project:math-to-python <数式>` | 数式を実行可能な Python コードに変換 | [.claude/commands/math-to-python.md](.claude/commands/math-to-python.md) |
| `/project:concept-check <概念>` | ソクラテス式問答で理解度をチェック | [.claude/commands/concept-check.md](.claude/commands/concept-check.md) |

例:
```
/project:teach-baby ベクトルってなに？
/project:column ニュートンとライプニッツの微積分戦争
/project:visualize 正規分布の標準偏差
/project:explain-symbol ∂
```

### 対応 CLI ツール

- **Claude Code** (`claude`) — `CLAUDE.md` 経由で全設定が自動ロード
- **Gemini CLI** (`gemini`) — `GEMINI.md` 経由で全設定が自動ロード
- **Codex CLI** (`codex`) — `AGENTS.md` をネイティブで読む

3ツールすべて [`AGENTS.md`](AGENTS.md) を共通指示書として読みます。
**clone した瞬間から本環境と同等の AI 体験** が手に入る仕組みについては [`docs/ai_environment_setup.md`](docs/ai_environment_setup.md) を参照。

---

## 📚 主要ドキュメント

| ドキュメント | 内容 |
|---|---|
| [`AGENTS.md`](AGENTS.md) | AI 共通指示書 (3ツール共通の説明スタイル・規約) |
| [`docs/setup.md`](docs/setup.md) | セットアップ詳細 (OS別トラブルシューティング含む) |
| [`docs/learning_path.md`](docs/learning_path.md) | 学習ロードマップ (Phase −1 〜 8、約3か月コース) |
| [`docs/ai_environment_setup.md`](docs/ai_environment_setup.md) | clone 直後から本環境と同等の AI 体験を実現する仕組み |
| [`pyproject.toml`](pyproject.toml) | Python 依存関係 |
| [`LICENSE`](LICENSE) | MIT License |

---

## 環境

- Python 3.10+ (uv が自動取得)
- NumPy / SciPy / SymPy / matplotlib / Jupyter / JAX / ipywidgets
- OS: Windows / Mac / Linux すべて対応

## ライセンス

[MIT License](LICENSE) — 自由に使用・改変・再配布できます。

## 貢献

個人学習用リポジトリですが、誤りの指摘や改善提案は Issue / PR で歓迎します。
