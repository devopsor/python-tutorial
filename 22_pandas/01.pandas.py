#################################Pandas######################################

#What is Pandas?

# Pandas is a flexible, high-performance, open-source Python library(※) built specifically to provide data 
# structures and analysis tools for data scientists.

# As a developer, you’ll find that Pandas is like a programmatic, GUI-free Excel. 
# When you import data into a Pandas, you get a DataFrame object that represents your data as 
# a series of columns and rows — much like you’d see in an Excel worksheet.

# This makes it very easy to analyze and clean up data sets. 
# Performing operations like removing rows that don’t meet certain criteria, automatically removing 
# columns that have too many missing values, or adding new columns calculated from existing columns 
# can usually be done with a single function call.

# Working with tables of data this way — by cleaning and transforming the data using clean, 
# easy-to-understand Python — is usually much quicker and more portable for developers than 
# point-and-click your way through complex, built-in Excel functions or writing custom VBA code.

#Installation

# pip install pandas
# pip install jupyterlab

print('------------------------Welcome to Pandas!---------------------')
print('Installation methods:')
print('---------------------------------------------------------------')
print('pip install pandas')

# import pandas as pd
# df = pd.read_csv('survey_results_public.csv')
# schema_df = pd.read_csv('survey_results_schema.csv')

# pd.set_option('display.max_columns', 5)
# pd.set_option('display.max_rows', 10)

# df
# df.shape
# df.info()
# df.head ()
# schema_df

# API
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html



# https://insights.stackoverflow.com/survey
#######################################pandas
"""
 ['BooleanDtype',
 'Categorical',
 'CategoricalDtype',
 'CategoricalIndex',
 'DataFrame',
 'DateOffset',
 'DatetimeIndex',
 'DatetimeTZDtype',
 'ExcelFile',
 'ExcelWriter',
 'Flags',
 'Float32Dtype',
 'Float64Dtype',
 'Float64Index',
 'Grouper',
 'HDFStore',
 'Index',
 'IndexSlice',
 'Int16Dtype',
 'Int32Dtype',
 'Int64Dtype',
 'Int64Index',
 'Int8Dtype',
 'Interval',
 'IntervalDtype',
 'IntervalIndex',
 'MultiIndex',
 'NA',
 'NaT',
 'NamedAgg',
 'Period',
 'PeriodDtype',
 'PeriodIndex',
 'RangeIndex',
 'Series',
 'SparseDtype',
 'StringDtype',
 'Timedelta',
 'TimedeltaIndex',
 'Timestamp',
 'UInt16Dtype',
 'UInt32Dtype',
 'UInt64Dtype',
 'UInt64Index',
 'UInt8Dtype',
 '__all__',
 '__builtins__',
 '__cached__',
 '__deprecated_num_index_names',
 '__dir__',
 '__doc__',
 '__docformat__',
 '__file__',
 '__getattr__',
 '__git_version__',
 '__loader__',
 '__name__',
 '__package__',
 '__path__',
 '__spec__',
 '__version__',
 '_config',
 '_is_numpy_dev',
 '_libs',
 '_testing',
 '_typing',
 '_version',
 'api',
 'array',
 'arrays',
 'bdate_range',
 'compat',
 'concat',
 'core',
 'crosstab',
 'cut',
 'date_range',
 'describe_option',
 'errors',
 'eval',
 'factorize',
 'get_dummies',
 'get_option',
 'infer_freq',
 'interval_range',
 'io',
 'isna',
 'isnull',
 'json_normalize',
 'lreshape',
 'melt',
 'merge',
 'merge_asof',
 'merge_ordered',
 'notna',
 'notnull',
 'offsets',
 'option_context',
 'options',
 'pandas',
 'period_range',
 'pivot',
 'pivot_table',
 'plotting',
 'qcut',
 'read_clipboard',
 'read_csv',
 'read_excel',
 'read_feather',
 'read_fwf',
 'read_gbq',
 'read_hdf',
 'read_html',
 'read_json',
 'read_orc',
 'read_parquet',
 'read_pickle',
 'read_sas',
 'read_spss',
 'read_sql',
 'read_sql_query',
 'read_sql_table',
 'read_stata',
 'read_table',
 'read_xml',
 'reset_option',
 'set_eng_float_format',
 'set_option',
 'show_versions',
 'test',
 'testing',
 'timedelta_range',
 'to_datetime',
 'to_numeric',
 'to_pickle',
 'to_timedelta',
 'tseries',
 'unique',
 'util',
 'value_counts',
 'wide_to_long'] 
"""