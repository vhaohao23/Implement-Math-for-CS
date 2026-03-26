import pandas as pd
import numpy as np

def find_row(x,f):
    for i in range(1,len(f)):
        if f[i][0]==x:
            return i
    return -1

def find_col(y,f):
    for i in range(1,len(f[0])):
        if f[0][i]==y:
            return i
    return -1

def find_near_point(x,y,f):
    x0, y0 = f[1][0], f[0][1]
    min_dist=abs(x0-x)**2+abs(y0-y)**2
    for i in range(1,len(f)):
        for j in range(1,len(f[i])):
            dist=abs(f[i][0]-x)**2+abs(f[0][j]-y)**2
            if dist<min_dist:
                min_dist=dist
                x0,y0=f[i][0],f[0][j]
    return x0,y0

def find_near_left_row(x,f):
    min_dist=abs(f[0][0]-x)**2
    xnear=0
    for i in range(1,len(f)):
        if f[i][0]<x:
            dist=abs(f[i][0]-x)**2
            if dist<min_dist:
                min_dist=dist
                xnear=f[i][0]
    return int(xnear)

def find_near_right_row(x,f):
    min_dist=abs(f[0][0]-x)**2
    xnear=0
    for i in range(1,len(f)):
        if f[i][0]>x:
            dist=abs(f[i][0]-x)**2
            if dist<min_dist:
                min_dist=dist
                xnear=f[i][0]

    return int(xnear)

def find_near_left_col(y,f):
    min_dist=abs(f[0][0]-y)**2
    ynear=0
    for i in range(1,len(f[0])):
        if f[0][i]<y:
            dist=abs(f[0][i]-y)**2
            if dist<min_dist:
                min_dist=dist
                ynear=f[0][i]
    return int(ynear)

def find_near_right_col(y,f):
    min_dist=abs(f[0][0]-y)**2
    ynear=0
    for i in range(1,len(f[0])):
        if f[0][i]>y:
            dist=abs(f[0][i]-y)**2
            if dist<min_dist:
                min_dist=dist
                ynear=f[0][i]
    return int(ynear)

def derivative_x(x,y,f):
    ykey = find_col(y, f)
    xkey = find_row(x, f)

    if xkey>1:
        x_left=find_row(find_near_left_row(x,f),f)
        df_left = (f[x_left][ykey] - f[xkey][ykey]) / (f[x_left][0] - x)
    if xkey<len(f)-1:
        x_right=find_row(find_near_right_row(x,f),f)
        df_right=(f[x_right][ykey]-f[xkey][ykey])/(f[x_right][0]-x)

    if xkey==1:
        return df_right
    if xkey==len(f)-1:
        return df_left

    return (df_left+df_right)/2

def derivative_y(x,y,f):
    xkey = find_row(x, f)
    ykey = find_col(y, f)

    if ykey>1:
        y_left=find_col(find_near_left_col(y,f),f)
        df_left=(f[xkey][y_left]-f[xkey][ykey])/(f[0][y_left]-y)

    if ykey<len(f[0])-1:
        y_right=find_col(find_near_right_col(y,f),f)
        df_right=(f[xkey][y_right]-f[xkey][ykey])/(f[0][y_right]-y)

    if ykey==1:
        return df_right
    if ykey==len(f[0])-1:
        return df_left

    return (df_left+df_right)/2

def L(x,y):
    x0, y0 = find_near_point(x,y,f)
    row = find_row(x0, f)
    col = find_col(y0, f)

    return derivative_x(x0,y0,f)*(x-x0) + derivative_y(x0,y0,f)*(y-y0) + f[row][col]

x, y = map(int, input("Enter the x and y values: ").split())
df=pd.read_csv("data.csv",header=None)

arr=df.to_numpy(dtype=float).tolist()
f=[row[:] for row in arr]

print("Approximation of f(x,y) at x =", x, "and y =", y, "is", L(x,y))
