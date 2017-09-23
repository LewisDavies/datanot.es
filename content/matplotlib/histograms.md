Title: Histograms
Slug: matplotlib/histograms
Category: Matplotlib
Tags: random, normal, hist, show
Date: 2017-09-24
Modified: 2017-09-24

#### Import libraries


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

#### Generate some data


```python
data = np.random.normal(170, 5, 10000)
data[:5]
```




    array([ 173.89148841,  168.20440104,  166.1964813 ,  172.59987584,
            169.52490202])



#### Plot data


```python
fig = plt.hist(data, bins='auto', normed=True)
plt.show()
```


![png](../images/histograms_6_0.png)
