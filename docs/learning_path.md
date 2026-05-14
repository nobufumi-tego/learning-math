# 学習ロードマップ — 投資対効果を最大化する順序

## 全体方針

**目的別に「いますぐ要る順」で学ぶ**:
1. 論文・生成AIの数式を**読める**ようになる（最優先）
2. 数式を**Pythonコードに変換**できるようになる
3. 自分で**機械学習を実装**できるようになる

## 推奨スケジュール（社会人想定: 週5時間 × 3か月）

### Phase −1: ターミナル/CLI/Python の地ならし（1〜2週間 / 約3時間） — 該当者のみ

**この段階のゴール**: 真っ黒な画面に拒否反応がなくなり、`uv run lab.py` が打てる。

ターミナル・コマンド入力・Python という言葉に触ったことがない方は、**まずここから**。
ペンギンの **ペンタ** がガイド役。

- [ ] `start_here/00_pet_terminal/README.md` を読む (5分)
- [ ] `01_what_is_terminal.md` — 真っ黒な画面の正体・歴史 (15分)
- [ ] `02_meet_your_pet.md` — シェル(ペンタ)に挨拶 (15分)
- [ ] `03_first_commands.md` — pwd/ls/cd の3つの命令 (20分)
- [ ] `04_files_and_folders.md` — ファイル操作 (30分)
- [ ] `05_pipes_and_combine.md` — パイプの魔法 (25分)
- [ ] `06_why_cli_in_modern_work.md` — 仕事で爆速になる理由 (20分)
- [ ] `07_python_for_pets.md` — Python 入門 (20分)
- [ ] `08_uv_keeps_pet_healthy.md` — uv の役割 (15分)
- [ ] `09_ai_cli_as_smart_pet.md` — AI CLI 時代へ (20分)

### コラム（休憩中・移動中に）
- [ ] `columns/00_history_of_computer.md` — コンピュータ80年史
- [ ] `columns/01_unix_philosophy.md` — UNIXの哲学
- [ ] `columns/02_keyboard_age.md` — キーボード文化
- [ ] `columns/03_open_source.md` — オープンソースの物語

**チェックポイント**:
- ターミナルを開いて `pwd` `ls` `cd` を打てる
- 「rm はゴミ箱に入らない」と知っている
- `uv sync` と `uv run lab.py` が何をしているか説明できる
- AI CLI (Claude/Gemini/Codex) の存在を知っていて、起動できる

### Phase 0: 数学アレルギーを溶かす（1〜2週間 / 約5時間） — 初心者向け

**この段階のゴール**: 「数学って実生活で役に立つんだ」と腹落ちする。

数学に苦手意識がある方は、ここから始めてください。**数式を一切使わず**、たとえ話と Jupyter のスライダーで遊びながら、世界の見え方を変えます。

- [ ] `start_here/README.md` を読む (5分)
- [ ] `start_here/01_why_math.md` — そもそも数学って何の役に立つ？ (15分)
- [ ] `start_here/02_pythagoras.md` — ピタゴラスの定理 (30分)
- [ ] `start_here/notebooks/01_pythagoras.ipynb` で**スライダーを動かして遊ぶ** (15分)
- [ ] `start_here/03_trigonometry.md` — 三角関数 (45分)
- [ ] `start_here/notebooks/02_trigonometry.ipynb` で sin/cos を可視化 (20分)
- [ ] `start_here/notebooks/03_trig_usecases.ipynb` で音波・GPS・フーリエ (30分)
- [ ] `start_here/04_logarithm.md` — 対数・地震・デシベル (30分)

### 読み物コラム（疲れたとき・移動中・休憩時に）
- [ ] `start_here/columns/00_what_is_math.md` — 数学5000年史
- [ ] `start_here/columns/01_pythagoras_story.md` — ピタゴラス教団のドラマ
- [ ] `start_here/columns/02_trig_in_real_world.md` — 三角関数が現代社会のどこにいるか
- [ ] `start_here/columns/03_zero_invention.md` — ゼロの発明
- [ ] `start_here/columns/04_e_and_pi.md` — π と e の不思議
- [ ] `start_here/columns/05_math_in_ai.md` — AI で使われている数学

**チェックポイント**:
- 「ピタゴラスの定理 = GPS の距離計算」と説明できる
- スマホ・音楽・ゲームの裏側に三角関数があると気付ける
- Jupyter Lab を起動してセルを実行できる
- Claude Code / Gemini で `/project:teach-baby <概念>` を使って質問できる

### Phase 1: 読める目を作る（2週間 / 約10時間）

**この段階のゴール**: 論文の Abstract が記号アレルギーなく読める

- [ ] `00_notation/01_basic_symbols.md` — 基本記号 (30分)
- [ ] `00_notation/02_set_theory.md` — 集合 (1h)
- [ ] `00_notation/03_logic_symbols.md` — 論理 ∀ ∃ ⇒ (1h)
- [ ] `00_notation/04_function_notation.md` — 関数 (30分)
- [ ] `00_notation/05_summation_product.md` — Σ Π ∫ (1h)
- [ ] `00_notation/06_greek_letters.md` — ギリシャ文字 (30分)
- [ ] `00_notation/examples/notation_to_python.py` を実行 (30分)

**チェックポイント**:
- Claude Code に「論文によく出る `∀ε > 0, ∃δ > 0` の意味を説明して」と聞いて、自力で理解の正誤確認ができる
- ChatGPT で機械学習の論文を1段落出して、出てきた記号をすべて識別できる

### Phase 2: 線形代数（2週間 / 約10時間）

**この段階のゴール**: 行列の積、転置、逆行列、固有値が NumPy で書ける

- [ ] `01_linear_algebra/01_vectors.md` (1h)
- [ ] `01_linear_algebra/02_matrices.md` (2h)
- [ ] `01_linear_algebra/03_eigenvalues.md` (2h)
- [ ] `01_linear_algebra/04_decompositions.md` (2h)
- [ ] `01_linear_algebra/examples/vectors_and_matrices.py` 実行・改造

**チェックポイント**:
- 連立方程式 `Ax = b` を解ける
- 主成分分析の意味を説明できる

### Phase 3: 微積分（2週間 / 約10時間）

**この段階のゴール**: 勾配を計算でき、ML の損失関数を微分できる

- [ ] `02_calculus/01_limits.md` (1h)
- [ ] `02_calculus/02_derivatives.md` (2h)
- [ ] `02_calculus/03_integrals.md` (2h)
- [ ] `02_calculus/04_multivariable.md` (2h)
- [ ] `02_calculus/05_gradient_jacobian.md` (3h)
- [ ] `02_calculus/examples/derivative_demo.py` 実行・改造

**チェックポイント**:
- 連鎖律 `(g∘f)'(x) = g'(f(x))f'(x)` を使える
- 勾配 ∇f を SymPy と数値の両方で計算できる

### Phase 4: 確率・統計（2週間 / 約10時間）

- [ ] `03_probability_statistics/01_probability_basics.md` (1.5h)
- [ ] `03_probability_statistics/02_distributions.md` (2h)
- [ ] `03_probability_statistics/03_expectation_variance.md` (1.5h)
- [ ] `03_probability_statistics/04_bayes.md` (2h)
- [ ] `03_probability_statistics/examples/distribution_demo.py` 実行・改造

### Phase 5: 最適化（1週間 / 約5時間）

- [ ] `05_optimization/01_basic_concepts.md` (1.5h)
- [ ] `05_optimization/02_gradient_descent.md` (2h)
- [ ] `05_optimization/examples/gradient_descent_demo.py` 実行・改造

### Phase 6: ML への統合（2週間 / 約10時間）

**この段階のゴール**: 線形回帰を NumPy だけで実装できる

- [ ] `06_ml_math_bridge/01_loss_functions.md` (2h)
- [ ] `06_ml_math_bridge/02_backprop.md` (3h)
- [ ] `06_ml_math_bridge/examples/loss_and_gradient.py` 実行・改造（標準形式）
- [ ] 自分で線形回帰を NumPy で実装

### Phase 7: JAX への移行（2週間 / 約8時間）

**この段階のゴール**: 現代の機械学習研究コード（JAX + Flax）を読める

- [ ] `07_jax/01_basics.md` — jax.numpy・配列不変性・PRNGキー (1h)
- [ ] `07_jax/02_autodiff.md` — jax.grad で自動微分 (1.5h)
- [ ] `07_jax/03_jit_vmap.md` — jit / vmap で高速化・ベクトル化 (1.5h)
- [ ] `07_jax/examples/jax_basics.py` (30分)
- [ ] `07_jax/examples/grad_demo.py` (30分)
- [ ] `07_jax/examples/jit_vmap_demo.py` (30分)
- [ ] 既存のサンプルの `_jax.py` 版を読み比べる:
  - `01_linear_algebra/examples/vectors_and_matrices_jax.py`
  - `02_calculus/examples/derivative_demo_jax.py`
  - `05_optimization/examples/gradient_descent_demo_jax.py`
  - `06_ml_math_bridge/examples/loss_and_gradient_jax.py`
- [ ] 線形回帰を **JAX で再実装** （Phase 6 と読み比べる）

**チェックポイント**:
- `jax.grad` が「関数を渡すと勾配関数が返ってくる」と説明できる
- `jit` を付けるだけで速くなる理由（XLAコンパイル）を説明できる
- `vmap` を使ってバッチ処理を1行で書ける

### Phase 8: 離散数学（必要に応じて）

- [ ] `04_discrete_math/01_logic.md` (1h)
- [ ] `04_discrete_math/02_proof_techniques.md` (2h)
- [ ] `04_discrete_math/03_combinatorics.md` (1.5h)

## 学習のコツ

### 毎日のサイクル（30分）
1. 該当ファイルを読む（10分）
2. examples/ のコードを実行（5分）
3. Claude Code で `/project:concept-check <概念>` で理解度確認（10分）
4. わからない記号を `glossary/symbol_reference.md` に追記（5分）

### つまづいたとき
- `/project:explain-symbol <記号>` で記号解説
- `/project:math-to-python <数式>` で Python 化
- `/project:concept-check <概念>` でソクラテス式問答

### 学習ノートの蓄積
- 新しい記号は必ず `glossary/symbol_reference.md` に追記
- 新しい英語用語は `glossary/jp_en_terms.md` に追記
- 自分なりの気付きは `notebooks/` に書き留める

## 「合格ライン」の例

各 Phase 終了時に以下ができれば合格:

- Phase −1: 真っ黒な画面が怖くない。`uv run lab.py` を打って、Jupyter を立ち上げられる
- Phase 0: 「数学って実生活のここに居るんだ」と少なくとも3つ例を挙げられる
- Phase 1: 論文を読んで「記号で詰まる」が消える
- Phase 2: `np.linalg.solve` `np.linalg.eig` を自分の問題に使える
- Phase 3: 勾配降下法のコードを写経でなく自分で書ける
- Phase 4: 「サイコロの期待値は 3.5」を式と Python の両方で示せる
- Phase 5: 学習率を変えると収束がどう変わるか実験できる
- Phase 6: 線形回帰を NumPy だけで実装できる
- Phase 7: 同じ線形回帰を **JAX で再実装** し、勾配導出を `jax.value_and_grad` に置き換えられる

## ゴール後

ここまで終わったら:
- 機械学習の入門書（『パターン認識と機械学習』『深層学習』）に挑戦できる
- arXiv の論文を Abstract レベルで読み解ける
- 生成AIに ML 関連のコードを書かせて、出てきた数式を検算できる
- **JAX + Flax** で簡単なニューラルネットワークを書けるレベルへ進める
- Google DeepMind や Anthropic 由来の研究コードを読み解ける
