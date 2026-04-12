import pandas as pd
calories={"day1": 2000,"day 2":1800,"day 3": 2333}
series=pd.Series(calories)
print(series)
print(series[series>2000])