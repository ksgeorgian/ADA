import math
import numpy as np


def multiStage_graph(c,n,stages):
    cost = [0]*n
    sol=[0]*n
    cost[n-1]=0
    path=[0]*stages
    for j in range(n-2,-1,-1):
        cost[j]=math.inf
        for i in range(j,n):
            if c[j,i]==math.inf:
                continue
            else:
                if cost[j]>c[j,i]+cost[i]:
                    cost[j]=c[j,i]+cost[i]
                    sol[j]=i
    path[0]=0
    path[stages-1]=n-1
    for j in range(1,stages-1):
        path[j]=sol[path[j-1]]
    return path,cost


c=np.array([[math.inf, 5, 7, math.inf, math.inf, math.inf, math.inf],
            [math.inf, math.inf, math.inf, 2, 3, math.inf, math.inf],
            [math.inf, math.inf, math.inf, math.inf, 8, 1, math.inf],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 8],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 3],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 9],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf]])
n=7
stages=4
sol,min_cost=multiStage_graph(c,n,stages)
print("The path undertaken for minimum cost to reach from source to sink:")
print(sol)
print("The minimum cost from source to sink is: ",end="")
print(min_cost[0])
