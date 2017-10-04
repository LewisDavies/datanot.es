Title: Filtering Data
Slug: pandas/filtering-data
Category: Pandas
Tags: DataFrame, loc, query
Date: 2017-08-05
Modified: 2017-10-04

#### Import libraries


```python
import pandas as pd
```

#### Create DataFrame


```python
data = {
    'name': ['Theresa', 'David', 'Gordon', 'Tony', 'John'],
    'colour': ['Blue', 'Blue', 'Red', 'Red', 'Blue'],
    'score1': [1, 5, 5, 3, 5],
    'score2': [None, 3, 7, 5, 7],
    'score3': [None, 5, 6, 9, None]
}

df = pd.DataFrame(data)
df
```




<div>
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
We can select columns with simple square brackets if we don't want to filter our data, as in the first example. However, the `.loc` accessor allows filtering at the same time.

After this example, we'll use `.loc` for the sake of consistency and flexibility.


```python
df[['name', 'colour']]
```




<div>
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




```python
# We don't want to filter any rows so we select them all with a colon
df.loc[:, ['name', 'colour']]
```




<div>
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



#### Filter rows on values in a column


```python
df.loc[df['score1'] >= 3]
```




<div>
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



#### Two ways of filtering on multiple columns


```python
df.loc[(df['score1'] >= 3) & (df['score2'] >= 5)]
```




<div>
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




```python
# With .query, variables can be referenced with @variable_name
minimum = 5
df.query('score1 >= 3 and score2 >= @minimum')
```




<div>
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



#### Return a Series as a DataFrame
If your result is a Pandas Series, it can look a bit naff when it is returned. Wrap your columns in a list to return a DataFrame instead and it'll be nicely formatted.


```python
df.loc[:, ['name']]
```




<div>
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
