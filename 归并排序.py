def merge(li,low,mid,high):
    i = low
    j = mid+1
    tmp = []
    while i<=mid and j<=high:
        print(i,j)
        print(len(li))
        if li[i]<li[j]:
            tmp.append(li[i])
            i +=1
        else:
            tmp.append(li[j])
            j+=1
    while i<=mid:
        tmp.append(li[i])
        i+=1
    while j<=high:
        tmp.append(li[j])
        j+=1
    li[low:high+1] = tmp
def merge_sort(li,low,high):
    if low < high: #表示至少有两个数,如果，low=high则跳出执行下一步
        mid = (low+high)//2
        #print("1=",li,low,mid,high)
        merge_sort(li,low,mid)
        # print("2=",li,low,mid,high)
        merge_sort(li,mid+1,high)
        #print("3=",li,low,mid,high)
        merge(li,low,mid,high)

li=[2,1,8,7,5,3,6,4]
merge_sort(li,0,len(li)-1)
print(li)




