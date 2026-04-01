import numpy as np
import pandas as pd

class LinearAproximation:
    def __init__(self, csv_path):
        self.raw_df = pd.read_csv(csv_path)
        # Lưu lại min, max để chuẩn hóa input x sau này
        self.df_min = self.raw_df.min()
        self.df_max = self.raw_df.max()

        # Chuẩn hóa toàn bộ bảng dữ liệu
        self.df = (self.raw_df - self.df_min) / (self.df_max - self.df_min)

        self.dfi = self.df.drop(columns=self.df.columns[-1])
        self.dfo = self.df.iloc[:, -1]
        self.feature = self.dfi.columns

    def find_nearest_point(self,x):
        data=self.dfi.to_numpy(dtype=float)
        return np.linalg.norm(data-x,axis=1).argmin()

    def find_x0_left_index(self,all_dist,feature,x0):
        all_dist_left = all_dist[self.dfi.loc[all_dist["origin_idx"].to_numpy(), feature].to_numpy() < x0[feature]]

        if all_dist_left.empty:
            return None

        min_dist_left = all_dist_left["dist"].min()
        # origin idx of the close point in the left
        close_other_feature = all_dist_left[all_dist_left["dist"] == min_dist_left]["origin_idx"].to_numpy()
        # origin idx of the closest point in the left
        closest_other_feature = np.abs(self.dfi.loc[close_other_feature, feature].to_numpy() - x0[feature]).argmin()

        return close_other_feature[closest_other_feature]

    def find_x0_right_index(self,all_dist,feature,x0):
        all_dist_right = all_dist[self.dfi.loc[all_dist["origin_idx"].to_numpy(), feature].to_numpy() > x0[feature]]

        if all_dist_right.empty:
            return None

        min_dist_right = all_dist_right["dist"].min()

        close_other_feature = all_dist_right[all_dist_right["dist"] == min_dist_right]["origin_idx"].to_numpy()

        closest_other_feature = np.abs(self.dfi.loc[close_other_feature, feature].to_numpy() - x0[feature]).argmin()

        return close_other_feature[closest_other_feature]

    def partial_df(self,feature,x0_index):
        new_df=self.dfi.copy()
        new_df["origin_idx"]=new_df.index

        df0 = new_df.drop(self.dfi.index[x0_index]) #exclude the x0
        df0=df0.drop(columns=feature) #exclude the specific feature

        x0=self.dfi.iloc[x0_index]

        all_dist=pd.DataFrame(
            np.linalg.norm(df0.drop(columns="origin_idx").to_numpy()-x0.drop(labels=feature).to_numpy(),axis=1),
            columns=["dist"]
        )

        all_dist["origin_idx"]=df0["origin_idx"].to_numpy()

        #left
        x0_left_index=self.find_x0_left_index(all_dist,feature,x0)
        x0_left=self.dfi.iloc[x0_left_index] if x0_left_index is not None else None


        #right
        x0_right_index=self.find_x0_right_index(all_dist,feature,x0)
        x0_right=self.dfi.iloc[x0_right_index] if x0_right_index is not None else None

        #total
        y0_left=self.dfo.loc[x0_left_index] if not x0_left is None else 0
        y0_right=self.dfo.loc[x0_right_index] if not x0_right is None else 0
        y0=self.dfo.loc[x0_index]

        if x0_left is None :
            return (y0_right - y0) / (x0_right[feature] - x0[feature]) if not x0_right is None else 0

        if x0_right is None:
            return (y0_left - y0) / (x0_left[feature] - x0[feature])

        df_left=(y0_left-y0)/(x0_left[feature]-x0[feature])
        df_right=(y0_right-y0)/(x0_right[feature]-x0[feature])

        # print(
        #     f"Feature {feature}: x0={x0[feature]}, x_left={x0_left[feature]}, x_right={x0_right[feature]}, slope={(df_left + df_right) / 2}")

        return (df_left+df_right)/2


    def approximation(self,x):
        x0_index=self.find_nearest_point(x)

        x=pd.Series(x,index=self.dfi.columns)

        x0=self.dfi.iloc[x0_index]
        L=self.dfo.loc[x0_index]

        for feature in self.dfi.columns:
            L+=self.partial_df(feature,x0_index)*(x[feature]-x0[feature])

        print(f"Nearst point:{self.df.iloc[x0_index].to_numpy()}")

        return L

la=LinearAproximation("data_multiD.cs"
                      "v")
feature=la.dfi.columns
x=[_ for _ in range(len(feature))]
for i in range(len(x)):
    x[i]=float(input(f"{feature[i]}: "))

print(f"L(x) = {la.approximation(x)}")
