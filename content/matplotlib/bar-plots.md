Title: Bar Plots
Slug: matplotlib/bar-plots
Category: Matplotlib
Tags: random, normal, plot, xlabel, ylabel, xticks, ylim, show
Date: 2017-09-19
Modified: 2017-09-24

### Import libraries


```python
import pandas as pd
import matplotlib.pyplot as plt
```

### Generate some data


```python
index = ['Gary', 'Philippa', 'Norman', 'Susie']
data = {'height': [183, 175, 160, 155]}

df = pd.DataFrame(data=data, index=index)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Gary</th>
      <td>183</td>
    </tr>
    <tr>
      <th>Philippa</th>
      <td>175</td>
    </tr>
    <tr>
      <th>Norman</th>
      <td>160</td>
    </tr>
    <tr>
      <th>Susie</th>
      <td>155</td>
    </tr>
  </tbody>
</table>
</div>



### Plot the data


```python
fig = df.plot(kind='bar', figsize=(8,5))
plt.xlabel('Name')
plt.ylabel('Height (cm)')
# Labels are displayed vertically without this line
plt.xticks(rotation=0)
# Trim the y-axis for greater detail
plt.ylim(100,)
plt.show()
```


![png](bar-plots_files/bar-plots_6_0.png)

