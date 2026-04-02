import pandas as pd
import numpy as np


def find_left_y0(arr,y):
    ma=0
    ry=None
    for i in range(1,len(arr[0])):
        if (arr[0][i]<arr[0][y] and i!=y):
            if (ma==0 or arr[0][i]>ma):
                ma=arr[0][i]
                ry=i

    return ry

def find_right_y0(arr,y):
    mi=1000000
    ry=None
    for i in range(1,len(arr[0])):
        if (arr[0][i]>arr[0][y] and i!=y):
            if (mi==1000000 or arr[0][i]<mi):
                mi=arr[0][i]
                ry=i
    return ry

def find_left_x0(arr,x):
    ma=0
    rx=None
    for i in range(1,len(arr)):
        if (arr[i][0]<arr[x][0] and i!=x):
            if (ma==0 or arr[i][0]>ma):
                ma=arr[i][0]
                rx=i
    return rx

def find_right_x0(arr,x):
    mi=1000000
    rx=None
    for i in range(1,len(arr)):
        if (arr[i][0]>arr[x][0] and i!=x):
            if (mi==1000000 or arr[i][0]<mi):
                mi=arr[i][0]
                rx=i
    return rx


df=pd.read_csv("data.csv",header=None)

arr=df.to_numpy(dtype=float).tolist()

#arcoding to y
darry=[row[:] for row in arr]

for x in range(1,len(arr)):
    for y in range(1,len(arr[x])):
        ry_left= find_left_y0(arr, y)
        ry_right= find_right_y0(arr, y)

        if (ry_left==None): darry[x][y]= (arr[x][ry_right] - arr[x][y]) / (arr[0][ry_right] - arr[0][y])
        elif (ry_right==None): darry[x][y]= (arr[x][y] - arr[x][ry_left]) / (arr[0][y] - arr[0][ry_left])
        else:
            df_left=(arr[x][ry_right]-arr[x][y])/(arr[0][ry_right]-arr[0][y])
            df_right=(arr[x][y]-arr[x][ry_left])/(arr[0][y]-arr[0][ry_left])
            darry[x][y] = (df_left + df_right) / 2
darry=darry[1:]
darry=[x[1:] for x in darry]

darry=np.array(darry)


#according to x
darrx=[row[:] for row in arr]

for y in range(1,len(arr[0])):
    for x in range(1,len(arr)):
        rx_left= find_left_x0(arr, x)
        rx_right= find_right_x0(arr, x)

        if (rx_left==None): darrx[x][y]= (arr[rx_right][y] - arr[x][y]) / (arr[rx_right][0] - arr[x][0])
        elif (rx_right==None) : darrx[x][y] = (arr[x][y] - arr[rx_left][y]) / (arr[x][0] - arr[rx_left][0])
        else:
            df_left=(arr[rx_right][y] - arr[x][y]) / (arr[rx_right][0] - arr[x][0])
            df_right=(arr[x][y] - arr[rx_left][y]) / (arr[x][0] - arr[rx_left][0])
            darrx[x][y] = (df_left + df_right) / 2
darrx=darrx[1:]
darrx=[d[1:] for d in darrx]

ans=[row[:] for row in arr]
for x in range(1,len(arr)):
    for y in range(1,len(arr[x])):
        ans[x][y] = f"{darrx[x - 1][y - 1]:.2f},{darry[x - 1][y - 1]:.2f}"

col=ans[0][1:]
idx=[row[0] for row in arr[1:]]
ans=[d[1:] for d in ans[1:]]


df=pd.DataFrame(ans, index=idx, columns=col)
print(df)
df.to_csv( "derivative.csv",index=True)
