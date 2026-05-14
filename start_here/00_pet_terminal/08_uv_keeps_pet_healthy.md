# 08. uv はペンタの世話係 — Python のバージョンも依存関係も全部おまかせ

```
       ／￣￣＼
      |  ・ω・  |   ぼくのご飯やお薬の管理、誰がしてくれるの？
      |   ⌒    |   そう、それが「uv」！
       ＼____／
```

## なぜ Python のお世話が必要なのか

Python って便利だけど、ちょっと厄介な性質があります:

### 厄介 1: バージョンがいろいろある
- Python 2 (2000年〜2020年、もう廃止)
- Python 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 ...

ライブラリによって「**Python 3.10 以上が必要**」「**3.9 でしか動かない**」など、相性問題があります。
**犬種ごとに合う餌が違う**、みたいな話。

### 厄介 2: ライブラリ同士の相性
NumPy、JAX、TensorFlow など、ライブラリ同士でも:
- 「JAX 0.4 は NumPy 1.26 以上を要求」
- 「TensorFlow 2.15 は Python 3.11 まで対応」

など、**互換性のジグソーパズル**があります。
人間がやると、すぐに地獄。

### 厄介 3: プロジェクトごとに環境を分けたい
- プロジェクト A は Python 3.10 + 古い NumPy
- プロジェクト B は Python 3.13 + 最新 JAX

これを「**1台のPCで両方使えるようにしたい**」となると、**仮想環境**が必要。

## uv はこれら全部を解決する救世主

**uv** は、2024年に登場した、Python 環境マネージャ。
**Astral** という会社 (Rust で高速ツールを作る人たち) が作りました。

uv のすごいところ:

| 機能 | 効果 |
|---|---|
| Python 本体の管理 | 必要なバージョンを自動でダウンロード |
| 仮想環境の作成 | プロジェクトごとに別環境 |
| ライブラリのインストール | 依存関係を自動解決 |
| 速度 | 従来の `pip` より **10〜100倍** 速い (Rust 製) |
| ロックファイル | 完全な再現性 |

つまり「**Python の世話、ぜんぶやっておいたよ**」と言ってくれる、ペンタの世話係です。

## uv のインストール

(すでに `docs/setup.md` にも書いてありますが、ここにも置いておきます)

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

数字が出てくればOK。

## uv の3つの基本コマンド

このリポジトリで使うのは、ほぼ次の3つだけです:

### 1. `uv sync` — ペンタの環境を整える

```bash
uv sync
```

何が起きるか:
1. プロジェクトが要求する Python のバージョンを自動でインストール
2. `pyproject.toml` に書かれた依存ライブラリを全部インストール
3. `.venv/` フォルダに**仮想環境**を作る

これで、誰の PC でも**全く同じ環境**が再現できます。
**「私の環境では動いたのに、他の人の環境では動かない」** がほぼ無くなる。

### 2. `uv run <command>` — 整えた環境で何かを動かす

```bash
uv run python hello.py            # Python ファイル実行
uv run lab.py                     # Jupyter Lab 起動 (リポジトリ専用設定込み)
uv run jupyter lab                # Jupyter Lab 起動 (素のまま、個人設定で)
uv run pytest                     # テスト実行
```

`uv run` を頭につけると、自動で「**さっき整えた環境**」を使ってくれます。
**毎回 `source .venv/bin/activate` のような呪文を唱えなくていい**のがありがたい。

> 💡 **`uv run lab.py` と `uv run jupyter lab` の違い**
>
> このリポジトリには [`lab.py`](../../lab.py) というラッパースクリプトがあります。
> これを使うと、`.md` ファイルをダブルクリックしたときに **Markdown Preview モード**(綺麗な見た目)で開いてくれます。
>
> 普通の `uv run jupyter lab` だと、`.md` ファイルが**生のテキスト編集モード**で開いてしまい、初心者には見にくいので、本リポジトリでは **`uv run lab.py` を推奨** しています。

### 3. `uv add <package>` — 新しいライブラリを追加

```bash
uv add pandas
```

これで:
- `pandas` がインストールされる
- `pyproject.toml` に「pandas を依存関係に追加した」と記録される

仲間に「私の環境を再現して」と言われたら、`uv sync` だけで OK。

## なぜ仮想環境が必要なのか

「全部のプロジェクトで同じ Python を使えばいいじゃん」と思いますよね。
でも、それは**衛生問題**です。

たとえば:
- プロジェクト A で `numpy 1.20` を使ってる
- プロジェクト B で `numpy 2.0` を使いたい
- 両方を同じ Python に入れたら… **どっちか壊れる**

仮想環境は、**プロジェクトごとに独立したペンタを飼う**みたいなもの:

```
プロジェクトA/.venv/          ← Python 3.10 + numpy 1.20 + ...
プロジェクトB/.venv/          ← Python 3.13 + numpy 2.0 + ...
プロジェクトC/.venv/          ← Python 3.11 + jax + ...
```

それぞれが**完全に隔離**されているので、お互い影響しない。
壊れたら `.venv/` を消してもう一度 `uv sync` で再生できる。

## このリポジトリでの典型的な使い方

```bash
# 1. リポジトリのフォルダに移動
cd path/to/leaning-math

# 2. 環境セットアップ (初回のみ)
uv sync

# 3. Jupyter Lab 起動
uv run lab.py

# 4. または Python スクリプトを直接実行
uv run python 00_notation/examples/notation_to_python.py

# 5. 新しいライブラリが欲しくなったら
uv add scikit-learn
```

これだけ覚えておけば、もう Python 環境で困りません。

## 他にも環境マネージャはあるけど…

| ツール | 特徴 |
|---|---|
| **pip + venv** | 標準だけど遅い、設定が手動 |
| **conda** | 科学計算でよく使われる、重い |
| **poetry** | 機能豊富、けど少し遅い |
| **pipenv** | 一時期流行った、今は廃れ気味 |
| **uv** | 2024年登場、爆速、機能全部入り 🌟 |

uv はまだ新しいけど、**圧倒的な速度と使い勝手**で、急速に普及中。
このリポジトリでは uv を採用しています。

## トラブル対処

### `uv sync` が失敗する
- インターネット接続を確認
- 出てきたエラーメッセージをそのまま Claude / Gemini にコピペして相談

### `uv: command not found`
- インストール後、ターミナルを一度閉じて開き直す
- それでもダメなら PATH 設定が必要 (検索すれば手順が出る)

### 仮想環境を消してやり直したい
```bash
rm -rf .venv      # Mac/Linux
# Windows PowerShell:
# Remove-Item -Recurse -Force .venv
uv sync           # 作り直し
```

これで完全リセット。気軽にやり直せるのも uv の良さ。

## まとめ

- Python はバージョン・ライブラリ・仮想環境の管理が必要
- **uv** がそれを全部、爆速で、自動でやってくれる
- 3つの基本コマンド: `uv sync`, `uv run <cmd>`, `uv add <pkg>`
- どんな OS でも、誰の PC でも、同じ環境を再現できる
- 困ったら `.venv` を消して `uv sync` で再生

次は最終章 — **AI 時代の CLI** へ。
Claude Code・Gemini CLI・Codex を、**ペンタの賢い兄弟分**として迎え入れましょう。

→ [`09_ai_cli_as_smart_pet.md`](09_ai_cli_as_smart_pet.md)

---

## 🔍 ググってみよう

- **uv** — Astral 製、Rust で書かれた爆速 Python ツール
- **Astral** — uv と ruff を作っている会社
- **Rust** — uv が書かれている、安全で速いシステム言語
- **ruff** — 同じく Astral 製の Python リンター/フォーマッター
- **pyproject.toml** — Python プロジェクトの設定ファイルの新しい標準
- **PEP 621** — `pyproject.toml` の仕様を定めた文書
- **仮想環境 (venv)** — プロジェクトごとに独立した Python 環境
- **依存関係解決** — 互いに矛盾しないライブラリのバージョンを自動で見つける技術
- **ロックファイル** — `uv.lock` 等。完全な再現性のために必須

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`07_python_for_pets.md`](07_python_for_pets.md) | [章 TOP](README.md) | [📚 ROOT README](../../README.md) | [`09_ai_cli_as_smart_pet.md`](09_ai_cli_as_smart_pet.md) |
