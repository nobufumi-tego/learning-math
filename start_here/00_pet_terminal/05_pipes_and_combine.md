# 05. パイプ `|` — CLI の超能力、「組み合わせる」の魔法

```
       ／￣￣＼
      |  ・ω・  |   今日は、ぼくが一番ワクワクする魔法を見せるよ。
      |   ⌒    |   小さな芸を「つなげて」、すごい技にする方法。
       ＼____／
```

このページで、ターミナルの**真の力**を知ることになります。
ここを越えると、もうマウス操作には戻れません。

## CLI の哲学: 小さい道具をつなぐ

ターミナルの命令 (コマンド) は、ひとつひとつが**シンプルで小さい**です。
- `ls` は「並べる」だけ
- `cat` は「中身を見る」だけ
- `wc` は「数を数える」だけ

「えっ、こんなんで何ができるの？」と思いますよね。
ところがこれを **「パイプ」** という道具でつなぐと、**とんでもないことができる**んです。

これを **UNIX の哲学** と呼びます (詳しくは [`columns/01_unix_philosophy.md`](columns/01_unix_philosophy.md))。

## パイプ `|` とは

**`|`** という縦棒を使って、こう書きます:

```bash
コマンドA | コマンドB
```

意味: 「**A の出力を、そのまま B の入力に渡す**」

ペンタの言葉で言うと:
- A: 「これ、できた!」
- B: 「ありがとう、続きは僕がやるね」

これだけ。けど、これが革命的。

## 例 1: 「Python ファイルだけ表示する」

普通 (シェルだけで):
```bash
ls
```
返事:
```
README.md  data.csv  hello.py  notes.txt  script.py
```

でも、`.py` ファイルだけ見たい。
そんなとき:

**Mac / Linux:**
```bash
ls | grep .py
```

**Windows (PowerShell):**
```powershell
ls | Select-String '\.py$'
# または短縮 alias で:
ls *.py
```

返事:
```
hello.py
script.py
```

> 💡 **PowerShell の `Select-String`** は Linux の `grep` 相当。短く `sls` という alias もあります。

何が起きたか:
1. `ls` がファイル一覧を出した
2. `|` がそれを `grep .py` に渡した
3. `grep` が `.py` を含む行だけ表示した

まるで2匹のペットが連携してチームプレーしてるみたい。

## 例 2: 「ファイルが何個あるか数える」

**Mac / Linux:**
```bash
ls | wc -l
```

**Windows (PowerShell):**
```powershell
(ls).Count
# またはパイプで:
ls | Measure-Object | Select-Object -ExpandProperty Count
```

返事:
```
5
```

- `ls` が一覧を出す
- `wc -l` (Linux) / `Measure-Object` (PowerShell) が**行数**を数える
- 結果: 5 個のファイルがある

これ、Finder/エクスプローラでファイル数を数えるより**圧倒的に速い**。
1万ファイルあっても一瞬。

## 例 3: 連続パイプ — 3段重ね、4段重ねもできる

**Mac / Linux:**
```bash
ls -l | grep .txt | sort | head -3
```

**Windows (PowerShell):**
```powershell
ls | Where-Object Name -like '*.txt' | Sort-Object Name | Select-Object -First 3
```

意味:
1. `ls -l` で詳しい一覧を出す
2. `.txt` だけに絞る
3. アルファベット順にソート
4. 最初の3個だけ表示

たった一行で、 「**.txt ファイルを名前順に並べて、上位3つを取り出す**」。
GUI でやろうとしたら何分かかるか…。

## リダイレクト `>` `>>` — 結果をファイルに保存

パイプと一緒に覚えておきたいのが**リダイレクト**:

**Mac / Linux:**
```bash
ls > file_list.txt           # 一覧をファイルに保存 (上書き)
ls >> file_list.txt          # 追記
```

**Windows (PowerShell):**
```powershell
ls | Out-File file_list.txt -Encoding utf8           # 上書き
ls | Out-File file_list.txt -Encoding utf8 -Append    # 追記
# 短く:
ls > file_list.txt           # 動くが、文字コードに注意
```

組み合わせると:

**Mac / Linux:**
```bash
ls | grep .py > python_files.txt
```

**Windows (PowerShell):**
```powershell
ls *.py | Out-File python_files.txt -Encoding utf8
```

「Python ファイルの一覧を、`python_files.txt` に保存」。

## よく使うパイプ仲間たち

### Mac / Linux ↔ Windows PowerShell 対応表

| やりたいこと | Mac / Linux | Windows PowerShell |
|---|---|---|
| 文字列で抽出 | `grep <文字列>` | `Select-String <文字列>` (alias `sls`) |
| 並び替え | `sort` | `Sort-Object` (alias `sort`) |
| 重複削除 | `uniq` | `Get-Unique` (alias `gu`) または `Sort-Object -Unique` |
| 行数を数える | `wc -l` | `Measure-Object -Line` |
| 先頭 N 行 | `head -n N` | `Select-Object -First N` |
| 末尾 N 行 | `tail -n N` | `Select-Object -Last N` |
| 列を抜き出す・計算 | `awk '{...}'` | `ForEach-Object { ... }` |
| 文字列を置換 | `sed 's/A/B/'` | `-replace 'A','B'` (演算子) |
| N 列目を取り出す | `cut -f N` | `% { ($_ -split "`t")[N] }` |
| 文字を置換 | `tr 'a' 'b'` | `-replace 'a','b'` |
| 結果を引数として次へ | `xargs` | `% { command $_ }` (パイプ + ForEach) |

> 💡 **PowerShell の独特なパラダイム**: PowerShell は **テキストの行ではなく "オブジェクト" がパイプを流れる** ため、Linux のようなテキスト処理コマンドとは思想が違います。最初は戸惑いますが、`Get-Member` で「今パイプを流れているのは何か」を確認できます。
>
> 「Linux 風が完全に良い」場合は、Windows でも **Git Bash** を使えば `grep`/`awk`/`sed` などがそのまま動きます ([`columns/04_git_challenge.md`](columns/04_git_challenge.md))。

## 実用例: 仕事で使えるワンライナー

### 例 A: 自分が今日コミットした件数

**Mac / Linux:**
```bash
git log --author=$(git config user.name) --since=midnight | grep "^commit" | wc -l
```

**Windows (PowerShell):**
```powershell
(git log --author=(git config user.name) --since=midnight | Select-String '^commit').Count
```

「自分が今日 commit した件数」を一瞬で。

### 例 B: フォルダで一番大きいファイル TOP 5

**Mac / Linux:**
```bash
ls -lhS | head -6
```

**Windows (PowerShell):**
```powershell
ls | Sort-Object Length -Descending | Select-Object -First 5
```

### 例 C: ログから "ERROR" を含む行だけ集計

**Mac / Linux:**
```bash
cat application.log | grep ERROR | wc -l
```

**Windows (PowerShell):**
```powershell
(Get-Content application.log | Select-String ERROR).Count
```

「**ログにエラーが何回出てるか**」が即座に分かる。
DevOps エンジニアの日常です。

### 例 D: ある単語がコードに何回出てるか

**Mac / Linux:**
```bash
grep -r "TODO" .
```

**Windows (PowerShell):**
```powershell
Get-ChildItem -Recurse -File | Select-String "TODO"
```

「カレントフォルダ以下のすべてのファイルから "TODO" を探せ」。
コードレビュー前のセルフチェックに便利。

### 例 E: 100個の写真ファイル名を CSV に整理

**Mac / Linux:**
```bash
ls *.jpg | awk '{print NR","$0}' > photos.csv
```

**Windows (PowerShell):**
```powershell
$i = 0
ls *.jpg | ForEach-Object { $i++; "$i,$($_.Name)" } | Out-File photos.csv -Encoding utf8
```

これだけで CSV ができあがる。

## 「組み合わせる」感覚

パイプの本質は、**人間の発想と道具の組み合わせを限界まで高めること**。

GUI ソフトは「**作った人が想定したこと**」しかできません。
でもパイプを使えば、**あなたの発想次第で無限の道具**が作れる。

たとえばこういうこと:

> 「先週 Slack でチームに送った日報の中で、'バグ' という単語が何回出てきたか」
> 「自分のフォルダで、1MB を超えるファイルだけリストアップ」
> 「3つのCSVから、特定の列だけ抜き出して合体」

GUI ならそれぞれ専用ソフトが必要。CLI なら**ワンライナー** (1行) で済みます。

## 「Unix の哲学」を一行で

> **小さく、ひとつのことをうまくやる道具を、組み合わせて大きな仕事をする**

これが、1970年代に AT&T ベル研究所で生まれた **Unix の哲学**。
50年経った今も、Linux・macOS・Android・iOS の根っこには、この思想が生きています。

そして、**生成AIへのプロンプト**も、実はこの考え方で作るとうまくいきます:
「**まずコレをやって、次にコレをやって、最後にコレ**」と段階的に伝える。
AI 時代の人類は、Unix の哲学を**自然に身につけている**人ほど強い、と言われます。

## まとめ

- `|` (パイプ) = 「**前の出力を次の入力にバトンタッチ**」
- `>` (リダイレクト) = 「**結果をファイルに書き込む**」
- 小さな命令を組み合わせるのが **Unix の哲学**
- GUI ソフトでは不可能な作業が、ワンライナーで実現する
- これが**プロのエンジニアの "瞬殺力" の正体**

次は、なぜ CLI が今日の仕事・趣味でこれほど効くのかを、具体例で見ていきます。

→ [`06_why_cli_in_modern_work.md`](06_why_cli_in_modern_work.md)

---

## 🔍 ググってみよう

- **Unix philosophy** — Doug McIlroy の有名な言葉「Do one thing and do it well」
- **awk** — 1977年生まれ、玄人がよく使う1行プログラミング言語
- **sed** — Stream EDitor、文字列置換の達人
- **xargs** — 「ファイル名を引数に変換する」便利屋
- **grep** — 1973年から使われている、文字列検索の王様
- **regex (正規表現)** — grep / sed と組み合わせて使う、パターンマッチ言語
- **シェルワンライナー** — 1行で巨大な仕事をするテクニック集
- **fzf** — 対話的に検索できる、モダンなツール

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`04_files_and_folders.md`](04_files_and_folders.md) | [章 TOP](README.md) | [📚 ROOT README](../../README.md) | [`06_why_cli_in_modern_work.md`](06_why_cli_in_modern_work.md) |
