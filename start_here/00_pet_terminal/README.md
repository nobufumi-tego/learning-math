# 00. ペットと学ぶターミナル基礎 — はじめに

```
      ／￣￣＼
     |  ・ω・  |   こんにちは。ペンギンの「ペンタ」だよ。
     |   ⌒    |   今日からよろしくね。
      ＼____／
```

このリポジトリのほとんどの章では、「ターミナル」と呼ばれる**真っ黒な画面**を使います。
でも、もしあなたがその画面を見て **「うわっ、無理…」** と思ったとしても、大丈夫。

この章では、**ペンギンのペンタ** と一緒に、ターミナルがそもそも何なのか、なぜそれを使うと仕事や趣味が爆速になるのか、を**ゼロから**学びます。

## なぜ「ペット」と学ぶか

ターミナルって、実は**ペットを飼うのに似ている**んです:

- 名前を呼べば応えてくれる (コマンドを入力すると返事してくれる)
- いくつかの「芸 (コマンド)」を覚えさせると、毎日のお仕事をしてくれる
- 仲良くなるほど、できることが増えていく
- 怒鳴っても無駄。**正しい言葉で話しかける**のがコツ

つまり、**ターミナルは怖い機械じゃなくて、賢い相棒** です。
ペンタと一緒に、ゆっくり仲良くなっていきましょう。

## この章のゴール

この章を全部読み終わったら、あなたは次のことができるようになります:

- ✅ ターミナルを開いて、怖がらずに最初の命令を打てる
- ✅ ファイルを作る・移動する・コピーする・読む
- ✅ 「パイプ」「リダイレクト」という CLI の超能力を知っている
- ✅ なぜ CLI が現代の仕事で必須なのか、自分の言葉で説明できる
- ✅ Python と uv の正体を理解している
- ✅ Claude Code などの **AI CLI** を使う準備ができている

## この章の道のり

| ステップ | 内容 | 所要時間 |
|---|---|---|
| [`01_what_is_terminal.md`](01_what_is_terminal.md) | そもそも、真っ黒な画面って何？（歴史も） | 15分 |
| [`02_meet_your_pet.md`](02_meet_your_pet.md) | ペンタ（シェル）に挨拶する | 15分 |
| [`03_first_commands.md`](03_first_commands.md) | 最初の3つのおまじない: `pwd`・`ls`・`cd` | 20分 |
| [`04_files_and_folders.md`](04_files_and_folders.md) | ファイルとフォルダを触る | 30分 |
| [`05_pipes_and_combine.md`](05_pipes_and_combine.md) | パイプ `\|` で芸を組み合わせる | 25分 |
| [`06_why_cli_in_modern_work.md`](06_why_cli_in_modern_work.md) | なぜ CLI で仕事が爆速になるか | 20分 |
| [`07_python_for_pets.md`](07_python_for_pets.md) | ペンタが Python を覚える | 20分 |
| [`08_uv_keeps_pet_healthy.md`](08_uv_keeps_pet_healthy.md) | uv = ペンタの世話係 | 15分 |
| [`09_ai_cli_as_smart_pet.md`](09_ai_cli_as_smart_pet.md) | AI CLI 時代 (Claude / Gemini / Codex) | 20分 |

合計約 3 時間。一気にやらず、**1日 1〜2 章ずつ**進めるのがおすすめです。

## コラム欄（疲れたとき・休憩中に）

`columns/` フォルダの中に、ちょっとした読み物があります:

| ファイル | 話 |
|---|---|
| [`columns/00_history_of_computer.md`](columns/00_history_of_computer.md) | コンピュータの80年史ざっくり |
| [`columns/01_unix_philosophy.md`](columns/01_unix_philosophy.md) | UNIX の哲学 — 小さく作って組み合わせる |
| [`columns/02_keyboard_age.md`](columns/02_keyboard_age.md) | なぜ今もキーボードが王様なのか |
| [`columns/03_open_source.md`](columns/03_open_source.md) | なぜ世界の道具がタダで配られているのか |
| [`columns/04_git_challenge.md`](columns/04_git_challenge.md) | **チャレンジ**: Git 入門 — 一人でも、チームでも強すぎる味方 |

## あなたの OS は何でも大丈夫

- **Windows**: PowerShell や Windows Terminal を使います
- **Mac**: Terminal.app または iTerm2
- **Linux**: GNOME Terminal、Konsole など

このリポジトリのコマンドは、ほぼすべての OS で動くように書かれています。
細かい違いがあれば、その都度ペンタが教えてくれます。

## 「ググってみよう」コーナーについて

このリポジトリでは、章の最後に**「ググってみよう」キーワード**を散りばめます。

> 🔍 **ググってみよう**: テレタイプ, VT100, GNU/Linux, AI Native CLI

こういうキーワードをクリック…じゃなくて Google にコピペして検索すると、世界が広がります。
**自分で調べる楽しさ**を、ここで覚えていってください。

## 始める前のセットアップ

このリポジトリの中身を触り始める前に、もし可能なら次の準備をしておくと、後で楽になります。
（次のページから始めるなら、**まだ何もインストールしなくて大丈夫**です）

- Windows なら **Windows Terminal** をインストール (Microsoft Store から)
- Mac は最初から **Terminal.app** が入っている
- Linux ユーザは…もう仲間です

詳しいセットアップは [`../../docs/setup.md`](../../docs/setup.md) を参照。

---

それでは、ペンタと一緒に最初の一歩を踏み出しましょう。

→ [`01_what_is_terminal.md`](01_what_is_terminal.md) へ

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [start_here 入口](../README.md) | (このページが章 TOP) | [📚 ROOT README](../../README.md) | [`01_what_is_terminal.md`](01_what_is_terminal.md) |
