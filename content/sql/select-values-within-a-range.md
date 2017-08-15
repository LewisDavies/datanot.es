Title: Select Values Within a Range
Slug: sql/select-values-within-a-range
Category: SQL
Tags: SELECT, FROM, WHERE, BETWEEN, LIMIT
Date: 2017-08-08
Modified: 2017-08-09

### Load ipython-sql extension


```python
# The 2 lines below prevent an error message from being displayed when we run %load_ext sql
import warnings
warnings.filterwarnings('ignore')

%load_ext sql
%config SqlMagic.feedback = False
```

### Connect to the database


```python
%%sql

postgresql://localhost/dvdrental
```




    'Connected: None@dvdrental'



### Find values within a range with BETWEEN
Note that this is an inclusive search: results matching the specified values are included


```python
%%sql

SELECT
    f.title
    , f.length
FROM
    film f
WHERE
    f.length BETWEEN 110 AND 120
-- For convenience, we'll only show the first 5 results
LIMIT
    5
```




<table>
    <tr>
        <th>title</th>
        <th>length</th>
    </tr>
    <tr>
        <td>Chamber Italian</td>
        <td>117</td>
    </tr>
    <tr>
        <td>Affair Prejudice</td>
        <td>117</td>
    </tr>
    <tr>
        <td>Alabama Devil</td>
        <td>114</td>
    </tr>
    <tr>
        <td>Amadeus Holy</td>
        <td>113</td>
    </tr>
    <tr>
        <td>Apocalypse Flamingos</td>
        <td>119</td>
    </tr>
</table>



### Find values outside the same range


```python
%%sql

SELECT
    f.title
    , f.length
FROM
    film f
WHERE
    f.length NOT BETWEEN 110 AND 120
LIMIT
    5
```




<table>
    <tr>
        <th>title</th>
        <th>length</th>
    </tr>
    <tr>
        <td>Grosse Wonderful</td>
        <td>49</td>
    </tr>
    <tr>
        <td>Airport Pollock</td>
        <td>54</td>
    </tr>
    <tr>
        <td>Bright Encounters</td>
        <td>73</td>
    </tr>
    <tr>
        <td>Academy Dinosaur</td>
        <td>86</td>
    </tr>
    <tr>
        <td>Ace Goldfinger</td>
        <td>48</td>
    </tr>
</table>
