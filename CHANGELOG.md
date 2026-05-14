# 📋 更新履歴 (Changelog)

> ⚙️ **このファイルは自動生成されます**
> 
> [`scripts/generate_changelog.py`](scripts/generate_changelog.py) が [`.github/workflows/changelog.yml`](.github/workflows/changelog.yml) によって **`main` への push 毎に自動実行** され、git コミット履歴から再生成されます。
> 
> 手動で編集しないでください (上書きされます)。コミットメッセージは [Conventional Commits](https://www.conventionalcommits.org/ja/) に準拠することを推奨します。

---

## 2026-05-14

### ✨ 新機能・新規追加

- `17386ff` feat(jupyter): repo 同梱の JupyterLab 設定 + lab.py ランチャー
- `e0435ad` feat(02_calculus): 微積分章を完成 (5サブ章 + 5ノートブック)
- `f98bbd1` feat(latex): 02_calculus の数式を LaTeX (MathJax) 化
- `bf0df17` feat(03_probability): 確率・統計章を LaTeX 形式で完成 (4章 + 4ノート)
- `a30073e` feat(latex): 01_linear_algebra と 07_jax の主要数式を LaTeX 化
- `6a46a58` feat(latex-nb): 既存 12 ノートブックの markdown セルに LaTeX 数式を併記
- `b0dc510` feat(ch5-6): 05_optimization と 06_ml_math_bridge 章を完成
- `e668d37` feat(ch4): 04_discrete_math 章を完成 (3サブ章 + 3ノート)
- `3dbba76` feat(appendix): 章別おすすめ書籍・Web リソース集を追加
- `b1448ef` feat(setup): リポ取得後ワンショットで Jupyter Lab を起動するスクリプトを追加
- `e840a3b` feat(setup): Windows ダブルクリック起動の start.bat を追加
- `b3f1db7` feat(launch): start スクリプトで README.md を JupyterLab に自動オープン
- `c743b1c` feat(deps): matplotlib の日本語豆腐化対策に japanize-matplotlib を追加

### 🐛 バグ修正

- `c996d60` fix(docs): pet_terminal README の「例」を実際の見栄えで表示
- `ae2bf28` fix(bayes): underbrace+日本語 text の LaTeX 崩れを修正
- `94e8fa2` fix(setup): Windows 起動スクリプトのエンコード問題を解消
- `d881292` fix(notebooks): matplotlib 使用 22 notebook に japanize_matplotlib 追加

### 📝 ドキュメント

- `5ae486d` docs(nav): 各章末にナビゲーションブロックを追加 + ファイル名のリンク化規約
- `d2dc590` docs(readme): ROOT README を全章ドキュメントへの導線ハブに再構築
- `7a2587a` docs(nav): ナビブロックを 4 カラムに拡張 (📚 全体 TOP リンクを追加)
- `fb6c793` docs(notebooks): 全ノートブックに二段ナビを実装
- `ee326ef` docs(jupyter): Jupyter Lab の停止方法を 3 か所に追加
- `b7b9680` docs(jupyter): 英語ダイアログ翻訳ガイドを追加
- `1a7dd6c` docs(setup): ZIP ダウンロード手順を追加 + 動作検証済み
- `73f6b31` docs(git): チャレンジ章「Git 入門」を新規追加
- `7c2a824` docs(cli): 全 CLI 解説に PowerShell 例を併記
- `f9675fd` docs(readme): トップに Appendix への案内を追加
- `dac5b71` docs(appendix): コラム「AIがコードを書く時代に大学院生はどう学ぶか」追加
- `a34f517` docs(chapters): 各章 README にコラム「AI時代の大学院生の学び方」へのリンク追加
- `75ac7a8` docs(disclaimer): 未検証教材としての免責事項を全章に明示
- `44fa470` docs(license): デュアルライセンス導入 (Code: MIT, Docs: CC BY-NC-SA 4.0)
- `504137f` docs(license): 各章 README にライセンスバナー追加 + 連絡先 email 追加
- `c265a59` docs(disclaimer): 連絡先から email を削除し GitHub チャネルに一本化
- `405fb31` docs(readme): ライセンス記述をデュアルライセンスに統一
- `7b36eda` docs(launch): 各章 README にワンショット起動方法 (start.bat/sh/ps1) を反映
- `2666517` docs(readme): ZIP 展開手順を OS 別に追加 (初心者の最大つまずき対策)
- `f2d568f` docs(setup): 初回起動の待ち時間と進捗の見方を明示
- `e52388e` docs(launch): 各章 README の起動方法ブロックに待ち時間注意を追加
- `cdf2b39` docs(jupyter): JupyterLab 完全ビギナーガイドを新設 + 全所からリンク
- `690a9f6` docs(jupyter): 残り 2 章 (00_notation, 07_jax) にも JupyterLab ガイドリンク追加
- `83c84bb` docs(jupyter): セルが [*] で止まる症状を WebSocket 切れ視点で詳解

### 🤖 CI/CD

- `e130b90` ci(changelog): CHANGELOG 自動生成 (GitHub Actions + git log)

### 🔧 その他の整備

- `78f7681` chore(gitignore): notes/ を git 管理対象外に追加
- `aa69420` chore(pyproject): license フィールド + デュアルライセンス表記を追加

### 📌 その他

- `a0b4e12` Initial commit: Leaning Math (大学院数学基礎 × Python × 生成AI)

---

_Total commits indexed: **45**_
