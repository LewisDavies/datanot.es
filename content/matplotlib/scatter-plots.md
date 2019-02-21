Title: Scatter Plots
Slug: matplotlib/scatter-plots
Category: Matplotlib
Tags: random, randint, figure, scatter, xlabel, ylabel, legend, show
Date: 2017-09-24
Modified: 2017-09-24

### Import libraries


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

### Generate some data


```python
x1 = np.random.randint(100, 200, 50)
y1 = np.random.randint(1000, 10000, 50)
x2 = np.random.randint(100, 200, 50)
y2 = np.random.randint(1000, 10000, 50)
```

### Plot the data


```python
# fig = plt.hist(data, bins='auto', normed=True)

fig = plt.figure(figsize=(8,5))
plt.scatter(x1, y1, alpha=0.8, label='Group 1')
plt.scatter(x2, y2, alpha=0.8, label='Group 2')
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.legend(loc='best')
plt.show()
```


![png](scatter-plots_files/scatter-plots_6_0.png)

