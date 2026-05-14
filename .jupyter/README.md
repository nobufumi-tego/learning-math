# `.jupyter/` — リポジトリ同梱の JupyterLab 設定

このフォルダは、**clone した人が `uv run lab.py` で起動するだけで、本リポジトリ専用の JupyterLab 設定が自動適用される** ようにするためのものです。

## 何が設定されているか

| ファイル | 効果 |
|---|---|
| `lab/user-settings/@jupyterlab/docmanager-extension/plugin.jupyterlab-settings` | `.md` ファイルをダブルクリックで開いたときに、**Markdown Preview** モードで表示する |

## 仕組み

リポジトリ ルートの [`lab.py`](../lab.py) が、起動時に環境変数 `JUPYTERLAB_SETTINGS_DIR` を**この `.jupyter/lab/user-settings/`** に向けます。
そのため `uv run lab.py` で起動した JupyterLab だけが、この設定を読みます。

通常の `uv run jupyter lab` で起動した場合は、ユーザーの `~/.jupyter/lab/user-settings/` の設定が使われます (本リポジトリの設定は適用されません)。

## 個人用にカスタマイズしたい場合

このフォルダの設定を直接編集すると、リポジトリ全体の挙動が変わります (PR で他の人にも影響)。
**個人だけの設定**を試したい場合は:

1. `~/.jupyter/lab/user-settings/` 配下にユーザー個人の設定を置く (通常起動 `uv run jupyter lab` で適用される)
2. または、本リポジトリの設定をローカルでだけ書き換える (gitignore の `*.local.json` パターンを参考に)

## 設定の書き方

JupyterLab の Settings Editor (Settings → Settings Editor) で確認できる JSON 設定を、対応するファイルにコピーすれば永続化できます。

例: ダークテーマをデフォルトに
```
.jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings
```
の中身:
```json
{
    "theme": "JupyterLab Dark"
}
```

詳しくは [JupyterLab の Settings 公式ドキュメント](https://jupyterlab.readthedocs.io/en/stable/user/directories.html#user-settings-directory) を参照。
