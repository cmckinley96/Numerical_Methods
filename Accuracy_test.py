import numpy as np
import scipy.linalg as la

#######################################################################
# These functions are intended to test the accuracy of the various    #
# scipy linear algebra functions.                                     #
#                                                                     #
#       Colin McKinley | September 2018                               #
#######################################################################

#Multiply random matrix by its inverse and calculate norm of residual with
#identity matrix.
def myinvcheck(n):
    A = np.random.normal(0, 1, (n, n))
    B = np.linalg.inv(A)
    combined = np.matmul(A,B)
    I = np.eye(n)
    residual = combined - I
    return np.linalg.norm(residual,2)

#Create a random nxn matrix A, random nx1 b, and solve Ax=b. Return norm of
#residual
def mysolvecheck(n):
    A = np.random.normal(0, 1, (n, n))
    b = np.random.normal(0, 1, (n, 1))
    x = np.linalg.solve(A, b)
    return np.linalg.norm(np.matmul(A, x) - b, 2)

#PLU decomposition to solve Ax=b and compare with other solvers
def pluDecomp(A,b):
    #Inputs:
    #A, matrix
    #b, right hand vector
    #Outputs:
    #x1, PLU Solution
    #r1, norm of residual x1
    #x2, solution using linalg.solve
    #r2 norm of residual x2

    (P, L, U) = la.lu(A)
    D = np.matmul(P, b)
    Y = la.solve(L, D)
    x1 = la.solve(U, Y)
    r1 = la.norm(np.matmul(A, x1) - b, 2)
    x2 = la.solve(A, b)
    r2 = la.norm(np.matmul(A, x2) - b, 2)
    print "\nr1:", r1
    print "x1: \n", x1
    print "\nr2:", r2
    print "x2:\n", x2


if __name__ == "__main__":
    n = 7
    print("\nInverse Check: ")
    print(myinvcheck(n))
    print("\nla.solve check: ")
    print(myinvcheck(n))
    print("\nPLU Vs. la.solve:")
    print "="*20
    A = np.random.normal(0, 1, (n, n))
    b = np.random.normal(0, 1, (n, 1))
    pluDecomp(A, b)

    A = np.array([[5, 7],
                  [9, 3]])
    b = np.array([[16],
                  [9]])
    print("\nTesting PLU again")
    print "="*20
    pluDecomp(A, b)
