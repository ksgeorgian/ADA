import random


def gen_num(n,s):
    sol=[]
    d=s
    i=0
    while d>=9:
        if(i<n):
            sol.append(9)
            i+=1
            d=d-9
        else:
            return False
            break
    if(i==n):
        return False
    else:
        sol.append(d)
        j=i+1
        for k in range(j,n):
            sol.append(0)
    return sol


s = random.randint(30,60)
n = random.randint(6,10)
print("sum of the digits of the number:")
print(s)
print("Number of digits in the number:")
print(n)
sol=gen_num(n,s)
if sol==False:
    print("The given data is incorrect")
else:
    sum=0
    for j in range(n):
        sum=sum+(sol[j]*(pow(10,n-j-1)))
    print("The largest number generated from the given data is:")
    print(sum)
