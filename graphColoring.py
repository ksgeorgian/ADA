import math
import numpy as np
def Gcoloring(G,x,k,m,n):
    while(True):
        nextValue(G,x,k,m,n)
        if x[k]==0:
            return
        if k==n-1:
            print(x)
        else:
            Gcoloring(G,x,k+1,m,n)

def nextValue(G,x,k,m,n):
    while(True):
        x[k]=(x[k]+1)%(m+1)
        if x[k]==0:
            return
        j=0
        while j<n:
            if not G[k,j]==0 and x[k]==x[j]:
                break
            j+=1
        if j==n:
            return


G=np.zeros(shape=(7,7))
edges={(0,1),(0,2),(1,3),(1,4),(2,4),(2,5),(3,6),(4,6),(5,6)}
for edge in edges:
    G[edge[0],edge[1]]=1
    G[edge[1],edge[0]]=1
print("The Edge Adjacency Matrix:")
print(G)
x=[0]*7
m=2
print("The number of colours to be used for Graph Colouring:",m)
n=7
print("The solutions possible with",m,"colours:")
Gcoloring(G,x,0,m,n)