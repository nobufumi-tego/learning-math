# セットアップ手順 — Windows / Mac / Linux 共通

このリポジトリは **uv** で Python 環境を完全管理しており、**Windows・Mac・Linux で同じ手順** で動きます。

## 前提条件

- インターネット接続
- ターミナル (Windows なら PowerShell、Mac なら Terminal、Linux ならお好みで)

## ステップ 0: uv をインストール

uv は Astral 社製の超高速 Python パッケージマネージャ。Python 本体のインストールから依存解決まで全部やってくれます。

### Mac / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 確認

```bash
uv --version
```

バージョンが表示されればOK。

## ステップ 1: リポジトリを取得して移動

```bash
# 自分のローカルにこのリポジトリがある前提
cd path/to/leaning-math
```

## ステップ 2: 依存関係のインストール (初回のみ)

```bash
uv sync
```

これだけ。以下が自動で行われます:
- Python 3.10 以上が自動でダウンロード/設定
- `.venv/` に仮想環境が作られる
- `pyproject.toml` の依存パッケージ (NumPy / SciPy / SymPy / matplotlib / Jupyter / JAX / ipywidgets...) がすべてインストール

数分かかります (JAX は少し大きいパッケージなので)。

## ステップ 3: Jupyter Lab を起動

```bash
uv run lab.py
```

ブラウザが自動で開き、Jupyter Lab の画面が表示されます。

左のファイルツリーから `start_here/notebooks/01_pythagoras.ipynb` を開いて、上から順にセル実行 (Shift+Enter) してみてください。

> 💡 **`lab.py` って何?**
> リポジトリ ルートの [`lab.py`](../lab.py) は、本リポジトリ専用の JupyterLab 設定 (`.jupyter/lab/user-settings/`) を読み込んでから JupyterLab を起動するラッパースクリプトです。
> これにより、`.md` ファイルをダブルクリックしたときに **自動的に Markdown Preview モード** で表示されます (raw な markdown を編集モードで開かなくて済む)。
>
> 通常の `uv run jupyter lab` でも起動できますが、その場合は本リポジトリの設定は適用されません。
> 詳細は [`.jupyter/README.md`](../.jupyter/README.md) を参照。

## ステップ 3.5: Jupyter Lab を止める ⚠️

学習が終わったら、**起動したターミナル**で:

**`Ctrl+C` を 2 回押す** (Mac/Linux/Windows 共通)

すると "Shutdown this Jupyter server (y/[n])?" と聞かれます。
2回押せば即停止、聞かれたら `y` でも OK。

> ⚠️ **ブラウザのタブを × で閉じるだけでは止まりません！**
> Jupyter サーバーはバックグラウンドで動き続けます。
> 翌日 `uv run lab.py` をすると、**`Port 8888 is already in use`** というエラーが出て起動できなくなります。
>
> **必ず**ターミナルで `Ctrl+C` × 2 回してから閉じてください。

### 別の停止方法: JupyterLab の UI から

JupyterLab 画面の上部メニューから:
**File → Shut Down** をクリック → 確認ダイアログで Shut Down

これでサーバー側も停止します (ターミナルもプロンプトに戻る)。

### もし停止し忘れて、再起動できなくなったら 🆘

「Port 8888 is already in use」が出たら、残った Jupyter プロセスを強制終了:

#### Mac / Linux
```bash
# 8888 ポートを使ってるプロセスを kill
lsof -ti:8888 | xargs kill -9

# または、jupyter プロセスを全部 kill
pkill -f jupyter
```

#### Windows (PowerShell)
```powershell
# jupyter プロセスを停止
Get-Process | Where-Object { $_.ProcessName -like "*jupyter*" } | Stop-Process -Force

# またはタスクマネージャーから "python" を探して終了
```

これでもダメなら、PC を再起動すれば確実に止まります。

## ステップ 3.6: JupyterLab でよく見る英語ダイアログ 🗣️

JupyterLab のダイアログは **デフォルトで英語** です。
初心者は急に英語が出るとドキッとしがちですが、以下のパターンを覚えておけば慌てません。

### よく出る 6 ダイアログ

#### ① ノートブックを閉じようとしたら… (一番よく見る)

```
┌─ Save your work ─────────────────────┐
│ Save changes in "01_pythagoras.ipynb" │
│ before closing?                       │
│                                       │
│      [Discard]  [Cancel]  [Save]      │
└───────────────────────────────────────┘
```

**翻訳**: 「変更内容を保存しますか？」

| ボタン | 意味 | 押す場面 |
|---|---|---|
| **Save** | **保存して閉じる** ← 通常はこれ | 編集内容を残したい (デフォルト推奨) |
| Discard | **破棄して閉じる** | 変更を捨てて元に戻したい |
| Cancel | **やっぱり閉じない** | 間違って閉じようとした |

#### ② JupyterLab 全体を停止しようとしたら

```
┌─ Shut down JupyterLab? ───────────────┐
│ Are you sure you want to shut down    │
│ JupyterLab?                           │
│                                       │
│         [Cancel]  [Shut Down]         │
└───────────────────────────────────────┘
```

**翻訳**: 「JupyterLab を停止してよいですか？」

| ボタン | 意味 |
|---|---|
| **Shut Down** | **停止する** ← 終わるときはこれ |
| Cancel | **やめる** (作業継続) |

#### ③ カーネルを再起動しようとしたら

```
┌─ Restart kernel? ─────────────────────┐
│ Do you want to restart the kernel?    │
│ All variables will be lost.           │
│                                       │
│         [Cancel]  [Restart]           │
└───────────────────────────────────────┘
```

**翻訳**: 「カーネルを再起動しますか？ **すべての変数が消えます**」

| ボタン | 意味 | 押す場面 |
|---|---|---|
| **Restart** | **再起動する** | コードがハングした、最初からやり直したい |
| Cancel | **やめる** | 変数を残したい |

> ⚠️ Restart を押すと、これまでセル実行で読み込んだデータや計算結果が**全部消えます**。再度上から順に Shift+Enter で実行し直す必要があります。

#### ④ 出力を全部クリアしようとしたら

```
┌─ Clear all outputs ───────────────────┐
│ Are you sure you want to clear        │
│ all outputs?                          │
│                                       │
│         [Cancel]  [Clear]             │
└───────────────────────────────────────┘
```

**翻訳**: 「全セルの出力結果を消去してよいですか？」

| ボタン | 意味 |
|---|---|
| **Clear** | **消去する** (コードは残る、出力だけ消える) |
| Cancel | やめる |

#### ⑤ ファイルが外部で変更されたとき

```
┌─ File Changed ────────────────────────┐
│ The file has been changed externally. │
│ Reload it?                            │
│                                       │
│      [Don't Reload]  [Reload]         │
└───────────────────────────────────────┘
```

**翻訳**: 「ファイルが外部で変更されました。再読み込みしますか？」

| ボタン | 意味 | 押す場面 |
|---|---|---|
| **Reload** | **外部の変更を取り込む** | git pull した後など |
| Don't Reload | **JupyterLab 側を残す** | 自分の編集を優先したい |

#### ⑥ ブラウザを閉じようとしたとき (ブラウザ標準)

```
┌─ このサイトを離れますか？ (ブラウザ依存) ─┐
│ 行った変更が保存されない可能性があります。│
│                                          │
│         [このページに留まる] [離れる]    │
└──────────────────────────────────────────┘
```

これは**ブラウザの標準ダイアログ** (Chrome/Firefox/Safari)。
言語はブラウザの言語設定に従うので、日本語で出ることが多い。

| ボタン | 意味 |
|---|---|
| **このページに留まる** | やっぱり閉じない |
| 離れる | そのまま閉じる (未保存は失われる可能性) |

### 💡 ダイアログを最小化するコツ

#### こまめに保存する: **`Ctrl+S` (Mac は `⌘S`)**
- 編集中、こまめに **`Ctrl+S`** を押す習慣を付けると、保存ダイアログが出る場面が激減します
- JupyterLab には **オートセーブ** もあり、デフォルトで 120 秒ごとに自動保存

#### File → Save Notebook (メニューから)
- 上部メニュー: **File → Save Notebook** (`⌘S` と同じ)
- File → **Save Notebook As...** で別名保存も可

### オプション: JupyterLab の UI を日本語化したい

「やっぱり全部日本語が良い」という場合:

```bash
# 日本語パッケージをインストール
uv add jupyterlab-language-pack-ja-JP

# JupyterLab を起動
uv run lab.py
```

JupyterLab 起動後:
1. **Settings → Language → 日本語 (Japanese)** を選択
2. ブラウザをリロード
3. **メニューもダイアログも全部日本語** になる

> 💡 ただし、**プログラミングの世界は基本的に英語が公用語**。エラーメッセージ・ドキュメント・Stack Overflow は英語です。
> 慣れるためにも **デフォルトの英語のまま** を推奨します (このガイドで翻訳が確認できます)。

## ステップ 4: Python スクリプトを直接実行する

各章の `examples/` 内のスクリプトはコマンドで直接実行できます。

```bash
# 例: 数学記号と Python の対応サンプル
uv run python 00_notation/examples/notation_to_python.py

# 例: 線形回帰を NumPy で学習
uv run python 06_ml_math_bridge/examples/loss_and_gradient.py

# 例: 同じ線形回帰を JAX で学習
uv run python 06_ml_math_bridge/examples/loss_and_gradient_jax.py
```

## ステップ 5: AI CLI で動的に学ぶ

### Claude Code

```bash
# インストール (初回のみ、Node.js 18+ が必要)
npm install -g @anthropic-ai/claude-code

# プロジェクトルートで起動
claude

# プロジェクト専用コマンドが使える
# > /project:teach-baby ベクトルってなに？
# > /project:column フーリエ変換
# > /project:visualize sin と cos の関係
# > /project:explain-symbol ∀
```

### Gemini CLI

```bash
# インストール (例: npm 経由)
# 公式インストール手順は: https://geminicli.com/docs/

cd path/to/leaning-math
gemini

# 同じく / 形式のコマンドが使える
```

### Codex CLI

```bash
# OpenAI Codex CLI のインストール手順に従う
cd path/to/leaning-math
codex
```

3ツールすべてが、このリポジトリの `AGENTS.md` を共通指示書として読みます。

## トラブルシューティング

### Windows で `uv` コマンドが見つからない

PowerShell を一度閉じて再度開いてみてください。インストール時に PATH が追加されますが、再起動するまで反映されない場合があります。

### `uv sync` で `jax` が失敗する

JAX は CPU 版をデフォルトで入れます。GPU 版が欲しい場合は別途インストール手順が必要です (今回は不要)。

### Jupyter Lab で日本語が文字化けする

matplotlib のフォントが原因。以下を notebooks の最初のセルに追加:

```python
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'  # または 'Hiragino Sans' (Mac), 'Meiryo' (Win)
```

### ipywidgets のスライダーが表示されない

セルを再実行してみてください。それでもダメなら:

```bash
uv run jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

### Python のバージョンが古いと言われる

uv が Python 3.10+ を自動取得するはずですが、明示的に指定:

```bash
uv python install 3.11
uv sync
```

## アンインストール

依存環境は `.venv/` フォルダ内なので、削除すれば完全に消えます:

```bash
rm -rf .venv  # Mac/Linux
Remove-Item -Recurse -Force .venv  # Windows PowerShell
```

uv 本体もアンインストール可能ですが、軽量なので残しておくと他のプロジェクトで使えて便利です。

## 次にすること

1. `start_here/README.md` を読む (このリポジトリの入口)
2. `docs/learning_path.md` を読む (学習ロードマップ)
3. `claude` または `gemini` で AI を起動して質問を始める
