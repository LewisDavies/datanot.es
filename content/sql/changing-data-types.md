Title: Changing Data Types
Slug: sql/changing-data-types
Category: SQL
Tags: SELECT, CAST, FROM, LIMIT, ::, float, int, date, time
Date: 2017-08-27
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



#### Two ways to cast
Data types can be changed with the `CAST` function, but the `::` shorthand can also be used. Here are a few examples.


```python
%%sql

SELECT
    p.payment_id
    , CAST(p.payment_id AS float) AS payment_id_casted
    , p.amount
    , p.amount::int as amount_casted
    , p.payment_date
    , CAST(p.payment_date AS date) as payment_date_casted
    , p.payment_date::time as payment_time_casted
FROM
    payment p
LIMIT
    5
```




<table>
    <tr>
        <th>payment_id</th>
        <th>payment_id_casted</th>
        <th>amount</th>
        <th>amount_casted</th>
        <th>payment_date</th>
        <th>payment_date_casted</th>
        <th>payment_time_casted</th>
    </tr>
    <tr>
        <td>17503</td>
        <td>17503.0</td>
        <td>7.99</td>
        <td>8</td>
        <td>2007-02-15 22:25:46.996577</td>
        <td>2007-02-15</td>
        <td>22:25:46.996577</td>
    </tr>
    <tr>
        <td>17504</td>
        <td>17504.0</td>
        <td>1.99</td>
        <td>2</td>
        <td>2007-02-16 17:23:14.996577</td>
        <td>2007-02-16</td>
        <td>17:23:14.996577</td>
    </tr>
    <tr>
        <td>17505</td>
        <td>17505.0</td>
        <td>7.99</td>
        <td>8</td>
        <td>2007-02-16 22:41:45.996577</td>
        <td>2007-02-16</td>
        <td>22:41:45.996577</td>
    </tr>
    <tr>
        <td>17506</td>
        <td>17506.0</td>
        <td>2.99</td>
        <td>3</td>
        <td>2007-02-19 19:39:56.996577</td>
        <td>2007-02-19</td>
        <td>19:39:56.996577</td>
    </tr>
    <tr>
        <td>17507</td>
        <td>17507.0</td>
        <td>7.99</td>
        <td>8</td>
        <td>2007-02-20 17:31:48.996577</td>
        <td>2007-02-20</td>
        <td>17:31:48.996577</td>
    </tr>
</table>
