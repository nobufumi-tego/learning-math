# Project Memory Index (repo 同梱版)

このフォルダは **AI 学習環境の "記憶" を repo 内で配布** するためのものです。
`CLAUDE.md` から `@.claude/memory/...` で自動ロードされ、Claude Code / Gemini CLI / Codex CLI のすべてで同じ前提が共有されます。

詳細は [`docs/ai_environment_setup.md`](../../docs/ai_environment_setup.md) を参照。

## メモリ一覧（このリポジトリで蓄積された設計知）

- [User: 数学基礎の学習者の想定プロファイル](user_math_learner.md) — 数学記号が最大の壁、Python・AIと結びつけて学びたい
- [Feedback: 標準形式とJAX形式を併記](feedback_jax_dual_form.md) — 各章の examples は xxx.py + xxx_jax.py のペアで構成
- [Feedback: ベビーステップ章 + コラム + Jupyter notebook](feedback_baby_steps_and_columns.md) — start_here/ で数式ゼロから入る、歴史コラムで疲れを癒す、ipywidgets で対話的
- [Feedback: ペットと学ぶターミナル基礎章](feedback_pet_terminal_chapter.md) — CLI未経験者向けに start_here/00_pet_terminal/ をペンギンのペンタが案内
- [Feedback: Jupyter Lab 主のサンプル実行 + 冒頭の起動ガイド](feedback_jupyter_first.md) — 各章 md 冒頭に Jupyter起動ボックス、CLI/数学の前提が不安な人を該当章へ誘導
