Title: Working with Datetimes
Slug: sql/working-with-datetimes
Category: SQL
Tags: SELECT, FROM, LIMIT, to_char
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



#### Convert datetimes to other formats
Below are examples of different date formats followed by time formats. They can all be mixed and matched to get the format you need.


```python
%%sql

SELECT
    p.payment_id
    , p.payment_date
    , to_char(p.payment_date, 'YY-MM-DD')
    , to_char(p.payment_date, 'DD Month YYYY')
    , to_char(p.payment_date, 'Dy DDth Mon')
    -- Year followed by week number
    , to_char(p.payment_date, 'YYYY-"W"IW')
FROM
    payment p
LIMIT
    5
```




<table>
    <tr>
        <th>payment_id</th>
        <th>payment_date</th>
        <th>to_char</th>
        <th>to_char_1</th>
        <th>to_char_2</th>
        <th>to_char_3</th>
    </tr>
    <tr>
        <td>17503</td>
        <td>2007-02-15 22:25:46.996577</td>
        <td>07-02-15</td>
        <td>15 February  2007</td>
        <td>Thu 15th Feb</td>
        <td>2007-W07</td>
    </tr>
    <tr>
        <td>17504</td>
        <td>2007-02-16 17:23:14.996577</td>
        <td>07-02-16</td>
        <td>16 February  2007</td>
        <td>Fri 16th Feb</td>
        <td>2007-W07</td>
    </tr>
    <tr>
        <td>17505</td>
        <td>2007-02-16 22:41:45.996577</td>
        <td>07-02-16</td>
        <td>16 February  2007</td>
        <td>Fri 16th Feb</td>
        <td>2007-W07</td>
    </tr>
    <tr>
        <td>17506</td>
        <td>2007-02-19 19:39:56.996577</td>
        <td>07-02-19</td>
        <td>19 February  2007</td>
        <td>Mon 19th Feb</td>
        <td>2007-W08</td>
    </tr>
    <tr>
        <td>17507</td>
        <td>2007-02-20 17:31:48.996577</td>
        <td>07-02-20</td>
        <td>20 February  2007</td>
        <td>Tue 20th Feb</td>
        <td>2007-W08</td>
    </tr>
</table>




```python
%%sql

SELECT
    p.payment_id
    , p.payment_date
    , to_char(p.payment_date, 'HH24:MI:SS:US')
    , to_char(p.payment_date, 'HH:MI:SS AM')
    , to_char(p.payment_date, 'HH:MI a.m.')
FROM
    payment p
LIMIT
    5
```




<table>
    <tr>
        <th>payment_id</th>
        <th>payment_date</th>
        <th>to_char</th>
        <th>to_char_1</th>
        <th>to_char_2</th>
    </tr>
    <tr>
        <td>17503</td>
        <td>2007-02-15 22:25:46.996577</td>
        <td>22:25:46:996577</td>
        <td>10:25:46 PM</td>
        <td>10:25 p.m.</td>
    </tr>
    <tr>
        <td>17504</td>
        <td>2007-02-16 17:23:14.996577</td>
        <td>17:23:14:996577</td>
        <td>05:23:14 PM</td>
        <td>05:23 p.m.</td>
    </tr>
    <tr>
        <td>17505</td>
        <td>2007-02-16 22:41:45.996577</td>
        <td>22:41:45:996577</td>
        <td>10:41:45 PM</td>
        <td>10:41 p.m.</td>
    </tr>
    <tr>
        <td>17506</td>
        <td>2007-02-19 19:39:56.996577</td>
        <td>19:39:56:996577</td>
        <td>07:39:56 PM</td>
        <td>07:39 p.m.</td>
    </tr>
    <tr>
        <td>17507</td>
        <td>2007-02-20 17:31:48.996577</td>
        <td>17:31:48:996577</td>
        <td>05:31:48 PM</td>
        <td>05:31 p.m.</td>
    </tr>
</table>



There are many ways that datetimes can be converted in Postgres. For more examples, [see the docs](https://www.postgresql.org/docs/current/static/functions-formatting.html).
