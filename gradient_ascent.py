import random

import sympy as sp

def df(func,x,x0,a,b):
    h=(b-a)/10000
    x_right= x0 + h
    x_left= x0 - h

    f=func.subs(x,x0)
    f_right=func.subs(x, x_right)
    f_left=func.subs(x, x_left)

    df_right= (f_right-f)/h
    df_left= (f - f_left) / h

    return (df_right+df_left)/2

def gradient_ascent(func,x,xt,a=-sp.oo,b=sp.oo):
    learning_rate=1e-2
    for i in range(1000):
        df_xt=df(func,x,xt,a,b)
        xt=xt+learning_rate*df_xt

    return xt
def find_max(func,a=-sp.oo,b=sp.oo):
    x=sp.symbols("x")

    considered_list=[func.subs(x,a),func.subs(x,b)]

    while True:
        rx=random.uniform(a,b)
        x0=gradient_ascent(func,x,rx,a,b)
        val=round(float(func.subs(x, x0)), 4)
        if val not in considered_list:
            considered_list.append(val)
            print(f"Considered list: {considered_list[-1]}")
        else:
            break

    return max(considered_list)

func=input("Nhap ham hoc:")
print(find_max(sp.simplify(func),a=-100,b=100))
