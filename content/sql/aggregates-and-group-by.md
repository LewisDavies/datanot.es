Title: Aggregates and GROUP BY
Slug: sql/aggregates-and-group-by
Category: SQL
Tags: SELECT, FROM, LIMIT, GROUP BY, sum, avg, max, min, count
Date: 2017-08-10
Modified: 2017-08-15

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



#### Sample from `film` table


```python
%%sql

SELECT
    f.film_id
    , f.title
    , f.rental_rate
    , f.length
FROM
    film f
LIMIT
    5
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>rental_rate</th>
        <th>length</th>
    </tr>
    <tr>
        <td>133</td>
        <td>Chamber Italian</td>
        <td>4.99</td>
        <td>117</td>
    </tr>
    <tr>
        <td>384</td>
        <td>Grosse Wonderful</td>
        <td>4.99</td>
        <td>49</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Airport Pollock</td>
        <td>4.99</td>
        <td>54</td>
    </tr>
    <tr>
        <td>98</td>
        <td>Bright Encounters</td>
        <td>4.99</td>
        <td>73</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
        <td>0.99</td>
        <td>86</td>
    </tr>
</table>



#### Syntax example — `sum`


```python
%%sql

SELECT
    sum(f.length)
FROM
    film f
```




<table>
    <tr>
        <th>sum</th>
    </tr>
    <tr>
        <td>115272</td>
    </tr>
</table>



#### Other aggregate functions
**`avg`**: Mean of all column values

**`max`**: Highest value in the column

**`min`**: Lowest value in the column

**`count`**: Total number of non-null values

\*Some aggregates, including `max`, `min` and `count`, can also be applied to strings.

#### `GROUP BY`
Let's say we want to find the mean film length at each price point, and all films cost £0.99, £2.99 or £4.99.


```python
%%sql

SELECT
    f.rental_rate
    , avg(f.length)
FROM
    film f
GROUP BY
    f.rental_rate
```




<table>
    <tr>
        <th>rental_rate</th>
        <th>avg</th>
    </tr>
    <tr>
        <td>4.99</td>
        <td>115.8244047619047619</td>
    </tr>
    <tr>
        <td>0.99</td>
        <td>112.9120234604105572</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>117.1888544891640867</td>
    </tr>
</table>



You can group according to more than one column to drill down into your data, but make sure to add all non-aggregates to your `GROUP BY` clause.


```python
%%sql

SELECT
    f.rental_rate
    , f.rating
    , avg(f.length)
FROM
    film f
GROUP BY
    f.rental_rate
    , f.rating
ORDER BY
    f.rental_rate ASC
    , f.rating ASC
```




<table>
    <tr>
        <th>rental_rate</th>
        <th>rating</th>
        <th>avg</th>
    </tr>
    <tr>
        <td>0.99</td>
        <td>G</td>
        <td>106.7187500000000000</td>
    </tr>
    <tr>
        <td>0.99</td>
        <td>PG</td>
        <td>108.3548387096774194</td>
    </tr>
    <tr>
        <td>0.99</td>
        <td>PG-13</td>
        <td>114.1111111111111111</td>
    </tr>
    <tr>
        <td>0.99</td>
        <td>R</td>
        <td>123.1857142857142857</td>
    </tr>
    <tr>
        <td>0.99</td>
        <td>NC-17</td>
        <td>111.1780821917808219</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>G</td>
        <td>113.9661016949152542</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>PG</td>
        <td>116.6562500000000000</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>PG-13</td>
        <td>123.5675675675675676</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>R</td>
        <td>116.3833333333333333</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>NC-17</td>
        <td>114.1666666666666667</td>
    </tr>
    <tr>
        <td>4.99</td>
        <td>G</td>
        <td>112.9636363636363636</td>
    </tr>
    <tr>
        <td>4.99</td>
        <td>PG</td>
        <td>110.9558823529411765</td>
    </tr>
    <tr>
        <td>4.99</td>
        <td>PG-13</td>
        <td>123.3636363636363636</td>
    </tr>
    <tr>
        <td>4.99</td>
        <td>R</td>
        <td>115.8923076923076923</td>
    </tr>
    <tr>
        <td>4.99</td>
        <td>NC-17</td>
        <td>114.4647887323943662</td>
    </tr>
</table>
