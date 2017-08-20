Title: Common Table Expressions
Slug: sql/common-table-expressions
Category: SQL
Tags: WITH, SELECT, FROM, LIMIT, OVER, PARTITION BY, ORDER BY, DESC, rank
Date: 2017-08-16
Modified: 2017-08-16

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



#### Using the `WITH` clause
We use the `WITH` keyword to create temporary tables just for the query we're currently working on. These are called Common Table Expressions (CTEs).

In the simple example below, we execute the query in the `WITH` clause and then return all rows from it.


```python
%%sql

WITH rental_cte AS (
    SELECT
        r.rental_id
        , customer_id
        , r.return_date
    FROM
        rental r
    LIMIT
        10
)

SELECT
    *
FROM
    rental_cte rc
```




<table>
    <tr>
        <th>rental_id</th>
        <th>customer_id</th>
        <th>return_date</th>
    </tr>
    <tr>
        <td>2</td>
        <td>459</td>
        <td>2005-05-28 19:40:33</td>
    </tr>
    <tr>
        <td>3</td>
        <td>408</td>
        <td>2005-06-01 22:12:39</td>
    </tr>
    <tr>
        <td>4</td>
        <td>333</td>
        <td>2005-06-03 01:43:41</td>
    </tr>
    <tr>
        <td>5</td>
        <td>222</td>
        <td>2005-06-02 04:33:21</td>
    </tr>
    <tr>
        <td>6</td>
        <td>549</td>
        <td>2005-05-27 01:32:07</td>
    </tr>
    <tr>
        <td>7</td>
        <td>269</td>
        <td>2005-05-29 20:34:53</td>
    </tr>
    <tr>
        <td>8</td>
        <td>239</td>
        <td>2005-05-27 23:33:46</td>
    </tr>
    <tr>
        <td>9</td>
        <td>126</td>
        <td>2005-05-28 00:22:40</td>
    </tr>
    <tr>
        <td>10</td>
        <td>399</td>
        <td>2005-05-31 22:44:21</td>
    </tr>
    <tr>
        <td>11</td>
        <td>142</td>
        <td>2005-06-02 20:56:02</td>
    </tr>
</table>



#### A common use for CTEs — ranking your results
As explained in the page on [Window Functions]({{ SITEURL }}/sql/using-temporary-tables-in-queries-common-table-expressions.html), CTEs are useful when ranking our results.

Here we will find the last 3 films returned by a sample of customers.


```python
%%sql

WITH rental_cte AS (
    SELECT
        r.rental_id
        , customer_id
        , r.return_date
        , rank() OVER(PARTITION BY r.customer_id ORDER BY r.return_date DESC) as rk
    FROM
        rental r
)

SELECT
    *
FROM
    rental_cte rc
WHERE
    rc.rk < 4
-- Show only the first 3 customers to save space
LIMIT
    9
```




<table>
    <tr>
        <th>rental_id</th>
        <th>customer_id</th>
        <th>return_date</th>
        <th>rk</th>
    </tr>
    <tr>
        <td>15315</td>
        <td>1</td>
        <td>2005-08-30 01:51:46</td>
        <td>1</td>
    </tr>
    <tr>
        <td>15298</td>
        <td>1</td>
        <td>2005-08-28 22:49:37</td>
        <td>2</td>
    </tr>
    <tr>
        <td>14825</td>
        <td>1</td>
        <td>2005-08-27 07:01:57</td>
        <td>3</td>
    </tr>
    <tr>
        <td>15145</td>
        <td>2</td>
        <td>2005-08-31 15:51:04</td>
        <td>1</td>
    </tr>
    <tr>
        <td>14743</td>
        <td>2</td>
        <td>2005-08-29 00:18:56</td>
        <td>2</td>
    </tr>
    <tr>
        <td>14475</td>
        <td>2</td>
        <td>2005-08-27 08:59:32</td>
        <td>3</td>
    </tr>
    <tr>
        <td>14699</td>
        <td>3</td>
        <td>2005-08-29 18:08:48</td>
        <td>1</td>
    </tr>
    <tr>
        <td>13403</td>
        <td>3</td>
        <td>2005-08-27 19:23:07</td>
        <td>2</td>
    </tr>
    <tr>
        <td>15619</td>
        <td>3</td>
        <td>2005-08-26 07:21:14</td>
        <td>3</td>
    </tr>
</table>
