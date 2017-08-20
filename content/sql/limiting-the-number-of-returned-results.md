Title: Limiting the Number of Returned Results
Slug: sql/limiting-the-number-of-returned-results
Category: SQL
Tags: SELECT, FROM, LIMIT, OFFSET
Date: 2017-08-11
Modified: 2017-08-11

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



#### Sample data


```python
%%sql

SELECT
    *
FROM
    category c
```




<table>
    <tr>
        <th>category_id</th>
        <th>name</th>
        <th>last_update</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Action</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Animation</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Children</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Classics</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Comedy</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Documentary</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Drama</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Family</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Foreign</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Games</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Horror</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Music</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>13</td>
        <td>New</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Sci-Fi</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Sports</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Travel</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
</table>



#### Using LIMIT


```python
%%sql

SELECT
    *
FROM
    category c
LIMIT
    5
```




<table>
    <tr>
        <th>category_id</th>
        <th>name</th>
        <th>last_update</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Action</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Animation</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Children</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Classics</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Comedy</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
</table>



#### Removing the first *n* results


```python
%%sql

SELECT
    *
FROM
    category c
LIMIT
    5
OFFSET
    5
```




<table>
    <tr>
        <th>category_id</th>
        <th>name</th>
        <th>last_update</th>
    </tr>
    <tr>
        <td>6</td>
        <td>Documentary</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Drama</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Family</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Foreign</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Games</td>
        <td>2006-02-15 09:46:27</td>
    </tr>
</table>
