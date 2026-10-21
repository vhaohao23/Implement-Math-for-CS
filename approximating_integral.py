import sympy as sp

def left_endpoint(func,a,b):
    x=sp.symbols("x")
    n=1000
    xi=a
    deltax=(b-a)/n
    res=0

    for i in range(n):
        res+=func.subs(x,xi)*deltax
        xi+=deltax

    return res

def midpoint(func,a,b):
    x=sp.symbols("x")
    n=1000
    deltax=(b-a)/n
    xi=a+deltax/2
    res=0

    for i in range(n):
        res+=func.subs(x,xi)*deltax
        xi+=deltax

    return res

def right_endpoint(func,a,b):
    x=sp.symbols("x")
    n=1000
    deltax=(b-a)/n
    xi=b
    res=0

    for i in range(n):
        res=res+func.subs(x,xi)*deltax
        xi-=deltax

    return res

def trapezoidal_rule(func,a,b):
    x=sp.symbols("x")
    n=1000
    deltax=(b-a)/n
    xi=a
    res=func.subs(x,xi)*deltax/2

    for i in range(1,n):
        xi+=deltax
        res+=func.subs(x,xi)*deltax

    xi=b
    res+func.subs(x,xi)*deltax/2
    return res

def simpson_rule(func,a,b):
    x=sp.symbols("x")
    n=1000
    deltax=(b-a)/n
    xi=a
    res=func.subs(x,xi)*deltax/3
    for i in range(1,n):
        xi+=deltax
        res+=func.subs(x,xi)* ( 4/3*deltax if (i%2==1) else 2/3*deltax)

    xi=b
    res+=func.subs(x,xi)*deltax/3
    return res


def input_func():
    x=sp.symbols("x")
    func=sp.sympify(input("Enter a function: "))

    print(f"Left end point: {left_endpoint(func, 10, 20)}")
    print(f"Midpoint: {midpoint(func,10,20)}")
    print(f"Right end point: {right_endpoint(func,10,20)}")
    print(f"Trapezoidal rule: {trapezoidal_rule(func, 10, 20)}")
    print(f"Simpson rule: {simpson_rule(func, 10, 20)}")

input_func()