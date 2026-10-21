import pandas as pd
import numpy as np
import derivative_2d as d2d

def derivative_df(arr):
    rows = len(arr)
    cols = len(arr[0])

    res = []

    for i in range(1, rows):
        row_result = []
        for j in range(1, cols):
            dx, dy = d2d.compute_point_derivative(arr, i, j)
            row_result.append(f"{dx:.2f},{dy:.2f}")
        res.append(row_result)

    dfhead = arr[0][1:]
    dfidx = [r[0] for r in arr[1:]]

    df_res = pd.DataFrame(res, index=dfidx, columns=dfhead)
    new_arr = df_res.to_numpy(dtype=float).tolist()
    return new_arr

def derivative_n_level(arr, n):
    if n==1:
        return derivative_df(arr)
    else:
        new_arr = derivative_n_level(arr, n-1)
        return derivative_df(new_arr)


df = pd.read_csv("data.csv", header=None)
arr = df.to_numpy(dtype=float).tolist()
n=int(input("Enter the level of derivative: "))
derivative_arr = derivative_n_level(arr, n)

df_result = pd.DataFrame(derivative_arr, index=df.index, columns=df.columns)

df_result.to_csv("derivative.csv", index=True)

print(df_result)