# def insert_sort(li):
#     for i in range(1,len(li)):
#         tmp = li[i]
#         j = i-1 #表示手里牌的下标
#         while j>=0 and li[j]>tmp:
#             li[j+1]=li[j]#往右移一个
#             j -=1 #再往前比对大小箭头往左移一个
#         li[j+1]=tmp#再把tmp元素写回来
# li = list(range(10))
# import random
# random.shuffle(li)
# print(li)
# insert_sort(li)
# print(li)


#希尔排序

def insert_gap(li,gap):
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i-gap
        while j >=0 and li[j]>tmp:

            li[j+gap] =li[j]
            j -= gap
        li[j+gap] = tmp


def shell_sort(li):
    d = len(li)//2
    while d>=1:#表示d如果变成1，变成1组的时候退出
        insert_gap(li,d)
        d//=2
        print("li=", li,)


li=[5,7,4,6,3,1,2,9]
shell_sort(li)
print(li)
