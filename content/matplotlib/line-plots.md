Title: Line Plots
Slug: matplotlib/line-plots
Category: Matplotlib
Tags: date_range, DataFrame, figure, plot, xlabel, ylabel, xticks, legend, show
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
index = pd.date_range('2017-09-18', '2017-09-22')
data = {
    'Company A': [66.78, 69.70, 71.59, 71.44, 72.15],
    'Company B': [90.98, 89.12, 85.47, 82.33, 84.66],
    'Company C': [55.10, 56.88, 57.49, 65.76, 71.25]
}
df = pd.DataFrame(data=data, index=index)
df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Company A</th>
      <th>Company B</th>
      <th>Company C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-09-18</th>
      <td>66.78</td>
      <td>90.98</td>
      <td>55.10</td>
    </tr>
    <tr>
      <th>2017-09-19</th>
      <td>69.70</td>
      <td>89.12</td>
      <td>56.88</td>
    </tr>
    <tr>
      <th>2017-09-20</th>
      <td>71.59</td>
      <td>85.47</td>
      <td>57.49</td>
    </tr>
    <tr>
      <th>2017-09-21</th>
      <td>71.44</td>
      <td>82.33</td>
      <td>65.76</td>
    </tr>
    <tr>
      <th>2017-09-22</th>
      <td>72.15</td>
      <td>84.66</td>
      <td>71.25</td>
    </tr>
  </tbody>
</table>
</div>



#### Plot the data


```python
fig = plt.figure(figsize=(8,5))

plt.plot(df.index, df['Company A'])
plt.plot(df.index, df['Company B'])
plt.plot(df.index, df['Company C'])

plt.xlabel('Date')
plt.ylabel('Value')
x_labels = df.index.strftime('%d %b %Y')
plt.xticks(df.index, x_labels)
plt.legend(loc='lower right')
plt.show()
```


![png](line-plots_files/line-plots_6_0.png)

