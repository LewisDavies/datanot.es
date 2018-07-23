Title: Box and Whisker Plots with Alternatives
Slug: seaborn/box-and-whisker-plots-with-alternatives
Category: Seaborn
Tags: load_dataset, head, boxplot, violinplot, stripplot, swarmplot
Date: 2018-07-23
Modified: 2018-07-23

#### Import libraries


```python
import seaborn as sns
sns.set_style('darkgrid')
```

#### Load and inspect data


```python
df = sns.load_dataset('mpg')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>cylinders</th>
      <th>displacement</th>
      <th>horsepower</th>
      <th>weight</th>
      <th>acceleration</th>
      <th>model_year</th>
      <th>origin</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>8</td>
      <td>307.0</td>
      <td>130.0</td>
      <td>3504</td>
      <td>12.0</td>
      <td>70</td>
      <td>usa</td>
      <td>chevrolet chevelle malibu</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>8</td>
      <td>350.0</td>
      <td>165.0</td>
      <td>3693</td>
      <td>11.5</td>
      <td>70</td>
      <td>usa</td>
      <td>buick skylark 320</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>8</td>
      <td>318.0</td>
      <td>150.0</td>
      <td>3436</td>
      <td>11.0</td>
      <td>70</td>
      <td>usa</td>
      <td>plymouth satellite</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.0</td>
      <td>8</td>
      <td>304.0</td>
      <td>150.0</td>
      <td>3433</td>
      <td>12.0</td>
      <td>70</td>
      <td>usa</td>
      <td>amc rebel sst</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.0</td>
      <td>8</td>
      <td>302.0</td>
      <td>140.0</td>
      <td>3449</td>
      <td>10.5</td>
      <td>70</td>
      <td>usa</td>
      <td>ford torino</td>
    </tr>
  </tbody>
</table>
</div>



#### A simple box and whiskers plot
Box and whisker plots let us plot a continuous variable against a categorical variable. The box itself shows the upper and lower quartiles alongside the median, with the whiskers extending to 1.5 times the inter-quartile range by default. Any points outside this range are outliers.

First we plot the miles per gallon of various cars according to where they were designed. Next, a new column showing whether the car was made after 1975 is made and the data is split according to this.


```python
sns.boxplot(data=df, x='origin', y='mpg');
```


![png](box-and-whisker-plots-with-alternatives_files/box-and-whisker-plots-with-alternatives_6_0.png)



```python
df['year > 1975'] = df['model_year'] > 75
sns.boxplot(data=df, x='origin', y='mpg', hue='year > 1975');
```


![png](box-and-whisker-plots-with-alternatives_files/box-and-whisker-plots-with-alternatives_7_0.png)


#### Alternatives
The main alternative to the box and whisker plot is the violin plot. This combines a box plot with a kernel density estimate, giving us an idea of the underlying distribution of the data. It also present different ways to visualize our dataset.


```python
sns.violinplot(data=df, x='origin', y='mpg');
```


![png](box-and-whisker-plots-with-alternatives_files/box-and-whisker-plots-with-alternatives_9_0.png)



```python
sns.violinplot(data=df, x='origin', y='mpg', hue='year > 1975', split=True);
```


![png](box-and-whisker-plots-with-alternatives_files/box-and-whisker-plots-with-alternatives_10_0.png)


These can be combined with swarm or strip plots to make interesting visualizations.


```python
sns.violinplot(data=df, x='origin', y='mpg', color='lightgray')
sns.stripplot(data=df, x='origin', y='mpg', jitter=True);
```


![png](box-and-whisker-plots-with-alternatives_files/box-and-whisker-plots-with-alternatives_12_0.png)


The Seaborn docs are pretty great and have loads of practical examples. Here are the links for [box plots](https://seaborn.pydata.org/generated/seaborn.boxplot.html), [violin plots](https://seaborn.pydata.org/generated/seaborn.violinplot.html), [strip plots](https://seaborn.pydata.org/generated/seaborn.stripplot.html), and [swarm plots](https://seaborn.pydata.org/generated/seaborn.swarmplot.html).
