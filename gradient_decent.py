import random
def f(x):
    return 3*x**2 - 2*x + 2
def df(x):
    return 6*x - 2

def gradient_descent(init, learning_rate, num_iterations):
    x = init
    for _ in range(num_iterations):
        gradient = df(x)
        x = x - learning_rate * gradient
    return x

def solve_gradient_descent():
    ans=100000
    for _ in range(10):
        init=random.uniform(-3, 3)
        ans=min(ans,gradient_descent(init, 0.05, 100))
    
    return ans

print("Min of f(x) is ", solve_gradient_descent())