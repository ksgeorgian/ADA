import math
import numpy as np


def shortest_all_path(cost, A, n):
    for i in range(n):
        for j in range(n):
            A[i,j]=cost[i,j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i,j]=min(A[i,j],A[i,k]+A[k,j])


cost=np.array([[0,4,11],
              [6,0,2],
              [3,math.inf,0]])
A = np.zeros(shape=(3,3))
n=3
print("The shortest distances between the pairs of different vertices:")
shortest_all_path(cost,A,n)
print(A)
