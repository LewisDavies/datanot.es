Title: Select Values Within a Range
Slug: sql/select-values-within-a-range
Category: SQL
Tags: SELECT, FROM, WHERE, BETWEEN, LIMIT
Date: 2017-08-08
Modified: 2017-08-27

#### Load ipython-sql extension


```python
# The 2 lines below prevent an error message from being displayed when we run %load_ext sql
import warnings
warnings.filterwarnings('ignore')

%load_ext sql
%config SqlMagic.feedback = False
```

#### Connect to the database


```python
%%sql

postgresql://localhost/dvdrental
```




    'Connected: None@dvdrental'



#### Find values within a range with BETWEEN
Note that this is an inclusive search: in the example below, movies that are 110 or 120 minutes long will be returned in the full results.


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



#### Find values outside the same range


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



#### Using BETWEEN with datetimes
It is easy to be caught out by datetimes when using between. In the example below `'2007-02-15'` is interpreted as '`2007-02-15 00:00:00`', so the latest results are from just before midnight.


```python
%%sql

SELECT
    p.payment_id
    , p.payment_date
FROM
    payment p
WHERE
    p.payment_date BETWEEN '2007-02-14' AND '2007-02-15'
ORDER BY
    p.payment_date DESC
LIMIT
    5
```




<table>
    <tr>
        <th>payment_id</th>
        <th>payment_date</th>
    </tr>
    <tr>
        <td>17743</td>
        <td>2007-02-14 23:53:34.996577</td>
    </tr>
    <tr>
        <td>18322</td>
        <td>2007-02-14 23:52:46.996577</td>
    </tr>
    <tr>
        <td>19212</td>
        <td>2007-02-14 23:47:05.996577</td>
    </tr>
    <tr>
        <td>17617</td>
        <td>2007-02-14 23:33:58.996577</td>
    </tr>
    <tr>
        <td>19421</td>
        <td>2007-02-14 23:32:48.996577</td>
    </tr>
</table>



When we cast `p.payment_date` as a `date`, the time part is removed. This means that payments from `2007-02-15` are now included in the results.


```python
%%sql

SELECT
    p.payment_id
    , p.payment_date
FROM
    payment p
WHERE
    p.payment_date::date BETWEEN '2007-02-14' AND '2007-02-15'
ORDER BY
    p.payment_date DESC
LIMIT
    5
```




<table>
    <tr>
        <th>payment_id</th>
        <th>payment_date</th>
    </tr>
    <tr>
        <td>18335</td>
        <td>2007-02-15 23:59:49.996577</td>
    </tr>
    <tr>
        <td>18676</td>
        <td>2007-02-15 23:56:48.996577</td>
    </tr>
    <tr>
        <td>18610</td>
        <td>2007-02-15 23:52:34.996577</td>
    </tr>
    <tr>
        <td>19199</td>
        <td>2007-02-15 23:48:31.996577</td>
    </tr>
    <tr>
        <td>19229</td>
        <td>2007-02-15 23:44:25.996577</td>
    </tr>
</table>


