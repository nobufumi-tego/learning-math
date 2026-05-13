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
uv run jupyter lab
```

ブラウザが自動で開き、Jupyter Lab の画面が表示されます。

左のファイルツリーから `start_here/notebooks/01_pythagoras.ipynb` を開いて、上から順にセル実行 (Shift+Enter) してみてください。

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
