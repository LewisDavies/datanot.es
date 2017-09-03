Title: Finding Percentile Values
Slug: sql/finding-percentile-values
Category: SQL
Tags: SELECT, FROM, WHERE, WITH, AS, GROUP BY, ORDER BY, AS, OVER, ARRAY, WITHIN GROUP, ntile, max, unnest, percentile_disc, percentile_cont
Date: 2017-09-03
Modified: 2017-09-03

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



#### Finding quartile values in older versions of PostgreSQL
The number in the `ntile` function can be replaced as necessary. For example, we would use 5 to find the 20th, 40th, 60th, 80th and 100th percentiles, or 100 to find every percentile.


```python
%%sql

WITH quartiles AS (
    SELECT
        f.length,
        ntile(4) OVER(ORDER BY f.length) AS quartile
    FROM
        film f
  )

SELECT
    max(q.length) AS quartiles
FROM
    quartiles q
GROUP BY
    quartile
ORDER BY
    quartile
```




<table>
    <tr>
        <th>quartiles</th>
    </tr>
    <tr>
        <td>80</td>
    </tr>
    <tr>
        <td>114</td>
    </tr>
    <tr>
        <td>149</td>
    </tr>
    <tr>
        <td>185</td>
    </tr>
</table>



#### Newer, simpler functions
Version 9.4 introduced a number of new functions that reduce the need for a CTE or subquery when finding percentiles. We can use `percentile_disc` to return the first value that matches or exceeds a particular percentile, whereas `percentile_cont` will interpolate between values if the exact percentile needed isn't found.


```python
%%sql

SELECT
    unnest(percentile_disc(ARRAY[0.25, 0.5, 0.75, 1]) WITHIN GROUP (ORDER BY f.length)) AS discrete_quartiles
    , unnest(percentile_cont(ARRAY[0.25, 0.5, 0.75, 1]) WITHIN GROUP (ORDER BY f.length)) AS continuous_quartiles
FROM
    film f
```




<table>
    <tr>
        <th>discrete_quartiles</th>
        <th>continuous_quartiles</th>
    </tr>
    <tr>
        <td>80</td>
        <td>80.0</td>
    </tr>
    <tr>
        <td>114</td>
        <td>114.0</td>
    </tr>
    <tr>
        <td>149</td>
        <td>149.25</td>
    </tr>
    <tr>
        <td>185</td>
        <td>185.0</td>
    </tr>
</table>



#### One final example
If only one percentile is required, the `unnest` function and `ARRAY` constructor can be removed and your chosen percentile added instead.


```python
%%sql

SELECT
    percentile_disc(0.5) WITHIN GROUP (ORDER BY f.length) AS median
FROM
    film f
```




<table>
    <tr>
        <th>median</th>
    </tr>
    <tr>
        <td>114</td>
    </tr>
</table>



These examples are based on information on the [2ndQuadrant PostgreSQL blog](https://blog.2ndquadrant.com/the-within-group-and-filter-sql-clauses-of-postgresql-9-4/).
