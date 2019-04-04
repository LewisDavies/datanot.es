Title: Importing Data
Slug: pandas/importing-data
Category: Pandas
Tags: read_csv, read_excel, psycopg2
Date: 2017-08-01
Modified: 2019-04-02

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
