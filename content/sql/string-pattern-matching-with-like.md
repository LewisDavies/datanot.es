Title: String Pattern Matching with LIKE
Slug: sql/string-pattern-matching-with-like
Category: SQL
Tags: SELECT, FROM, WHERE, LIKE
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



### Find matches to a single character
Use an underscore to find values that match a single character


```python
%%sql

SELECT
    c.customer_id
    , c.first_name
    , c.last_name
FROM
    customer c
WHERE
    c.first_name LIKE 'Andre_'
```




<table>
    <tr>
        <th>customer_id</th>
        <th>first_name</th>
        <th>last_name</th>
    </tr>
    <tr>
        <td>81</td>
        <td>Andrea</td>
        <td>Henderson</td>
    </tr>
    <tr>
        <td>333</td>
        <td>Andrew</td>
        <td>Purdy</td>
    </tr>
</table>



Note that underscores can be combined to match a specific number of characters


```python
%%sql

SELECT
    c.customer_id
    , c.first_name
    , c.last_name
FROM
    customer c
WHERE
    c.first_name LIKE 'Jam__'
```




<table>
    <tr>
        <th>customer_id</th>
        <th>first_name</th>
        <th>last_name</th>
    </tr>
    <tr>
        <td>146</td>
        <td>Jamie</td>
        <td>Rice</td>
    </tr>
    <tr>
        <td>299</td>
        <td>James</td>
        <td>Gannon</td>
    </tr>
    <tr>
        <td>531</td>
        <td>Jamie</td>
        <td>Waugh</td>
    </tr>
</table>



### Find matches to a sequence of characters
A percent sign will match any number of characters


```python
%%sql

SELECT
    c.customer_id
    , c.first_name
    , c.last_name
FROM
    customer c
WHERE
    c.first_name LIKE 'Charl%'
```




<table>
    <tr>
        <th>customer_id</th>
        <th>first_name</th>
        <th>last_name</th>
    </tr>
    <tr>
        <td>130</td>
        <td>Charlotte</td>
        <td>Hunter</td>
    </tr>
    <tr>
        <td>220</td>
        <td>Charlene</td>
        <td>Alvarez</td>
    </tr>
    <tr>
        <td>306</td>
        <td>Charles</td>
        <td>Kowalski</td>
    </tr>
    <tr>
        <td>495</td>
        <td>Charlie</td>
        <td>Bess</td>
    </tr>
</table>



Note that ```%``` will match zero-length sequences, as in the example below


```python
%%sql

SELECT
    c.customer_id
    , c.first_name
    , c.last_name
FROM
    customer c
WHERE
    c.first_name LIKE '%Jonathan%'
```




<table>
    <tr>
        <th>customer_id</th>
        <th>first_name</th>
        <th>last_name</th>
    </tr>
    <tr>
        <td>353</td>
        <td>Jonathan</td>
        <td>Scarborough</td>
    </tr>
</table>


