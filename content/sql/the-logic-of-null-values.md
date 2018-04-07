Title: The Logic of NULL Values
Slug: sql/the-logic-of-null-values
Category: SQL
Tags: SELECT, FROM, WHERE, LIMIT, AS, AND, OR, ORDER BY, ASC, TRUE, FALSE, NULL
Date: 2017-08-28
Modified: 2017-08-28

This is a fairly simple overview of three-value logic and null values in SQL. This guide is based on the information in [this article](https://www.red-gate.com/simple-talk/sql/learn-sql-server/sql-and-the-snare-of-three-valued-logic/), which offers much more depth and other examples.

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



#### `TRUE` and `FALSE` values
These work as you might expect if you have programming experience or an understanding of Boolean values.


```python
%%sql

SELECT
    TRUE = TRUE AS true_equals_true
    , TRUE = FALSE AS true_equals_false
    , FALSE = FALSE AS false_equals_false
    , TRUE AND FALSE AS true_and_false
    , TRUE OR FALSE AS true_or_false
```




<table>
    <tr>
        <th>true_equals_true</th>
        <th>true_equals_false</th>
        <th>false_equals_false</th>
        <th>true_and_false</th>
        <th>true_or_false</th>
    </tr>
    <tr>
        <td>True</td>
        <td>False</td>
        <td>True</td>
        <td>False</td>
        <td>True</td>
    </tr>
</table>



#### `NULL`, the third logical value
In SQL, `TRUE`, `FALSE` and `NULL` are fully separate and distinct. This means that `NULL` equals neither `TRUE` nor `FALSE`. In fact, even `NULL` doesn't equal `NULL`.


```python
%%sql

SELECT
    TRUE = NULL AS true_equals_null
    , FALSE = NULL AS false_equals_null
    , NULL = NULL AS null_equals_null
```




<table>
    <tr>
        <th>true_equals_null</th>
        <th>false_equals_null</th>
        <th>null_equals_null</th>
    </tr>
    <tr>
        <td>None</td>
        <td>None</td>
        <td>None</td>
    </tr>
</table>



#### Testing for `NULL` values
If even `NULL` doesn't equal `NULL`, how do we test for it? It's simple: we use `IS NULL` or `IS NOT NULL`.


```python
%%sql

SELECT
    TRUE IS NULL AS true_is_null
    , TRUE IS NOT NULL AS true_is_not_null
    , FALSE IS NULL AS false_is_null
    , FALSE IS NOT NULL AS false_is_not_null
    , NULL IS NULL AS null_is_null
    , NULL IS NOT NULL AS null_is_not_null
```




<table>
    <tr>
        <th>true_is_null</th>
        <th>true_is_not_null</th>
        <th>false_is_null</th>
        <th>false_is_not_null</th>
        <th>null_is_null</th>
        <th>null_is_not_null</th>
    </tr>
    <tr>
        <td>False</td>
        <td>True</td>
        <td>False</td>
        <td>True</td>
        <td>True</td>
        <td>False</td>
    </tr>
</table>



#### `NULL` values in practice
We can use our video rental database to see the effects of this. The last day on which the store had videos returned was 2nd September 2005.


```python
%%sql

SELECT
    r.rental_id
    , r.return_date
FROM
    rental r
WHERE
    r.return_date > '2005-09-02'
ORDER BY
    r.return_date ASC
LIMIT
    5
```




<table>
    <tr>
        <th>rental_id</th>
        <th>return_date</th>
    </tr>
    <tr>
        <td>15971</td>
        <td>2005-09-02 01:28:33</td>
    </tr>
    <tr>
        <td>16040</td>
        <td>2005-09-02 02:19:33</td>
    </tr>
    <tr>
        <td>16005</td>
        <td>2005-09-02 02:35:22</td>
    </tr>
</table>



But we know that some videos haven't been returned, so these videos have the value `NULL` for `r.return_date`.


```python
%%sql

SELECT
    count(r.rental_id) AS outstanding_loans
FROM
    rental r
WHERE
    r.return_date IS NULL
```




<table>
    <tr>
        <th>outstanding_loans</th>
    </tr>
    <tr>
        <td>183</td>
    </tr>
</table>



To include oustanding loans in the results, we add one line to our query. This works provided we know that `NULL` is only used for unreturned rentals.


```python
%%sql

SELECT
    r.rental_id
    , r.return_date
FROM
    rental r
WHERE
    r.return_date > '2005-09-02'
    OR r.return_date IS NULL
ORDER BY
    r.return_date ASC
LIMIT
    5
```




<table>
    <tr>
        <th>rental_id</th>
        <th>return_date</th>
    </tr>
    <tr>
        <td>15971</td>
        <td>2005-09-02 01:28:33</td>
    </tr>
    <tr>
        <td>16040</td>
        <td>2005-09-02 02:19:33</td>
    </tr>
    <tr>
        <td>16005</td>
        <td>2005-09-02 02:35:22</td>
    </tr>
    <tr>
        <td>12101</td>
        <td>None</td>
    </tr>
    <tr>
        <td>11563</td>
        <td>None</td>
    </tr>
</table>


