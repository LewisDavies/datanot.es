Title: Ranking Results with Window Functions
Slug: sql/ranking-results-with-window-functions
Category: SQL
Tags: SELECT, FROM, LIMIT, OVER, PARTITION BY, ORDER BY, rank
Date: 2017-08-15
Modified: 2017-08-15

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



### Sample from `customer` table


```python
%%sql

SELECT
    r.rental_id
    , customer_id
    , r.return_date
FROM
    rental r
LIMIT
    5
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
</table>



### Ranking our results
Using the `OVER` clause allows us to run a function on the results returned from the database. In this example we rank all customer rentals in the order they were returned, most-recent first, for each customer.


```python
%%sql

SELECT
    r.rental_id
    , customer_id
    , r.return_date
    , rank() OVER(PARTITION BY r.customer_id ORDER BY r.return_date DESC) as rk
FROM
    rental r
-- Show only the first 10 results or the results are waaay to big!
LIMIT
    10
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
        <td>13176</td>
        <td>1</td>
        <td>2005-08-23 08:50:54</td>
        <td>4</td>
    </tr>
    <tr>
        <td>14762</td>
        <td>1</td>
        <td>2005-08-23 01:30:57</td>
        <td>5</td>
    </tr>
    <tr>
        <td>12250</td>
        <td>1</td>
        <td>2005-08-22 23:05:29</td>
        <td>6</td>
    </tr>
    <tr>
        <td>13068</td>
        <td>1</td>
        <td>2005-08-20 14:44:16</td>
        <td>7</td>
    </tr>
    <tr>
        <td>11824</td>
        <td>1</td>
        <td>2005-08-19 10:11:54</td>
        <td>8</td>
    </tr>
    <tr>
        <td>11299</td>
        <td>1</td>
        <td>2005-08-10 16:40:52</td>
        <td>9</td>
    </tr>
    <tr>
        <td>10437</td>
        <td>1</td>
        <td>2005-08-10 12:12:04</td>
        <td>10</td>
    </tr>
</table>



### Working with our rankings
Once you've made the query above, we can use it as a Common Table Expression to filter it. For example, let's find the two most-recently returned films for each customer.


```python
%%sql

WITH rental_ranked AS (
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
    rental_ranked rr
WHERE
    rr.rk < 3
LIMIT
    10
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
        <td>15147</td>
        <td>4</td>
        <td>2005-08-28 14:33:23</td>
        <td>1</td>
    </tr>
    <tr>
        <td>13807</td>
        <td>4</td>
        <td>2005-08-28 09:06:40</td>
        <td>2</td>
    </tr>
    <tr>
        <td>13209</td>
        <td>5</td>
        <td>None</td>
        <td>1</td>
    </tr>
    <tr>
        <td>14053</td>
        <td>5</td>
        <td>2005-08-26 20:50:59</td>
        <td>2</td>
    </tr>
</table>



Note that `None` is ranked above all other times. To avoid this, we would add a `WHERE` clause to our CTE specifying `return_date IS NOT NULL`.

There are lots of other window functions that can be used in place of `rank`; [check the Postgres docs](https://www.postgresql.org/docs/9.6/static/functions-window.html) for full details.
