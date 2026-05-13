# Leaning Math — 大学院数学基礎 × Python × 生成AI

「数学を全く知らない人」から「最先端AIの数学を理解する人」まで、**1つの道のり** で学ぶための個人学習リポジトリです。

## このリポジトリでできること

- 数学記号アレルギーを克服する
- 数式と Python (NumPy / JAX) を行き来できるようになる
- 生成AIに賢く指示を出せるようになる
- 機械学習の論文・コードを読み解けるようになる

## 3分で始める (Windows / Mac / Linux 共通)

```bash
# 1. uv をインストール (初回のみ)
# Mac/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows:
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. リポジトリのフォルダに移動
cd path/to/leaning-math

# 3. 依存関係のインストール
uv sync

# 4. Jupyter Lab を起動
uv run jupyter lab
```

ブラウザが自動で開いたら **`start_here/notebooks/01_pythagoras.ipynb`** を開いてください。
詳細な手順は [`docs/setup.md`](docs/setup.md) を参照。

## どこから始めるか — 学習者のレベル別

### 🐧 ターミナルもプログラミングも触ったことがない人
→ **`start_here/00_pet_terminal/`** から始める
- ペンギンの **ペンタ** と一緒に、真っ黒な画面の正体・CLI・Python・uv・AI CLI を学ぶ
- 4本のコラムでコンピュータ80年史、UNIX 哲学、キーボード文化、オープンソースを楽しむ
- 約3時間で「ターミナル怖くない、むしろ最強」となる

### 🌱 数学が全くわからない・苦手意識が強い人
→ **`start_here/`** から始める
- 数式ゼロ、たとえ話だけで「数学とは何か」を体感
- ピタゴラスの定理、三角関数、対数を「実生活の道具」として理解
- 歴史コラム (`columns/`) で、人類のドラマとして楽しむ
- Jupyter Lab (`notebooks/`) でスライダーを動かして遊ぶ

### 🌿 高校数学はやったけど忘れている人
→ **`00_notation/`** で記号の読み解きから

### 🌳 ML/AIの実装ができるようになりたい人
→ **`01_linear_algebra/`** → **`02_calculus/`** → **`06_ml_math_bridge/`** → **`07_jax/`**

詳しい順序は [`docs/learning_path.md`](docs/learning_path.md) を参照。

## ディレクトリ概要

| ディレクトリ | 内容 | 対象レベル |
|---|---|---|
| `start_here/00_pet_terminal/` | ペンタと学ぶターミナル基礎 + 4本のコラム | ⓪ ターミナル未経験者 |
| `start_here/` | 数学を全く知らない人向けベビーステップ + コラム + Jupyter notebook | ★ 最初 |
| `00_notation/` | 数学記号・論理・集合 | ★ |
| `01_linear_algebra/` | 線形代数 | ★★ |
| `02_calculus/` | 微積分・多変数解析 | ★★ |
| `03_probability_statistics/` | 確率・統計 | ★★ |
| `04_discrete_math/` | 離散数学・証明 | ★ |
| `05_optimization/` | 最適化 | ★★ |
| `06_ml_math_bridge/` | 機械学習への橋渡し | ★★★ |
| `07_jax/` | JAX (自動微分・JIT・vmap) | ★★★ |
| `glossary/` | 用語集・記号リファレンス | 参照用 |
| `notebooks/` | Jupyter Lab 作業用 | 作業用 |
| `docs/` | セットアップ手順、学習ロードマップ | 参照用 |

## Python 実装の方針: 「標準形式」 + 「JAX形式」 の併記

各章の `examples/` には以下の2形式を併置します:
- `xxx.py` — **標準形式** (NumPy / SymPy / SciPy): 数式 → コード対応が直感的
- `xxx_jax.py` — **JAX形式**: `jax.grad` で自動微分、`@jit` で高速化

JAX を最終到達点に据えることで、研究論文の最先端コード (Gemini, AlphaFold, etc.) が読める素養を獲得します。

## AI CLI で動的に学ぶ

3つの CLI ツールすべてで、専用カスタムコマンドが使えます:

| コマンド | 効果 |
|---|---|
| `/project:teach-baby <なんでも>` | 数式ゼロ・たとえ話だけで超やさしく説明 |
| `/project:column <トピック>` | 歴史・偉人エピソード・現代の使われ方の読み物 |
| `/project:visualize <概念>` | matplotlib + ipywidgets で対話的可視化コード生成 |
| `/project:explain-symbol <記号>` | 数学記号を「読み方・意味・Python対応・例」の4点で解説 |
| `/project:math-to-python <数式>` | 数式を実行可能な Python コードに変換 |
| `/project:concept-check <概念>` | ソクラテス式問答で理解度をチェック |

例:
```
/project:teach-baby ベクトルってなに？
/project:column ニュートンとライプニッツの微積分戦争
/project:visualize 正規分布の標準偏差
/project:explain-symbol ∂
```

### 対応 CLI ツール

- **Claude Code**: `claude` で起動
- **Gemini CLI**: `gemini` で起動
- **Codex CLI**: `codex` で起動

3ツールすべて `AGENTS.md` を共通指示書として読みます (`CLAUDE.md`, `GEMINI.md` は `@AGENTS.md` の1行インポート)。

## 環境

- Python 3.10+ (uv が自動取得)
- NumPy / SciPy / SymPy / matplotlib / Jupyter / JAX / ipywidgets
- OS: Windows / Mac / Linux すべて対応

## ライセンス

[MIT License](LICENSE) — 自由に使用・改変・再配布できます。

## 貢献

個人学習用リポジトリですが、誤りの指摘や改善提案は Issue / PR で歓迎します。

## 詳細ドキュメント

- [`docs/setup.md`](docs/setup.md) — 詳細セットアップ手順 (OS別トラブルシューティング含む)
- [`docs/ai_environment_setup.md`](docs/ai_environment_setup.md) — **clone 直後から本環境と同等の AI ドリブン体験** を実現する仕組み (memory 同梱の説明)
- [`docs/learning_path.md`](docs/learning_path.md) — 学習ロードマップ (約3か月コース)
- [`start_here/README.md`](start_here/README.md) — 数学初心者向けの入口
