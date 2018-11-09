'"square root of a function using newton rapson method"'
def func( x ):
    return x * x * x - x * x + 2
 
 def derfun( x ):
    return 3 * x * x - 2 * x
def newtonRaphson( x ):
    h = func(x) / derifun(x)
    while abs(h) >= 0.0001:
        h = func(x)/derifun(x)
         
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
     
    print("The value of the root is : ",
                             "%.4f"% x)
x0 = -20 #(assumed value)

newtonRaphson(x0)
 