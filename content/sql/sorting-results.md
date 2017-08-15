Title: Sorting Results
Slug: sql/sorting-results
Category: SQL
Tags: SELECT, FROM, ORDER BY, LIMIT
Date: 2017-08-11
Modified: 2017-08-11

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



### Sort by a single column


```python
%%sql

SELECT
    f.film_id
    , f.title
    , f.rental_rate
    , f.length
FROM
    film f
ORDER BY
    f.length DESC
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
        <td>212</td>
        <td>Darn Forrester</td>
        <td>4.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>141</td>
        <td>Chicago North</td>
        <td>4.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>182</td>
        <td>Control Anthem</td>
        <td>4.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>426</td>
        <td>Home Pity</td>
        <td>4.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>349</td>
        <td>Gangs Pride</td>
        <td>2.99</td>
        <td>185</td>
    </tr>
</table>



### Sort by multiple columns


```python
%%sql

SELECT
    f.film_id
    , f.title
    , f.rental_rate
    , f.length
FROM
    film f
ORDER BY
    f.length DESC
    , f.rental_rate ASC
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
        <td>609</td>
        <td>Muscle Bright</td>
        <td>2.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>690</td>
        <td>Pond Seattle</td>
        <td>2.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>349</td>
        <td>Gangs Pride</td>
        <td>2.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>991</td>
        <td>Worst Banger</td>
        <td>2.99</td>
        <td>185</td>
    </tr>
    <tr>
        <td>872</td>
        <td>Sweet Brotherhood</td>
        <td>2.99</td>
        <td>185</td>
    </tr>
</table>
