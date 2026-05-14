# Leaning Math — 大学院数学基礎 × Python × 生成AI

[![Docs License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Docs-CC_BY--NC--SA_4.0-lightgrey.svg)](LICENSE-DOCS)
[![Code License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![Status: Personal Learning](https://img.shields.io/badge/status-personal_learning_(unreviewed)-orange.svg)](DISCLAIMER.md)

「数学を全く知らない人」から「最先端AIの数学を理解する人」まで、**1つの道のり** で学ぶための個人学習リポジトリです。

> ## ⚠️ 免責事項 (必読 / Must Read)
>
> 本リポジトリは **特定の個人が学習目的で生成 AI と協働して作成した未検証の教材** です。
> 専門家による監修・査読は **受けていません**。
>
> - 数式・コード・歴史記述・引用に **誤りや古い情報が含まれている可能性** があります (AI ハルシネーションのリスク)
> - 必ず **教科書・査読済み論文・公式ドキュメント等の一次情報源で検証** してください
> - いかなる組織・機関の見解も示しません。**作成者個人の学習過程の記録** です
> - 利用により生じたいかなる損害についても、作成者は **一切の責任を負いません**
> - 引用・転載・SNS 共有時は **「個人作成の未検証教材」 と明示** してください
>
> 詳細は **[`DISCLAIMER.md`](DISCLAIMER.md)** を参照。誤りの指摘は Issue / PR で歓迎しますが対応保証はありません。

> ## 📜 ライセンス (デュアルライセンス)
>
> | 対象 | ライセンス |
> |---|---|
> | **コード** (`*.py`, スクリプト等) | [**MIT**](LICENSE-CODE) — 商用・非商用問わず自由に利用可 |
> | **文書** (`*.md`, notebook の markdown セル, コラム等) | [**CC BY-NC-SA 4.0**](LICENSE-DOCS) — **非商用利用のみ** 許可、改変版も同条件で公開 |
>
> 個人学習・研究室・無償の勉強会での利用は自由です。
> **書籍化・有料講座・企業研修・有償配布等の商用利用は事前にご相談ください** ([`DISCLAIMER.md`](DISCLAIMER.md#-商用利用について--commercial-use))。
> 詳細・判定基準は [`LICENSE`](LICENSE) を参照。

---

## このリポジトリでできること

- 数学記号アレルギーを克服する
- 数式と Python (NumPy / JAX) を行き来できるようになる
- 生成AIに賢く指示を出せるようになる
- 機械学習の論文・コードを読み解けるようになる

---

## 🚀 3分で始める (Windows / Mac / Linux 共通)

### Step 1: リポジトリを取得 — 2 つの方法から選ぶ

**🟢 ZIP ダウンロード (git 未経験者向け・カンタン)**

1. このページの上部にある緑色の **`<> Code`** → **`Download ZIP`** をクリック
2. ZIP を **「展開」 (解凍)** する — 「開く」 や「中身を見る」 ではダメ。OS 別の正しい手順は下の折り畳みを参照
3. 展開して出てきた `learning-math-main/` フォルダの中で起動スクリプト (Step 2) を実行

<details>
<summary><b>🪟 Windows の展開手順 — よくある失敗とともに</b></summary>

❌ **よくある失敗**: ZIP をダブルクリックすると、エクスプローラが「**フォルダのように**」 中身を表示します。これを「展開できた」 と勘違いしてしまう人が多い。
この状態で `start.bat` を実行しても、**動きません** (依存ファイルが読めない仮想表示なので)。

> 「**展開** (Extract)」 と「**開く** (Open)」 は別物です。アイコンが「ジッパーのついたフォルダ」 なら、まだ展開されていません。

✅ **正しい手順**:

1. ダウンロードした `learning-math-main.zip` を **右クリック**
2. メニューから **「すべて展開...」** (英語版なら **Extract All...**) を選択
3. 展開先フォルダが表示されるので、確認して **「展開」** ボタン
   - パスに **日本語やスペース** が含まれない場所が無難 (例: `C:\projects\` のような短い英語パス)
4. 展開後、`learning-math-main` フォルダが現れる
5. その中の `start.bat` を **ダブルクリック** ✅

> 💡 ファイル名末尾の `.zip` が見えない場合: エクスプローラの「表示」 → 「ファイル名拡張子」 にチェックを入れると見えます。

</details>

<details>
<summary><b>🍎 Mac の展開手順</b></summary>

1. ダウンロードした `learning-math-main.zip` を **ダブルクリック**
   → 同じフォルダ (通常は `~/Downloads/`) に `learning-math-main/` が自動作成されます
2. **ターミナル** を開く (アプリケーション → ユーティリティ → ターミナル.app)
3. 展開したフォルダに移動:
   ```bash
   cd ~/Downloads/learning-math-main
   ```
4. 起動スクリプトを実行:
   ```bash
   ./start.sh
   ```

> 💡 もし「**`./start.sh`: Permission denied**」 と出たら: `chmod +x start.sh && ./start.sh` で実行権限を付与してください (ZIP 経由だと実行ビットが落ちることがあります)。

</details>

<details>
<summary><b>🐧 Linux の展開手順</b></summary>

CLI なら:
```bash
unzip learning-math-main.zip
cd learning-math-main
chmod +x start.sh && ./start.sh
```

GUI ファイラの場合は ZIP を右クリック → 「**ここに展開**」 / 「**Extract here**」。

</details>

**🔵 git clone (git に慣れている人向け、推奨)**

```bash
git clone https://github.com/nobufumi-tego/learning-math.git
```

> 💡 git clone なら **展開作業も実行ビット問題も Mark of the Web も全部発生しません**。
> git に少しでも慣れている方はこちらを推奨します。git 未経験で興味のある方は [`start_here/00_pet_terminal/columns/04_git_challenge.md`](start_here/00_pet_terminal/columns/04_git_challenge.md) で git 入門ができます。

### Step 2: ⭐ ワンショットスクリプトで起動 (推奨)

リポジトリのフォルダに移動して、自分の OS のスクリプトを実行するだけです:

| OS | 起動方法 | 備考 |
|---|---|---|
| **🪟 Windows (初心者・GUI 派)** | エクスプローラから [`start.bat`](start.bat) を **ダブルクリック** | 管理者権限不要・PowerShell 設定変更不要 |
| 🪟 Windows (PowerShell 派) | `.\start.ps1` | 実行ポリシーで止まる場合は下の補足を参照 |
| **🍎 Mac / 🐧 Linux** | `./start.sh` | ターミナルで実行 |

スクリプトが以下を全部自動でやってくれます:
1. **uv** が未インストールなら公式インストーラを実行 (ユーザー領域、管理者権限不要)
2. **依存関係を sync** (初回は数分かかります)
3. **Jupyter Lab を起動** (ブラウザが自動で開きます)

ブラウザが開いたら **[`start_here/notebooks/01_pythagoras.ipynb`](start_here/notebooks/01_pythagoras.ipynb)** を開いてください。

#### ⏰ 待ち時間の目安 — 「フリーズしてない?」 と心配しないでください

**初回起動は時間がかかります**。NumPy・JAX・JupyterLab など合計 **数百 MB のダウンロード** が発生するためです。
気長に待ってください。コーヒーを淹れる、ストレッチする、メールを 1 通返すくらいの時間です ☕

| ステップ | 初回 | 2 回目以降 | 何が起きてる? |
|---|---|---|---|
| 1. uv インストール | 10〜30 秒 | スキップ | uv 本体 (約 30MB) を `~/.local/bin/` にダウンロード |
| 2. `uv sync` で依存関係取得 | **3〜10 分** | 1〜3 秒 | NumPy / SciPy / JAX / JupyterLab など合計 500MB〜1GB をダウンロード + キャッシュ |
| 3. Jupyter Lab 起動 | 10〜30 秒 | 5〜10 秒 | カーネル初期化 → ブラウザ自動オープン |
| **合計** | **約 5〜15 分** | **約 10〜20 秒** | |

> 🪟 **Windows で「応答なし」 表示が出ても焦らない** — 大量のファイル展開中で OS が表示を更新できないだけです。コーヒーを淹れて戻ってくれば終わっています。
>
> 🌐 **ネットワークが遅い環境では更に時間がかかります** (公衆 Wi-Fi、モバイル回線等)。可能なら最初の 1 回だけは安定した有線/Wi-Fi 環境で実行してください。
>
> 📊 **進捗の見方**: ターミナル / コマンドプロンプト画面に `Building` `Downloading` `Resolved` `Installed` などのメッセージが流れていれば作業中です。何も流れていなくても uv の解決アルゴリズムが動いている可能性があるので、**最低 10 分は待ってから** 中止判断してください。
>
> ❌ **やってはいけないこと**: 「遅いから」 と Ctrl+C で中断 → やり直すとさらに遅くなる (キャッシュが半端な状態に)。**一度始めたら最後まで待つ** のが一番速い。

> 💾 **ディスク容量**: 全部入って約 **1〜2GB** (Python 環境 + Jupyter 関連 + 数値計算ライブラリ)。空き容量にご注意。

#### 🆘 つまずきポイントとフォールバック

<details>
<summary><b>🪟 Windows で「スクリプトの実行が無効」 と出た場合</b></summary>

以下のいずれかを試してください:

- **方法 A (一番カンタン)**: いったんウィンドウを閉じて、エクスプローラから [`start.bat`](start.bat) を**ダブルクリック** — `.bat` は ExecutionPolicy の影響を受けません
- **方法 B (PowerShell で 1 回だけ Bypass)**:
  ```powershell
  powershell -ExecutionPolicy Bypass -File .\start.ps1
  ```
- **方法 C (今後ずっと有効化)** — PowerShell を 1 回だけ開いて:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```
  (管理者権限不要、`CurrentUser` スコープなのであなたのユーザーだけに影響)

</details>

<details>
<summary><b>🪟 Windows で ZIP 展開後に「ブロックされたファイル」 警告が出る場合 (Mark of the Web)</b></summary>

GitHub から ZIP で取得して展開した `.ps1` / `.bat` には「インターネットから来た」 マークが付き、警告が出ることがあります。

- **解決法 A**: 展開した `learning-math-main` フォルダを右クリック → **プロパティ** → 下部の **「☐ 許可する (Unblock)」 にチェック** → OK
  → フォルダ内のすべてのファイルが一括で許可されます
- **解決法 B (PowerShell で一発)**: フォルダで PowerShell を開き、
  ```powershell
  Get-ChildItem -Recurse | Unblock-File
  ```

`git clone` で取得した場合は、この警告は出ません。

</details>

<details>
<summary><b>🐧 Mac / Linux で「Permission denied」 と出た場合</b></summary>

```bash
chmod +x start.sh && ./start.sh
```

git clone なら実行ビット付きで取得されるはずですが、ZIP 展開だと外れることがあります。

</details>

### 🛑 停止方法

Jupyter Lab を停止するには、起動したターミナル / PowerShell ウィンドウで **Ctrl+C を 2 回** 押してください。

### 🔧 各ステップを手動で実行したい方

スクリプトを使わず仕組みを理解しながら進めたい方は、[`docs/setup.md`](docs/setup.md) の **手動セットアップ** セクションを参照してください (uv インストール → `uv sync` → `uv run lab.py` の 3 段階)。トラブルシューティング情報も同じ場所にあります。

---

## 🎯 どこから始めるか — 学習者のレベル別 入口

### 🐧 ターミナルもプログラミングも触ったことがない人

→ 最初の1ページ: **[`start_here/00_pet_terminal/README.md`](start_here/00_pet_terminal/README.md)**

ペンギンの **ペンタ** と一緒に、真っ黒な画面の正体・CLI・Python・uv・AI CLI を学ぶ (約3時間)。

### 🌱 数学が全くわからない・苦手意識が強い人

→ 最初の1ページ: **[`start_here/README.md`](start_here/README.md)**

数式ゼロ、たとえ話だけで「数学とは何か」を体感。ピタゴラス・三角関数・対数を「実生活の道具」として理解。

### 🌿 高校数学はやったけど忘れている人

→ 最初の1ページ: **[`00_notation/README.md`](00_notation/README.md)** で記号の読み解きから

### 🌳 ML/AIの実装ができるようになりたい人

→ [`01_linear_algebra/`](01_linear_algebra/README.md) → [`02_calculus/`](02_calculus/README.md) → [`06_ml_math_bridge/`](06_ml_math_bridge/README.md) → [`07_jax/`](07_jax/README.md)

詳しい順序は [`docs/learning_path.md`](docs/learning_path.md) を参照。

### 🚀 本リポジトリの先へ進みたい人 (書籍・Web リソース)

→ **[`appendix/`](appendix/README.md)** — 章別おすすめ書籍 (50 冊) + オンライン教材 + 進路別ロードマップ

| ファイル | 内容 |
|---|---|
| [`appendix/README.md`](appendix/README.md) | 章別早見表 + 学習目標別の進路 |
| [`appendix/books.md`](appendix/books.md) | 📕 厳選書籍 50 冊 (日英・初級〜上級・有料/無料) |
| [`appendix/online.md`](appendix/online.md) | 🌐 YouTube・MOOC・公式ドキュメント・論文サイト |
| [`appendix/learning_paths.md`](appendix/learning_paths.md) | 🎯 大学院 / MLエンジニア / LLM / DS 別ロードマップ |

---

## 📚 全章ドキュメント案内 (すべてのページに直接アクセス)

### Phase −1: 🐧 ペットと学ぶターミナル基礎

📂 [`start_here/00_pet_terminal/`](start_here/00_pet_terminal/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_what_is_terminal.md`](start_here/00_pet_terminal/01_what_is_terminal.md) | 真っ黒な画面の正体 (歴史: テレタイプ→VT100) |
| 02 | [`02_meet_your_pet.md`](start_here/00_pet_terminal/02_meet_your_pet.md) | シェル (ペンタ) に挨拶 — bash/zsh/PowerShell |
| 03 | [`03_first_commands.md`](start_here/00_pet_terminal/03_first_commands.md) | 最初の3命令: `pwd` / `ls` / `cd` |
| 04 | [`04_files_and_folders.md`](start_here/00_pet_terminal/04_files_and_folders.md) | ファイル操作: `mkdir` / `touch` / `cp` / `mv` / `rm` |
| 05 | [`05_pipes_and_combine.md`](start_here/00_pet_terminal/05_pipes_and_combine.md) | パイプ `\|` の魔法 |
| 06 | [`06_why_cli_in_modern_work.md`](start_here/00_pet_terminal/06_why_cli_in_modern_work.md) | なぜ CLI で仕事が爆速になるのか |
| 07 | [`07_python_for_pets.md`](start_here/00_pet_terminal/07_python_for_pets.md) | ペンタが Python を覚える |
| 08 | [`08_uv_keeps_pet_healthy.md`](start_here/00_pet_terminal/08_uv_keeps_pet_healthy.md) | `uv` はペンタの世話係 |
| 09 | [`09_ai_cli_as_smart_pet.md`](start_here/00_pet_terminal/09_ai_cli_as_smart_pet.md) | AI CLI 時代 (Claude/Gemini/Codex) |

📖 コラム (読み物):
- [`columns/00_history_of_computer.md`](start_here/00_pet_terminal/columns/00_history_of_computer.md) — コンピュータ80年史
- [`columns/01_unix_philosophy.md`](start_here/00_pet_terminal/columns/01_unix_philosophy.md) — UNIX の哲学
- [`columns/02_keyboard_age.md`](start_here/00_pet_terminal/columns/02_keyboard_age.md) — キーボードがマウスより速い理由
- [`columns/03_open_source.md`](start_here/00_pet_terminal/columns/03_open_source.md) — オープンソースの物語
- 🎯 **[`columns/04_git_challenge.md`](start_here/00_pet_terminal/columns/04_git_challenge.md) — チャレンジ章: Git 入門** (一人でもチームでも強すぎる味方)

---

### Phase 0: 🌱 数学を全く知らない人向け

📂 [`start_here/`](start_here/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_why_math.md`](start_here/01_why_math.md) | そもそも数学って何の役に立つ？ |
| 02 | [`02_pythagoras.md`](start_here/02_pythagoras.md) | ピタゴラスの定理 (家・GPS・AI) |
| 03 | [`03_trigonometry.md`](start_here/03_trigonometry.md) | 三角関数 (スマホ・音楽・アニメ) |
| 04 | [`04_logarithm.md`](start_here/04_logarithm.md) | 対数 (地震・デシベル・pH) |

📖 コラム:
- [`columns/00_what_is_math.md`](start_here/columns/00_what_is_math.md) — 数学はどこから来たか (5000年史)
- [`columns/01_pythagoras_story.md`](start_here/columns/01_pythagoras_story.md) — ピタゴラスは数学者か宗教家か
- [`columns/02_trig_in_real_world.md`](start_here/columns/02_trig_in_real_world.md) — 三角関数が現代社会のどこに居るか
- [`columns/03_zero_invention.md`](start_here/columns/03_zero_invention.md) — ゼロの発明
- [`columns/04_e_and_pi.md`](start_here/columns/04_e_and_pi.md) — π と e の不思議
- [`columns/05_math_in_ai.md`](start_here/columns/05_math_in_ai.md) — 今のAIは数学のどこで動いているか

📓 Jupyter ノートブック (対話的に遊べる):
- [`notebooks/01_pythagoras.ipynb`](start_here/notebooks/01_pythagoras.ipynb) — ピタゴラスの定理
- [`notebooks/02_trigonometry.ipynb`](start_here/notebooks/02_trigonometry.ipynb) — 三角関数
- [`notebooks/03_trig_usecases.ipynb`](start_here/notebooks/03_trig_usecases.ipynb) — 音波・GPS・フーリエ

---

### Phase 1: 📐 数学記号と論理

📂 [`00_notation/`](00_notation/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_basic_symbols.md`](00_notation/01_basic_symbols.md) | 等号・不等号・無限・数の集合 (ℕℤℚℝℂ) |
| 02 | [`02_set_theory.md`](00_notation/02_set_theory.md) | 集合 ∈ ∉ ⊂ ⊃ ∪ ∩ |
| 03 | [`03_logic_symbols.md`](00_notation/03_logic_symbols.md) | 論理 ∀ ∃ ⇒ ⇔ ∧ ∨ ¬ |
| 04 | [`04_function_notation.md`](00_notation/04_function_notation.md) | 関数記法 f: A → B, ↦ |
| 05 | [`05_summation_product.md`](00_notation/05_summation_product.md) | Σ (総和) / Π (総乗) / ∫ (積分) |
| 06 | [`06_greek_letters.md`](00_notation/06_greek_letters.md) | ギリシャ文字一覧と慣習 |

🐍 サンプル:
- [`examples/notation_to_python.py`](00_notation/examples/notation_to_python.py) — 記号 → Python 対応例

---

### Phase 2: 📊 線形代数

📂 [`01_linear_algebra/`](01_linear_algebra/README.md) — 章 TOP

| # | 解説 (md) | 動かす (ipynb) | 内容 |
|---|---|---|---|
| 01 | [`01_vectors.md`](01_linear_algebra/01_vectors.md) | [`01_vectors.ipynb`](01_linear_algebra/notebooks/01_vectors.ipynb) | ベクトル・内積・ノルム・コサイン類似度 |
| 02 | [`02_matrices.md`](01_linear_algebra/02_matrices.md) | [`02_matrices.ipynb`](01_linear_algebra/notebooks/02_matrices.ipynb) | 行列・行列積・転置・逆行列・線形変換 |
| 03 | [`03_eigenvalues.md`](01_linear_algebra/03_eigenvalues.md) | [`03_eigenvalues.ipynb`](01_linear_algebra/notebooks/03_eigenvalues.ipynb) | 固有値・固有ベクトル・PCA・PageRank |
| 04 | [`04_decompositions.md`](01_linear_algebra/04_decompositions.md) | [`04_decompositions.ipynb`](01_linear_algebra/notebooks/04_decompositions.ipynb) | LU・QR・Cholesky・SVD (画像圧縮・推薦) |

🐍 CLI 実行サンプル:
- [`examples/vectors_and_matrices.py`](01_linear_algebra/examples/vectors_and_matrices.py) — 標準形式 (NumPy)
- [`examples/vectors_and_matrices_jax.py`](01_linear_algebra/examples/vectors_and_matrices_jax.py) — JAX形式

---

### Phase 3: 🌀 微積分

📂 [`02_calculus/`](02_calculus/README.md) — 章 TOP

| # | 解説 (md) | 動かす (ipynb) | 内容 |
|---|---|---|---|
| 01 | [`01_limits.md`](02_calculus/01_limits.md) | [`01_limits.ipynb`](02_calculus/notebooks/01_limits.ipynb) | 極限・連続性・e の定義 |
| 02 | [`02_derivatives.md`](02_calculus/02_derivatives.md) | [`02_derivatives.ipynb`](02_calculus/notebooks/02_derivatives.ipynb) | 微分 (SymPy/数値/JAX) ・連鎖律 |
| 03 | [`03_integrals.md`](02_calculus/03_integrals.md) | [`03_integrals.ipynb`](02_calculus/notebooks/03_integrals.ipynb) | 積分・リーマン和・期待値 |
| 04 | [`04_multivariable.md`](02_calculus/04_multivariable.md) | [`04_multivariable.ipynb`](02_calculus/notebooks/04_multivariable.ipynb) | 多変数関数・偏微分・勾配ベクトル |
| 05 | [`05_gradient_jacobian.md`](02_calculus/05_gradient_jacobian.md) | [`05_gradient_jacobian.ipynb`](02_calculus/notebooks/05_gradient_jacobian.ipynb) | ∇f / Jf / Hf — ML微分の総合編 |

🐍 CLI 実行サンプル:
- [`examples/derivative_demo.py`](02_calculus/examples/derivative_demo.py) — 標準形式 (SymPy / 数値差分)
- [`examples/derivative_demo_jax.py`](02_calculus/examples/derivative_demo_jax.py) — JAX形式 (`jax.grad`)

---

### Phase 4: 🎲 確率・統計

📂 [`03_probability_statistics/`](03_probability_statistics/README.md) — 章 TOP

| # | 解説 (md) | 動かす (ipynb) | 内容 |
|---|---|---|---|
| 01 | [`01_probability_basics.md`](03_probability_statistics/01_probability_basics.md) | [`01_probability_basics.ipynb`](03_probability_statistics/notebooks/01_probability_basics.ipynb) | 確率・独立性・条件付き確率・大数の法則 |
| 02 | [`02_distributions.md`](03_probability_statistics/02_distributions.md) | [`02_distributions.ipynb`](03_probability_statistics/notebooks/02_distributions.ipynb) | 正規・二項・ポアソン・指数、中心極限定理 |
| 03 | [`03_expectation_variance.md`](03_probability_statistics/03_expectation_variance.md) | [`03_expectation_variance.ipynb`](03_probability_statistics/notebooks/03_expectation_variance.ipynb) | 期待値・分散・共分散・標準化 |
| 04 | [`04_bayes.md`](03_probability_statistics/04_bayes.md) | [`04_bayes.ipynb`](03_probability_statistics/notebooks/04_bayes.ipynb) | ベイズの定理・ベイズ更新・ナイーブベイズ |

🐍 CLI 実行サンプル:
- [`examples/distribution_demo.py`](03_probability_statistics/examples/distribution_demo.py) — 各種分布の可視化

---

### Phase 5: ⛰️ 最適化

📂 [`05_optimization/`](05_optimization/README.md) — 章 TOP

| # | 解説 (md) | 動かす (ipynb) | 内容 |
|---|---|---|---|
| 01 | [`01_basic_concepts.md`](05_optimization/01_basic_concepts.md) | [`01_basic_concepts.ipynb`](05_optimization/notebooks/01_basic_concepts.ipynb) | 最小化・凸関数・ヘッセ行列 |
| 02 | [`02_gradient_descent.md`](05_optimization/02_gradient_descent.md) | [`02_gradient_descent.ipynb`](05_optimization/notebooks/02_gradient_descent.ipynb) | GD/SGD/Mini-batch/Momentum/Adam |

🐍 CLI 実行サンプル:
- [`examples/gradient_descent_demo.py`](05_optimization/examples/gradient_descent_demo.py) — 標準形式 (手で勾配導出)
- [`examples/gradient_descent_demo_jax.py`](05_optimization/examples/gradient_descent_demo_jax.py) — JAX形式 (`jax.grad`)

---

### Phase 6: 🌉 機械学習への橋渡し

📂 [`06_ml_math_bridge/`](06_ml_math_bridge/README.md) — 章 TOP

| # | 解説 (md) | 動かす (ipynb) | 内容 |
|---|---|---|---|
| 01 | [`01_loss_functions.md`](06_ml_math_bridge/01_loss_functions.md) | [`01_loss_functions.ipynb`](06_ml_math_bridge/notebooks/01_loss_functions.ipynb) | MSE・クロスエントロピー・正則化 |
| 02 | [`02_backprop.md`](06_ml_math_bridge/02_backprop.md) | [`02_backprop.ipynb`](06_ml_math_bridge/notebooks/02_backprop.ipynb) | 誤差逆伝播・手書き vs JAX |

🐍 CLI 実行サンプル:
- [`examples/loss_and_gradient.py`](06_ml_math_bridge/examples/loss_and_gradient.py) — 線形回帰 + クロスエントロピー (NumPy)
- [`examples/loss_and_gradient_jax.py`](06_ml_math_bridge/examples/loss_and_gradient_jax.py) — JAX で線形回帰 (自動微分)

---

### Phase 7: ⚡ JAX (自動微分・JIT・vmap)

📂 [`07_jax/`](07_jax/README.md) — 章 TOP

| # | ページ | 内容 |
|---|---|---|
| 01 | [`01_basics.md`](07_jax/01_basics.md) | `jax.numpy`・配列の不変性・PRNGキー |
| 02 | [`02_autodiff.md`](07_jax/02_autodiff.md) | `jax.grad`・`value_and_grad`・高階微分・ヤコビアン・ヘッシアン |
| 03 | [`03_jit_vmap.md`](07_jax/03_jit_vmap.md) | `@jit` で高速化・`vmap` でベクトル化 |

🐍 サンプル:
- [`examples/jax_basics.py`](07_jax/examples/jax_basics.py) — NumPy と JAX の対応
- [`examples/grad_demo.py`](07_jax/examples/grad_demo.py) — 自動微分の威力
- [`examples/jit_vmap_demo.py`](07_jax/examples/jit_vmap_demo.py) — JIT と vmap のベンチマーク

---

### Phase 8: 🔢 離散数学 (補助)

📂 [`04_discrete_math/`](04_discrete_math/README.md) — 章 TOP

| # | 解説 (md) | 動かす (ipynb) | 内容 |
|---|---|---|---|
| 01 | [`01_logic.md`](04_discrete_math/01_logic.md) | [`01_logic.ipynb`](04_discrete_math/notebooks/01_logic.ipynb) | 命題論理、真理表、ド・モルガン |
| 02 | [`02_proof_techniques.md`](04_discrete_math/02_proof_techniques.md) | [`02_proof_techniques.ipynb`](04_discrete_math/notebooks/02_proof_techniques.ipynb) | 直接証明・背理法・帰納法 |
| 03 | [`03_combinatorics.md`](04_discrete_math/03_combinatorics.md) | [`03_combinatorics.ipynb`](04_discrete_math/notebooks/03_combinatorics.ipynb) | 順列・組合せ・二項定理・スターリング |

---

## 📖 用語集・リファレンス

📂 [`glossary/`](glossary/README.md)

- [`symbol_reference.md`](glossary/symbol_reference.md) — 数学記号 → Python 対応の逆引き辞書
- [`jp_en_terms.md`](glossary/jp_en_terms.md) — 日英用語対訳 (英語論文の辞書)

---

## 📚 さらに学びたい人へ — Appendix (書籍 + Web リソース)

📂 [`appendix/`](appendix/README.md) — **本リポジトリの後どこへ進むか** を網羅したガイド

| ファイル | 内容 |
|---|---|
| [`appendix/README.md`](appendix/README.md) | 章別おすすめ早見表 + 学習目標別ロードマップ |
| [`appendix/books.md`](appendix/books.md) | **書籍 50 冊** — 日英・初級〜上級・有料/無料、なぜおすすめか付き |
| [`appendix/online.md`](appendix/online.md) | **オンライン教材** — YouTube / MOOC / 公式ドキュメント / 論文サイト |
| [`appendix/learning_paths.md`](appendix/learning_paths.md) | 大学院・MLエンジニア・LLM開発・データサイエンティスト 別の進路 |

**最初の 1 歩**:
- 📕 [数学ガール](appendix/books.md#数学ガール) (結城浩) — 数学アレルギーをなくす物語
- 📕 [プログラミングのための線形代数](appendix/books.md#プログラミングのための線形代数) — エンジニア向けの ML 基礎
- 🌐 [3Blue1Brown](appendix/online.md#3blue1brown) — 数学を動画で直感的に
- 🌐 [Karpathy: Neural Networks Zero to Hero](appendix/online.md#karpathy-neural-networks-zero-to-hero) — GPT を 1 から実装

---

## 📋 更新履歴

このリポジトリの変更履歴は [`CHANGELOG.md`](CHANGELOG.md) で確認できます。
**`main` への push 毎に GitHub Actions が git ログから自動生成・更新** するので、最新状態が常に反映されます ([ワークフロー定義](.github/workflows/changelog.yml) / [生成スクリプト](scripts/generate_changelog.py))。

---

## 🛠️ Python 実装の方針: 「標準形式」 + 「JAX形式」 の併記

各章の `examples/` には以下の2形式を併置します:
- `xxx.py` — **標準形式** (NumPy / SymPy / SciPy): 数式 → コード対応が直感的
- `xxx_jax.py` — **JAX形式**: `jax.grad` で自動微分、`@jit` で高速化

JAX を最終到達点に据えることで、研究論文の最先端コード (Gemini, AlphaFold, etc.) が読める素養を獲得します。

---

## 🤖 AI CLI で動的に学ぶ

3つの CLI ツールすべてで、専用カスタムコマンドが使えます:

| コマンド | 効果 | 詳細 |
|---|---|---|
| `/project:teach-baby <なんでも>` | 数式ゼロ・たとえ話だけで超やさしく説明 | [.claude/commands/teach-baby.md](.claude/commands/teach-baby.md) |
| `/project:column <トピック>` | 歴史・偉人エピソード・現代の使われ方の読み物 | [.claude/commands/column.md](.claude/commands/column.md) |
| `/project:visualize <概念>` | matplotlib + ipywidgets で対話的可視化コード生成 | [.claude/commands/visualize.md](.claude/commands/visualize.md) |
| `/project:explain-symbol <記号>` | 数学記号を「読み方・意味・Python対応・例」の4点で解説 | [.claude/commands/explain-symbol.md](.claude/commands/explain-symbol.md) |
| `/project:math-to-python <数式>` | 数式を実行可能な Python コードに変換 | [.claude/commands/math-to-python.md](.claude/commands/math-to-python.md) |
| `/project:concept-check <概念>` | ソクラテス式問答で理解度をチェック | [.claude/commands/concept-check.md](.claude/commands/concept-check.md) |

例:
```
/project:teach-baby ベクトルってなに？
/project:column ニュートンとライプニッツの微積分戦争
/project:visualize 正規分布の標準偏差
/project:explain-symbol ∂
```

### 対応 CLI ツール

- **Claude Code** (`claude`) — `CLAUDE.md` 経由で全設定が自動ロード
- **Gemini CLI** (`gemini`) — `GEMINI.md` 経由で全設定が自動ロード
- **Codex CLI** (`codex`) — `AGENTS.md` をネイティブで読む

3ツールすべて [`AGENTS.md`](AGENTS.md) を共通指示書として読みます。
**clone / ZIP 展開 した瞬間から本環境と同等の AI 体験** が手に入る仕組みについては [`docs/ai_environment_setup.md`](docs/ai_environment_setup.md) を参照。

---

## 📚 主要ドキュメント

| ドキュメント | 内容 |
|---|---|
| [`AGENTS.md`](AGENTS.md) | AI 共通指示書 (3ツール共通の説明スタイル・規約) |
| [`docs/setup.md`](docs/setup.md) | セットアップ詳細 (OS別トラブルシューティング含む) |
| [`docs/learning_path.md`](docs/learning_path.md) | 学習ロードマップ (Phase −1 〜 8、約3か月コース) |
| [`docs/ai_environment_setup.md`](docs/ai_environment_setup.md) | clone / ZIP 直後から本環境と同等の AI 体験を実現する仕組み |
| [`pyproject.toml`](pyproject.toml) | Python 依存関係 |
| [`LICENSE`](LICENSE) | デュアルライセンスのガイド (Code: MIT / Docs: CC BY-NC-SA 4.0) |
| [`LICENSE-CODE`](LICENSE-CODE) | コード用ライセンス (MIT 本文) |
| [`LICENSE-DOCS`](LICENSE-DOCS) | 文書用ライセンス (CC BY-NC-SA 4.0 サマリ + 公式 legalcode へのリンク) |
| [`DISCLAIMER.md`](DISCLAIMER.md) | 免責事項 + 商用利用の連絡窓口 |

---

## 環境

- Python 3.10+ (uv が自動取得)
- NumPy / SciPy / SymPy / matplotlib / Jupyter / JAX / ipywidgets
- OS: Windows / Mac / Linux すべて対応

## ライセンス

本リポジトリは **デュアルライセンス** で公開しています。詳細とファイル区分の判定基準は [`LICENSE`](LICENSE) を参照してください。

| 対象 | ライセンス | 利用条件の要約 |
|---|---|---|
| **コード** (`*.py`, `lab.py`, `scripts/`, notebook の code セル, 設定ファイル等) | [**MIT**](LICENSE-CODE) | 商用・非商用問わず自由に使用・改変・再配布可。MIT ライセンス表記を残してください |
| **文書** (`*.md`, notebook の markdown セル, コラム, 用語集, 図等) | [**CC BY-NC-SA 4.0**](LICENSE-DOCS) | **非商用利用のみ** 許可。改変版も同条件で公開してください (ShareAlike) |

### 何が許可され、何が要相談か

- ✅ **個人学習・研究室・無料の勉強会・大学のゼミ等での利用** — 自由 (どちらのライセンスも許可)
- ✅ **コードを自分のプロジェクト (商用含む) で再利用** — MIT なので自由
- ✅ **fork して AI と組んで章を拡張、非商用で再公開** — CC BY-NC-SA 4.0 で同条件公開なら自由
- ❌ **書籍化 / 有料講座 / 企業内研修 / 有償配布 / paid SaaS への組み込み等の商用利用** — **要相談** ([`DISCLAIMER.md` の連絡窓口](DISCLAIMER.md#-商用利用について--commercial-use))
- ❌ **改変して MIT 等のより緩いライセンスに変えて再公開 (ShareAlike 違反)** — 不可

ライセンスは「無断で儲ける人をブロック」 するためのものであり、**学習者・研究者の自由な利用は積極的に推奨します**。

## 貢献

個人学習用リポジトリですが、誤りの指摘や改善提案は Issue / PR で歓迎します ([`DISCLAIMER.md`](DISCLAIMER.md#contributions) の通り、対応は保証されません)。
