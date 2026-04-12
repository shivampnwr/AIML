import pandas as pd
print(pd.__version__)
# series : is 1 dimensionallabelled  array that can hold any data type
            # think of it as an single column in a spread sheet
data= [10,11 ,12]
series=pd.Series(data)
#  to add the new labels
series=pd.Series(data,index=["a","b","c"])
print(series)
# to access the series a value directly we can access by label loc
print(series.loc["a"])
# also we can set the value using loc
series.loc["c"]=19
print(series)
# iloc is for integer location
# print(series.iloc[1])
print(series[series<20])