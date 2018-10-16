Title: Adding, Removing & Changing Columns
Slug: pandas/adding-removing-and-changing-columns
Category: Pandas
Tags: DataFrame, dropna, 
Date: 2018-10-16
Modified: 2018-10-16

#### Import libraries


```python
import numpy as np
import pandas as pd
```

#### Create data


```python
index = ['Norman', 'Phyllis', 'Esteban', 'Maureen', 'Chiquitita']
data = {
    'Favourite Colour': ['Purple', 'Blue', 'Red', 'Mauve', 'Orange']
}

df = pd.DataFrame(data=data, index=index)
df
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
      <th>Favourite Colour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Norman</th>
      <td>Purple</td>
    </tr>
    <tr>
      <th>Phyllis</th>
      <td>Blue</td>
    </tr>
    <tr>
      <th>Esteban</th>
      <td>Red</td>
    </tr>
    <tr>
      <th>Maureen</th>
      <td>Mauve</td>
    </tr>
    <tr>
      <th>Chiquitita</th>
      <td>Orange</td>
    </tr>
  </tbody>
</table>
</div>



#### Adding new columns


```python
# Different column per row
df['City'] = ['London', 'Vancouver', 'Buenos Aires', 'Cape Town', 'Beijing']
# The same value for all columns
df['Favourite Number'] = 1
df
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
      <th>Favourite Colour</th>
      <th>City</th>
      <th>Favourite Number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Norman</th>
      <td>Purple</td>
      <td>London</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Phyllis</th>
      <td>Blue</td>
      <td>Vancouver</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Esteban</th>
      <td>Red</td>
      <td>Buenos Aires</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Maureen</th>
      <td>Mauve</td>
      <td>Cape Town</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Chiquitita</th>
      <td>Orange</td>
      <td>Beijing</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



#### Reordering columns


```python
df = df[['Favourite Number', 'City', 'Favourite Colour']]
df
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
      <th>Favourite Number</th>
      <th>City</th>
      <th>Favourite Colour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Norman</th>
      <td>1</td>
      <td>London</td>
      <td>Purple</td>
    </tr>
    <tr>
      <th>Phyllis</th>
      <td>1</td>
      <td>Vancouver</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>Esteban</th>
      <td>1</td>
      <td>Buenos Aires</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>Maureen</th>
      <td>1</td>
      <td>Cape Town</td>
      <td>Mauve</td>
    </tr>
    <tr>
      <th>Chiquitita</th>
      <td>1</td>
      <td>Beijing</td>
      <td>Orange</td>
    </tr>
  </tbody>
</table>
</div>



#### Changing a column


```python
df['Favourite Number'] = np.random.randint(0, 100, 5)
df
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
      <th>Favourite Number</th>
      <th>City</th>
      <th>Favourite Colour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Norman</th>
      <td>78</td>
      <td>London</td>
      <td>Purple</td>
    </tr>
    <tr>
      <th>Phyllis</th>
      <td>51</td>
      <td>Vancouver</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>Esteban</th>
      <td>10</td>
      <td>Buenos Aires</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>Maureen</th>
      <td>75</td>
      <td>Cape Town</td>
      <td>Mauve</td>
    </tr>
    <tr>
      <th>Chiquitita</th>
      <td>75</td>
      <td>Beijing</td>
      <td>Orange</td>
    </tr>
  </tbody>
</table>
</div>



#### Removing columns


```python
df.drop('Favourite Number', axis=1, inplace=True)
df
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
      <th>City</th>
      <th>Favourite Colour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Norman</th>
      <td>London</td>
      <td>Purple</td>
    </tr>
    <tr>
      <th>Phyllis</th>
      <td>Vancouver</td>
      <td>Blue</td>
    </tr>
    <tr>
      <th>Esteban</th>
      <td>Buenos Aires</td>
      <td>Red</td>
    </tr>
    <tr>
      <th>Maureen</th>
      <td>Cape Town</td>
      <td>Mauve</td>
    </tr>
    <tr>
      <th>Chiquitita</th>
      <td>Beijing</td>
      <td>Orange</td>
    </tr>
  </tbody>
</table>
</div>


