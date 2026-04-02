import numpy as np
import pandas as pd

class LinearRegression:
    def __init__(self, csv_path=None):
        if csv_path:
            self.read_csv(csv_path)

    def read_csv(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.x = self.df.drop(columns=self.df.columns[-1]).values
        self.y = self.df.iloc[:, -1].values.reshape(-1, 1)#vertical
        self.w = np.random.uniform(0, 1, (self.x.shape[1], 1)) #vertical
        self.learning_rate = np.full(shape=(self.x.shape[1], 1), fill_value=1e-6)


    def grad(self):
        N=self.x.shape[0]
        return 1/N*self.x.transpose() @ ((self.x @ self.w) -self.y)


    def loss(self):
        N=self.x.shape[0]
        return 1/(2*N) * (np.linalg.norm((self.x @ self.w) -self.y)**2)

    def gradient_descent(self):
        grad = self.grad()

        for ith_iter in range(1, 1000):
            self.w -= self.learning_rate * grad
            print(f"iteration {ith_iter}: loss={self.loss()}")


            grad = self.grad()

        return self.w

    def predict(self,inp):
        self.gradient_descent()
        return (inp @ self.w).item()


# g=LinearRegression("data_multiD.csv")
#
# ans=g.predict(np.array([120,1.5,200]))
#
# print(f"Predicted value is {ans}")