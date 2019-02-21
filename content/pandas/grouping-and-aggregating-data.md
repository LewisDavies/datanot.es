Title: Grouping and Aggregating Data
Slug: pandas/grouping-and-aggregating-data
Category: Pandas
Tags: head, describe, groupby, mean, nunique, agg
Date: 2017-09-24
Modified: 2019-02-20

### Import libraries


```python
import pandas as pd
import seaborn as sns

# Mac users who get an error: go to Python in your applications folder and click Install Certificates
iris_df = sns.load_dataset("iris")
```

### Inspect data


```python
iris_df.head()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>setosa</td>
    </tr>
  </tbody>
</table>
</div>



### Grouping data
We use the `groupby()` method with a column name to, you guessed it, group our data. This returns a `DataFrameGroupBy` object.


```python
iris_df.groupby('species')
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x1164540f0>



To use this object, we need to chain another method afterwards. This usually an aggregate of some kind.


```python
iris_df.groupby('species').mean()
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
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>5.006</td>
      <td>3.428</td>
      <td>1.462</td>
      <td>0.246</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>5.936</td>
      <td>2.770</td>
      <td>4.260</td>
      <td>1.326</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>6.588</td>
      <td>2.974</td>
      <td>5.552</td>
      <td>2.026</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Find the 36th percentiles
iris_df.groupby('species').quantile(0.36)
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
      <th>0.36</th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>4.9</td>
      <td>3.3</td>
      <td>1.400</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>5.7</td>
      <td>2.7</td>
      <td>4.100</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>6.3</td>
      <td>2.8</td>
      <td>5.264</td>
      <td>1.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Use .agg to find multiple aggreagates
iris_df.groupby('species').agg(['var', 'std'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">sepal_length</th>
      <th colspan="2" halign="left">sepal_width</th>
      <th colspan="2" halign="left">petal_length</th>
      <th colspan="2" halign="left">petal_width</th>
    </tr>
    <tr>
      <th></th>
      <th>var</th>
      <th>std</th>
      <th>var</th>
      <th>std</th>
      <th>var</th>
      <th>std</th>
      <th>var</th>
      <th>std</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>0.124249</td>
      <td>0.352490</td>
      <td>0.143690</td>
      <td>0.379064</td>
      <td>0.030159</td>
      <td>0.173664</td>
      <td>0.011106</td>
      <td>0.105386</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>0.266433</td>
      <td>0.516171</td>
      <td>0.098469</td>
      <td>0.313798</td>
      <td>0.220816</td>
      <td>0.469911</td>
      <td>0.039106</td>
      <td>0.197753</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>0.404343</td>
      <td>0.635880</td>
      <td>0.104004</td>
      <td>0.322497</td>
      <td>0.304588</td>
      <td>0.551895</td>
      <td>0.075433</td>
      <td>0.274650</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Find different aggreagates for different columns
iris_df.groupby('species').agg({
    'sepal_length': ['min', 'max'],
    'sepal_width': ['count']
})

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">sepal_length</th>
      <th>sepal_width</th>
    </tr>
    <tr>
      <th></th>
      <th>min</th>
      <th>max</th>
      <th>count</th>
    </tr>
    <tr>
      <th>species</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>setosa</th>
      <td>4.3</td>
      <td>5.8</td>
      <td>50</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>4.9</td>
      <td>7.0</td>
      <td>50</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>4.9</td>
      <td>7.9</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>


