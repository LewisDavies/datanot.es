Title: Applying Categories to Continuous Data
Slug: pandas/applying-categories-to-continuous-data
Category: Pandas
Tags: describe, nunique, cut, value_counts, sort_index, floor, ceil, max, min, 
Date: 2017-09-24
Modified: 2017-09-24

#### Import libraries


```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from bokeh.sampledata.iris import flowers
```

#### Inspect data


```python
flowers.describe()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
      <td>150.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.843333</td>
      <td>3.057333</td>
      <td>3.758000</td>
      <td>1.199333</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.828066</td>
      <td>0.435866</td>
      <td>1.765298</td>
      <td>0.762238</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.300000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.100000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.100000</td>
      <td>2.800000</td>
      <td>1.600000</td>
      <td>0.300000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.800000</td>
      <td>3.000000</td>
      <td>4.350000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.400000</td>
      <td>3.300000</td>
      <td>5.100000</td>
      <td>1.800000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.900000</td>
      <td>4.400000</td>
      <td>6.900000</td>
      <td>2.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
flowers['petal_length'].nunique()
```




    43



Petal length has the biggest range, so we take a closer look at that feature. We might consider using `value_counts` if there were relatively few values, but here we have 43 distinct values across all observations.

Let's start by using 3 evenly-sized bins.


```python
pd.cut(flowers['petal_length'], bins=3).value_counts().sort_index()
```




    (0.994, 2.967]    50
    (2.967, 4.933]    54
    (4.933, 6.9]      46
    Name: petal_length, dtype: int64



That's good and all, but our bins are a bit... ugly. If we want nice and neat bins, we can pass an array instead of a single value. Here we round down to the lowest value and up to the highest, then make a list of our bin edges. Finally, we add some labels for extra pizzazz.


```python
bins_left = np.floor(flowers['petal_length'].min())
bins_right = np.ceil(flowers['petal_length'].max())

bins = [i for i in range(int(bins_left), int(bins_right)+1, 2)]
bins
```




    [1, 3, 5, 7]




```python
labels = ['Short', 'Medium', 'Long']
pd.cut(flowers['petal_length'], bins=bins, labels=labels).value_counts().sort_index(ascending=False)
```




    Short     50
    Medium    57
    Long      42
    Name: petal_length, dtype: int64



#### Life on the edge
The eagle-eyed amongst you might have noticed a slight problem with the example above: our initial cut returns 150 results, but the second only 149.

This is because we passed a list to our second cut and, by default, `pd.cut` doesn't include the lowest value of lists. Here's how to get around this.


```python
# Our example from above without labels
pd.cut(flowers['petal_length'], bins=bins).value_counts().sort_index()
```




    (1, 3]    50
    (3, 5]    57
    (5, 7]    42
    Name: petal_length, dtype: int64




```python
# With include_lowest=True, the lowest edge is expanded by 0.1% to capture all values
pd.cut(flowers['petal_length'], bins=bins, include_lowest=True).value_counts().sort_index()
```




    (0.999, 3.0]    51
    (3.0, 5.0]      57
    (5.0, 7.0]      42
    Name: petal_length, dtype: int64



If things still aren't clear, [take a look at the docs](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html) or play around with `pd.cut` yourself - it's the best way to develop your understanding!
