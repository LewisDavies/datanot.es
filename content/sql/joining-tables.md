Title: Joining Tables
Slug: sql/joining-tables
Category: SQL
Tags: SELECT, FROM, WHERE, LIMIT, JOIN, INNER JOIN, OUTER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN, UNION, UNION ALL
Date: 2017-08-09
Modified: 2017-08-09

### Recommended reading
I recommend reading the [Coding Horror's explanation of SQL joins](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) for more detail. Here are a few examples for reference.

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



### Joining tables
When joining tables, it's handy to give them a shorter alias: this makes it easier to refer to them later. This is important as some tables may have common column names and it's important to differentiate between them.

Note that this method works in PostgreSQL, but you may need to add `AS` after the table name in other SQL implementations.


```python
%%sql

SELECT
    c.customer_id
    , c.first_name
    , c.last_name
    , a.address
    , a.district
    , a.city_id
FROM
    customer c
    -- To be explicit, INNER JOIN can also be used here
    JOIN address a on a.address_id = c.address_id
LIMIT
    5
```




<table>
    <tr>
        <th>customer_id</th>
        <th>first_name</th>
        <th>last_name</th>
        <th>address</th>
        <th>district</th>
        <th>city_id</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Mary</td>
        <td>Smith</td>
        <td>1913 Hanoi Way</td>
        <td>Nagasaki</td>
        <td>463</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Patricia</td>
        <td>Johnson</td>
        <td>1121 Loja Avenue</td>
        <td>California</td>
        <td>449</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Linda</td>
        <td>Williams</td>
        <td>692 Joliet Street</td>
        <td>Attika</td>
        <td>38</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Barbara</td>
        <td>Jones</td>
        <td>1566 Inegl Manor</td>
        <td>Mandalay</td>
        <td>349</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Elizabeth</td>
        <td>Brown</td>
        <td>53 Idfu Parkway</td>
        <td>Nantou</td>
        <td>361</td>
    </tr>
</table>



### Different types of join
In addition to `INNER JOIN`, you can also use `OUTER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `CROSS JOIN`. Since the syntax is essentially the same, I'll explain how they work.

### `INNER JOIN`
Find records in table 1 that have a match in table 2, ignoring records that don't appear in both tables. This is how the example above works.

### `OUTER JOIN`
Preserve all records from both tables. If a record from table 1 has a match in table 2, join them together. If a record from table 1 doesn't have a match in table 2, return the `NULL` values for the columns from table 2 (and vice versa).

### `LEFT JOIN` & `RIGHT JOIN`
In a `LEFT JOIN`, all data from the left table is preserved, with matching data from the right table join where it exists. In a `RIGHT JOIN`, the data from the right table is preserved instead.

The 'leftmost' table is the first table specified in your query. For example, in the query above `customer` is the left table and `address` is the right table.

### `CROSS JOIN`
Match all possible combinations of two tables. As you might expect, this can lead to very large tables and is probably the least common type of join. To deomnstrate, let's `CROSS JOIN` a small sub-selection on the `film` and `language` tables:


```python
%%sql

SELECT
    f.film_id
    , f.title
FROM
    film f
WHERE
    f.film_id < 4
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Ace Goldfinger</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Adaptation Holes</td>
    </tr>
</table>




```python
%%sql

SELECT
    l.language_id
    , l.name
FROM
    language l
WHERE
    l.language_id < 4
```




<table>
    <tr>
        <th>language_id</th>
        <th>name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>2</td>
        <td>Italian             </td>
    </tr>
    <tr>
        <td>3</td>
        <td>Japanese            </td>
    </tr>
</table>




```python
%%sql

SELECT
    f.film_id
    , f.title
    , l.language_id
    , l.name
FROM
    film f
    CROSS JOIN language l
WHERE
    f.film_id < 4
    AND l.language_id < 4
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>language_id</th>
        <th>name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
        <td>1</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
        <td>2</td>
        <td>Italian             </td>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
        <td>3</td>
        <td>Japanese            </td>
    </tr>
    <tr>
        <td>2</td>
        <td>Ace Goldfinger</td>
        <td>1</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>2</td>
        <td>Ace Goldfinger</td>
        <td>2</td>
        <td>Italian             </td>
    </tr>
    <tr>
        <td>2</td>
        <td>Ace Goldfinger</td>
        <td>3</td>
        <td>Japanese            </td>
    </tr>
    <tr>
        <td>3</td>
        <td>Adaptation Holes</td>
        <td>1</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>3</td>
        <td>Adaptation Holes</td>
        <td>2</td>
        <td>Italian             </td>
    </tr>
    <tr>
        <td>3</td>
        <td>Adaptation Holes</td>
        <td>3</td>
        <td>Japanese            </td>
    </tr>
</table>



### `UNION`
Combine the results of two or more `SELECT` statements into a single table. Returned results are stacked one above the other, not side-by-side as with the `JOIN`s listed above:


```python
%%sql

SELECT
    a.actor_id
    , a.first_name
    , a.last_name
FROM
    actor a
WHERE
    a.actor_id < 4
```




<table>
    <tr>
        <th>actor_id</th>
        <th>first_name</th>
        <th>last_name</th>
    </tr>
    <tr>
        <td>2</td>
        <td>Nick</td>
        <td>Wahlberg</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Linda</td>
        <td>Williams</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Ed</td>
        <td>Chase</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Mary</td>
        <td>Smith</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Penelope</td>
        <td>Guiness</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Patricia</td>
        <td>Johnson</td>
    </tr>
</table>




```python
%%sql

SELECT
    c.customer_id
    , c.first_name
    , c.last_name
FROM
    customer c
WHERE
    c.customer_id < 4
```




<table>
    <tr>
        <th>customer_id</th>
        <th>first_name</th>
        <th>last_name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Mary</td>
        <td>Smith</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Patricia</td>
        <td>Johnson</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Linda</td>
        <td>Williams</td>
    </tr>
</table>




```python
%%sql

SELECT
    a.actor_id
    , a.first_name
    , a.last_name
FROM
    actor a
WHERE
    a.actor_id < 4
    
UNION

SELECT
    c.customer_id
    , c.first_name
    , c.last_name
FROM
    customer c
WHERE
    c.customer_id < 4
```




<table>
    <tr>
        <th>actor_id</th>
        <th>first_name</th>
        <th>last_name</th>
    </tr>
    <tr>
        <td>2</td>
        <td>Nick</td>
        <td>Wahlberg</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Linda</td>
        <td>Williams</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Ed</td>
        <td>Chase</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Mary</td>
        <td>Smith</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Penelope</td>
        <td>Guiness</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Patricia</td>
        <td>Johnson</td>
    </tr>
</table>



If there were any duplicate rows in these results, `UNION` would have removed them. To preserve all rows including duplicates, use `UNION ALL`.
