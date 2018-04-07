Title: Selecting Rows and Cells
Slug: pandas/selecting-rows-and-cells
Category: Pandas
Tags: DataFrame, loc, iloc
Date: 2017-08-05
Modified: 2017-09-24

#### Import libraries


```python
import pandas as pd
```

#### Create DataFrame


```python
index = ['Theresa', 'David', 'Gordon', 'Tony', 'John']
data = {
    'colour': ['Blue', 'Blue', 'Red', 'Red', 'Blue'],
    'score1': [1, 5, 5, 3, 5],
    'score2': [None, 3, 7, 5, 7],
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
      <td>Blue</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>3</td>
      <td>5.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### Select columns
We can provide a single column name, a list, or a slice.


```python
df[['colour', 'score1']]
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Theresa</th>
      <td>Blue</td>
      <td>1</td>
    </tr>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>3</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



#### Select rows and cells by label


```python
df.loc['Theresa']
```




    colour    Blue
    score1       1
    score2     NaN
    score3     NaN
    Name: Theresa, dtype: object




```python
# Slices can be used to select a range of rows
df.loc['David':'Tony']
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
      <td>5</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>Gordon</th>
      <td>Red</td>
      <td>5</td>
      <td>7.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>Tony</th>
      <td>Red</td>
      <td>3</td>
      <td>5.0</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# We can filter columns with a second argument
df.loc['David':'Tony', 'score1']
```




    David     5
    Gordon    5
    Tony      3
    Name: score1, dtype: int64




```python
# Lists can also be used for this
df.loc[['David', 'John'], ['colour', 'score3']]
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
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Single cells can be selected
df.loc['Theresa', 'colour']
```




    'Blue'



#### Select by position
We can use `iloc` to look up data based on integers. For example, here we repeat the two selections directly above.


```python
df.iloc[[1, 4], [0, 3]]
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
      <th>score3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>David</th>
      <td>Blue</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>John</th>
      <td>Blue</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[0, 0]
```




    'Blue'


