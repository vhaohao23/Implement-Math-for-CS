x=[1,2,3,4,5,6,7,8,9]
y=[-2, 5, 18, 37, 62, 93, 130, 173, 222] # y=f(x)=3*x**2 - 2*x - 3
point=input("Enter the x-axis: ")
point = int(point)

xpos=x.index(point)
ypos=y[xpos]

def left_derivative(x, y, pos):
    if pos == 0:
        return None 
    return (y[pos] - y[pos - 1]) / (x[pos] - x[pos - 1])

def right_derivative(x, y, pos):
    if pos == len(x) - 1:
        return None 
    return (y[pos + 1] - y[pos]) / (x[pos + 1] - x[pos])

def  derivative(x, y, pos):
    l = left_derivative(x, y, pos)
    r = right_derivative(x, y, pos)
    
    if l is not None and r is not None:
        return (l + r) / 2
    elif l is not None:
        return l
    elif r is not None:
        return r
    else:
        return None
    
print("The derivative at x =", point, "is", derivative(x, y, xpos))
print("The derivative at x =", point, "is", derivative(x, y, xpos))

