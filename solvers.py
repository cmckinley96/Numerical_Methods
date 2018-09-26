#######################################################################
# These functions are intended to help me understand the various root #
# finding methods and be able to effectively implement them           #
#       Colin McKinley | September 2018                               #
#######################################################################

#Function for solving equation with Newton's method
def myNewton(f , f1 , x0 , n):
    # Solves f(x) = 0 by doing n steps of Newton's method starting at x0.
    # Inputs : f -- the function
    # f1 -- it's derivative
    # x0 -- starting guess, a number
    # n -- the number of steps to do
    # Output : x -- the approximate solution
    x = float(x0)  #set x equal to the initial guess x0
    for i in range(n): # Do n times
        x = x0 - f(x) / f1(x) #Newton's method
        x0 = x
    print(f(x))
    return x

#Function for solving equation with Bisection method
def bisectionMethod(f, a, b, tol):
    # Does bisection method for a function f until error under tolerance
    # Inputs : f -- a function
    # a,b -- left and right edges of the interval
    # tol -- the error tolerance
    # Outputs : x -- the estimated solution of f(x) = 0
    # e -- an upper bound on the error
    x = (float(a) + float(b)) / 2 #Starting guess is midpoint
    fValue = f(x) #get current value of f
    while abs(fValue) > tol:
        if fValue > 0:
            b = x
        elif fValue < 0:
            a = x
        else:
            print("????")
        x = (a + b) / 2
        fValue = f(x)
    print(fValue)
    return x

#Function for solving equation with Secant method
def secantMethod(f, x0, x1, tol):
    # Does Secant method for a function f until error under tolerance
    # Inputs : f -- a function
    # x0,x1 -- left and right edges of guess
    # tol -- the error tolerance
    # Outputs : x -- the estimated solution of f(x) = 0
    # e -- an upper bound on the error
    y0 = f(x0)
    y1 = f(x1)
    y = -1
    while abs(y) > tol:
        x = x1 - (y1*(x1 - x0) / (y1 - y0))
        y = f(x)
        x0 = x1
        y0 = y1
        x1 = x
        y1 = y
    print(y)
    return x

#Function for solving equation with Regula Falsa method
def regulaFalsaMethod(f, a, b, tol):
    # Does RegulaFalsa method for a function f until error under tolerance
    # Inputs : f -- a function
    # x0,x1 -- left and right edges of guess
    # tol -- the error tolerance
    # Outputs : x -- the estimated solution of f(x) = 0
    # e -- an upper bound on the error
    yA = f(a)
    yB = f(b)
    y = -1
    while abs(y) > tol:
        x = b - (yB*(b - a) / (yB - yA))
        y = f(x)
        if y > 0:
            b = x
        elif y < 0:
            a = x
    print(y)
    return x

#Test case with f(x) = x^5 -7
if __name__ == "__main__":
    f = lambda x: (x**5) - 7
    f1 = lambda x: 5 * (x**4)
    x0 = 2
    tol = .000001

    print("\nNewton's Method: ")
    print(myNewton(f, f1, x0, 100))
    print("\nBisection Method: ")
    print(bisectionMethod(f, -1.0, 10.0, tol))
    print("\nSecant Method: ")
    print(secantMethod(f, -1.0, 10.0, tol))
    print("\nRegula Falsa Method: ")
    print(regulaFalsaMethod(f, -1.0, 10.0, tol))
