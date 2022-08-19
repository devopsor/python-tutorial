
## Pandas

- [Pandas](#Pandas)
- [Installation](#installation)
- [Pandas Basics](#pandas-basics)

## Pandas 

#### What Is Pandas

**Pandas** is a package that is often used for data manipulation, and organizes data handled by machine learning methods, such as reading data saved in general data formats such as CSV and extracting some data by specifying conditions.

## Installation
```python
pip install pandas
pip install jupyterlab
```

## Pandas Basics

#### Download TestData
Download TestData to path **06_pandas**
* [Stackoverflow Survey](https://insights.stackoverflow.com/survey)

#### Start Jupyter
```python
jupyter notebook
```

#### Load Pandas package
```python
import pandas as pd
```
#### Reading and writing CSV files

```python
#データセットの読み込み
df = pd.read_csv('survey_results_public.csv')
#型の確認
type(df)　#pandas.core.frame.DataFrame
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html

```

#### Viewing DataFrames
```python
df
```

#### Display only the top few
```python
#If you want to check only a few data df.head(), use the method that the data frame has
# df.head()will display the first 5 data by default, but df.head(3)if you specify the number 
# of data you want to display as an argument, you can also display only the specified number
df.head()
df.head(3)

#If you want to extract a specific column, you can specify the name of the column you want 
# to retrieve using , as you would with dfa Python dictionary object
df['longitude'].head(3)
```

#### Saving CSV files
```python
# Pandas provides a method to save the contents of a dataframe object as a CSV file df.to_csv().
df.to_csv('sample.csv')
```

#### Shape of data frame
```python
# To check the number of rows and columns of a dataframe object, df.shape()use methods.
df.shape
```

#### Calculation of statistics
```python
# DataFrames also provide methods for computing statistics on the data within them
#平均
df.mean(numeric_only=True)
#分散
df.var(numeric_only=True)
# 各列の None, NaN, NaT のいずれでもない値の数
df.count()
# データの概要
df.describe()
# 相関係数の算出
df.corr()

```
#### Sorting

```python
# You can sort the values ​​by extracting a column from the df.sort_values()dataframe and calling a method . 
# Note that this method does not replace the values ​​in the original data frame with the values ​​after sorting, and returns the result.
# df.sort_values() sorts in ascending order by default
# ResponseId 列の値を昇順に並べ替え
df_as = df.sort_values(by='ResponseId')
df_as.head()

#If you want to sort in descending order, ascending=False specify the argument.
# ResponseId の列の値を降順に並べ替え
df_de = df.sort_values(by='ResponseId', ascending=False)
df_de.head()
```
#### Data Selection
```python
# There are multiple ways to select columns and rows. df.iloc[]Here we introduce partial selection of data using integer indices .
# データの確認
df.head(3)
# df.iloc[行, 列]
# 0 行目 ResponseId 列の選択
df.iloc[1, 0]
# 1 行目 MainBranch 列の選択
df.iloc[1, 1]
# すべての行の、最後の列を選択
t = df.iloc[:, -1]
# 先頭3件の表示
t.head(3)
# 型の確認
# If only one row or one column is extracted, a Series object is returned.
type(t)
# すべての行の、先頭の列から末尾の列のひとつ手前までを選択
x = df.iloc[:, 0:-1]
# 先頭の3件の表示
x.head(3)
# すべての行の、先頭の列から末尾の列のひとつ手前までを選択
x = df.iloc[:, :-1]
# 先頭の3件の表示
x.head(3)
# 型の確認
type(t)

```
#### Selecting Elements by Specifying Conditions
```python
# ResponseId 列を選択し、全要素に対し 73260 より大きいかどうかを計算
mask = df['ResponseId'] > 73260
mask.head()
# df[mask] の先頭 5 件を表示
df[mask].head()
```
#### Selecting Elements by Specifying Multiple Conditions
```python
# 73265 より小さい または 73260 より大きい
mask2 = (df['ResponseId'] < 73265) | (df['ResponseId'] > 73260)
mask2.head()
df[mask2].head()

mask3 = (df['ResponseId'] < 73265) & (df['ResponseId'] > 73260)
mask3.head()
df[mask3].head()

# You can also write the operation to check the elements that meet the conditions and the selection of 
# the elements that meet the conditions in one line.
df[(df['ResponseId'] > 73260) & (df['ResponseId'] < 73265)].head()

```
#### Replacing Elements Conditionally
```python
# Values ​​can be rewritten for elements selected by specifying conditions. 
# For example, try ResponseId to check some conditions for the columns separately and add a new column that 
# has a certain value if each condition is met df.ResponseId:
# 0 if less than 60000
# 1 for 60000 or more and less than 70000
# 2 for 70000 or more and less than 80000
# 3 for 80000 and above
# 新しい列 target を None で初期化
df['target'] = None
#All elements in the column None are This value is rewritten by conditional specification.
df.head()

#First create a mask corresponding to each condition.
mask1 = df['ResponseId'] < 60000
mask2 = (df['ResponseId'] >= 60000) & (df['ResponseId'] < 70000)
mask3 = (df['ResponseId'] >= 70000) & (df['ResponseId'] < 80000)
mask4 = df['ResponseId'] >= 80000

# We used to select rows or columns by integer index, df.iloc[] but use to specify columns by name df.loc[]
df.loc[mask1, 'target'] = 0
df.loc[mask2, 'target'] = 1
df.loc[mask3, 'target'] = 2
df.loc[mask4, 'target'] = 3
# 先頭から 5 番目までを表示
df.head()

```
#### Removal and interpolation of missing values
```python
# 欠損値を人為的に作成
df.iloc[0, 0] = None
# (0, 'ResponseId') の要素が NaN になっていることを確認
df.head(3)
# 欠損値のあるレコードを削除
df_dropna = df.dropna()
# 先頭から 3 件を表示
df_dropna.head(3)

```
#### Convert between ndarray and dataframe
```python
#pandas.core.frame.DataFrame
type(df)
# It is a NumPy ndarray. Dataframes and series valuesstore their values ​​as ndarrays in attributes.
type(df.values)
#pandas.core.series.Series
type(df['ResponseId'])
#numpy.ndarray
type(df['ResponseId'].values)

# Conversely, you can create series and dataframes from Python lists and ndarrays.
#  Let's generate an ndarray with random numbers as elements with NumPy and convert it to a data frame.
import numpy as np
df = pd.DataFrame(data=np.random.randn(10, 10))
df
```
#### Drawing a graph
```python
# You can call functions for visualization directly from the dataframe object. 
# You can use the graph drawing library called Matplotlib df.plot()
# グラフの描画
df.plot()
```