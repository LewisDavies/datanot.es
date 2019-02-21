Title: Finding Value Counts with FILTER
Slug: sql/finding-value-counts-with-filter
Category: SQL
Tags: SELECT, FROM, GROUP BY, ORDER BY, CASE, WHEN, THEN, AS, FILTER, count, sum
Date: 2017-09-03
Modified: 2017-09-03

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



### Basic `count` method


```python
%%sql

SELECT
    f.rental_duration
    , count(f.rental_duration)
FROM
    film f
GROUP BY
    f.rental_duration
ORDER BY
    f.rental_duration ASC
```




<table>
    <tr>
        <th>rental_duration</th>
        <th>count</th>
    </tr>
    <tr>
        <td>3</td>
        <td>203</td>
    </tr>
    <tr>
        <td>4</td>
        <td>203</td>
    </tr>
    <tr>
        <td>5</td>
        <td>191</td>
    </tr>
    <tr>
        <td>6</td>
        <td>212</td>
    </tr>
    <tr>
        <td>7</td>
        <td>191</td>
    </tr>
</table>



### A more flexible way with `CASE`
Let's say we want to categorise our values. In older versions of PostgreSQL, we would do something like this:


```python
%%sql

SELECT
    sum(CASE WHEN f.rental_duration < 5 THEN 1 ELSE 0 END) AS under_five
    , sum(CASE WHEN f.rental_duration >= 5 THEN 1 ELSE 0 END) AS five_or_over
FROM
    film f
```




<table>
    <tr>
        <th>under_five</th>
        <th>five_or_over</th>
    </tr>
    <tr>
        <td>406</td>
        <td>594</td>
    </tr>
</table>



### An even better way
Version 9.4 introduced `FILTER`, letting us write a better, more readable version of the above query.


```python
%%sql

SELECT
    count(*) FILTER(WHERE f.rental_duration < 5) AS under_five
    , count(*) FILTER(WHERE f.rental_duration >= 5) AS five_or_over
FROM
    film f
```




<table>
    <tr>
        <th>under_five</th>
        <th>five_or_over</th>
    </tr>
    <tr>
        <td>406</td>
        <td>594</td>
    </tr>
</table>



### `FILTER` in practice
With this new function, we can essentially create a pivot table with a single query.


```python
%%sql

SELECT
    f.rental_rate
    , count(*) FILTER(WHERE f.rental_duration < 5) AS under_five
    , count(*) FILTER(WHERE f.rental_duration >= 5) AS five_or_over
FROM
    film f
GROUP BY
    f.rental_rate
ORDER BY
    f.rental_rate ASC
```




<table>
    <tr>
        <th>rental_rate</th>
        <th>under_five</th>
        <th>five_or_over</th>
    </tr>
    <tr>
        <td>0.99</td>
        <td>150</td>
        <td>191</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>124</td>
        <td>199</td>
    </tr>
    <tr>
        <td>4.99</td>
        <td>132</td>
        <td>204</td>
    </tr>
</table>



These examples are based on information in [PostgreSQL: Up and Running](https://www.amazon.co.uk/PostgreSQL-Running-Regina-Obe/dp/1449373194/).
