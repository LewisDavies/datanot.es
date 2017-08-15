Title: Removing Duplicate Rows
Slug: sql/removing-duplicate-rows
Category: SQL
Tags: SELECT, FROM, WHERE, DISTINCT, DISTINCT ON
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



### Sample data


```python
%%sql

SELECT
    a.district
FROM
    address a
WHERE
    a.district = 'Saitama'
```




<table>
    <tr>
        <th>district</th>
    </tr>
    <tr>
        <td>Saitama</td>
    </tr>
    <tr>
        <td>Saitama</td>
    </tr>
    <tr>
        <td>Saitama</td>
    </tr>
</table>



### Remove duplicates with `DISTINCT`


```python
%%sql

SELECT DISTINCT
    a.district
FROM
    address a
WHERE
    a.district = 'Saitama'
```




<table>
    <tr>
        <th>district</th>
    </tr>
    <tr>
        <td>Saitama</td>
    </tr>
</table>



### Using `DISTINCT ON`
The above example was pretty unrealistic, I'll admit. However, you can include more columns and remove duplicates based on just one with `DISTINCT ON`.


```python
%%sql

SELECT
    *
FROM
    address a
WHERE
    a.district = 'Saitama'
```




<table>
    <tr>
        <th>address_id</th>
        <th>address</th>
        <th>address2</th>
        <th>district</th>
        <th>city_id</th>
        <th>postal_code</th>
        <th>phone</th>
        <th>last_update</th>
    </tr>
    <tr>
        <td>151</td>
        <td>1337 Lincoln Parkway</td>
        <td></td>
        <td>Saitama</td>
        <td>555</td>
        <td>99457</td>
        <td>597815221267</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>401</td>
        <td>168 Cianjur Manor</td>
        <td></td>
        <td>Saitama</td>
        <td>228</td>
        <td>73824</td>
        <td>679095087143</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>409</td>
        <td>1266 Laredo Parkway</td>
        <td></td>
        <td>Saitama</td>
        <td>380</td>
        <td>7664</td>
        <td>1483365694</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
</table>




```python
%%sql

SELECT DISTINCT ON (a.district)
    *
FROM
    address a
WHERE
    a.district = 'Saitama'
```




<table>
    <tr>
        <th>address_id</th>
        <th>address</th>
        <th>address2</th>
        <th>district</th>
        <th>city_id</th>
        <th>postal_code</th>
        <th>phone</th>
        <th>last_update</th>
    </tr>
    <tr>
        <td>151</td>
        <td>1337 Lincoln Parkway</td>
        <td></td>
        <td>Saitama</td>
        <td>555</td>
        <td>99457</td>
        <td>597815221267</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
</table>



Please remember that the use of `DISTINCT` is often considered 'code smell', meaning it signifies something is wrong with your code. Whenever possible, it's best to avoid duplicates with goods joins and filters instead.
