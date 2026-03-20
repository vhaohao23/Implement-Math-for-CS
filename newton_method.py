def f(x):
    return 3*x**2 - 2*x - 3
def df(x):
    return 6*x - 2

def newton_method(init):
    precision = 0.00001
    x=init
    
    while True:
        x= x - f(x)/df(x)
        if abs(f(x)) < precision:
            break
    return x

init=float(input("Input guess value:"))
print("Root of f(x) is ", newton_method(init))