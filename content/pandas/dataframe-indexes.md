Title: DataFrame Indexes
Slug: pandas/dataframe-index
Category: Pandas
Tags: DataFrame, set_index, loc, drop, xs
Date: 2017-10-04
Modified: 2017-10-04

#### Import libraries


```python
import pandas as pd
```

#### Generate data


```python
data = {
    'country': ['UK', 'Canada', 'UK', 'USA', 'France', 'USA', 'Canada'],
    'city': ['London', 'London', 'Birmingham', 'Birmingham', 'Paris', 'Paris', 'Paris'],
    'population': [8788000, 389000, 1101000, 212000, 2244000, 25000, 12000]
}

df0 = pd.DataFrame(data)
df0
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
      <th>city</th>
      <th>country</th>
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>London</td>
      <td>UK</td>
      <td>8788000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>London</td>
      <td>Canada</td>
      <td>389000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Birmingham</td>
      <td>UK</td>
      <td>1101000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Birmingham</td>
      <td>USA</td>
      <td>212000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Paris</td>
      <td>France</td>
      <td>2244000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Paris</td>
      <td>USA</td>
      <td>25000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Paris</td>
      <td>Canada</td>
      <td>12000</td>
    </tr>
  </tbody>
</table>
</div>



#### Set a new index
If an index is not specified, Pandas will give each row an integer label starting from 0. We can set `city` as the index, but ideally our indexes should be unique.


```python
df1 = df0.set_index('city')
df1
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
      <th>country</th>
      <th>population</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>London</th>
      <td>UK</td>
      <td>8788000</td>
    </tr>
    <tr>
      <th>London</th>
      <td>Canada</td>
      <td>389000</td>
    </tr>
    <tr>
      <th>Birmingham</th>
      <td>UK</td>
      <td>1101000</td>
    </tr>
    <tr>
      <th>Birmingham</th>
      <td>USA</td>
      <td>212000</td>
    </tr>
    <tr>
      <th>Paris</th>
      <td>France</td>
      <td>2244000</td>
    </tr>
    <tr>
      <th>Paris</th>
      <td>USA</td>
      <td>25000</td>
    </tr>
    <tr>
      <th>Paris</th>
      <td>Canada</td>
      <td>12000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Returns two results - not ideal!
df1.loc['London']
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
      <th>country</th>
      <th>population</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>London</th>
      <td>UK</td>
      <td>8788000</td>
    </tr>
    <tr>
      <th>London</th>
      <td>Canada</td>
      <td>389000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df0.set_index(df0['city'] + ', ' + df0['country']).drop(['city', 'country'], axis=1)
df2
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
      <th>population</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>London, UK</th>
      <td>8788000</td>
    </tr>
    <tr>
      <th>London, Canada</th>
      <td>389000</td>
    </tr>
    <tr>
      <th>Birmingham, UK</th>
      <td>1101000</td>
    </tr>
    <tr>
      <th>Birmingham, USA</th>
      <td>212000</td>
    </tr>
    <tr>
      <th>Paris, France</th>
      <td>2244000</td>
    </tr>
    <tr>
      <th>Paris, USA</th>
      <td>25000</td>
    </tr>
    <tr>
      <th>Paris, Canada</th>
      <td>12000</td>
    </tr>
  </tbody>
</table>
</div>



#### Multilevel indexes
Since each country-city combination is unique in our dataset, this pairing makes a good mulitlevel index. First we reset the index to it's original state, then set our new index.


```python
df3 = df0.set_index(['country', 'city'])
df3
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
      <th></th>
      <th>population</th>
    </tr>
    <tr>
      <th>country</th>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>UK</th>
      <th>London</th>
      <td>8788000</td>
    </tr>
    <tr>
      <th>Canada</th>
      <th>London</th>
      <td>389000</td>
    </tr>
    <tr>
      <th>UK</th>
      <th>Birmingham</th>
      <td>1101000</td>
    </tr>
    <tr>
      <th>USA</th>
      <th>Birmingham</th>
      <td>212000</td>
    </tr>
    <tr>
      <th>France</th>
      <th>Paris</th>
      <td>2244000</td>
    </tr>
    <tr>
      <th>USA</th>
      <th>Paris</th>
      <td>25000</td>
    </tr>
    <tr>
      <th>Canada</th>
      <th>Paris</th>
      <td>12000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Slicing at the top level of the index
df3.loc['UK']
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
      <th>population</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>London</th>
      <td>8788000</td>
    </tr>
    <tr>
      <th>Birmingham</th>
      <td>1101000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Slicing at both levels of the index
df3.loc[[('USA', 'Birmingham')]]
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
      <th></th>
      <th>population</th>
    </tr>
    <tr>
      <th>country</th>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>USA</th>
      <th>Birmingham</th>
      <td>212000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Slicing at a lower index level
df3.xs('Paris', level=1)
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
      <th>population</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>France</th>
      <td>2244000</td>
    </tr>
    <tr>
      <th>USA</th>
      <td>25000</td>
    </tr>
    <tr>
      <th>Canada</th>
      <td>12000</td>
    </tr>
  </tbody>
</table>
</div>


