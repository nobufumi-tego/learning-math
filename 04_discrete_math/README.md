# 04. 離散数学 (Discrete Mathematics)

> ⚠️ **未検証の個人学習教材**: 本章は AI 協働で作成され、専門家の監修を受けていません。誤りを含む可能性があるため、必ず一次情報源で検証してください ([詳細](../DISCLAIMER.md))。
> 📜 **ライセンス**: 文書 [CC BY-NC-SA 4.0](../LICENSE-DOCS) / コード [MIT](../LICENSE-CODE) — 商用利用 (書籍化・有料講座・企業研修等) は[要相談](../DISCLAIMER.md#-商用利用について--commercial-use)

**ゴール**: 命題論理・証明技法・組合せ論の基礎を理解する。
他の章ほど直接 ML には出てこないが、**論文の証明を読む素養**として有用。

## なぜ学ぶか
- 論文の「Theorem」「Lemma」「Proof」を読み解くため
- アルゴリズムの正しさを示す論法（数学的帰納法など）に慣れるため
- 計算量・組合せ数を扱うため

---

## 💡 動かす前に

このフォルダのコードは **Jupyter Lab** で対話的に動かすのが推奨です。

🚀 **起動方法** (リポジトリのルートで実行):
- 🪟 **Windows**: [`start.bat`](../start.bat) を **ダブルクリック** ⭐
- 🍎 **Mac** / 🐧 **Linux**: ターミナルで `./start.sh`
- 🪟 **PowerShell 派**: `.\start.ps1`
- 🛠️ **すでに環境がある人**: `uv run lab.py`

uv のインストールから依存関係取得、Jupyter Lab 起動まで全部自動です。

> ⏰ **初回起動は 5〜15 分かかります** (依存関係 500MB〜1GB のダウンロード)。途中で中断せず気長に待ってください。「応答なし」 と出ても OS 更新の遅延なので焦らず ☕
> 2 回目以降は 10〜20 秒で起動します。詳細は ROOT [`README.md`](../README.md#-待ち時間の目安--フリーズしてないと心配しないでください) の「待ち時間の目安」 参照。

詳細・トラブルシューティングは ROOT [`README.md`](../README.md#step-2--ワンショットスクリプトで起動-推奨) 参照。
🧪 **Jupyter Lab の使い方** (Shift+Enter でセル実行など) は [`docs/jupyter_lab_guide.md`](../docs/jupyter_lab_guide.md) を参照。

ブラウザが開いたら、左のファイルツリーから `04_discrete_math/notebooks/` を開いて、`01_logic.ipynb` から順に。

> 🐧 **「`uv` ってなに?」「ターミナルがわからない」方** は:
> - [`start_here/00_pet_terminal/`](../start_here/00_pet_terminal/README.md) — ペンタと学ぶターミナル基礎

---

## 学習ステップ

| md (解説) | ipynb (動かす) | 内容 | 所要時間 |
|---|---|---|---|
| [`01_logic.md`](01_logic.md) | [`notebooks/01_logic.ipynb`](notebooks/01_logic.ipynb) | 命題論理、真理表、ド・モルガン | 1時間 |
| [`02_proof_techniques.md`](02_proof_techniques.md) | [`notebooks/02_proof_techniques.ipynb`](notebooks/02_proof_techniques.ipynb) | 直接証明、背理法、帰納法 | 2時間 |
| [`03_combinatorics.md`](03_combinatorics.md) | [`notebooks/03_combinatorics.ipynb`](notebooks/03_combinatorics.ipynb) | 順列・組合せ・二項係数・パスカル | 1.5時間 |

各 md は読み物、各 ipynb は手を動かす場所。**両方をペアで進めるのが効果的**です。

## キーとなる Python ツール

```python
import math
from itertools import permutations, combinations

# n!
math.factorial(5)              # 120

# 組合せ ₙCₖ
math.comb(5, 2)                # 10

# 順列 ₙPₖ
math.perm(5, 2)                # 20

# 全順列を列挙
list(permutations([1, 2, 3]))  # [(1,2,3), (1,3,2), ...]

# 全組合せを列挙
list(combinations([1, 2, 3, 4], 2))  # [(1,2), (1,3), ...]
```

## 重要な記法

| 記号 | 読み方 | 意味 |
|---|---|---|
| $n!$ | n の階乗 | $1 \times 2 \times \dots \times n$ |
| $\binom{n}{k}$ | n choose k | n 個から k 個選ぶ組合せ数 |
| $P(n, k)$ または $_nP_k$ | n permute k | n 個から k 個並べる順列数 |
| $\land$, $\lor$, $\neg$ | AND, OR, NOT | 論理演算子 |
| $\Rightarrow$, $\Leftrightarrow$ | 含意・同値 | 論理的関係 |

組合せ数の公式:

$$
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

二項定理:

$$
(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k
$$

## ML への接続（薄め）
- 木構造の探索（決定木、ビーム探索）の計算量
- グラフ理論（GNN、知識グラフ）の基礎
- 確率分布の組合せ的な定義
- ナイーブベイズの独立性仮定 (論理)

---

## 📚 さらに学ぶ

- 📕 **[離散数学への招待](../appendix/books.md#離散数学への招待)** (Matoušek) — 体系的入門
- 📕 **[Concrete Mathematics](../appendix/books.md#concrete-mathematics)** (Knuth, Graham, Patashnik) — TAOCP の Knuth による名著
- 🌐 **[MIT 6.042 Math for CS](../appendix/online.md#mit-6042--60042-mathematics-for-computer-science)** — MIT 公開講義

- 📖 **学び方そのものを考える**: [AI がコードを書く時代に、大学院生はどう学ぶか](../appendix/columns/ai_era_grad_student.md) — 数学が苦手で AI 未経験の人向けの 5 章コラム

→ 全リソース一覧: [`appendix/`](../appendix/README.md)

---

## 📍 ナビゲーション

| ← 前 | 🏠 章 TOP | 📚 全体 TOP | 次 → |
|---|---|---|---|
| [`../07_jax/03_jit_vmap.md`](../07_jax/03_jit_vmap.md) | (このページが章 TOP) | [📚 ROOT README](../README.md) | 本リポジトリの全章を読破！[ROOT に戻る](../README.md) |

> 🎉 ここに辿り着いた方、お疲れさまでした。本リポジトリの旅は完結です。
