# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#min

import pandas as pd
import numpy as np

"""

Object Creation

"""

"""Creating a Series by passing a list of values, letting pandas create a default integer index:"""

s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

"""Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns:"""

dates = pd.date_range('20130101', periods=6)
#print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
#print(df)

"""Creating a DataFrame by passing a dict of objects that can be converted to series-like."""

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
#print(df2.dtypes)



"""

Viewing Data

"""

#print(df.head(1))
#print(df.tail(1))
#print(df.index)
#print(df.columns)

"""DataFrame.to_numpy() gives a NumPy representation of the underlying data. Note that this can be an expensive operation when your DataFrame has columns with different data types, which comes down to a fundamental difference between pandas and NumPy: NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column. When you call DataFrame.to_numpy(), pandas will find the NumPy dtype that can hold all of the dtypes in the DataFrame. This may end up being object, which requires casting every value to a Python object. DataFrame.to_numpy() does not include the index or column labels in the output."""

#print(df.to_numpy())
#print(df2.to_numpy())

"""describe() shows a quick statistic summary of your data:"""

#print(df.describe())

"""Transposing your data (Transposing a dataset means swapping its rows and columns so that the rows become columns and the columns become rows):"""
#print(df.T)

"Sorting by an axis (sorts based off top axis, aka d to c to b to a because ascending=False) Axis=0 will sort by the left side axis:"
#print(df.sort_index(axis=1, ascending=False))

"""Sort by values...row with lowest b value goes up top. Rows are all stacked according to B value"""
#print(df.sort_values(by='B'))


"""

Selection

"""

"""Getting"""
# Selecting a single column, which yields a Series, equivalent to df.A:

#print(df["A"])
#print(df.A)

# Selecting via [], which slices the rows.

#print(df[0:3])
#print(df['20130102':'20130104'])

"""Selection By Label"""
# For getting a cross section using a label:
#print(df.loc[dates[2]])

# Selecting on a multi-axis by label:
#print(df.loc[:, ['A', 'B']])

# Showing label slicing, both endpoints are included:
#print(df.loc['20130102':'20130104', ['A', 'B']])

# Reduction in the dimensions of the returned object
#print(df.loc['20130102', ['A', 'B']])

# For getting a scalar value (A scalar is a simple single numeric value (as in 1, 2/3, 3.14, etc.), usually integer, fixed point, or float (single or double), as opposed to an array, structure, object, complex vector (real plus imaginary or magnitude plus angle components), higher dimensional vector or matrix (etc.))
#print(df.loc[dates[0], 'A'])

#For getting fast access to a scalar (equivalent to the prior method):
#print(df.at[dates[0], 'A'])

"""Selection by position"""

# Select via the position of the passed integers:
# prints out the values of fourth row
#print(df.iloc[3])

# By integer slices, acting similar to numpy/python:
# first slice handles row, second handles column
# in 3:5, only 3 and 4 will be shown
#print(df.iloc[3:5, 0:2])
#print(df.iloc[2:5, 0:2])
#print(df.iloc[2:5, 0:3])

# By lists of integer position locations, similar to the numpy/python style:
#print(df.iloc[[1, 2, 4], [0, 2]])

# For slicing rows ot columns explicitly:
#row:
#print(df.iloc[1:3, :])
#column:
#print(df.iloc[:, 1:3])

# for getting a value explicitly:
#print(df.iloc[1, 1])

#For getting fast access to a scalar (equivalent to the prior method):
#print(df.iat[1, 1])

"""Boolean Indexing"""

# Using a single column’s values to select data.
#print(df[df['A'] > 0])

# Selecting values from a DataFrame where a boolean condition is met.
# turns all negative numbers to NaN
#print(df[df > 0])

# Using the isin() method for filtering:
#df2 = df.copy()
#df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
#print(df2)
#print(df2[df2['E'].isin(['two', 'four'])])


"""Setting"""
# Setting a new column automatically aligns the data by the indexes.
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
#print(s1)
df['F'] = s1
#print(df)

# Setting values by label:
df.at[dates[0], 'A'] = 0

# Setting values by position:
df.iat[0, 1] = 0

# Setting by assigning with a NumPy array:
df.loc[:, 'D'] = np.array([5] * len(df))

# A where operation with Setting
#df2 = df.copy()
#df2[df2 > 0] = -df2
#print(df2)

"""

Missing Data

pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations.
"""
# Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.

#df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])

#df1.loc[dates[0]:dates[1], 'E'] = 1
#print(df1)

# To drop any rows that have missing data
#print(df1.dropna(how="any"))

# Fill missing data
#print(df1.fillna(value=5))

# Get boolean mask where values are nan
#print(pd.isna(df1))

"""

Operations

Operations in general exclude missing data.
"""
print(df)
"""Stats"""
#Performing a descriptive statistic:
#print(df.mean())

# Same operation on the other axis:
#print(df.mean(1))

# Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically broadcasts along the specified dimension.
