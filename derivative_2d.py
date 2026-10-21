import pandas as pd
import numpy as np

def find_nearest(coords, current_idx):
    val = coords[current_idx]
    left_idx = None
    right_idx = None

    max_left = -float('inf')
    min_right = float('inf')

    for i in range(1, len(coords)):
        if i == current_idx: continue

        if coords[i] < val:
            if coords[i] > max_left:
                max_left = coords[i]
                left_idx = i

        if coords[i] > val:
            if coords[i] < min_right:
                min_right = coords[i]
                right_idx = i

    return left_idx, right_idx



def compute_point_derivative(arr, row, col):

    x_coords = [r[0] for r in arr]
    r_left, r_right = find_nearest(x_coords, row)

    if r_left is None:
        df_dx = (arr[r_right][col] - arr[row][col]) / (arr[r_right][0] - arr[row][0])
    elif r_right is None:
        df_dx = (arr[row][col] - arr[r_left][col]) / (arr[row][0] - arr[r_left][0])
    else:
        df_dx_left = (arr[row][col] - arr[r_left][col]) / (arr[row][0] - arr[r_left][0])
        df_dx_right = (arr[r_right][col] - arr[row][col]) / (arr[r_right][0] - arr[row][0])
        df_dx = (df_dx_left + df_dx_right) / 2

    y_coords = arr[0]
    c_left, c_right = find_nearest(y_coords, col)

    if c_left is None:
        df_dy = (arr[row][c_right] - arr[row][col]) / (arr[0][c_right] - arr[0][col])
    elif c_right is None:
        df_dy = (arr[row][col] - arr[row][c_left]) / (arr[0][col] - arr[0][c_left])
    else:
        df_dy_left = (arr[row][col] - arr[row][c_left]) / (arr[0][col] - arr[0][c_left])
        df_dy_right = (arr[row][c_right] - arr[row][col]) / (arr[0][c_right] - arr[0][col])
        df_dy = (df_dy_left + df_dy_right) / 2

    return df_dx, df_dy



df = pd.read_csv("data.csv", header=None)
arr = df.to_numpy(dtype=float).tolist()

rows = len(arr)
cols = len(arr[0])

result_data = []

for i in range(1, rows):
    row_result = []
    for j in range(1, cols):
        dx, dy = compute_point_derivative(arr, i, j)
        row_result.append(f"{dx:.2f},{dy:.2f}")
    result_data.append(row_result)

dfhead = arr[0][1:]
dfidx = [r[0] for r in arr[1:]]

df_result = pd.DataFrame(result_data, index=dfidx, columns=dfhead)

df_result.to_csv("derivative.csv", index=True)