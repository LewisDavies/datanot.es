Title: Conditional Expressions with CASE
Slug: sql/conditional-expressions-with-case
Category: SQL
Tags: SELECT, FROM, LIMIT, CASE
Date: 2017-08-15
Modified: 2017-08-15

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



#### Sample from `film` table


```python
%%sql

SELECT
    f.film_id
    , f.title
    , f.rental_rate
    , f.length
FROM
    film f
LIMIT
    5
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>rental_rate</th>
        <th>length</th>
    </tr>
    <tr>
        <td>133</td>
        <td>Chamber Italian</td>
        <td>4.99</td>
        <td>117</td>
    </tr>
    <tr>
        <td>384</td>
        <td>Grosse Wonderful</td>
        <td>4.99</td>
        <td>49</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Airport Pollock</td>
        <td>4.99</td>
        <td>54</td>
    </tr>
    <tr>
        <td>98</td>
        <td>Bright Encounters</td>
        <td>4.99</td>
        <td>73</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
        <td>0.99</td>
        <td>86</td>
    </tr>
</table>



#### Using aggregates


```python
%%sql
SELECT
    f.film_id
    , f.title
    , CASE
        WHEN f.length > 160 THEN 'Way too long'
        WHEN f.length > 120 THEN 'Getting a bit bored now'
        WHEN f.length > 80 THEN 'Goldilocks zone'
        ELSE 'Bit of a rip-off'
        END
FROM
    film f
LIMIT
    10
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>case</th>
    </tr>
    <tr>
        <td>133</td>
        <td>Chamber Italian</td>
        <td>Goldilocks zone</td>
    </tr>
    <tr>
        <td>384</td>
        <td>Grosse Wonderful</td>
        <td>Bit of a rip-off</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Airport Pollock</td>
        <td>Bit of a rip-off</td>
    </tr>
    <tr>
        <td>98</td>
        <td>Bright Encounters</td>
        <td>Bit of a rip-off</td>
    </tr>
    <tr>
        <td>1</td>
        <td>Academy Dinosaur</td>
        <td>Goldilocks zone</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Ace Goldfinger</td>
        <td>Bit of a rip-off</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Adaptation Holes</td>
        <td>Bit of a rip-off</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Affair Prejudice</td>
        <td>Goldilocks zone</td>
    </tr>
    <tr>
        <td>5</td>
        <td>African Egg</td>
        <td>Getting a bit bored now</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Agent Truman</td>
        <td>Way too long</td>
    </tr>
</table>
