Title: Iterating Over a DataFrame
Slug: pandas/iterating-over-a-dataframe
Category: Pandas
Tags: DataFrame, iterrows, iteritems
Date: 2018-10-16
Modified: 2018-10-16

#### Import libraries


```
import numpy as np
import pandas as pd
```

#### Create data


```
df = pd.DataFrame({
    'First': np.random.randint(1, 6, 5), 
    'Second': np.random.randint(4, 10, 5),
    'Third': np.random.randint(10, 20, 5)
})
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
      <th>First</th>
      <th>Second</th>
      <th>Third</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>9</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
      <td>18</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>9</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>6</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>9</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



#### Iterate over rows


```
for index, row in df.iterrows(): # The index and row are returned as a tuple 
    print('Index: {}'.format(index)) 
    print('Row Values: {}'.format(row.values), end='\n\n')
```

    Index: 0
    Row Values: [ 1  9 14]
    
    Index: 1
    Row Values: [ 2  6 18]
    
    Index: 2
    Row Values: [ 4  9 12]
    
    Index: 3
    Row Values: [ 2  6 12]
    
    Index: 4
    Row Values: [ 5  9 12]
    
    

#### Iterate over columns


```
for name, col in df.iteritems(): # As above, these are returned as a tuple
    print('Name: {}'.format(name))
    print('Column Values: {}'.format(col.values), end='\n\n')
```

    Name: First
    Column Values: [1 2 4 2 5]
    
    Name: Second
    Column Values: [9 6 9 6 9]
    
    Name: Third
    Column Values: [14 18 12 12 12]
    
    
