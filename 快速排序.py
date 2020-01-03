def partition(li, left, right): #先把第一个数作为中间一个数把一个列表分成两个
    tmp = li[left]
    while left<right: #终止条件是左右两个指针一样
        while left<right and li[right]>=tmp: #从右边开始，找到比tmp大的数
            right -=1
        li[left]=li[right]#和左边的交换
        while left<right and li[left]<=tmp:
            left +=1
        li[right]=li[left]

    li[left]=tmp
    print(li)
    return left

def quick_sort(li,left,right):
    if left<right:
        mid = partition(li,left,right)
        quick_sort(li,left,mid)
        quick_sort(li,mid+1,right)
li=[10,2,6,7,9,1,4,3]

quick_sort(li,0,len(li)-1)

print(li)
