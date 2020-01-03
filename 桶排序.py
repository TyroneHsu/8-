def bucket_order(li, n=100, num_max=10000):#n是桶的个数，num_max是最大的数
    buckets = [[] for var in range(n)] #在一个列表里制造n个空桶
    for var in li:
        i = var //(num_max//n) #表示列表里的数进入哪一个箱子
        buckets[i].append(var)
        #利用冒泡排序将每个加到桶里
        for j in range(len(buckets[i])-1,0,-1):#对桶里的数进行排序从后往前冒泡排序
            if buckets[i][j]<buckets[i][j-1]:
                buckets[i][j],buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
            #到这里，桶里数都是有序的
    sorted_li=[]
    for _ in buckets:#将桶里的数都添加到新的列表里
        sorted_li.extend(_)
    return sorted_li

import random

li = [random.randint(0,100) for num in range(100)]
li = bucket_order(li)
print (li)


