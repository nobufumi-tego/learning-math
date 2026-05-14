---
name: feedback-jupyter-first
description: leaning-math プロジェクトでは各章のサンプル実行は Jupyter Lab を主とし、CLIが分からない人向けの案内を必ず冒頭に置く
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 46859aa3-5076-4b04-98c3-795608e48b12
---

leaning-math プロジェクトでは、各章のサンプル実行は **Jupyter Lab を主**、`.py` の CLI 実行を副、として設計する。

## 各章 md の冒頭に必ず置く要素
1. **「💡 このページのコードを動かすには」ボックス**
2. `uv run lab.py` のコマンド
3. 該当 `<章>/notebooks/<該当>.ipynb` のファイルツリー上のパス
4. **🐧 CLI/uv が分からない人** への [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) 誘導
5. **数学の前提が不安な人** への [`start_here/`](../start_here/README.md) や [`00_notation/`](../00_notation/README.md) 誘導

## ディレクトリ構造
各章には:
- `examples/*.py` — CLI 実行用 (副)
- `notebooks/*.ipynb` — Jupyter で対話的 (主、ipywidgets でスライダー)

## Why
ユーザーが「各章のサンプル実行は Jupyter lab を使ってください」「それを理解できてない人向けに、その章のリンク案内や、CLIでの最低限の操作解説をし、そのための基礎知識理解を促す」と明示的に要望。

学習者を**置き去りにしない**ことが本リポジトリの大原則。

## How to apply
- 新しい章を書くときは必ず冒頭ボックスを置く
- AGENTS.md と `.claude/rules/teaching-style.md` にテンプレートが明文化
- 既存章 (00_notation, 07_jax) も将来同じ形に揃える余地あり
- 関連: [[user-math-learner]], [[feedback-baby-steps-and-columns]], [[feedback-pet-terminal-chapter]]
