Title: DataFrame Aggregates
Slug: pandas/dataframe-aggregates
Category: Pandas
Tags: aggregates, max, min, sum, count, mean, median
Date: 2017-08-03
Modified: 2017-08-03

# Aggregates


```python
import pandas as pd
```


```python
data = {'name': ['Theresa', 'David', 'Gordon', 'Tony', 'John'],
        'colour': ['Blue', 'Blue', 'Red', 'Red', 'Blue'],
        'score1': [1, 5, 5, 3, 5],
        'score2': [None, 3, 7, 5, 7],
        'score3': [None, 5, 6, None, 9]}

df = pd.DataFrame(data)
```


```python
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
      <th>colour</th>
      <th>name</th>
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Blue</td>
      <td>Theresa</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Blue</td>
      <td>David</td>
      <td>5</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Red</td>
      <td>Gordon</td>
      <td>5</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Red</td>
      <td>Tony</td>
      <td>3</td>
      <td>5.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Blue</td>
      <td>John</td>
      <td>5</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.max()
```




    colour     Red
    name      Tony
    score1       5
    score2       7
    score3       9
    dtype: object




```python
df.min()
```




    colour     Blue
    name      David
    score1        1
    score2        3
    score3        5
    dtype: object




```python
df.sum()
```




    colour            BlueBlueRedRedBlue
    name      TheresaDavidGordonTonyJohn
    score1                            19
    score2                            22
    score3                            20
    dtype: object




```python
df.count()
```




    colour    5
    name      5
    score1    5
    score2    4
    score3    3
    dtype: int64




```python
df.mean()
```




    score1    3.800000
    score2    5.500000
    score3    6.666667
    dtype: float64




```python
df.median()
```




    score1    5.0
    score2    6.0
    score3    6.0
    dtype: float64




```python

```
