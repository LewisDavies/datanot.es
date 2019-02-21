Title: Calculating a Rolling Value
Slug: pandas/calculating-a-rolling-value
Category: Pandas
Tags: date_range, random, randint, DataFrame, head, rolling, mean, max, head, resample
Date: 2017-09-25
Modified: 2017-09-25

### Import libraries


```python
import numpy as np
import pandas as pd
```

### Create DataFrame


```python
dates = pd.date_range('2017-01-01', '2017-06-30')
data = {'value': np.random.randint(0, 100, len(dates))}

df = pd.DataFrame(data=data, index=dates)
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>71</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>58</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>68</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>83</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>59</td>
    </tr>
  </tbody>
</table>
</div>



### Create a rolling value
When calling `rolling`, we need to say how many periods we're working over. Our data was measured daily, so passing the argument `3` means we calculate rolling values over three days.


```python
df_roll = df.rolling(3)
df_roll
```




    Rolling [window=3,center=False,axis=0]




```python
df_roll.mean().head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>65.666667</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>69.666667</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>70.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_roll.max().head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>71.0</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>83.0</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>83.0</td>
    </tr>
  </tbody>
</table>
</div>



### Combining with `resample`
If you want to resample your data first, the [Pandas docs](https://pandas.pydata.org/pandas-docs/stable/computation.html#window-functions) recommend the pattern below. Firstly we call `resample('M').mean()` and get a monthly mean, then create a rolling object, then chain `mean()` once again to get the rolling average.


```python
df.resample('M').mean().rolling(3).mean()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-31</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-02-28</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2017-03-31</th>
      <td>50.643241</td>
    </tr>
    <tr>
      <th>2017-04-30</th>
      <td>49.044675</td>
    </tr>
    <tr>
      <th>2017-05-31</th>
      <td>48.551971</td>
    </tr>
    <tr>
      <th>2017-06-30</th>
      <td>49.598566</td>
    </tr>
  </tbody>
</table>
</div>


