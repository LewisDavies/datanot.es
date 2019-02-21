Title: Pivot Tables
Slug: pandas/pivot-tables
Category: Pandas
Tags: head, pivot_table
Date: 2017-09-25
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



### Create pivot table


```python
# By default, the mean of your values is calculated
iris_df.pivot_table(
    values=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
    index='species'
)
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
      <th>petal_length</th>
      <th>petal_width</th>
      <th>sepal_length</th>
      <th>sepal_width</th>
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
      <td>1.462</td>
      <td>0.246</td>
      <td>5.006</td>
      <td>3.428</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>4.260</td>
      <td>1.326</td>
      <td>5.936</td>
      <td>2.770</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>5.552</td>
      <td>2.026</td>
      <td>6.588</td>
      <td>2.974</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Other aggregates can be specified, such as min, mix, count, mean and std
iris_df.pivot_table(
    values=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
    index='species',
    aggfunc='std'
)
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
      <th>petal_length</th>
      <th>petal_width</th>
      <th>sepal_length</th>
      <th>sepal_width</th>
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
      <td>0.173664</td>
      <td>0.105386</td>
      <td>0.352490</td>
      <td>0.379064</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>0.469911</td>
      <td>0.197753</td>
      <td>0.516171</td>
      <td>0.313798</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>0.551895</td>
      <td>0.274650</td>
      <td>0.635880</td>
      <td>0.322497</td>
    </tr>
  </tbody>
</table>
</div>




```python
# We can add margins=True to apply our chosen aggfunc to the pivot table
iris_df.pivot_table(
    values=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
    index='species',
    aggfunc='max',
    margins=True
)
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
      <th>petal_length</th>
      <th>petal_width</th>
      <th>sepal_length</th>
      <th>sepal_width</th>
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
      <td>1.9</td>
      <td>0.6</td>
      <td>5.8</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>versicolor</th>
      <td>5.1</td>
      <td>1.8</td>
      <td>7.0</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>virginica</th>
      <td>6.9</td>
      <td>2.5</td>
      <td>7.9</td>
      <td>3.8</td>
    </tr>
    <tr>
      <th>All</th>
      <td>6.9</td>
      <td>2.5</td>
      <td>7.9</td>
      <td>4.4</td>
    </tr>
  </tbody>
</table>
</div>


