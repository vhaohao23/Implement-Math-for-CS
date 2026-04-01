import sympy as sp

x=sp.Symbol('x')
k=sp.Symbol('k',integer=True,nonnegative=True)

def radius_of_convergence(c_n):
    c_n_plus_1=c_n.subs(k,k+1)
    L=sp.limit(sp.Abs(c_n_plus_1/c_n),k,sp.oo)
    return sp.oo if L == 0 else sp.simplify(1 / L)

# def find_cn(func,x):
#     series_gen=sp.fps(func,x,0)
#     return series_gen.ak.formula

def find_cn(func, x):
 ak = sp.fps(func, x,0).ak.formula # Normalize whatever index symbol SymPy used to global `k`
 idx = next((s for s in ak.free_symbols if s != x), k)
 return sp.simplify(ak.subs(idx, k))

def rep_by_series(func_s,n_s=10):
    func=sp.sympify(func_s)
    print(f"Represent: {sp.series(func,x,0,n=n_s)}")
    
    c_n=find_cn(func,x)
    print(f"c_n: {c_n}")
    print(f"Radius of convergence: {radius_of_convergence(c_n)}")

    # dfi=func
    # for i in range(n_s):
    #     df0=dfi.subs(x,0)
    #     print(f"c{i}= {df0/sp.factorial(i)}")
    #     dfi=sp.diff(dfi)

    t1=sp.series(func,x,0,n=1).removeO()
    t2=sp.series(func,x,0,n=2).removeO()
    t3=sp.series(func,x,0,n=3).removeO()
    t4=sp.series(func,x,0,n=4).removeO()
    t5=sp.series(func,x,0,n=5).removeO()


    p=sp.plot(func,t1,t2,t3,t4,t5, (x, -5, 5), show=False, legend=True)
    p[0].line_color='blue'
    p[1].line_color='red'
    p[2].line_color='green'
    p[3].line_color='yellow'
    p[4].line_color='black'
    p[5].line_color='orange'
    p[0].label='f(x)'
    p[1].label='t1'
    p[2].label='t2'
    p[3].label='t3'
    p[4].label='t4'
    p[5].label='t5'


    # p.show()

func=input("Enter the function: ")
rep_by_series(func)


