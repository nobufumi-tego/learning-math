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

```bash
cd ~                      # ホームに戻る
mkdir penta_sandbox       # 「penta_sandbox」フォルダを作る
cd penta_sandbox          # 中に入る
pwd                       # 確認: ~/penta_sandbox にいるはず
```

`mkdir` は **MaKe DIRectory** の略。「ディレクトリを作れ」。

これで、何をやっても他に影響しない**安全な遊び場**ができました。

## ファイルを作る: `touch`

```bash
touch hello.txt
ls
```

返事:
```
hello.txt
```

`touch` は本来「**ファイルの最終更新日時をいじる**」命令ですが、ファイルが存在しないときは**空っぽのファイルを作ってくれる**ので、よく「新規ファイル作成」に使われます。

中身を確認:

```bash
cat hello.txt
```

何も表示されない。空っぽだから当たり前。

## ファイルに中身を書く: `echo` と `>`

ターミナルからファイルに書き込む、一番簡単な方法:

```bash
echo "こんにちは、ペンタ！" > hello.txt
```

`>` は **リダイレクト** という記号。
本来は画面に表示する内容を、**ファイルに保存**してくれる魔法です。

中身を確認:
```bash
cat hello.txt
```

返事:
```
こんにちは、ペンタ！
```

書けた!

### `>>` で追記

```bash
echo "今日はいい天気だね" >> hello.txt
cat hello.txt
```

返事:
```
こんにちは、ペンタ！
今日はいい天気だね
```

`>` は**上書き**、`>>` は**追記**。
これを間違えると、せっかく書いた内容が消えるので要注意。

## ファイルの中身を見る: `cat`

```bash
cat hello.txt
```

`cat` は **conCATenate** の略 (連結する、の意味)。
本来は複数ファイルを連結する命令ですが、1つだけ指定すると単に中身を表示してくれます。

長いファイルなら:
```bash
less hello.txt          # ページ送りで見る (q で終了)
head hello.txt           # 先頭10行
tail hello.txt           # 末尾10行
wc -l hello.txt          # 行数を数える
```

## コピーする: `cp`

```bash
cp hello.txt hello_backup.txt   # コピー
ls                               # 確認
```

返事:
```
hello.txt  hello_backup.txt
```

`cp` は **CoPy** の略。「**この子を、こっちにも作って**」。

フォルダごとコピーするには `-r` (recursive、再帰的に):
```bash
mkdir new_folder
cp -r penta_sandbox new_folder/
```

## 動かす・名前を変える: `mv`

```bash
mv hello_backup.txt greeting.txt   # 名前変更
ls
```

返事:
```
hello.txt  greeting.txt
```

`mv` は **MoVe** の略。**移動** と **名前変更** の両方をやってくれます。
(プログラマー文化的に、「動かして名前も変えれば同じことだろ」というロジック)

別のフォルダに動かす:
```bash
mkdir archive
mv greeting.txt archive/
ls archive/
```

返事:
```
greeting.txt
```

## 消す: `rm` ⚠️

```bash
rm hello.txt
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

```bash
rm -i hello.txt    # -i = interactive、削除前に確認してくれる
```

慣れるまでは `-i` を付けるか、ごみ箱コマンド `trash` (要インストール) を使うのが良いです。

## フォルダを消す: `rmdir` と `rm -r`

空のフォルダなら:
```bash
rmdir empty_folder
```

中身があるフォルダごと削除 (危険):
```bash
rm -r folder_name
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
