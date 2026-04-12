# filtering:keeping the rows that matches the condition
import pandas as pd
df=pd.read_csv("pokemon.csv")
legendery=df[df["Legendary"]==True]
dark_water=df[(df["Type 1"]=="Dark") | (df["Type 2"]=="Water")]
# print(legendery.to_string())
# print(dark_water)
fire_flying=df[(df["Type 1"]=="Fire" )& (df["Type 2"]=="Flying")]
print(fire_flying)
