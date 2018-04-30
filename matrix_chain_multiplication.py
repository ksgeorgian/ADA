import math
import numpy as np


def matrix_chain_order(p,m,s):
    n=len(p)
    for i in range(n-1):
        m[i,i]=0

    for l in range(2,n):
        for i in range(n-l):
            j=i+l-1
            m[i,j]=math.inf
            for k in range(i,j):
                q=m[i,k]+m[k+1,j]+p[i]*p[k+1]*p[j+1]
                if q<m[i,j]:
                    m[i,j]= q
                    s[i,j]= k

    return m,s


def print_optimal_par(s,i,j):
    if i == j:
        print("A"+str(i),end="")
    else:
        print("(",end="")
        print_optimal_par(s,i,int(s[i,j]))
        print_optimal_par(s,int(s[i,j]+1),j)
        print(")",end="")


p=[5,10,3,12,5,50]
n=len(p)
m=np.zeros(shape=(n-1,n-1))
s=np.zeros(shape=(n-1,n-1))
m,s=matrix_chain_order(p,m,s)
print("Matrix showing the minimum number of multiplications required to achieve the solution")
print(m)
print("Matrix for seeing the break-point for multiplication order")
print(s)
print("The required order of multiplication of matrices:")
print_optimal_par(s,0,n-2)