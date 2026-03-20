import pandas as pd
import numpy as np

df=pd.read_csv("data.csv",header=None)

arr=df.to_numpy(dtype=float).tolist()
darr=[row[:] for row in arr]

for x in range(1,len(arr)):
    for y in range(1,len(arr[x])):
        if (y==1): darr[x][y]=(arr[x][y+1]-arr[x][y])/(arr[0][y+1]-arr[0][y])
        elif (y==len(arr[x])-1): darr[x][y]=(arr[x][y]-arr[x][y-1])/(arr[0][y]-arr[0][y-1])
        else:
            darr[x][y] = (arr[x][y + 1] - arr[x][y - 1]) / (arr[0][y + 1] - arr[0][y - 1])

darr=darr[1:]
darr=[x[1:] for x in darr]

darr=np.array(darr)
df=pd.DataFrame(darr)
print(df)
pd.save(df, "derivative.csv")