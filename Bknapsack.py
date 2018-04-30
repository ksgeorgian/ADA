def bound(cp,cw,k):
    b=cp
    c=cw
    for i in range(k+1,n):
        c=c+w[i]
        if c<=m:
            b=b+p[i]
        else:
            c=c-w[i]
            return b+(((m-c)/w[i])*p[i])
    return b

def Bknap(cp,cw,k):
    global fp
    global fw
    if (cw+w[k])<=m:
        y[k]=1
        if k<n-1:
            Bknap(cp+p[k],cw+w[k],k+1)
        if (cp+p[k])>=fp and k==n-1:
            fp=cp+p[k]
            fw=cw+w[k]
            for j in range(k+1):
               x[j]=y[j]

    if bound(cp,cw,k)>=fp:
        y[k]=0
        if k<n-1:
           Bknap(cp,cw,k+1)
        if cp>fp and k==n-1:
            fp=cp
            fw=cw
            for j in range(k+1):
                x[j]=y[j]

p = [8,12,14,16,12,9]
w = [2,4,7,12,9,9]
m = 20
n=len(w)
x=[0]*n
y=[0]*n
cp=cw=fp=fw=0
print("The weight array:")
print(w)
print("The profit array:")
print(p)
print("The limit capacity of the Knapsack: {}".format(m))
Bknap(cp,cw,0)
print("The solution set:")
print(x)
print("The maximum profit that can be earned:")
print(fp)
