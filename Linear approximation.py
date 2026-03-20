def f(x):
    return 3*x**2 - 2*x - 3
def df(x):
    return 6*x - 2

def linear_approximation(a,x):
    return f(a) + df(a)*(x - a)

x=1.998
a=2
print("Linear approximaition result at x =", x, "is", linear_approximation(a,x))