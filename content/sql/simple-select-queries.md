Title: Simple SELECT Queries
Slug: sql/simple-select-queries
Category: SQL
Tags: SELECT, FROM
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



### Select all rows and columns


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



### Select specific columns
Columns are separated by commas. Putting the comma on the following line makes it simpler to comment out columns when testing your query.


```python
%%sql

SELECT
    c.category_id
    , c.name
FROM
    category c
```




<table>
    <tr>
        <th>category_id</th>
        <th>name</th>
    </tr>
    <tr>
        <td>1</td>
        <td>Action</td>
    </tr>
    <tr>
        <td>2</td>
        <td>Animation</td>
    </tr>
    <tr>
        <td>3</td>
        <td>Children</td>
    </tr>
    <tr>
        <td>4</td>
        <td>Classics</td>
    </tr>
    <tr>
        <td>5</td>
        <td>Comedy</td>
    </tr>
    <tr>
        <td>6</td>
        <td>Documentary</td>
    </tr>
    <tr>
        <td>7</td>
        <td>Drama</td>
    </tr>
    <tr>
        <td>8</td>
        <td>Family</td>
    </tr>
    <tr>
        <td>9</td>
        <td>Foreign</td>
    </tr>
    <tr>
        <td>10</td>
        <td>Games</td>
    </tr>
    <tr>
        <td>11</td>
        <td>Horror</td>
    </tr>
    <tr>
        <td>12</td>
        <td>Music</td>
    </tr>
    <tr>
        <td>13</td>
        <td>New</td>
    </tr>
    <tr>
        <td>14</td>
        <td>Sci-Fi</td>
    </tr>
    <tr>
        <td>15</td>
        <td>Sports</td>
    </tr>
    <tr>
        <td>16</td>
        <td>Travel</td>
    </tr>
</table>


