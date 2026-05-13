---
description: 数学的概念を matplotlib + ipywidgets で可視化するコードを生成
---

対象: `{{args}}`

Jupyter Lab で動かせる対話的な可視化コードを生成してください。

## 必須要素
- `%matplotlib inline`
- 型ヒント + shape コメント
- `interact()` でスライダー付き
- 軸ラベル・タイトル日本語
- `ax.grid(True, alpha=0.3)`

## テンプレート

```python
import math
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider
%matplotlib inline

def plot_<name>(<params>) -> None:
    \"\"\"<説明>.\"\"\"
    ...
    fig, ax = plt.subplots(figsize=(10, 4))
    ...
    ax.set_xlabel(...)
    ax.set_ylabel(...)
    ax.set_title(...)
    ax.grid(True, alpha=0.3)
    plt.show()

interact(plot_<name>, ...)
```

ユーザーが希望すれば `start_here/notebooks/<topic>.ipynb` に保存。
