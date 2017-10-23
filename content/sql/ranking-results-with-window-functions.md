Title: Ranking Results with Window Functions
Slug: sql/ranking-results-with-window-functions
Category: SQL
Tags: SELECT, FROM, LIMIT, WHERE, OVER, PARTITION BY, ORDER BY, DESC, rank
Date: 2017-08-15
Modified: 2017-08-16

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



#### Ranking results
Using the `OVER` clause allows us to run a function on the results returned from the database. In this example we rank films from longest to shortest at each rental rate.


```python
%%sql

SELECT
    f.film_id
    , f.title
    , f.rental_rate
    , f.length
    , rank() OVER(PARTITION BY f.rental_rate ORDER BY f.length DESC) as rk
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
        <th>rk</th>
    </tr>
    <tr>
        <td>813</td>
        <td>Smoochy Control</td>
        <td>0.99</td>
        <td>184</td>
        <td>1</td>
    </tr>
    <tr>
        <td>886</td>
        <td>Theory Mermaid</td>
        <td>0.99</td>
        <td>184</td>
        <td>1</td>
    </tr>
    <tr>
        <td>821</td>
        <td>Sorority Queen</td>
        <td>0.99</td>
        <td>184</td>
        <td>1</td>
    </tr>
    <tr>
        <td>996</td>
        <td>Young Language</td>
        <td>0.99</td>
        <td>183</td>
        <td>4</td>
    </tr>
    <tr>
        <td>128</td>
        <td>Catch Amistad</td>
        <td>0.99</td>
        <td>183</td>
        <td>4</td>
    </tr>
</table>



Note that since 3 films are tied for first place, the rank given to the next longest films is 4. If we wanted the next rank to be 2 instead, we could use `dense_rank` in place of `rank`.

#### Working with our rankings
Once you've made the query above, we can use it as a [Common Table Expression]({{ SITEURL }}/sql/common-table-expressions.html) to filter it. For example, let's try to find the 3 longest films at each price point.


```python
%%sql

WITH film_cte AS (
    SELECT
        f.film_id
        , f.title
        , f.rental_rate
        , f.length
        , rank() OVER(PARTITION BY f.rental_rate ORDER BY f.length DESC) as rk
    FROM
        film f
)

SELECT
    *
FROM
    film_cte fc
WHERE
    fc.rk < 4
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>rental_rate</th>
        <th>length</th>
        <th>rk</th>
    </tr>
    <tr>
        <td>813</td>
        <td>Smoochy Control</td>
        <td>0.99</td>
        <td>184</td>
        <td>1</td>
    </tr>
    <tr>
        <td>886</td>
        <td>Theory Mermaid</td>
        <td>0.99</td>
        <td>184</td>
        <td>1</td>
    </tr>
    <tr>
        <td>821</td>
        <td>Sorority Queen</td>
        <td>0.99</td>
        <td>184</td>
        <td>1</td>
    </tr>
    <tr>
        <td>690</td>
        <td>Pond Seattle</td>
        <td>2.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>872</td>
        <td>Sweet Brotherhood</td>
        <td>2.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>991</td>
        <td>Worst Banger</td>
        <td>2.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>349</td>
        <td>Gangs Pride</td>
        <td>2.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>609</td>
        <td>Muscle Bright</td>
        <td>2.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>426</td>
        <td>Home Pity</td>
        <td>4.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>817</td>
        <td>Soldiers Evolution</td>
        <td>4.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>212</td>
        <td>Darn Forrester</td>
        <td>4.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>182</td>
        <td>Control Anthem</td>
        <td>4.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>141</td>
        <td>Chicago North</td>
        <td>4.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
</table>



#### Tailoring our results
Hmm, it looks like more than three films are tied in the £2.99 and £4.99 price bands. If we want to avoid this, one option is to use `row_number`, specifying how to sort the results.

Now we'll return the 3 longest films at each rental rate in alphabetical order.


```python
%%sql

WITH film_ranked AS (
    SELECT
        f.film_id
        , f.title
        , f.rental_rate
        , f.length
        , row_number() OVER(PARTITION BY f.rental_rate ORDER BY f.length DESC, f.title ASC) as rk
    FROM
        film f
)

SELECT
    *
FROM
    film_ranked fr
WHERE
    fr.rk < 4
```




<table>
    <tr>
        <th>film_id</th>
        <th>title</th>
        <th>rental_rate</th>
        <th>length</th>
        <th>rk</th>
    </tr>
    <tr>
        <td>813</td>
        <td>Smoochy Control</td>
        <td>0.99</td>
        <td>184</td>
        <td>1</td>
    </tr>
    <tr>
        <td>821</td>
        <td>Sorority Queen</td>
        <td>0.99</td>
        <td>184</td>
        <td>2</td>
    </tr>
    <tr>
        <td>886</td>
        <td>Theory Mermaid</td>
        <td>0.99</td>
        <td>184</td>
        <td>3</td>
    </tr>
    <tr>
        <td>349</td>
        <td>Gangs Pride</td>
        <td>2.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>609</td>
        <td>Muscle Bright</td>
        <td>2.99</td>
        <td>185</td>
        <td>2</td>
    </tr>
    <tr>
        <td>690</td>
        <td>Pond Seattle</td>
        <td>2.99</td>
        <td>185</td>
        <td>3</td>
    </tr>
    <tr>
        <td>141</td>
        <td>Chicago North</td>
        <td>4.99</td>
        <td>185</td>
        <td>1</td>
    </tr>
    <tr>
        <td>182</td>
        <td>Control Anthem</td>
        <td>4.99</td>
        <td>185</td>
        <td>2</td>
    </tr>
    <tr>
        <td>212</td>
        <td>Darn Forrester</td>
        <td>4.99</td>
        <td>185</td>
        <td>3</td>
    </tr>
</table>



There are lots of other window functions that can also be used here. [Check the Postgres docs](https://www.postgresql.org/docs/current/static/functions-window.html) for full details.
