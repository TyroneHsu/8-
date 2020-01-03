def count_sort(li, maxcount):#最大的数
    count = [0 for _ in range(maxcount+1)] #从0开始所以打印maxcount+1个
    for i in li:
        count[i]+=1#如果列表里有这个数，则在count[i]这个位置加1
    print (count)
    li.clear()
    for ind, i in enumerate(count):
        for i in range(i): #i 表示每个数出现的个数
            li.append(ind) #需要将数append i次


import random

li = [random.randint(0,20) for _ in range(20)]
print(li)
count_sort(li,20)
print(li)
