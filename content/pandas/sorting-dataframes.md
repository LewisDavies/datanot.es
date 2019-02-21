Title: Sorting Data
Slug: pandas/sorting-data
Category: Pandas
Tags: DataFrame, head, sort_values, set_index, sort_index
Date: 2017-09-25
Modified: 2017-09-25

### Import libraries


```python
import numpy as np
import pandas as pd
```

### Create DataFrame


```python
data = {
    'name': ['Regina', 'Barbie', 'Gaz', 'Jiminy', 'Fran'],
    'number': np.random.randint(0, 100, 5)
}

df = pd.DataFrame(data)
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Regina</td>
      <td>40</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Barbie</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Gaz</td>
      <td>84</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jiminy</td>
      <td>68</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Fran</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>



### Sorting our values


```python
# Sorting in alphabetical order
df.sort_values('name')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Barbie</td>
      <td>75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Fran</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Gaz</td>
      <td>84</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jiminy</td>
      <td>68</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Regina</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Sorting numbers in reverse order
df.sort_values('number', ascending=False)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>number</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>Gaz</td>
      <td>84</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Barbie</td>
      <td>75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Jiminy</td>
      <td>68</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Regina</td>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Fran</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
</div>



### Sorting our index


```python
df.set_index('name').sort_index(ascending=False)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>number</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Regina</th>
      <td>40</td>
    </tr>
    <tr>
      <th>Jiminy</th>
      <td>68</td>
    </tr>
    <tr>
      <th>Gaz</th>
      <td>84</td>
    </tr>
    <tr>
      <th>Fran</th>
      <td>23</td>
    </tr>
    <tr>
      <th>Barbie</th>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>


