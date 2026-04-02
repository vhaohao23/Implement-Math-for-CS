# from linear_approximation_multiD import LinearAproximation
#
# la=LinearAproximation("data_multiD.csv")
# feature=la.dfi.columns
#
# x=[_ for _ in range(len(feature))]
# for i in range(len(x)):
#     x[i]=float(input(f"{feature[i]}: "))
#
# print(f"Approximate {la.dfo.name} = {la.approximation(x)}")
#
import numpy as np

from linear_regression import LinearRegression

g=LinearRegression("data_multiD.csv")

ans=g.predict(np.array([125,3,2,5]))

print(f"Predicted value is {ans}")