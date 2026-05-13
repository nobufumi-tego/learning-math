---
name: feedback-baby-steps-and-columns
description: leaning-math プロジェクトには start_here/ 入口、数式ゼロの説明、コラム読み物、Jupyter notebookによる対話学習を入れる
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 46859aa3-5076-4b04-98c3-795608e48b12
---

leaning-math プロジェクトでは、**学習体験の質**を高めるため以下を組み込む:

1. **start_here/ 章** — 数学を全く知らない/苦手意識のある人向けの入口
2. **数式ゼロの説明** — `/project:teach-baby` コマンドで起動。たとえ話のみで説明
3. **コラム欄** (`start_here/columns/`) — 歴史・偉人エピソード・現代の使われ方を読み物風に
4. **Jupyter notebook** (`start_here/notebooks/`) — ipywidgets でスライダー対話的に遊べる
5. **クロスプラットフォーム** — Windows/Mac/Linux すべてで `uv sync && uv run jupyter lab` で起動

**Why:** ユーザー自身が「数学アレルギー」かつ「実生活で何の役に立つのか分からない」状態を表明。技術的内容だけだと読んでいて疲れるので、歴史や現代の使われ方の話を読み物として混ぜたい、という明示的なフィードバック。

**How to apply:**
- 「これを学ぶと何の役に立つのか」を常に最初に提示する
- 専門用語を出すなら必ず日常語訳をセットで
- 抽象的な定義より、具体例・絵・たとえ話を優先
- 「自明」「明らか」と言わない
- 数学的事実を書くとき、可能なら歴史的背景や現代の応用例も短く添える
- Jupyter notebook を作るときは ipywidgets でスライダー対話的に
- 関連: [[user-math-learner]], [[feedback-jax-dual-form]]

## 新規追加された CLI コマンド (Claude / Gemini 両方)
- `/project:teach-baby <概念>` — 数式ゼロのベビーステップ説明
- `/project:column <トピック>` — 歴史 + 現代の使われ方のエッセイ生成
- `/project:visualize <概念>` — matplotlib + ipywidgets の対話可視化コード生成
