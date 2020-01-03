

def radix_sort(li):
    max_num = max(li)
    it = 0 #定义迭代次数，0～9迭代1次，两位数迭代两次
    while 10**it <= max_num:#最大值9->1,99->2,888->3
        buckets = [[] for _ in range(10)] #0-9个数
        for var in li:
            # 987->it=1 987//1%10=7  , 987//10=98%10=8; it=3 987//100=9 9%10=9
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)# 按哪一个位排就进那一个位上数字的桶
            #分桶完成
        li.clear()
        for j in buckets:
            li.extend(j)
        #把数重新写回li
        it+= 1



import random
li = list(range(100))
random.shuffle(li)
radix_sort(li)
print(li)




