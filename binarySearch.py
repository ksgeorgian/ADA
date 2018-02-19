import random
import time
import math
import numpy
import matplotlib.pyplot as plot
from collections import OrderedDict


def binarySearch(arr,low,high,test,count):
    if low==high:
        if arr[low]==test:
            count+=1
            return low,count
        else:
            count+=1
            return -1,count
    else:
        mid=math.floor((low+high)/2)
        if arr[mid]==test:
            count+=1
            return mid,count
        elif arr[mid]<test:
            count+=1
            return binarySearch(arr,mid+1,high,test,count)
        else:
            count+=1
            return binarySearch(arr,low,mid-1,test,count)



iterations=1000
observations=5
init_size=100
increment=100
experiments=5
dict_list=[]
index_list=[]

for exp in range(experiments):
    comparisons=OrderedDict()
    time_avg=OrderedDict()
    for observation in range(observations):
        sum1=0
        time_per_iteration=[]
        sample_range=range(init_size+increment*observation+1)
        #arr = list(random.sample(sample_range, init_size + increment * observation))
        #arr=sorted(arr)
        arr=[x for x in sample_range]
        print(arr)
        for iteration in range(iterations):
            test=random.choice(sample_range)
            start=time.time()
            index,count=binarySearch(arr,0,len(arr)-1,test,0)
            end=time.time()
            time_taken=end-start
            time_per_iteration.append(time_taken)
            sum1+=count
        comparisons[init_size + increment * observation] = sum1 / iterations
        time_avg[init_size + increment * observation] = sum(time_per_iteration) / iterations
    dict_list.append(time_avg)
    index_list.append(comparisons)
print(dict_list)
print(index_list)

colors=['green','orange','blue','yellow','red']
fig=plot.figure()
graph=fig.add_subplot(1,1,1)
graph.set_xlabel('Number of elements in array(N)')
graph.set_ylabel('Average Time taken to search(in seconds)')
graph.set_title('Binary Search Analysis')
N=list(range(init_size,init_size+increment *observations,increment))
for i in range(experiments):
    graph.plot(N,dict_list[i].values(),label='Experiment ' +str(i+1),color=colors[i])
plot.legend()
plot.show()


bar_width=0.15
x=numpy.arange(len(N))
for j in range(experiments):
    plot.bar(x + bar_width *j,index_list[j].values(),width=bar_width,label='Experiment '+ str(j+1),color=colors[j])
plot.xticks(x+bar_width*2,N)
plot.xlabel('No.of array elements(N)')
plot.ylabel('Average number of comparisons')
plot.title('No. of elements VS average No. of comparisons made')
plot.legend()
plot.show()
