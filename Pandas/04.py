import pandas as pd

df = pd.read_csv("pokemon.csv",index_col="Name")

# selection by column
# print(df["Name"].to_string())
# print(df["Type 1"].to_string())
# print(df[["Name","Type 1"]].to_string())


# selection by rows
# print(df.loc["Pikachu"])
# print(df.loc["Charizard",["Attack","Defense"]])
# print(df.loc["Charizard":"Pikachu",["Attack","Defense"]])
# integer indexing
# print(df.iloc[0:21,0:3])
# print(df)

# input by the user
pokemon=input(" enter the name of the pokemon:")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")