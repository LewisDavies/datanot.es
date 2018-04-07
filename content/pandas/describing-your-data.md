Title: Describing Your Data
Slug: pandas/describing-your-data
Category: Pandas
Tags: info, describe, max, min, sum, count, mean, median, std, corr
Date: 2017-08-05
Modified: 2017-08-05

#### Import libraries


```python
import pandas as pd
```

#### Create DataFrame


```python
data = {'name': ['Theresa', 'David', 'Gordon', 'Tony', 'John'],
        'colour': ['Blue', 'Blue', 'Red', 'Red', 'Blue'],
        'score1': [1, 5, 5, 3, 5],
        'score2': [None, 3, 7, 5, 7],
        'score3': [None, 5, 6, 9, None]}

df = pd.DataFrame(data)
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
      <td>9.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Blue</td>
      <td>John</td>
      <td>5</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### DataFrame information


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5 entries, 0 to 4
    Data columns (total 5 columns):
    colour    5 non-null object
    name      5 non-null object
    score1    5 non-null int64
    score2    4 non-null float64
    score3    3 non-null float64
    dtypes: float64(2), int64(1), object(2)
    memory usage: 280.0+ bytes
    

#### Basic DataFrame statistics


```python
df.describe()
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.800000</td>
      <td>5.500000</td>
      <td>6.666667</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.788854</td>
      <td>1.914854</td>
      <td>2.081666</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.000000</td>
      <td>4.500000</td>
      <td>5.500000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.000000</td>
      <td>7.000000</td>
      <td>7.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.000000</td>
      <td>7.000000</td>
      <td>9.000000</td>
    </tr>
  </tbody>
</table>
</div>



#### Maximum values


```python
df.max()
```




    colour     Red
    name      Tony
    score1       5
    score2       7
    score3       9
    dtype: object



#### Minimum values


```python
df.min()
```




    colour     Blue
    name      David
    score1        1
    score2        3
    score3        5
    dtype: object



#### Sum of values


```python
df.sum()
```




    colour            BlueBlueRedRedBlue
    name      TheresaDavidGordonTonyJohn
    score1                            19
    score2                            22
    score3                            20
    dtype: object



#### Count non-null values


```python
df.count()
```




    colour    5
    name      5
    score1    5
    score2    4
    score3    3
    dtype: int64



#### Mean values


```python
df.mean()
```




    score1    3.800000
    score2    5.500000
    score3    6.666667
    dtype: float64



#### Median values


```python
df.median()
```




    score1    5.0
    score2    6.0
    score3    6.0
    dtype: float64



#### Standard deviation of values


```python
df.std()
```




    score1    1.788854
    score2    1.914854
    score3    2.081666
    dtype: float64



#### Correlation matrix


```python
df.corr()
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>score1</th>
      <td>1.000000</td>
      <td>0.174078</td>
      <td>-0.970725</td>
    </tr>
    <tr>
      <th>score2</th>
      <td>0.174078</td>
      <td>1.000000</td>
      <td>0.240192</td>
    </tr>
    <tr>
      <th>score3</th>
      <td>-0.970725</td>
      <td>0.240192</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>


