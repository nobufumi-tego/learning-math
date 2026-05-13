---
name: feedback-jax-dual-form
description: leaning-math プロジェクトでは Python コードを「標準形式 (NumPy/SymPy) + JAX形式」の2つで併記する
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 46859aa3-5076-4b04-98c3-795608e48b12
---

leaning-math プロジェクトでは、Python の数式コードを必ず以下の2形式で併記する:

1. **標準形式**: NumPy / SymPy / SciPy で書く（数式 → コード対応が直感的）
2. **JAX形式**: `jax.numpy`, `jax.grad`, `jit`, `vmap` を使う（自動微分・高速化）

**Why:** ユーザーは数学を学んで最終的に最先端の ML 研究コード（JAX を使う Gemini, AlphaFold 系）を読めるようになりたい。標準形式で「数式とコードの対応」を体得した上で JAX に進む方が学習効率が高い、というユーザーの方針。

**How to apply:**
- 各章の `examples/` には `xxx.py`（標準形式）と `xxx_jax.py`（JAX形式）を併置
- 説明・回答時は「順序」が大事: 標準形式を先、JAX形式を後
- 計算が主目的でない場合（記号解説、SymPy記号計算、組合せ列挙など）は JAX 形式を省略してよい
- JAX の入門は `07_jax/` 章にまとまっているので、そこを参照
- AGENTS.md と `.claude/rules/teaching-style.md` にこのルールが明文化されている
- 関連: [[user-math-learner]]
