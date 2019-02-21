Title: Parsing Datetimes
Slug: pandas/parsing-datetimes
Category: Pandas
Tags: DataFrame, info, to_datetime, read_csv, read_sql, parse_dates
Date: 2017-09-21
Modified: 2017-09-21

### Import libraries


```python
import numpy as np
import pandas as pd
```

### Create DataFrame
Let's make some wildly inaccurate data. Note that the datatype of `dates` column is `object` because it contains text.


```python
dates = ['2017-09-04', '2017-09-05', '2017-09-06', '2017-09-07',
         '2017-09-08', '2017-09-09', '2017-09-10', '2017-09-11',
         '2017-09-12', '2017-09-13', '2017-09-14', '2017-09-15', 
         '2017-09-16', '2017-09-17']
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
      <td>2017-09-04</td>
      <td>69</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2017-09-05</td>
      <td>75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2017-09-06</td>
      <td>80</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017-09-07</td>
      <td>60</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2017-09-08</td>
      <td>64</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 14 entries, 0 to 13
    Data columns (total 2 columns):
    date        14 non-null object
    rainfall    14 non-null int64
    dtypes: int64(1), object(1)
    memory usage: 304.0+ bytes


### Converting a column to datetime


```python
df['date'] = pd.to_datetime(df['date'])
```


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 14 entries, 0 to 13
    Data columns (total 2 columns):
    date        14 non-null datetime64[ns]
    rainfall    14 non-null int64
    dtypes: datetime64[ns](1), int64(1)
    memory usage: 304.0 bytes


### Converting on import
If using a function like `pd.read_csv` or `pd.read_sql`, you can make use of the `parse_dates` parameter.


```python
# If the index contains datetimes
pd.read_csv('your_data.csv', parse_dates=True)

# When other columns contain datetimes, pass a list of name
pd.read_sql(your_query, parse_dates=['confirmed_at', 'updated_at'])
```
