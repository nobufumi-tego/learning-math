# コラム 04 (チャレンジ): Git とは何か — 一人でも、チームでも、強すぎる味方

> *ZIPダウンロードでも本リポジトリは使えます。でも、Git を覚えると見える景色が変わります。*

```
       ／￣￣＼
      |  ・ω・  |   ぼくがチャレンジ枠で紹介したい技術、それが Git だよ。
      |   ⌒    |   一度わかると、人生のあらゆる「変化」を扱う力が手に入る。
       ＼____／
```

> 📚 これは**チャレンジ章**です。本リポジトリの学習に Git は**必須ではありません** (ZIP で十分動きます)。
> でも、「**一度これを覚えたら世界が広がるよ**」というツールなので、興味があったら読み進めてください。

---

## 1. そもそも Git って何?

**Git (ギット)** は、**「ファイルの変更履歴を全部記録してくれるタイムマシン」** です。

正式名称は **「分散バージョン管理システム」** (Distributed Version Control System, DVCS)。
言葉は難しいけど、やってることはシンプル:

- ファイルを編集する
- 区切りごとに「**スナップショット**」を保存
- いつでも「過去のあの時点」に戻れる
- 別ブランチで実験して、ダメなら捨てられる
- チームメンバーと変更を**マージ**できる

### Git の生みの親: Linus Torvalds (Linux の人)

2005年、**Linux カーネル**の開発者だった Linus Torvalds (リーナス・トーバルズ) は、当時使っていた商用バージョン管理システム (BitKeeper) のライセンス問題に怒って、

**「もういい、自分で作る!」**

と週末で Git の原型を書き上げました。**約 2 週間で実用レベル**に到達。
Linux カーネルを管理するためのツールとして始まりましたが、すぐに世界中のソフトウェア開発で使われるようになりました。

> 余談: Linus は「**バージョン管理の天才**」とも言われます。Linux と Git、彼が作った 2 つのものが、現代社会のソフトウェアインフラを根底から支えています。

### Git ≠ GitHub (これ重要!)

初心者がよく混同する 2 つ:

| 名前 | 何か |
|---|---|
| **Git** | 自分の PC で動く、変更履歴管理のソフト |
| **GitHub** | Git のリポジトリを「クラウドで共有・管理」するウェブサービス (Microsoft 傘下) |

- Git だけでも使える (オフラインで完結)
- GitHub に push すれば、世界中の人と共有できる
- 似たサービス: GitLab、Bitbucket、Codeberg

つまり Git は「ツール」、GitHub は「Git で作ったものを置く場所」です。

---

## 2. Git の何が嬉しいのか — 7 つのメリット

### 🥇 (1) 履歴が**完全に**残る (Undo が無限)

普段ファイルを編集していて、「**昨日の状態に戻したい!**」と思うこと、ありますよね。

Word の Undo は数十回で消える。Time Machine も粒度が荒い。
Git は **「あなたが commit するたびにスナップショット」** が永遠に残ります。3年前の状態にも、1ヶ月前の状態にも、戻せる。

```bash
git log              # 履歴を見る
git checkout <ハッシュ>  # 過去の任意の時点に戻る
```

### 🥈 (2) **分岐 (ブランチ)** で気軽に実験できる

「**この機能、入れたいけど壊しそうで怖い**」というとき:

```bash
git branch experiment    # 新ブランチを作る
git checkout experiment  # そのブランチに切り替え
# ガンガン実験、壊しても OK
git checkout main        # 元のブランチに戻る → 実験は隔離されたまま
```

ダメなら `git branch -D experiment` でブランチごと捨てられる。
**現実世界でも「もし○○だったら」のシミュレーションができる感じ**。

### 🥉 (3) **チーム作業**で衝突を解決する道具

複数人で同じファイルを編集すると、衝突します。
Git は「**誰がどこをいつ変えたか**」を全部追えるので、衝突しても**自動マージ**してくれることが多く、ダメな部分だけ手動で解決すればいい。

メールで Excel を行き来させる「○○_最終_v2_最終_本当.xlsx」現象とは無縁。

### (4) **個人開発**でも超有用

「自分一人なのに git?」と思うかもしれませんが、一人こそ Git が効きます:

- 朝の自分が書いたコード、夜の自分が壊した → **昨日のコミットに戻る**
- 自宅 PC と会社 PC で同じプロジェクトを進めたい → **GitHub 経由で同期**
- 突然 PC が壊れた → **GitHub にあれば全部復活**
- 「あれ、なんでこの行こう書いたんだっけ?」→ **`git blame` で当時の自分の commit を発見**

### (5) AI 時代に**特に**重要

ChatGPT・Claude・Cursor などが書いたコードを、人間が読まずに使うのは危険。
Git があれば:

- AI が変更した「**前後の差分**」を見て確認できる
- 「**この変更を取り消したい**」が安全にできる
- 「**前回うまく動いてた状態**」に瞬時に戻れる

**AI ファースト時代** には、Git なしでコードを書くのは恐ろしい。

### (6) **ポートフォリオ** になる

GitHub にあなたが書いたコードを置いておくと、**転職活動の名刺**になります。
プロのエンジニアは、職務経歴書より GitHub の方が重視される世界。

### (7) **オープンソースに参加**できる

Linux も Python も VS Code も Blender も、世界中の人が GitHub で協同開発しています。
**「あの有名ソフトに自分の名前が刻まれる**」という体験ができます (誤字修正の小さな PR でも OK)。

---

## 3. 超やさしい入門編

### Step 0: Git をインストール

| OS | インストール方法 |
|---|---|
| **Mac** | `brew install git` (Homebrew) または公式インストーラ |
| **Linux** | `sudo apt install git` (Ubuntu) / `sudo dnf install git` (Fedora) |
| **Windows** | [Git for Windows](https://git-scm.com/download/win) からダウンロード |

確認:
```bash
git --version
# git version 2.x.x が出ればOK
```

### Step 1: 自分の名前を登録 (初回のみ)

Git は**誰がコミットしたか**を記録するので、最初に登録:

```bash
git config --global user.name "あなたの名前"
git config --global user.email "your-email@example.com"
```

### Step 2: 最初の3コマンド

新しいフォルダで、Git を始めてみる:

```bash
mkdir my-first-git
cd my-first-git
git init                                  # ① Git を始める
echo "hello git" > hello.txt
git add hello.txt                         # ② 変更を選ぶ (ステージング)
git commit -m "最初のコミット: hello.txt 追加"  # ③ スナップショットを保存
```

`git log` を打つと、**人類が初めて自分の変更を git で記録した瞬間**が見られます。

### Step 3: 履歴を見る・戻る

```bash
git log              # 履歴一覧
git log --oneline    # 簡潔表示
git diff             # 直前 commit との差分
git status           # 今の状態
```

過去に戻る (危険なのでまず練習用):
```bash
git checkout <コミットハッシュ>   # 過去の状態に切り替え
git checkout main                # 戻る
```

### Step 4: GitHub に置いてみる

1. [GitHub](https://github.com) でアカウント作成 (無料)
2. 新規リポジトリを作成 (Web 画面の **+ → New repository**)
3. ローカルから push:

```bash
git remote add origin https://github.com/<あなたのユーザー名>/<リポジトリ名>.git
git branch -M main
git push -u origin main
```

これで **GitHub 上にあなたのコードが公開** されます。

### Step 5: 他の人のリポジトリを取得

このリポジトリの場合:
```bash
git clone https://github.com/nobufumi-tego/learning-math.git
cd learning-math
git pull            # 後日、最新版を取り込む
```

---

## 4. 本リポジトリでの実例

このリポジトリも、実は **Git で全変更履歴が記録されています**。

GitHub の上部メニュー **「Commits」** を開くと、全ての commit が見られます:
- https://github.com/nobufumi-tego/learning-math/commits/main

「あ、この章はこの日に追加されたんだ」「このバグはこのコミットで直されたんだ」が一目でわかる。
これが**プロジェクトの "歴史"** であり、Git の真価です。

### 自分でも変更してみたい場合

GitHub では:
1. **Fork** ボタン: このリポジトリを自分のアカウントにコピー
2. ローカルに git clone
3. 自分の好きに変更してコミット
4. **Pull Request** ボタン: 「この変更を本家に取り込んでください」と提案

これが **オープンソースへの貢献** の基本フロー。

---

## 5. もっと知りたいときの「筋のいい」学習リソース

### 🎯 まず最初に読むべき (無料・公式)

- **[Pro Git 書籍 (日本語版)](https://git-scm.com/book/ja/v2)** ⭐ 最もおすすめ
  - Git 公式サイトが配布する**完全無料の書籍**
  - 日本語訳もあり、これ一冊でほぼ全て学べる
  - 寝る前に少しずつ読むのに最適

- **[Git 公式ドキュメント](https://git-scm.com/doc)**
  - リファレンスとして手元に

### 🎮 インタラクティブに学ぶ (実際に手を動かす)

- **[Learn Git Branching](https://learngitbranching.js.org/?locale=ja)** ⭐⭐ 超おすすめ
  - **ブラウザ上で git ブランチを視覚的に操作できる**
  - 日本語対応
  - ゲーム感覚で「ブランチ・マージ・リベース」を体得できる
  - 1〜2時間でブランチ操作の達人になれる

### 📺 動画で学ぶ

- **[GitHub Skills](https://skills.github.com/)**
  - GitHub 公式のインタラクティブ チュートリアル
  - 「PR の出し方」など実践的

- **YouTube 検索: "git tutorial 日本語"**
  - 「KENTA」「とらゼミ」「平岡さん」あたりが評判良い

### 📚 日本語の名サイト

- **[サル先生のGit入門 (Backlog)](https://backlog.com/ja/git-tutorial/)**
  - イラストたっぷりで超やさしい
  - 「初めての Git」 がこれで腑に落ちる人多数

- **[GitHub 公式ガイド (日本語)](https://docs.github.com/ja)**
  - GitHub 機能の正確なリファレンス

### 🧠 もう一段深く

- **[Git from the Bottom Up (邦訳: 砂場で学ぶ Git)](https://jwiegley.github.io/git-from-the-bottom-up/)**
  - Git の**内部構造**から理解する硬派な良書
  - 中級〜上級向け

- **[Oh Shit, Git!?!](https://ohshitgit.com/ja)** (URL最後の `ja` で日本語)
  - 「やらかした!」ときの**復旧コマンド集**
  - **トラブった時のお守り**

### 🎓 独学が辛いときの救命

- **ChatGPT / Claude に聞く** ← 実は最強かも
  - 「git で○○したい、どうコマンドを打つ?」と日本語で質問
  - 「このエラーが出た: \[エラー文]」で解決法を聞く
  - **エラー文の英語に怯えず、AI に丸投げで OK**

---

## 6. 「最初の一歩」 のおすすめロードマップ

| Day | やること | リソース |
|---|---|---|
| 1日目 | git をインストール、`git --version` 確認、自分の名前登録 | このコラム + サル先生 |
| 2日目 | 練習用フォルダで `init`/`add`/`commit` を 5回やる | サル先生のGit入門 |
| 3日目 | GitHub アカウント作成、空リポジトリを作って `push` してみる | GitHub 公式ガイド |
| 4日目 | このリポジトリを **fork** してみる、自分のアカウントに複製 | GitHub UI |
| 5日目 | Learn Git Branching を 30分やってブランチに慣れる | learngitbranching.js.org |
| 1週間後 | 自分の何か (メモ、設定ファイル、Python練習) を git 管理してみる | 自分のペースで |

これで**git使える人**の仲間入り。

---

## 7. ここで挫折しないコツ

- ⚠️ **「全部覚えよう」としない**: `init`/`add`/`commit`/`push`/`pull` の 5 つから始める
- ⚠️ **`git rebase` `git cherry-pick` は最初は触らない**: パワフルだが事故りやすい
- ⚠️ **怖いと思ったら ChatGPT に貼って聞く**: 怒られないし、正確に答えてくれる
- ⚠️ **「やらかした!」と思ったら Oh Shit, Git!?! を見る**: ほぼ全パターンの復旧法あり
- ⚠️ **PR (Pull Request) は早めに体験する**: 「読まれる前提でコードを書く」感覚は他で得られない

---

## まとめ

| 観点 | 一言 |
|---|---|
| Git とは | ファイル変更履歴のタイムマシン |
| 何が嬉しい | Undo無限・実験できる・チーム作業・AI時代の安全網 |
| 最初に覚える | `init`, `add`, `commit`, `push`, `pull` |
| 一番おすすめの教材 | Pro Git (無料書籍) + Learn Git Branching |
| 困ったとき | ChatGPT/Claude に聞く + Oh Shit, Git!?! |

Git は最初の数日で「うっ、覚えること多い…」となりますが、**1週間使えば手に馴染み、1ヶ月使えば手放せなくなる** ツールです。

本リポジトリは ZIP でも遊べますが、**git 管理にすると「自分で章を増やしたり、AI と一緒に改造する」体験が桁違いに楽しくなります**。

ぜひチャレンジしてみてください。

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`03_open_source.md`](03_open_source.md) | [章 TOP](../README.md) | [📚 ROOT README](../../../README.md) | 本流に戻る: [`../09_ai_cli_as_smart_pet.md`](../09_ai_cli_as_smart_pet.md) |
