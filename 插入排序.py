#第一张为手上的牌，初始时手中就一张牌，然后从无序区摸牌插入到手里牌的正确位置
def insert_sort(li):
    for i in range(1,len(li)):#i表示从无序区摸的牌
        tmp = li[i]
        j=i-1 #j表示手里牌的下标
        while j>=0 and li[j]>tmp: #两个条件，如果手上的牌
            li[j+1]=li[j]#手里的数往右移
            j -= 1
        li[j+1]=tmp
        print(li)

li = [3,2,4,1,5,7,9,6,8]

insert_sort(li)






