num=int(input("enter the element to be searched"))
a=[2,4,5,1,6,7,8,9,12,11,43,54,34,79]
a.sort()
print(a)
l=len(a)
low=0
up=l-1
mid=0
flag=0
while low<=up:
    mid=(low+up)//2
    if num<a[mid]:
        up=mid-1
    elif num>a[mid]:
        low=mid+1
    elif num==a[mid]:
        flag=1
        #print("position : ",mid)
        break
if flag==1:
    print("found")
else:
    print("not found")




