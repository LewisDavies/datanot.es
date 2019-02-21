Title: Working with Strings
Slug: sql/working-with-strings
Category: SQL
Tags: SELECT, FROM, JOIN, LIMIT, ||, upper, lower, substring, left, right
Date: 2017-08-27
Modified: 2017-08-27

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



### Manipulating strings
**`||`**: Concatenate two or more strings together

**`upper`**: Convert to uppercase

**`lower`**: Convert to lowercase


```python
%%sql

SELECT
    ci.city
    , ci.city || ', ' || co.country as concatenated
    , upper(ci.city)
    , lower(ci.city)
FROM
    city ci
    JOIN country co on co.country_id = ci.country_id
LIMIT
    5
```




<table>
    <tr>
        <th>city</th>
        <th>concatenated</th>
        <th>upper</th>
        <th>lower</th>
    </tr>
    <tr>
        <td>Kabul</td>
        <td>Kabul, Afghanistan</td>
        <td>KABUL</td>
        <td>kabul</td>
    </tr>
    <tr>
        <td>Batna</td>
        <td>Batna, Algeria</td>
        <td>BATNA</td>
        <td>batna</td>
    </tr>
    <tr>
        <td>Bchar</td>
        <td>Bchar, Algeria</td>
        <td>BCHAR</td>
        <td>bchar</td>
    </tr>
    <tr>
        <td>Skikda</td>
        <td>Skikda, Algeria</td>
        <td>SKIKDA</td>
        <td>skikda</td>
    </tr>
    <tr>
        <td>Tafuna</td>
        <td>Tafuna, American Samoa</td>
        <td>TAFUNA</td>
        <td>tafuna</td>
    </tr>
</table>



### Substrings
**`substring`**: Return a substring based on an index (starting from 1) or a regular expression

**`left`**: Return first $n$ characters

**`right`**: Return last $n$ characters

`left` and `right` can also take negative indexes to trim characters from the opposite end of the string.


```python
%%sql

SELECT
    ci.city
    , substring(ci.city from 1 for 2)
    , substring(ci.city from 3)
    , left(ci.city, 2)
    , right(ci.city, 3)
    , left(ci.city, -3) AS left_neg
    , right(ci.city, -2) AS right_pos
FROM
    city ci
    JOIN country co on co.country_id = ci.country_id
LIMIT
    5
```




<table>
    <tr>
        <th>city</th>
        <th>substring</th>
        <th>substring_1</th>
        <th>left</th>
        <th>right</th>
        <th>left_neg</th>
        <th>right_pos</th>
    </tr>
    <tr>
        <td>Kabul</td>
        <td>Ka</td>
        <td>bul</td>
        <td>Ka</td>
        <td>bul</td>
        <td>Ka</td>
        <td>bul</td>
    </tr>
    <tr>
        <td>Batna</td>
        <td>Ba</td>
        <td>tna</td>
        <td>Ba</td>
        <td>tna</td>
        <td>Ba</td>
        <td>tna</td>
    </tr>
    <tr>
        <td>Bchar</td>
        <td>Bc</td>
        <td>har</td>
        <td>Bc</td>
        <td>har</td>
        <td>Bc</td>
        <td>har</td>
    </tr>
    <tr>
        <td>Skikda</td>
        <td>Sk</td>
        <td>ikda</td>
        <td>Sk</td>
        <td>kda</td>
        <td>Ski</td>
        <td>ikda</td>
    </tr>
    <tr>
        <td>Tafuna</td>
        <td>Ta</td>
        <td>funa</td>
        <td>Ta</td>
        <td>una</td>
        <td>Taf</td>
        <td>funa</td>
    </tr>
</table>



This is just a selection of the string methods available in Postgres. For more examples, [see the docs](https://www.postgresql.org/docs/current/static/functions-string.html).
