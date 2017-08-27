Title: Subqueries
Slug: sql/subqueries
Category: SQL
Tags: SELECT, CAST, FROM, WHERE, LIMIT, avg
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



#### Using a subquery as a condition


```python
%%sql

SELECT
    f.film_id
    , f.title
    , f.length
FROM
    film f
WHERE
    f.length > (
        SELECT
            avg(f.length)
        FROM
            film f
    )
LIMIT
    5
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>length</th>
    </tr>
    <tr>
        <td>133</td>
        <td>Chamber Italian</td>
        <td>117</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Affair Prejudice</td>
        <td>117</td>
    </tr>
    <tr>
        <td>5</td>
        <td>African Egg</td>
        <td>130</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Agent Truman</td>
        <td>169</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Alamo Videotape</td>
        <td>126</td>
    </tr>
</table>



#### Selecting a column with a subquery
This isn't the most practical example, but you can select individual columns using a subquery.


```python
%%sql

SELECT
    f.film_id
    , f.title
    , f.length
    , (SELECT l.name FROM language l WHERE l.language_id = f.language_id)
FROM
    film f
LIMIT
    5
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>length</th>
        <th>name</th>
    </tr>
    <tr>
        <td>133</td>
        <td>Chamber Italian</td>
        <td>117</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>384</td>
        <td>Grosse Wonderful</td>
        <td>49</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>8</td>
        <td>Airport Pollock</td>
        <td>54</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>98</td>
        <td>Bright Encounters</td>
        <td>73</td>
        <td>English             </td>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
        <td>86</td>
        <td>English             </td>
    </tr>
</table>
