Title: Basic Filtering with WHERE
Slug: sql/basic-filtering-with-where
Category: SQL
Tags: SELECT, FROM, WHERE, AND, OR
Date: 2017-08-07
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



### A simple example


```python
%%sql

SELECT
    *
FROM
    customer_list cl
WHERE
    -- Note that equality tests use just one equals sign
    cl.country = 'Canada'
```




<table>
    <tr>
        <th>id</th>
        <th>name</th>
        <th>address</th>
        <th>zip code</th>
        <th>phone</th>
        <th>city</th>
        <th>country</th>
        <th>notes</th>
        <th>sid</th>
    </tr>
    <tr>
        <td>476</td>
        <td>Derrick Bourque</td>
        <td>1153 Allende Way</td>
        <td>20336</td>
        <td>856872225376</td>
        <td>Gatineau</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>463</td>
        <td>Darrell Power</td>
        <td>1844 Usak Avenue</td>
        <td>84461</td>
        <td>164414772677</td>
        <td>Halifax</td>
        <td>Canada</td>
        <td>active</td>
        <td>2</td>
    </tr>
    <tr>
        <td>189</td>
        <td>Loretta Carpenter</td>
        <td>891 Novi Sad Manor</td>
        <td>5379</td>
        <td>247646995453</td>
        <td>Oshawa</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>410</td>
        <td>Curtis Irby</td>
        <td>432 Garden Grove Street</td>
        <td>65630</td>
        <td>615964523510</td>
        <td>Richmond Hill</td>
        <td>Canada</td>
        <td>active</td>
        <td>2</td>
    </tr>
    <tr>
        <td>436</td>
        <td>Troy Quigley</td>
        <td>983 Santa F Way</td>
        <td>47472</td>
        <td>145720452260</td>
        <td>Vancouver</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
</table>



### Filter on multiple conditions with AND


```python
%%sql

SELECT
    *
FROM
    customer_list cl
WHERE
    cl.country = 'Canada'
    AND cl.sid = 1
```




<table>
    <tr>
        <th>id</th>
        <th>name</th>
        <th>address</th>
        <th>zip code</th>
        <th>phone</th>
        <th>city</th>
        <th>country</th>
        <th>notes</th>
        <th>sid</th>
    </tr>
    <tr>
        <td>476</td>
        <td>Derrick Bourque</td>
        <td>1153 Allende Way</td>
        <td>20336</td>
        <td>856872225376</td>
        <td>Gatineau</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>189</td>
        <td>Loretta Carpenter</td>
        <td>891 Novi Sad Manor</td>
        <td>5379</td>
        <td>247646995453</td>
        <td>Oshawa</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>436</td>
        <td>Troy Quigley</td>
        <td>983 Santa F Way</td>
        <td>47472</td>
        <td>145720452260</td>
        <td>Vancouver</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
</table>



### The OR operator


```python
%%sql

SELECT
    *
FROM
    customer_list cl
WHERE
    cl.country = 'Canada'
    OR cl.city = 'Graz'
```




<table>
    <tr>
        <th>id</th>
        <th>name</th>
        <th>address</th>
        <th>zip code</th>
        <th>phone</th>
        <th>city</th>
        <th>country</th>
        <th>notes</th>
        <th>sid</th>
    </tr>
    <tr>
        <td>476</td>
        <td>Derrick Bourque</td>
        <td>1153 Allende Way</td>
        <td>20336</td>
        <td>856872225376</td>
        <td>Gatineau</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>173</td>
        <td>Audrey Ray</td>
        <td>1010 Klerksdorp Way</td>
        <td>6802</td>
        <td>493008546874</td>
        <td>Graz</td>
        <td>Austria</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>463</td>
        <td>Darrell Power</td>
        <td>1844 Usak Avenue</td>
        <td>84461</td>
        <td>164414772677</td>
        <td>Halifax</td>
        <td>Canada</td>
        <td>active</td>
        <td>2</td>
    </tr>
    <tr>
        <td>189</td>
        <td>Loretta Carpenter</td>
        <td>891 Novi Sad Manor</td>
        <td>5379</td>
        <td>247646995453</td>
        <td>Oshawa</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>410</td>
        <td>Curtis Irby</td>
        <td>432 Garden Grove Street</td>
        <td>65630</td>
        <td>615964523510</td>
        <td>Richmond Hill</td>
        <td>Canada</td>
        <td>active</td>
        <td>2</td>
    </tr>
    <tr>
        <td>436</td>
        <td>Troy Quigley</td>
        <td>983 Santa F Way</td>
        <td>47472</td>
        <td>145720452260</td>
        <td>Vancouver</td>
        <td>Canada</td>
        <td>active</td>
        <td>1</td>
    </tr>
</table>



### Combining operators
This query will return all details of people matching ONE of the following conditions:
- They live in London
- They are named Clive and don't live in Berlin


```python
%%sql

SELECT
    *
FROM
    customer_list cl
WHERE
    cl.city = 'Kabul'
    OR (
        cl.name = 'Cecil Vines'
        AND cl.city = 'London'
    )
```




<table>
    <tr>
        <th>id</th>
        <th>name</th>
        <th>address</th>
        <th>zip code</th>
        <th>phone</th>
        <th>city</th>
        <th>country</th>
        <th>notes</th>
        <th>sid</th>
    </tr>
    <tr>
        <td>218</td>
        <td>Vera Mccoy</td>
        <td>1168 Najafabad Parkway</td>
        <td>40301</td>
        <td>886649065861</td>
        <td>Kabul</td>
        <td>Afghanistan</td>
        <td>active</td>
        <td>1</td>
    </tr>
    <tr>
        <td>512</td>
        <td>Cecil Vines</td>
        <td>548 Uruapan Street</td>
        <td>35653</td>
        <td>879347453467</td>
        <td>London</td>
        <td>United Kingdom</td>
        <td>active</td>
        <td>1</td>
    </tr>
</table>


