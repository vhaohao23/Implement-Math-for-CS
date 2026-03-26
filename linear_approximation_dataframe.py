import pandas as pd
import numpy as np

class LinearApproximation:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path,index_col=0)
        self.df.index=self.df.index
        self.df.columns=self.df.columns

        self.df.index = pd.to_numeric(self.df.index, errors="raise")
        self.df.columns = pd.to_numeric(self.df.columns, errors="raise")


    def find_nearest_point(self,x,y):
        x0=self.df.index[np.abs(self.df.index-x).argmin()]
        y0=self.df.columns[np.abs(self.df.columns-y).argmin()]
        return x0,y0

    def derivative_x(self,x0,y0):
        if self.df.index.get_loc(x0)==0:
            right_x0=self.df.index[np.abs(self.df.index>x0)].min()
            dtu=self.df.loc[right_x0,y0]-self.df.loc[x0,y0]
            dmau=right_x0-x0
            return dtu/dmau
        elif self.df.index.get_loc(x0)==len(self.df.index)-1:
            left_x0=self.df.index[np.abs(self.df.index<x0)].max()
            dtu=self.df.loc[x0,y0]-self.df.loc[left_x0,y0]
            dmau=x0 - left_x0
            return dtu/dmau
        else:
            right_x0=self.df.index[np.abs(self.df.index>x0)].min()
            left_x0=self.df.index[np.abs(self.df.index<x0)].max()
            dtu_right=self.df.loc[right_x0,y0]-self.df.loc[x0,y0]
            dtu_left=self.df.loc[left_x0,y0]-self.df.loc[x0,y0]
            dmau_right=right_x0-x0
            dmau_left=left_x0-x0
            return (dtu_right/dmau_right+dtu_left/dmau_left)/2.0
    def derivative_y(self, x0,y0):
        if self.df.columns.get_loc(y0)==0:
            right_y0=self.df.columns[np.abs(self.df.columns>y0)].min()
            dtu=self.df.loc[x0,right_y0]-self.df.loc[x0,y0]
            dmau=right_y0-y0
            return dtu/dmau
        elif self.df.columns.get_loc(y0) == len(self.df.columns) - 1:
            left_y0 = self.df.columns[np.abs(self.df.columns < y0)].max()
            dtu = self.df.loc[x0, y0] - self.df.loc[x0, left_y0]
            dmau = y0 - left_y0
            return dtu / dmau
        else:
            right_y0 = self.df.columns[np.abs(self.df.columns > y0)].min()
            left_y0 = self.df.columns[np.abs(self.df.columns < y0)].max()
            dtu_right = self.df.loc[x0, right_y0] - self.df.loc[x0, y0]
            dtu_left = self.df.loc[x0, left_y0] - self.df.loc[x0, y0]
            dmau_right = right_y0 - y0
            dmau_left = left_y0 - y0
            return (dtu_right/dmau_right+dtu_left/dmau_left)/2.0
    def approximation(self,x,y):
        x0,y0=self.find_nearest_point(x,y)
        return self.derivative_x(x0,y0)*(x-x0)+self.derivative_y(x0,y0)*(y-y0)+self.df.loc[x0,y0]

sol=LinearApproximation("data.csv")
x,y=map(float,input("Enter x,y: ").split())
print(sol.approximation(x,y))