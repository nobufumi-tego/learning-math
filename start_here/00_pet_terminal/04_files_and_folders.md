# 04. ファイルとフォルダを触る — 作る・読む・コピー・消す

```
       ／￣￣＼
      |  ・ω・  |   今日はぼくのおもちゃ箱（ファイル）を整理してみよう。
      |   ⌒    |   慎重にね。「rm」は要注意の命令だよ。
       ＼____／
```

このページで覚える命令:

| 命令 | 意味 |
|---|---|
| `mkdir` | フォルダを**作る** |
| `touch` | 空のファイルを**作る** |
| `cat` | ファイルの中身を**見る** |
| `cp` | **コピー**する |
| `mv` | **動かす / 名前を変える** |
| `rm` | **消す** ← ⚠️ 要注意 |

## まず、安全な遊び場を作る

人のフォルダで遊ぶと、大事なファイルを壊すかも。
まずは、**ペンタ専用の砂場**を作りましょう。

**Mac / Linux:**
```bash
cd ~                      # ホームに戻る
mkdir penta_sandbox       # 「penta_sandbox」フォルダを作る
cd penta_sandbox          # 中に入る
pwd                       # 確認: ~/penta_sandbox にいるはず
```

**Windows (PowerShell):**
```powershell
cd ~                      # ホームに戻る
mkdir penta_sandbox       # alias で同じ命令
cd penta_sandbox
pwd                       # 確認
```

`mkdir` は **MaKe DIRectory** の略。「ディレクトリを作れ」。
**Windows でも mkdir はそのまま使えます** (`New-Item -ItemType Directory` の alias)。

これで、何をやっても他に影響しない**安全な遊び場**ができました。

## ファイルを作る: `touch`

**Mac / Linux:**
```bash
touch hello.txt
ls
```

**Windows (PowerShell):**
```powershell
New-Item hello.txt        # PowerShell には touch が無い
# または、内容を空のまま作りたいだけなら:
"" | Out-File hello.txt
ls
```

返事:
```
hello.txt
```

`touch` は本来「**ファイルの最終更新日時をいじる**」命令ですが、ファイルが存在しないときは**空っぽのファイルを作ってくれる**ので、よく「新規ファイル作成」に使われます。
PowerShell には標準で `touch` がないので、`New-Item` を使います。

中身を確認:

```bash
cat hello.txt             # Mac/Linux/PowerShell すべてOK (PowerShell では Get-Content の alias)
```

何も表示されない。空っぽだから当たり前。

## ファイルに中身を書く: `echo` と `>`

ターミナルからファイルに書き込む、一番簡単な方法:

**Mac / Linux:**
```bash
echo "こんにちは、ペンタ！" > hello.txt
```

**Windows (PowerShell):**
```powershell
"こんにちは、ペンタ！" | Out-File hello.txt -Encoding utf8
# または短く (ただし文字コードが UTF-16 になる場合があるので注意):
echo "こんにちは、ペンタ！" > hello.txt
```

`>` は **リダイレクト** という記号。
本来は画面に表示する内容を、**ファイルに保存**してくれる魔法です。

> ⚠️ **PowerShell の文字コード罠**: PowerShell の `>` はデフォルトで UTF-16 (UTF-8 BOM ありの場合も) で書き出すことがあります。日本語を扱うなら `Out-File ... -Encoding utf8` を推奨。

中身を確認:
```bash
cat hello.txt    # Mac/Linux/PowerShell すべてOK
```

返事:
```
こんにちは、ペンタ！
```

書けた!

### `>>` で追記

**Mac / Linux:**
```bash
echo "今日はいい天気だね" >> hello.txt
cat hello.txt
```

**Windows (PowerShell):**
```powershell
"今日はいい天気だね" | Out-File hello.txt -Encoding utf8 -Append
cat hello.txt
```

返事:
```
こんにちは、ペンタ！
今日はいい天気だね
```

`>` は**上書き**、`>>` は**追記** (PowerShell では `-Append` フラグ)。
これを間違えると、せっかく書いた内容が消えるので要注意。

## ファイルの中身を見る: `cat`

```bash
cat hello.txt
```

`cat` は **conCATenate** の略 (連結する、の意味)。
本来は複数ファイルを連結する命令ですが、1つだけ指定すると単に中身を表示してくれます。

長いファイルなら:

**Mac / Linux:**
```bash
less hello.txt          # ページ送りで見る (q で終了)
head hello.txt           # 先頭10行
tail hello.txt           # 末尾10行
wc -l hello.txt          # 行数を数える
```

**Windows (PowerShell):**
```powershell
cat hello.txt | more                          # ページ送り
Get-Content hello.txt -Head 10                # 先頭10行
Get-Content hello.txt -Tail 10                # 末尾10行
(Get-Content hello.txt).Count                 # 行数を数える
```

## コピーする: `cp`

**Mac / Linux:**
```bash
cp hello.txt hello_backup.txt   # コピー
ls                               # 確認
```

**Windows (PowerShell):**
```powershell
cp hello.txt hello_backup.txt    # alias でそのまま動く
# または:
Copy-Item hello.txt hello_backup.txt
ls
```

返事:
```
hello.txt  hello_backup.txt
```

`cp` は **CoPy** の略。「**この子を、こっちにも作って**」。

フォルダごとコピーするには `-r` (recursive、再帰的に):

**Mac / Linux:**
```bash
mkdir new_folder
cp -r penta_sandbox new_folder/
```

**Windows (PowerShell):**
```powershell
mkdir new_folder
cp -Recurse penta_sandbox new_folder\
# または:
Copy-Item -Recurse penta_sandbox new_folder\
```

## 動かす・名前を変える: `mv`

**Mac / Linux:**
```bash
mv hello_backup.txt greeting.txt   # 名前変更
ls
```

**Windows (PowerShell):**
```powershell
mv hello_backup.txt greeting.txt   # alias でそのまま動く
# または:
Move-Item hello_backup.txt greeting.txt
ls
```

返事:
```
hello.txt  greeting.txt
```

`mv` は **MoVe** の略。**移動** と **名前変更** の両方をやってくれます。
(プログラマー文化的に、「動かして名前も変えれば同じことだろ」というロジック)

別のフォルダに動かす:

**Mac / Linux:**
```bash
mkdir archive
mv greeting.txt archive/
ls archive/
```

**Windows (PowerShell):**
```powershell
mkdir archive
mv greeting.txt archive\
ls archive\
```

返事:
```
greeting.txt
```

## 消す: `rm` ⚠️

**Mac / Linux:**
```bash
rm hello.txt
ls
```

**Windows (PowerShell):**
```powershell
rm hello.txt              # alias で同じ
# または:
Remove-Item hello.txt
del hello.txt             # cmd.exe 由来の alias もOK
ls
```

`rm` は **ReMove** の略。**消す**。

⚠️ **超重要な注意**: ターミナルでの `rm` には、**「ごみ箱」がありません**。
Windows や Mac の「ごみ箱に入れる」とは違って、**完全削除** されます。
復元できません。一瞬で。永遠に。

### ペンタの忠告

```
       ／￣￣＼
      |  ；ω；  |   rm は本当に怖い命令。
      |   ⌒    |   特に「rm -rf /」は絶対に打たないで！
       ＼____／
```

`rm -rf /` は「**ルート (家全体) を強制的に再帰削除**」という、**OSを破壊する命令**です。
教科書にも「**絶対に打つな**」と書かれているくらいヤバい。

世の中には、新人エンジニアが間違って `rm -rf /` を打って、会社のサーバーを丸ごと消した実話があります (本気で会社が傾く)。

### `rm` を安全に使うコツ

**Mac / Linux:**
```bash
rm -i hello.txt    # -i = interactive、削除前に確認してくれる
```

**Windows (PowerShell):**
```powershell
Remove-Item hello.txt -Confirm   # 確認プロンプトつき
```

慣れるまでは `-i` (Linux) や `-Confirm` (PowerShell) を付けるか、ごみ箱コマンド (Mac/Linux: `trash` 要インストール) を使うのが良いです。

## フォルダを消す: `rmdir` と `rm -r`

空のフォルダなら:

**Mac / Linux:**
```bash
rmdir empty_folder
```

**Windows (PowerShell):**
```powershell
rmdir empty_folder    # alias で動く
# または:
Remove-Item empty_folder
```

中身があるフォルダごと削除 (危険):

**Mac / Linux:**
```bash
rm -r folder_name
```

**Windows (PowerShell):**
```powershell
Remove-Item -Recurse folder_name
# または短く:
rm -Recurse folder_name
```

## 練習: ペンタの整理整頓

砂場で、こんな練習をしてみましょう:

```bash
cd ~/penta_sandbox

# (1) 「practice」フォルダを作る
mkdir practice
cd practice

# (2) 3つのファイルを作る
touch apple.txt banana.txt cherry.txt
ls

# (3) それぞれに中身を書く
echo "りんごは赤い" > apple.txt
echo "バナナは黄色い" > banana.txt
echo "さくらんぼは赤い" > cherry.txt

# (4) 全部表示
cat apple.txt
cat banana.txt
cat cherry.txt

# (5) フォルダを2つ作る
mkdir red_fruits yellow_fruits

# (6) 仕分け
mv apple.txt red_fruits/
mv cherry.txt red_fruits/
mv banana.txt yellow_fruits/

# (7) 確認
ls red_fruits
ls yellow_fruits

# (8) 後片付け (注意して)
cd ~/penta_sandbox
rm -ri practice    # -ri なら確認してから消してくれる
```

おめでとう、これで**ファイル操作の基本**は完璧です。

## まとめ

### 命令と危険度

| 命令 | 意味 | 危険度 |
|---|---|---|
| `mkdir` | フォルダ作成 | 🟢 安全 |
| `touch` | 空ファイル作成 | 🟢 安全 |
| `cat` | 中身を見る | 🟢 安全 |
| `cp` | コピー | 🟡 上書きに注意 |
| `mv` | 移動・改名 | 🟡 上書きに注意 |
| `rm` | 削除 | 🔴 復元不可、要注意 |
| `>` | リダイレクト | 🟡 上書きに注意 |
| `>>` | 追記 | 🟢 安全 |

### Mac/Linux ↔ Windows PowerShell 対応表 (チートシート)

| やりたいこと | Mac / Linux | Windows PowerShell |
|---|---|---|
| フォルダ作成 | `mkdir foo` | `mkdir foo` (alias OK) |
| 空ファイル作成 | `touch foo.txt` | `New-Item foo.txt` |
| ファイル中身を見る | `cat foo.txt` | `cat foo.txt` (alias OK) |
| コピー | `cp a b` | `cp a b` (alias OK) |
| 移動・改名 | `mv a b` | `mv a b` (alias OK) |
| 削除 | `rm foo` | `rm foo` (alias OK) |
| フォルダごと削除 | `rm -r foo` | `rm -Recurse foo` |
| 中身を書き出し | `echo "X" > foo` | `"X" \| Out-File foo -Encoding utf8` |
| 末尾追記 | `echo "X" >> foo` | `"X" \| Out-File foo -Encoding utf8 -Append` |
| 先頭10行 | `head foo` | `Get-Content foo -Head 10` |
| 末尾10行 | `tail foo` | `Get-Content foo -Tail 10` |
| 行数 | `wc -l foo` | `(Get-Content foo).Count` |

> 💡 **PowerShell では Linux 由来の alias が大量に効く**ため、`mkdir` `cp` `mv` `rm` `cat` `ls` `cd` `pwd` などはコピペでだいたい動きます。
> 違いが大きい所だけ右側を覚えれば OK。

次のページでは、CLI の最大の魔法 **「パイプ `|`」** を学びます。
小さな命令を組み合わせて、**巨大な仕事**ができるようになります。

→ [`05_pipes_and_combine.md`](05_pipes_and_combine.md)

---

## 🔍 ググってみよう

- **rm -rf /** — 絶対に打ってはいけない命令、伝説のやらかし話を読む
- **trash CLI** — 安全な「ごみ箱付き rm」のコマンド
- **find コマンド** — ファイルを検索する
- **wildcard (\*, ?)** — `rm *.txt` で全 txt ファイル削除など
- **chmod, chown** — ファイルの権限を変える
- **シンボリックリンク (ln -s)** — ショートカット
- **dotfile (隠しファイル)** — `.gitignore` `.bashrc` など `.` で始まるファイル
- **`tree` コマンド** — フォルダ構造をきれいに表示

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`03_first_commands.md`](03_first_commands.md) | [章 TOP](README.md) | [📚 ROOT README](../../README.md) | [`05_pipes_and_combine.md`](05_pipes_and_combine.md) |
