Title: Selecting and Filtering Data
Slug: pandas/selecting-and-filtering-data
Category: Pandas
Tags: loc, iloc
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



#### Limit column selection


```python
df[['name', 'colour']]
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
      <th>name</th>
      <th>colour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Theresa</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>1</th>
      <td>David</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Gordon</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tony</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>4</th>
      <td>John</td>
      <td>Blue</td>
    </tr>
  </tbody>
</table>
</div>



#### Filter on values in a column


```python
df[df['score1'] >= 3]
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



#### Filter column and limit selection


```python
df[df['score1'] >= 1][['name', 'colour']]
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
      <th>name</th>
      <th>colour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Theresa</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>1</th>
      <td>David</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Gordon</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tony</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>4</th>
      <td>John</td>
      <td>Blue</td>
    </tr>
  </tbody>
</table>
</div>



#### Return a Series as a DataFrame


```python
# We can return a single column (a Series) using double square brackets
df[['name']]
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
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Theresa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>David</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Gordon</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tony</td>
    </tr>
    <tr>
      <th>4</th>
      <td>John</td>
    </tr>
  </tbody>
</table>
</div>
