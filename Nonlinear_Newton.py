import numpy as np
import scipy.linalg as la

#######################################################################
# This function is an implementation of Newton's method for nonlinear #
# systems of equations.                                               #
#                                                                     #
#   PARAMETERS:                                                       #
#       F:  np column matrix of equations f1, f2, ... fn.             #
#       DF: Jacobian of F.                                            #
#       X:  Initial guess for solution set.                           #
#       n:  Number of iterations.                                     #
#                                                                     #
# Currently prints solution iteratively, but can be easily changed to #
# return the final value of X.                                        #
#                                                                     #
#       Colin McKinley | September 2018                               #
#######################################################################

def multNewton(F, Df, X, n):
    #Evaluation of lambdas must be done on 1d array
    #Arrays are flattened and reshaped
    DfShape = np.shape(Df)
    FShape = np.shape(F)
    XShape = np.shape(X)

    #Create arrays to hold values
    DfNums = np.zeros((np.size(Df)))
    FNums = np.zeros((np.size(F)))
    for i in range(n):
        print i
        print "="*25
        #Fill Number arrays with values from lambdas
        for j, f in enumerate(F.flatten()):
            FNums[j] = f(X[0])

        for k, df in enumerate(Df.flatten()):
            DfNums[k] = df(X[0])

        #Reshape for matrix operations
        FNums = FNums.reshape(FShape)
        DfNums = DfNums.reshape(DfShape)

        #Solve system
        Dx = la.solve(-DfNums, FNums)

        #Transpose X to column
        X = X.T
        X += Dx

        #Flatten back to 1d arrays
        FNums = FNums.flatten()
        DfNums = DfNums.flatten()
        X = X.reshape(XShape)
        print X
    return "EXIT_SUCCESS"

#Simple test case with f1 = x0^3 + x1 - 1 & f2 = x1^3 -
if __name__ == "__main__":
    #Functions for f
    F = np.array([[lambda x: x[0]**3 + x[1] - 1],
                  [lambda x: x[1]**3 - x[0] + 1]])

    #Partial derivatives
    Df11 = lambda x: 3*(x[0]**2) + x[1] - 1
    Df12 = lambda x: 1
    Df21 = lambda x: -1
    Df22 = lambda x: 3*(x[0]**2) + x[1] - 1
    Df = np.array([[Df11, Df12], [Df21, Df22]])
    X = np.array([.5, .5])[np.newaxis]
    n = 100
    print(multNewton(F, Df, X, n))
