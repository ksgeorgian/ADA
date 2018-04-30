def NQueens(x,k,n):
    for i in range(n):
        if place(x,k,i):
            x[k]=i
            if k==n-1:
                print(x)
            else:
                NQueens(x,k+1,n)


def place(x,k,i):
    for j in range(k):
        if x[j]==i or (abs(x[j]-i)==abs(j-k)):
            return False
    return True

n=6
x=[-1]*n
print("The solution sets for",n,"queens:")
NQueens(x,0,n)

