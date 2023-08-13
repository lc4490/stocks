import pandas as pd
import numpy as np

data = open("playerinfo.txt", "r").read().split("\n")
headers = data[0].split(",")
stats = []
for stat in data[1:]:
    stats.append(stat.split(","))
df = pd.DataFrame(np.array(stats), columns=headers)



stocks = []
steals = df[["STL"]].to_numpy()
blocks = df[["BLK"]].to_numpy()
for i in range(len(steals)):
    stocks.append(float(steals[i][0])+float(blocks[i][0]))
df["stocks"]=stocks
df = df.sort_values(by=['stocks'], ascending=False)
print(df.head(10))