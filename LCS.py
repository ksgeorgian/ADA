import numpy as np


def LCS_length(X,Y):
    m=len(X)
    n=len(Y)
    c = np.zeros(shape=(m+1, n+1))
    b = np.empty(shape=(m+1, n+1),dtype=np.str)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                c[i, j]=c[i-1, j-1]+1
                b[i, j] = "D"

            else:
                if c[i-1 ,j]>=c[i, j-1]:
                    c[i, j]=c[i-1, j]
                    b[i, j] = "U"

                else:
                    c[i, j]=c[i, j-1]
                    b[i, j] = "H"
    return c, b


def print_LCS(b,X,i,j):
    if i==0 or j==0:
        return
    if b[i,j]=="D":
        print_LCS(b,X,i-1,j-1)
        print(X[i-1],end="")

    else:
        if b[i,j]=="U":
            print_LCS(b, X, i-1, j)
        else:
            print_LCS(b, X, i, j-1)


X = "CONGRUENCE"
Y= "CONVERGENCE"
i=len(X)
j=len(Y)
c,b=LCS_length(X,Y)
print(c)
print(b)
print("The LCS of the given sequences is:")
print_LCS(b,X,i,j)