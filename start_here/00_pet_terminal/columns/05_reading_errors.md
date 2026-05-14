# コラム 05: エラーメッセージは「敵」 じゃなくて「手紙」 — ペンタからの最初の伝言

> *赤い帯を見て固まらないために、ペンタが用意した「エラー読解」 入門。*

```
       ／￣￣＼
      |  ・ω・  |   赤い文字を見ると、固まっちゃうよね。
      |   ⌒    |   でもね、あれは「**エラーだぞ! 助けてくれ!**」っていう、
       ＼____／    Python くんからの手紙なんだ。
                    読み方さえ覚えれば、君の最強の味方になるよ。
```

---

## このコラムについて

**想定読者**: Python を初めて触る人、赤いエラー文を見ると心拍数が上がる人
**ゴール**: エラーを「読み解いて、対処する」 ことができるようになる
**所要時間**: 約 15 分

---

## 目次

- [1. エラーは怒られているわけじゃない](#1-エラーは怒られているわけじゃない)
- [2. トレースバックの読み方 — 「下から上」 が鉄則](#2-トレースバックの読み方--下から上-が鉄則)
- [3. 数学初心者がよく出会うエラー 7 選](#3-数学初心者がよく出会うエラー-7-選)
- [4. エラーが出たときの 3 ステップ対処法](#4-エラーが出たときの-3-ステップ対処法)
- [5. AI に聞くときのコツ](#5-ai-に聞くときのコツ)
- [6. エラーは成長の足跡](#6-エラーは成長の足跡)

---

## 1. エラーは怒られているわけじゃない

```
       ／￣￣＼
      |  ・ω・  |   人間は赤い文字を「叱られた」って感じるみたい。
      |   ⌒    |   でも Python くんは、ぼくたちを叱る能力すらないんだよ。
       ＼____／    あれは「**ぼくはこの状況がわからないよ、助けて**」って
                    必死に状況報告してくれているだけ。
```

エラーメッセージは:

- 🤖 **Python くんからの状況報告** (「ここで詰まったよ」)
- 📍 **何行目で詰まったか** 教えてくれる
- 🔍 **何が問題か** 説明してくれる (英語だけど、決まった単語パターンしかない)

つまり **デバッグ (= バグ取り) の最大の味方** がエラーメッセージです。
これを読めない人は、ずっと「真っ白な画面を見つめて何が起きたか分からない」 状態になる。
これを読める人は、「あ、ここね」 と 30 秒で原因にたどり着ける。

その差は学習スピードで **10 倍** くらい違います。覚悟しておきましょう。

---

## 2. トレースバックの読み方 — 「下から上」 が鉄則

エラーが出ると、こんな何行もある **「トレースバック (Traceback)」** が表示されます:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/path/to/your_code.py", line 42, in calculate_area
    return math.sqrt(radius_squared)
ValueError: math domain error
```

これを見て「うわっ」 となるのが普通です。でも、**読み方さえ知れば、ものすごくシンプル**。

### 🔑 ルール 1: **下から上に読む**

一番大事な情報は **一番下の行** にあります:

```
ValueError: math domain error
```

これが「**結論**」 です。`ValueError` (= 値がおかしい) という種類のエラーで、`math domain error` (= 数学的に定義されていない領域で計算しようとした) と言っている。

その**上**には、「どこで起きたか」 が時系列で書いてある:

```
File "/path/to/your_code.py", line 42, in calculate_area
    return math.sqrt(radius_squared)
```

→ `your_code.py` の 42 行目、`calculate_area` という関数の中で、`math.sqrt(radius_squared)` を呼んだときに起きた。

そう、ここで `radius_squared` が負の値だったから、平方根が取れなかった、と分かるわけです。

### 🔑 ルール 2: **エラーの種類名を覚える**

Python のエラーは **限られた種類の名前** しかありません。代表的なものを覚えればだいたい OK:

| エラー名 | 意味 | 例 |
|---|---|---|
| `SyntaxError` | 文法ミス | `print(` の閉じカッコ忘れ |
| `NameError` | その名前が見つからない | 変数名のタイポ、import 忘れ |
| `TypeError` | 型が合わない | 文字列と数値を `+` で繋ごうとした |
| `ValueError` | 型は合うけど値がおかしい | `int("abc")`、`math.sqrt(-1)` |
| `IndexError` | リストの範囲外を見ようとした | `[1,2,3][5]` |
| `KeyError` | 辞書に無いキーを見ようとした | `{'a': 1}['b']` |
| `ZeroDivisionError` | 0 で割った | `1/0` |
| `ImportError` / `ModuleNotFoundError` | ライブラリが見つからない | `import numpy` でインストール忘れ |
| `AttributeError` | そのオブジェクトにそんなメソッドはない | `'hello'.append('x')` |
| `IndentationError` | インデント (字下げ) が合ってない | スペースとタブの混在 |

→ 「あ、`TypeError` か」 とエラー名だけで原因の方向が見える。

---

## 3. 数学初心者がよく出会うエラー 7 選

数学を Python でやり始めると、出会う代表的なエラーたちです。
**今、ターミナルや Jupyter で実際に試してみてください**。エラーを「自分で出す」 のが、一番怖くなくなる方法です。

### 例 1: 0 で割る

```python
>>> 1 / 0
ZeroDivisionError: division by zero
```

数学的にも 0 除算は定義されていません。Python は **「未定義の演算は素直にエラーを出す**」 設計です。
ちなみに NumPy だと:
```python
>>> import numpy as np
>>> np.array([1.0]) / np.array([0.0])
array([inf])   # 警告は出るがエラーにはならず、無限大が入る
```
扱いが違うので注意。

### 例 2: 負の数の平方根 (実数の範囲)

```python
>>> import math
>>> math.sqrt(-1)
ValueError: math domain error
```

`math.sqrt` は実数しか扱えません。**虚数を扱いたいなら** `cmath` を使う:
```python
>>> import cmath
>>> cmath.sqrt(-1)
1j   # 虚数単位 i
```

### 例 3: log(0) や log(負)

```python
>>> import math
>>> math.log(0)
ValueError: math domain error
>>> math.log(-1)
ValueError: math domain error
```

「**対数の定義域は正の実数**」 という数学的事実が、Python の挙動として表れます。
`log(0) = -∞` (極限) ですが、Python は実数として返せないのでエラー。

### 例 4: 文字列を数値に変換できない

```python
>>> int("3.5")
ValueError: invalid literal for int() with base 10: '3.5'
```

`int()` は **整数の文字列** しか直接変換できません。小数を経由する必要あり:
```python
>>> int(float("3.5"))
3
```

### 例 5: import 忘れ

```python
>>> math.sqrt(4)
NameError: name 'math' is not defined
```

「`math` って名前、知らないよ」 と言われたら、**import 忘れ** がほぼ確実です:
```python
>>> import math
>>> math.sqrt(4)
2.0
```

### 例 6: 行列の shape 不一致 (線形代数で頻出)

```python
>>> import numpy as np
>>> A = np.array([[1, 2], [3, 4]])     # 2×2
>>> B = np.array([[1, 2, 3]])           # 1×3
>>> A @ B
ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, ...
```

行列積 `A @ B` は **A の列数 = B の行数** でないと計算できません。
これは線形代数を学ぶ過程で **必ず一度は出会う** エラー。`A.shape, B.shape` を print してデバッグするのが定石。

### 例 7: 集合に hashable でないものを入れる

```python
>>> {[1, 2], [3, 4]}
TypeError: unhashable type: 'list'
```

Python の集合 (`set`) は **要素にリストを入れられません** (リストは変更可能なため)。タプルなら OK:
```python
>>> {(1, 2), (3, 4)}    # ✅ OK
```

---

## 4. エラーが出たときの 3 ステップ対処法

```
       ／￣￣＼
      |  ・ω・  |   エラーを見たら、ぼくはこの 3 ステップで対処してるよ。
      |   ⌒    |   慣れれば 30 秒で原因が分かる!
       ＼____／
```

### Step 1: **一番下の行を読む** (5 秒)

```
ValueError: math domain error
```

→ エラーの種類 (`ValueError`) と、メッセージ (`math domain error`) を確認。
英語が分からなくても、辞書に意味は書いてある。`domain` = 「定義域」、`error` = 「エラー」。

### Step 2: **どこで起きたか見る** (10 秒)

```
File "my_code.py", line 42, in calculate
    return math.sqrt(radius_squared)
```

→ どのファイルの何行目で起きたか確認。Jupyter なら **どのセル** で起きたか。
そのコードを見て、「何の計算をしようとしていたか」 を思い出す。

### Step 3: **原因を仮説立てて修正** (1〜数分)

例: 「`math.sqrt` が呼ばれた、`math domain error` ということは、引数が負だったのでは?」

→ `print(radius_squared)` を 1 行入れて確認。負だったら、なぜ負になったかを追う。

これを繰り返すのが **デバッグ** です。

---

## 5. AI に聞くときのコツ

エラーが分からなければ AI (Claude / ChatGPT / Gemini) に聞くのも全然 OK です。
**ただし聞き方** が大事。

### ❌ 悪い例

```
エラーが出ます
```

→ AI: 「どんなエラーですか?」 と聞き返される。

### ✅ 良い例

```
以下の Python コードでエラーが出ました。原因と修正方法を教えてください。

[コード]
import math
def calculate_area(radius):
    return math.pi * math.sqrt(radius**2 - 100)

calculate_area(5)

[エラーメッセージ全文]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in calculate_area
ValueError: math domain error
```

→ AI: 「`radius=5` だと `5**2 - 100 = -75` で負になり、`math.sqrt` が ValueError を出します。意図と違う計算式の可能性があります。」 のように具体的に答えてくれる。

**ポイント**: **コード + エラー全文** を貼る。一部だけ貼っても AI は推測しかできません。

詳しくは `appendix/columns/ai_era_grad_student.md` も参照。

---

## 6. エラーは成長の足跡

```
       ／￣￣＼
      |  ・ω・  |   ぼくが一番伝えたいこと、それは──
      |   ⌒    |   **エラーをたくさん出した人ほど、強くなる**。
       ＼____／    
                    エラーが怖くなくなった瞬間、君は初心者を卒業だよ。
```

プロのプログラマは、**1 日に何十回もエラーを出します**。
理由は簡単で、**新しいことに挑戦している** からです。

逆に「エラーが出ない人」 は:
- (a) 既に書ける範囲のことしかやっていない (= 成長していない)
- (b) コードを実行していない (= 何も作っていない)

のどちらかです。

エラーは **「ここから学べるよ」** という、Python くんからのプレゼント。
1 つのエラーを乗り越えるたびに、君の理解は確実に 1 段階上がります。

---

## 🔍 ググってみよう

- **traceback** — Python のエラー追跡情報の正式名称
- **debugging** — バグを取る作業全般
- **`pdb`** — Python 標準のデバッガ (中級者向け)
- **`assert`** — 想定外の状態を早期に発見する文
- **try / except** — エラーをキャッチする仕組み (上級者向け)
- **rubber duck debugging** — アヒルに説明しながらバグを見つける有名な手法 (本当に効く)
- **Stack Overflow** — エラーメッセージで検索すると大体ヒットする神サイト
- **Python ドキュメント `errors` の章** — 公式のエラー一覧

---

## 🎯 今日から実践できること

1. **エラーを見たら逃げない**。まず一番下の行を読む
2. **エラーメッセージを Google / AI にコピペする** 習慣
3. **自分で意図的にエラーを出して、対処してみる** (上の例 1〜7 を全部試す)
4. **エラーが出ても焦らない**。Ctrl+C 連打して止めるのは最終手段
5. **エラーメッセージを「友達からの状況報告」 と捉える** マインドセット

---

## 関連リンク

- [`07_python_for_pets.md`](../07_python_for_pets.md) — Python の基礎 (戻って復習)
- [`09_ai_cli_as_smart_pet.md`](../09_ai_cli_as_smart_pet.md) — AI とエラー対処
- [`../../docs/jupyter_lab_guide.md`](../../../docs/jupyter_lab_guide.md) — Jupyter のトラブル対処 (Kernel リスタート等)
- [`../../../appendix/columns/ai_era_grad_student.md`](../../../appendix/columns/ai_era_grad_student.md) — AI への聞き方の作法

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`04_git_challenge.md`](04_git_challenge.md) | [章 TOP](../README.md) | [📚 ROOT README](../../../README.md) | (コラム終了 → [`../09_ai_cli_as_smart_pet.md`](../09_ai_cli_as_smart_pet.md)) |
