# dataframe: is a tabular data sturcture  containing rows and columns
#               it is like a excel spread sheet
import pandas as pd
data={"name":["pikachu","bulbasor","charizard"],
      "type":["electric","grass","fire"],
      "attack":[100,95,150]}
df=pd.DataFrame(data,index=['p1','p2','p3'])
print(df)
print(df.loc['p2'])
#  to add a new column
df["defense"]=["50","90","130"]
print(df)
# to add a new row
newrow=pd.DataFrame([{"name":"squirtle","type":"water","attack":80,"defense":140}],index=["p4"])
df=pd.concat([df,newrow])
print(df)