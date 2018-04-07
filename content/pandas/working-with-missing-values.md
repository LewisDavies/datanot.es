Title: Working with Missing Values
Slug: pandas/working-with-missing-values
Category: Pandas
Tags: DataFrame, dropna,  
Date: 2017-12-05
Modified: 2017-12-05

#### Import libraries


```python
import numpy as np
import pandas as pd
```

#### Create data


```python
index = ['Theresa', 'David', 'Gordon', 'Tony', 'John']
data = {
    'colour': [None, 'Blue', 'Red', 'Red', 'Blue'],
    'score1': [None, 5, 5, None, 5],
    'score2': [None, 3, 7, None, 7],
    'score3': [None, 5, 6, 9, None]
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
      <th>colour</th>
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Theresa</th>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### Finding missing data and filtering


```python
df.isnull()
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Theresa</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>David</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>John</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[df["colour"].notnull()]
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### Filling missing data


```python
df.fillna("missing")
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Theresa</th>
      <td>missing</td>
      <td>missing</td>
      <td>missing</td>
      <td>missing</td>
    </tr>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>missing</td>
      <td>missing</td>
      <td>9</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5</td>
      <td>7</td>
      <td>missing</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.fillna(method="ffill")
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Theresa</th>
      <td>None</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
filler = df[["score1", "score2", "score3"]].mean()
df.fillna(filler)
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Theresa</th>
      <td>None</td>
      <td>5.0</td>
      <td>5.666667</td>
      <td>6.666667</td>
    </tr>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>3.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5.0</td>
      <td>7.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>5.0</td>
      <td>5.666667</td>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>7.000000</td>
      <td>6.666667</td>
    </tr>
  </tbody>
</table>
</div>



#### Dropping missing data


```python
df.dropna(how="any")
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.dropna(how="all")
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
      <th>score1</th>
      <th>score2</th>
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### Including missing data when counting values


```python
df["score1"].value_counts(dropna=False)
```




     5.0    3
    NaN     2
    Name: score1, dtype: int64



#### Equality of missing data
When working with missing data, you'll probably see `NaN` fairly often. It's important to know that this value, which comes from the Numpy library, is not the same as `None` as found in vanilla Python.


```python
type(None)
```




    NoneType




```python
type(np.nan)
```




    float




```python
None == np.nan
```




    False


