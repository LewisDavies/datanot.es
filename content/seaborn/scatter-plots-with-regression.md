Title: Scatter Plots with Regression
Slug: seaborn/scatter-plots-with-regression
Category: Seaborn
Tags: load_dataset, head, lmplot, xlabel, ylabel, show
Date: 2017-09-26
Modified: 2017-09-26

#### Import libraries


```python
# Although not strictly required, importing pyplot allows for
# greater customization as Seaborn is built upon it
import matplotlib.pyplot as plt
import seaborn as sns
```

#### Load and inspect data


```python
df = sns.load_dataset('tips')
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>total_bill</th>
      <th>tip</th>
      <th>sex</th>
      <th>smoker</th>
      <th>day</th>
      <th>time</th>
      <th>size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16.99</td>
      <td>1.01</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10.34</td>
      <td>1.66</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.01</td>
      <td>3.50</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>23.68</td>
      <td>3.31</td>
      <td>Male</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>24.59</td>
      <td>3.61</td>
      <td>Female</td>
      <td>No</td>
      <td>Sun</td>
      <td>Dinner</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



#### Basic scatter plot
We use `lmplot` to plt two continuous variables against each other. The shaded area represents the 95% condfidence interval.


```python
sns.lmplot(x='total_bill', y='tip', data=df)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
```


![png](../images/scatter-plots-with-regression_6_0.png)


#### Separating our variables
Adding a `hue` argument lets us distinguish between different groups. Here we can see that tips from non-smokers were generally higher than from smokers.


```python
sns.lmplot(x='total_bill', y='tip', hue='smoker', data=df)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
```


![png](../images/scatter-plots-with-regression_8_0.png)


#### Adjusting the confidence interval
By default, Seaborn takes 1000 bootstrap samples of your data and uses a 95% confidence interval. Our regression line can also be changed to a polynomial.

Be careful when tweaking these parameters if your dataset is large — you might have to wait a while!


```python
sns.lmplot(x='total_bill', y='tip', hue='smoker',
           ci=99, n_boot=1500, order=3, data=df)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
```


![png](../images/scatter-plots-with-regression_10_0.png)


As always, [check the docs](https://seaborn.pydata.org/generated/seaborn.lmplot.html#seaborn.lmplot) for loads more options.
