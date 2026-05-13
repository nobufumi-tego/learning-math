---
description: 数式・数学的概念を実行可能なPythonコードに変換する
---

# 数式 → Python 変換コマンド

引数で渡された数式・数学的概念: `$ARGUMENTS`

これを**実行可能なPythonコード**に変換してください。

## 出力フォーマット（厳守）

### 1. 数式の解釈
- 数式を日本語で言語化する
- 登場する記号それぞれの意味を箇条書きで列挙
- 入力と出力が何かを明確にする

### 2. 直感的な説明
- この数式は何をしているか
- どんな値が返ってくるか

### 3. Python 実装（複数アプローチ）
- **アプローチA**: NumPy（数値計算）
- **アプローチB**: SymPy（記号計算、必要なら）
- 必要に応じて SciPy / 標準ライブラリ

各コードは:
- 型ヒント付き
- docstring 付き
- shape / 単位 / 次元のコメント付き
- そのまま `uv run python` で実行可能

### 4. 検証
- 既知の入力でテストする例
- 期待される出力との比較

### 5. ハマりポイント
- 数値誤差
- shape の不一致
- 発散・特異点
- 同じ記号の意味の揺れ

## コード例の構造

```python
"""<数式の説明>."""
from __future__ import annotations

import numpy as np


def compute_something(x: np.ndarray) -> np.ndarray:
    """<数式の言語化>.

    Args:
        x: 入力ベクトル。shape: (n,)

    Returns:
        計算結果。shape: (...)
    """
    # 計算ステップ1: <何をしているか>
    ...
    return result


if __name__ == "__main__":
    # 小さい具体例で検証
    x = np.array([1.0, 2.0, 3.0])  # shape: (3,)
    print(compute_something(x))
```
