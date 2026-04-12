# aggregatefunction:Reduces a set of values into a single summary value
                    # Used to summarize and analyze data
                    # Often used with the groupby() function 
import pandas as pd
df=pd.read_csv("pokemon.csv")
# Whole dataframe
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())
# Single Column
print("------Single Column-----")
print(df["HP"].mean())
print(df["HP"].sum(numeric_only=True))
print(df["Attack"].min(numeric_only=True))
print(df["Attack"].max(numeric_only=True))
print(df["Attack"].count())
# groupby() function
group= df.groupby("Type 1")
print(group["Attack"].mean())
print(group["Attack"].count())