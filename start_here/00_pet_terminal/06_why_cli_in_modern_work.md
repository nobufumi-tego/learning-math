# 06. なぜ CLI で仕事と趣味が爆速になるのか

```
       ／￣￣＼
      |  ・ω・  |   今日は「なぜターミナルを使う人は速いか」の話。
      |   ⌒    |   実例ベースで、6つの場面を見てみよう。
       ＼____／
```

ここまでで、ペンタとお散歩したり、ファイルを触ったり、パイプで連携したりできるようになりました。
でも本当の質問はこれ:

**「で、結局これ、自分の仕事や趣味に何の役に立つの？」**

答え: **多すぎて困るくらい役に立ちます**。
具体例を6つ見ていきましょう。

## 場面 1: 写真100枚を一気にリサイズしたい

旅行から帰ってきて、撮った写真100枚を「Instagram用に正方形にしたい」。

### マウスでやると
- 写真アプリで1枚開く
- リサイズメニューを選ぶ
- サイズを入力
- 保存
- 次の写真… × 100回 = **2時間コース**

### ターミナルなら

**Mac / Linux:**
```bash
mkdir resized
for f in *.jpg; do
    magick "$f" -resize 1080x1080^ -gravity center -extent 1080x1080 "resized/$f"
done
```

**Windows (PowerShell):**
```powershell
mkdir resized
Get-ChildItem *.jpg | ForEach-Object {
    magick $_.FullName -resize 1080x1080^ -gravity center -extent 1080x1080 "resized\$($_.Name)"
}
```

(`magick` は ImageMagick という画像加工ツール、要インストール)

**所要時間: 1分**。

書ける書けないより、「**こういうことができる**」と知ってるかどうかが運命を分けます。

## 場面 2: 確定申告の領収書、合計を出したい

毎月の領収書 CSV があって、年間合計を出したい。

### Excel でやると
- 12ファイル開く
- それぞれの合計を出す
- 別シートに貼り付ける
- 全部足す = **30分コース**

### ターミナルなら

**Mac / Linux:**
```bash
cat receipts_*.csv | awk -F',' '{sum+=$3} END {print sum}'
```

**Windows (PowerShell):**
```powershell
Get-ChildItem receipts_*.csv | Get-Content |
    ForEach-Object { ($_ -split ',')[2] -as [decimal] } |
    Measure-Object -Sum | Select-Object -ExpandProperty Sum
```

**3秒**で答えが出ます。
(Linux: `-F','` でカンマ区切り、`$3` で3列目、`sum+=` で合計 / PowerShell: `-split ','` でカンマ区切り、`[2]` で3列目)

## 場面 3: メール100通から、特定の差出人を抽出

`mailbox.txt` に1万行のメールログがあって、「上司からのメールだけ」を抽出。

### GUI のメールソフトでフィルタ作って…
**5分。設定を覚えるのも面倒**。

### ターミナルなら

**Mac / Linux:**
```bash
grep -A 3 "From: boss@company.com" mailbox.txt
```

**Windows (PowerShell):**
```powershell
Select-String "From: boss@company.com" mailbox.txt -Context 0,3
```

**0.1秒**。Linux の `-A 3` と PowerShell の `-Context 0,3` は「マッチ行とその後3行」を意味します。

## 場面 4: 毎朝、最新の経済ニュースを見たい

朝起きたら、好きなニュースサイトの新着10件をターミナルに出したい。

### ブラウザで
- 起動
- ブックマーク開く
- スクロールして見る = **3分**

### ターミナルなら

**Mac / Linux:**
```bash
curl -s https://example.com/feed | grep title | head -10
```

**Windows (PowerShell):**
```powershell
Invoke-WebRequest https://example.com/feed |
    Select-Object -ExpandProperty Content |
    Select-String title |
    Select-Object -First 10
```

**1秒**。
これを **「毎朝6時に自動実行」** する設定 (Linux: `cron` / Windows: `Task Scheduler`) を仕込めば、もう手動で見に行く必要すらない。

これが**自動化** (automation)。
プロのエンジニアは、こういう「自動化マシン」を**自分の影武者**みたいに何十台も動かしています。

## 場面 5: 複数の動画を MP3 に変換したい

YouTubeから保存した動画ファイル群を、音声だけに変換したい。

### 専用ソフトで
- インストール、起動、ファイル選択、変換… × 10ファイル = **15分**

### ターミナルなら

**Mac / Linux:**
```bash
for f in *.mp4; do
    ffmpeg -i "$f" "${f%.mp4}.mp3"
done
```

**Windows (PowerShell):**
```powershell
Get-ChildItem *.mp4 | ForEach-Object {
    ffmpeg -i $_.FullName ($_.BaseName + ".mp3")
}
```

**1分**。`ffmpeg` は世界中で使われる動画変換ツール (要インストール)。

## 場面 6: 文章100本から「typo」を一括検索

文章ファイルが100本あって、間違いやすい単語 `recieve` (正しくは `receive`) を全ファイルから探したい。

### Word で
- 全ファイル開く
- それぞれで検索 × 100 = **1時間**

### ターミナルなら

**Mac / Linux:**
```bash
grep -rn "recieve" .
```

**Windows (PowerShell):**
```powershell
Get-ChildItem -Recurse -File | Select-String "recieve"
```

**1秒**。再帰的にファイルを舐めて該当行を表示。

## なぜこんなに差が出るのか

### 理由 1: コンピュータは「同じことを繰り返す」のが得意
人間は同じ作業を100回やると疲れる。
コンピュータは何百万回でも同じ精度で繰り返せる。
**人間の仕事 = 命令を一行書く**、**コンピュータの仕事 = 実行する**、と分業すると、爆速になります。

### 理由 2: 命令を「保存」できる
GUI でやった操作は記憶に残らないけど、ターミナルで打った命令は **「履歴」** に残ります。
1ヶ月前にうまくいった命令を、また使える。
それを**スクリプト**として保存しておけば、**永久に再利用**できる。

### 理由 3: 「文字」だから AI と相性がいい
ChatGPT / Claude に「写真をリサイズしたいんだけど」と聞くと、すぐにターミナル命令を返してくれます。
GUI 操作は AI に質問しても説明しづらい (動画かスクショが必要)。
**AI 時代の効率化は、ほぼ全部 CLI 経由で起こっています**。

### 理由 4: リモートで使える
**地球の裏側のサーバー** を、自分の机から触れる。
GUI で同じことをすると、**画面転送のラグ**でストレス爆発。
だからクラウド (AWS, Google Cloud, Azure) は基本 CLI で操作します。

## 仕事の例: 職種別 CLI 利用

| 職種 | CLI で何をする |
|---|---|
| **データアナリスト** | CSV 集計、ログ解析、グラフ生成 |
| **エンジニア** | コード管理 (git)、デプロイ、サーバー操作 |
| **動画編集者** | ffmpeg で一括変換 |
| **ライター・編集者** | Markdown を一括処理、grep で typo 検索 |
| **研究者** | 実験データの自動集計、論文の参考文献整理 |
| **会計** | 領収書 CSV の集計、銀行 API でデータ取得 |
| **医療** | 大量の検査データの統計処理 |
| **写真家** | RAW データ一括現像、ファイル名整理 |

つまり、**ほぼあらゆる仕事が CLI で加速できる**。

## 趣味の例

| 趣味 | CLI でできること |
|---|---|
| **ゲーム** | サーバー管理、Mod 開発、自動セーブバックアップ |
| **音楽** | 曲のテンポ解析、自動 BPM 調整、楽譜生成 |
| **料理** | レシピのスケール変換 (4人前 → 2人前) を Python で計算 |
| **小説執筆** | 文字数集計、キャラ登場頻度分析 |
| **筋トレ** | 体重・体脂肪率の推移グラフ自動化 |
| **天体観測** | 月齢・日の出時刻の自動取得 |

## まずは「**コピペで動かしてみる**」

CLI を学ぶ最大のコツは、**完璧に理解してから使う**じゃなくて **使いながら理解する** こと。

ChatGPT や Claude に:

> 「私の Mac で、フォルダ内の写真を全部 1080×1080 にリサイズするコマンド教えて」

と聞けば、教えてくれます。
それを**そのままコピペ**して動かしてみる。
動いたら「**おお、こういう書き方なんだ**」と振り返る。

そう、**CLI は AI と相性が最高**です。
そしてその AI を使うのも、結局 CLI (Claude Code, Gemini CLI, Codex) です。

## まとめ

- CLI は **同じ作業を100倍速くする** ための道具
- マウス操作と違って、**保存・繰り返し・自動化・リモート操作**ができる
- ほぼあらゆる仕事と趣味で活用できる
- AI 時代において、**CLI を使えること = AI の能力を最大限引き出せること**

次は、CLI と組み合わせて使う **「Python」** という言語を、ペンタが覚えます。

→ [`07_python_for_pets.md`](07_python_for_pets.md)

---

## 🔍 ググってみよう

- **シェルスクリプト** — 命令をファイルにまとめて再利用する
- **cron** — Linux の定期実行スケジューラ (毎朝自動実行など)
- **ffmpeg** — 世界で一番使われている動画/音声変換ツール
- **ImageMagick** — 画像変換の定番
- **curl, wget** — Web からデータを取ってくる
- **jq** — JSON データを CLI で処理する神ツール
- **DevOps** — 開発と運用を自動化する文化、CLI が中心
- **GitHub Actions** — クラウドで CLI を自動実行する仕組み
- **Homebrew** (Mac) / **Chocolatey** (Windows) — CLIツールのインストールマネージャ

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`05_pipes_and_combine.md`](05_pipes_and_combine.md) | [章 TOP](README.md) | [📚 ROOT README](../../README.md) | [`07_python_for_pets.md`](07_python_for_pets.md) |
