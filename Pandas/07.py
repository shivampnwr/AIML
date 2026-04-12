# Data cleaning :  the process of fixing /removing pf incorrect, incompleteor irrevelent data
import pandas as pd
df=pd.read_csv("pokemon.csv")
# 1 drop irrevelent column
# df=df.drop(columns=["Legendary","#"])
# print(df)
#   2 handle the mising data
# df=df.dropna(subset=["Type 2"])
# df=df.fillna({"Type 2": "none"})
# print(df)
#  3 fix inconsistent values
# df["Type 1"]=df["Type 1"].replace({"Grass":"GRASS"})
# print(df)
#  4 Standardize text
# df["Name"]=df["Name"].str.lower()
# df["Name"]=df["Name"].str.upper()
# df["Name"]=df["Name"].str.title()
print(df)
# fix data type
df["Legendary"] = df["Legendary"].astype(int)
print(df)

# remove duplicate value
df=df.drop_duplicates()
print(df)