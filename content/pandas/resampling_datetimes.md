Title: Resampling Datetimes
Slug: pandas/resampling-datetimes
Category: Pandas
Tags: date_range, DataFrame, head, set_index, loc, resample, mean, min, count
Date: 2017-09-21
Modified: 2017-09-24

#### Import libraries


```python
import numpy as np
import pandas as pd
```

#### Create DataFrame


```python
dates = pd.date_range('2017-08-28', '2017-09-10')
rainfall = np.random.randint(60, 90, len(dates))

data = {'date': dates, 'rainfall': rainfall}

df = pd.DataFrame(data)
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>rainfall</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2017-08-28</td>
      <td>81</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-08-29</td>
      <td>73</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-08-30</td>
      <td>82</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-08-31</td>
      <td>70</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-09-01</td>
      <td>66</td>
    </tr>
  </tbody>
</table>
</div>



#### Selecting rows and cells
We use the `loc` function which takes a range of inputs. Here are a few examples.


```python
# We set the date column as index to make things easier
df.set_index('date', inplace=True)
```


```python
df.loc['2017-08-28']
```




    rainfall    81
    Name: 2017-08-28 00:00:00, dtype: int64




```python
df.loc['2017-09-08':'2017-09-10']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rainfall</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-09-08</th>
      <td>79</td>
    </tr>
    <tr>
      <th>2017-09-09</th>
      <td>75</td>
    </tr>
    <tr>
      <th>2017-09-10</th>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['August 2017']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rainfall</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-28</th>
      <td>81</td>
    </tr>
    <tr>
      <th>2017-08-29</th>
      <td>73</td>
    </tr>
    <tr>
      <th>2017-08-30</th>
      <td>82</td>
    </tr>
    <tr>
      <th>2017-08-31</th>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



#### Changing the observation period
Our (made up) date has been sampled daily, but we can investigate other intervals with `resample`. We then chain an aggregate method to return a DataFrame.


```python
# Average by month
df.resample('M').mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rainfall</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-31</th>
      <td>76.5</td>
    </tr>
    <tr>
      <th>2017-09-30</th>
      <td>74.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Lowest value by week
df.resample('W').min()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rainfall</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-09-03</th>
      <td>66</td>
    </tr>
    <tr>
      <th>2017-09-10</th>
      <td>67</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Number of values by month
df.resample('M').count()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rainfall</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-08-31</th>
      <td>4</td>
    </tr>
    <tr>
      <th>2017-09-30</th>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>


