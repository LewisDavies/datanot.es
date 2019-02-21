Title: Importing Data
Slug: pandas/importing-data
Category: Pandas
Tags: read_csv, read_excel, psycopg2
Date: 2017-08-01
Modified: 2019-02-20

### Import libraries


```python
import pandas as pd
```

### CSV


```python
# If the file is in your current working directory, you can use the filename as an arguement
df = pd.read_csv('data.csv')

# If the raw data is somewhere else, you'll need to specifiy the full path
file = '/path/to/file/data.csv'
df = pd.read_csv(file)

# You can specify the separator with the sep argument
df = pd.read_csv(file, sep=';')
```

### Excel 


```python
# By default, a DataFrame will be created from the first sheet of your Excel file
df = pd.read_excel('data.xlsx')

# We can specify the sheet to import with the sheetname argument (an integer or string)
df = pd.read_excel('data.xlsx', sheetname=1) # returns second sheet

# Specifying multiple sheets will return a dictionary of DataFrames
df_dict = pd.read_excel('data.xlsx', sheetname=[0, 2, 'Sheet4', 'Sales 2016'])
```

### SQL
Your credentials should always be stored in a separate location so you can share your notebook without sharing your login details. Ideally this would be in environment variables or your keychain, but a simple solution is to save them in a separate Python file and load them with the code below. **Make sure you don't commit these to git.**

Your ```db.py``` file should look like this:


```python
# Example db.py file
user = 'your_username'
password = 'your_super_tricky_password'
host = 'your_hostname'
port = 5432 # this is a common setting
database = 'your_database_identifier'
```


```python
# Load database credentials
exec(open("/path/to/file/db.py").read())
```


```python
# I mainly interact with a PostgreSQL database, so I use an additional library for this
import psycopg2

# We connect to the database - use the variable names from db.py
con = psycopg2.connect(user=user, password=password, host=host, port=port, database=database)

query = """
select
    c.id
    , c.name
    , c.city
from
    customers c
limit
    10
"""

# Then run the query, save the output as a DataFrame
df = pd.read_sql(query, con)

# And finally disconnect from the database
con.close()
```

### Some useful arguments


```python
# Specify a column to use as the index
df = pd.read_csv('data.csv', index_col=2)

# Change column names - length of names list must match the number of columns
df = pd.read_csv('data.csv', names=['Name', 'Age', 'Score'])

# If parse_dates = True, pandas will try to conver the index to datetime
df = pd.read_csv('data.csv', parse_dates=True)

# You can also pass in a list of columns to parse as datetimes
df = pd.read_csv('data.csv', parse_dates=['account_created_at', 'last_order_date']
```
