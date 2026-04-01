import numpy as np
import pandas as pd

class LinearApproximation:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.dfi = self.df.drop(columns=self.df.columns[-1])
        self.dfo = self.df.iloc[:, -1]
        print(self.df)
        self.feature = self.dfi.columns

    def find_nearest_point(self, x):
        data = self.dfi.to_numpy(dtype=float)
        return np.linalg.norm(data - x, axis=1).argmin()

    def partial_df(self, feature, x0_index):
        new_df = self.dfi.copy()
        new_df["origin_idx"] = new_df.index

        df0 = new_df.drop(self.dfi.index[x0_index])       # exclude x0
        df0 = df0.drop(columns=feature)                    # exclude the feature being differentiated

        x0 = self.dfi.iloc[x0_index]

        other_features = [f for f in self.dfi.columns if f != feature]
        all_dist = pd.DataFrame(
            np.linalg.norm(
                df0.drop(columns="origin_idx").to_numpy() - x0[other_features].to_numpy(),
                axis=1
            ),
            columns=["dist"]
        )
        all_dist["origin_idx"] = df0["origin_idx"].to_numpy()

        feature_vals = self.dfi.loc[all_dist["origin_idx"].to_numpy(), feature].to_numpy()

        # Left neighbors (feature value < x0's)
        left_mask = feature_vals < x0[feature]
        all_dist_left = all_dist[left_mask]

        # Right neighbors (feature value > x0's)
        right_mask = feature_vals > x0[feature]
        all_dist_right = all_dist[right_mask]

        if all_dist_left.empty and all_dist_right.empty:
            return 0

        def get_best_neighbor(side_dist):
            min_d = side_dist["dist"].min()
            candidates = side_dist[side_dist["dist"] == min_d]["origin_idx"].to_numpy()
            best = np.abs(self.dfi.loc[candidates, feature].to_numpy() - x0[feature]).argmin()
            return candidates[best]

        if all_dist_left.empty:
            idx_right = get_best_neighbor(all_dist_right)
            return (self.dfo.loc[idx_right] - self.dfo.loc[x0_index]) / \
                   (self.dfi.loc[idx_right, feature] - x0[feature])

        if all_dist_right.empty:
            idx_left = get_best_neighbor(all_dist_left)
            return (self.dfo.loc[idx_left] - self.dfo.loc[x0_index]) / \
                   (self.dfi.loc[idx_left, feature] - x0[feature])

        idx_left  = get_best_neighbor(all_dist_left)
        idx_right = get_best_neighbor(all_dist_right)

        y_left  = self.dfo.loc[idx_left]
        y_right = self.dfo.loc[idx_right]
        x_left  = self.dfi.loc[idx_left,  feature]
        x_right = self.dfi.loc[idx_right, feature]

        # ✅ Correct central difference formula
        return (y_right - y_left) / (x_right - x_left)

    def approximation(self, x):
        x0_index = self.find_nearest_point(x)
        x = pd.Series(x, index=self.dfi.columns)
        x0 = self.dfi.iloc[x0_index]
        L = self.dfo.loc[x0_index]

        for feature in self.dfi.columns:
            grad = self.partial_df(feature, x0_index)
            L += grad * (x[feature] - x0[feature])

        print(f"Nearest point index: {x0_index}, f(x0) = {self.dfo.loc[x0_index]}")
        return L


la = LinearApproximation("data_multiD.csv")
x=np.array([22,12,250])
print(f"L(x) = {la.approximation(x)}")