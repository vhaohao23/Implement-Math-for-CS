import numpy as np

from linear_regression import LinearRegression

g=LinearRegression("data_multiD.csv")

feature=g.df.drop(columns=g.df.columns[-1]).columns

x=[_ for _ in range(len(feature))]
for i in range(len(x)):
    x[i]=float(input(f"{feature[i]}: "))


ans=g.predict(x)

print(f"Predicted value is {ans}")