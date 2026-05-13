---
description: 数学的概念を matplotlib で可視化するコードを生成し、Jupyter Lab で動かせる形にする
---

# 数学概念の可視化コマンド

対象: `$ARGUMENTS`

このトピックを **視覚的に理解できるコード** を生成してください。
出力は **Jupyter Lab で動かせる形** にし、可能なら **ipywidgets でスライダー対話的** にしてください。

## 出力フォーマット

### 1. 何を見せるか (一言)
<可視化のゴールを短く>

### 2. Jupyter Lab セル形式

以下の形式で複数のコードセルとマークダウンセルを出力:

````
[Markdown セル]
## ステップ N: <何をするか>
<短い説明>

[Python セル]
```python
import math
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider
%matplotlib inline

# 実装
...
```
````

### 3. 必須要素

- **インライン表示**: `%matplotlib inline` を含める
- **型ヒント**: 関数引数に型ヒントを書く
- **コメント**: shape や単位を必ずコメントで明記
- **対話**: `interact()` でスライダーを付け、パラメータを動かせるように
- **ラベル**: 軸ラベル・タイトルを日本語で明記
- **グリッド**: `ax.grid(True, alpha=0.3)` を付ける

### 4. 構成テンプレート

1. インポートセル
2. 静的な例 (まず固定パラメータで描画)
3. スライダーで対話的に動かす版
4. 「これを動かしてみて気付くこと」のヒント

## 例: 「sin の波」の可視化

```python
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
%matplotlib inline

def plot_sin_wave(amplitude: float, frequency: float, phase: float) -> None:
    """sin の波形を描く.

    Args:
        amplitude: 振幅
        frequency: 周波数 (Hz)
        phase: 位相 (ラジアン)
    """
    t = np.linspace(0, 1, 1000)  # 1秒分、shape: (1000,)
    y = amplitude * np.sin(2 * np.pi * frequency * t + phase)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, y, 'b-')
    ax.set_xlabel('時間 (秒)')
    ax.set_ylabel('振幅')
    ax.set_title(f'sin 波: A={amplitude}, f={frequency}Hz, φ={phase:.2f}')
    ax.grid(True, alpha=0.3)
    plt.show()

interact(
    plot_sin_wave,
    amplitude=FloatSlider(min=0.1, max=2, step=0.1, value=1),
    frequency=FloatSlider(min=1, max=10, step=0.5, value=2),
    phase=FloatSlider(min=0, max=2 * np.pi, step=0.1, value=0),
);
```

## 保存

可視化コードは、ユーザーが希望すれば:
- `start_here/notebooks/<トピック>.ipynb` として保存
- または既存の関連ノートブックに追記

JSONとしての .ipynb 構造に注意して保存してください (cells 配列、metadata 等)。
