import random
import operator
from operator import itemgetter
from collections import OrderedDict
import numpy as np
def knapSack(W, wt, val, n):
    K = np.zeros(shape=(n+1,W+1))

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(profit[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    maxVal = K[n][W]
    solution=[]
    i=n
    w=W
    while i>0 and w>0:
        if not K[i][w] == K[i - 1][w]:
            solution.append(i-1)
            w = w-wt[i-1]
            i = i - 1
        else:
            i = i - 1

    return maxVal,  solution


# profit = {}
# for key in range(10):
#     profit[key]=random.randint(50,101)
# wt = {}
# for key in range(10):
#     wt[key]=random.randint(30,101)
# W = 300
profit = [8,12,16,9,3]
wt = [1,3,5,3,2]
W = 9
print("The respective weights of the given items are: ")
print(wt)
print("The corresponding profits on the given items are: ")
print(profit)
print("The maximum weight capacity of the Knapsack:")
print(W)
n = len(wt)
maxVal,solSet=knapSack(W, wt, profit, n)
print("The maximum profit that can be earned using Dynamic Knapsack algorithm:")
print(maxVal)
print("The objects added to the knapsack:")
print(solSet)