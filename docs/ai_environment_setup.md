# AI 学習環境のセットアップ — clone 直後から本環境と同等の体験を

このリポジトリは、Claude Code / Gemini CLI / Codex CLI を**プロジェクト固有の設計知 (memory) 込みで配布**しています。
clone するだけで、AI が「**この repo の流儀**」を理解した状態で動き出します。

## 何が同梱されているか

| 種別 | 場所 | 役割 |
|---|---|---|
| Agent 指示書 | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | 3 ツール共通の説明スタイル・規約 |
| カスタムコマンド | `.claude/commands/`, `.gemini/commands/` | `/project:teach-baby` など6種 |
| スキル | `.claude/skills/math-tutor/` | 数学チューター用ペルソナ |
| ルール | `.claude/rules/teaching-style.md` | 説明順序の厳守事項 |
| ツール設定 | `.claude/settings.json`, `.codex/config.toml` | hooks・権限・モデル選択 |
| **AI メモリ** | `.claude/memory/` | **設計判断・想定ユーザー像** ← ここがポイント |

## なぜメモリを repo に入れているか

通常、Claude Code のメモリは `~/.claude/projects/<project-id>/memory/` に保存され、**clone した相手には伝わりません**。

このリポジトリでは、**過去の対話で蓄積した設計判断 (どんな順序で説明すべきか、JAX をどう扱うか、初心者にどう接するか…)** を `.claude/memory/` に同梱し、`CLAUDE.md` から `@-import` で**自動ロード**するようにしています。

そのため clone した瞬間から、AI は

- 「数学記号は『読み方・意味・Python対応・例』の4点セットで説明する」
- 「サンプル実行は Jupyter Lab 主体、CLI が分からない人は `start_here/00_pet_terminal/` へ誘導」
- 「標準形式 (NumPy) と JAX 形式を併記する」

といった本リポジトリのルールを**理解した状態**で動きます。

## ツール別セットアップ

### Claude Code

```bash
# Claude Code をインストール (初回のみ)
npm install -g @anthropic-ai/claude-code

# repo フォルダで起動
cd path/to/learning-math
claude
```

`CLAUDE.md` が自動で読まれ、`@.claude/memory/...` も全部ロードされます。**追加作業ゼロ**。

確認方法:
```
> このリポジトリの設計方針を3つ挙げて
```
→ Jupyter主体 / 標準形式とJAX形式の併記 / ベビーステップ重視 などが返ってくれば成功。

### Gemini CLI

```bash
gemini
```

同様に `GEMINI.md` から自動ロードされます。

### Codex CLI

```bash
codex
```

Codex は `AGENTS.md` をネイティブで読みます。
ただし `@-import` は解釈しないので、メモリを参照させたい時は `.claude/memory/MEMORY.md` を**明示的に開いて**読むよう促してください。

## 「本物のメモリ」として永続化したい場合 (オプション)

`@-import` は会話のコンテキストにロードされるだけで、Claude Code の**永続メモリシステム**とは別です。
もしローカル環境で「これらを永続メモリとして登録」したい場合:

### Mac / Linux
```bash
# あなたのプロジェクトディレクトリの ID を確認 (Claude Code を一度起動すると作られる)
ls ~/.claude/projects/

# パスをコピーして:
TARGET=~/.claude/projects/<-your-project-id->/memory/
mkdir -p "$TARGET"
cp .claude/memory/*.md "$TARGET"
```

### Windows (PowerShell)
```powershell
$target = "$env:USERPROFILE\.claude\projects\<-your-project-id->\memory"
New-Item -ItemType Directory -Force -Path $target
Copy-Item .claude\memory\*.md $target
```

これで `/memory` コマンド等から「正式な」メモリとして扱われるようになります。
ただし `@-import` で十分機能するので、ほとんどの方はこの作業は不要です。

## 自分用にカスタマイズしたい

clone した方が自分のプロファイルに合わせて編集してOKです:

- `.claude/memory/user_math_learner.md` — あなたのレベル・目的に合わせて書き換え
- `.claude/memory/feedback_*.md` — 不要なものは `@-import` から外す
- 新しい好みを追加したい → `.claude/memory/feedback_my_style.md` を新規作成して `CLAUDE.md` に追記

**個人情報や機密はここに書かない**でください (公開リポジトリです)。
個人専用設定は `CLAUDE.local.md` (gitignore 済み) を作ってそこに。

## 動作確認チェックリスト

clone 後、以下が動けば AI 環境は本環境と同等:

- [ ] `claude` 起動 → エラーなし
- [ ] `> このリポジトリの設計方針を3つ挙げて` で 3 つ返る
- [ ] `/project:teach-baby ベクトル` でベビーステップ説明が返る
- [ ] `/project:explain-symbol ∀` で記号解説が返る
- [ ] `/project:column ピタゴラスの定理` でエッセイが返る
- [ ] `uv sync` 成功
- [ ] `uv run jupyter lab` でブラウザが開く
- [ ] `start_here/notebooks/01_pythagoras.ipynb` のセルが実行できる

すべてOKなら、本環境と同等の AI ドリブン学習体験が手に入っています。
