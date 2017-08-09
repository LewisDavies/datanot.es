Title: Select Values Appearing in a List
Slug: sql/select-values-appearing-in-a-list
Category: SQL
Tags: SELECT, FROM, WHERE, IN, NOT, LIMIT
Date: 2017-08-08
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



### Find values matching a list with IN


```python
%%sql
SELECT
    *
FROM
    address a
WHERE
    a.district IN ('Alberta', 'Jiangsu')
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
        <td>1</td>
        <td>47 MySakila Drive</td>
        <td>None</td>
        <td>Alberta</td>
        <td>300</td>
        <td></td>
        <td></td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>3</td>
        <td>23 Workhaven Lane</td>
        <td>None</td>
        <td>Alberta</td>
        <td>300</td>
        <td></td>
        <td>14033335568</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>201</td>
        <td>817 Bradford Loop</td>
        <td></td>
        <td>Jiangsu</td>
        <td>109</td>
        <td>89459</td>
        <td>264286442804</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>389</td>
        <td>500 Lincoln Parkway</td>
        <td></td>
        <td>Jiangsu</td>
        <td>210</td>
        <td>95509</td>
        <td>550306965159</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
</table>



### Find values not appearing in a list


```python
%%sql
SELECT
    *
FROM
    address a
WHERE
    a.district NOT IN ('Alberta', 'Jiangsu')
-- For convenience, we'll only show the first 5 results
LIMIT
    5
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
        <td>2</td>
        <td>28 MySQL Boulevard</td>
        <td>None</td>
        <td>QLD</td>
        <td>576</td>
        <td></td>
        <td></td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>4</td>
        <td>1411 Lillydale Drive</td>
        <td>None</td>
        <td>QLD</td>
        <td>576</td>
        <td></td>
        <td>6172235589</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>5</td>
        <td>1913 Hanoi Way</td>
        <td></td>
        <td>Nagasaki</td>
        <td>463</td>
        <td>35200</td>
        <td>28303384290</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>6</td>
        <td>1121 Loja Avenue</td>
        <td></td>
        <td>California</td>
        <td>449</td>
        <td>17886</td>
        <td>838635286649</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
    <tr>
        <td>7</td>
        <td>692 Joliet Street</td>
        <td></td>
        <td>Attika</td>
        <td>38</td>
        <td>83579</td>
        <td>448477190408</td>
        <td>2006-02-15 09:45:30</td>
    </tr>
</table>
