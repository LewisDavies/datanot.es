Title: Filtering Aggregates with HAVING
Slug: sql/filtering-aggregates-with-having
Category: SQL
Tags: SELECT, FROM, LIMIT, GROUP BY, avg
Date: 2017-08-09
Modified: 2017-08-09

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
    f.rental_rate
    , avg(f.length)
FROM
    film f
GROUP BY
    f.rental_rate
```




<table>
    <tr>
        <th>rental_rate</th>
        <th>avg</th>
    </tr>
    <tr>
        <td>4.99</td>
        <td>115.8244047619047619</td>
    </tr>
    <tr>
        <td>0.99</td>
        <td>112.9120234604105572</td>
    </tr>
    <tr>
        <td>2.99</td>
        <td>117.1888544891640867</td>
    </tr>
</table>



#### Filtering on returned aggregates


```python
%%sql

SELECT
    f.rental_rate
    , avg(f.length)
FROM
    film f
GROUP BY
    f.rental_rate
HAVING
    avg(f.length) > 117
```




<table>
    <tr>
        <th>rental_rate</th>
        <th>avg</th>
    </tr>
    <tr>
        <td>2.99</td>
        <td>117.1888544891640867</td>
    </tr>
</table>
